"""Converte um modelo de Termo de Referência da AGU (.docx) em Markdown fiel ao original.

Preserva o que a conversão em texto puro perde:
- numeração automática do Word (1., 1.1., 1.1.1 ...), resolvida a partir de numbering.xml
  e da herança de estilos de parágrafo (a numeração dos modelos AGU vem dos estilos);
- cor da fonte (o vermelho itálico dos modelos vem do estilo "Opcional", não do texto);
- cor de realce (amarelo, turquesa, verde, rosa, azul-petróleo, cinza);
- negrito, itálico, sublinhado e tachado;
- tabelas.

Uso:  python modelo_docx_para_md.py MODELO.docx > saida.md
      python modelo_docx_para_md.py --notas MODELO.docx > notas.md
O segundo modo extrai os comentários do Word (notas explicativas da AGU), cada um
com o número do item do modelo em que está ancorado.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
MC = 'http://schemas.openxmlformats.org/markup-compatibility/2006'
NS = {'w': W}


def q(tag):
    return '{%s}%s' % (W, tag)


def val(el, tag):
    """Valor de w:val de um filho, ou None se o filho não existir."""
    if el is None:
        return None
    c = el.find('w:' + tag, NS)
    if c is None:
        return None
    return c.get(q('val'), '__on__')


def onoff(v):
    if v is None:
        return None
    return v not in ('0', 'false', 'off', 'none')


# Cores de fonte: tons de vermelho do modelo são equivalentes -> "red".
COLOR_MAP = {'FF0000': 'red', 'EE0000': 'red', 'FF3333': 'red', 'C00000': 'red',
             '0000FF': 'blue', '000080': 'navy'}
# Realces do Word -> CSS (legenda oficial no próprio modelo).
HL_MAP = {'yellow': 'yellow', 'cyan': 'cyan', 'green': 'lime', 'magenta': 'magenta',
          'darkCyan': 'darkcyan', 'lightGray': 'lightgray', 'darkGray': 'darkgray',
          'red': 'red', 'blue': 'blue', 'darkYellow': 'olive', 'darkGreen': 'green'}


class Styles:
    def __init__(self, root):
        self.s = {}
        for st in root.findall('w:style', NS):
            self.s[st.get(q('styleId'))] = st
        self.default_p = next((sid for sid, st in self.s.items()
                               if st.get(q('type')) == 'paragraph' and st.get(q('default')) == '1'), None)

    def chain(self, sid):
        out, seen = [], set()
        while sid and sid in self.s and sid not in seen:
            seen.add(sid)
            out.append(self.s[sid])
            b = self.s[sid].find('w:basedOn', NS)
            sid = b.get(q('val')) if b is not None else None
        return out  # do mais específico ao mais geral

    def rpr(self, sid):
        """Propriedades de fonte resolvidas pela cadeia de estilos."""
        props = {}
        for st in reversed(self.chain(sid)):
            props.update(read_rpr(st.find('w:rPr', NS)))
        return props

    def numpr(self, sid):
        num_id = ilvl = None
        for st in self.chain(sid):
            np = st.find('w:pPr/w:numPr', NS)
            if np is None:
                continue
            if num_id is None and np.find('w:numId', NS) is not None:
                num_id = np.find('w:numId', NS).get(q('val'))
            if ilvl is None and np.find('w:ilvl', NS) is not None:
                ilvl = np.find('w:ilvl', NS).get(q('val'))
        return num_id, ilvl

    def outline(self, sid):
        for st in self.chain(sid):
            o = st.find('w:pPr/w:outlineLvl', NS)
            if o is not None:
                return int(o.get(q('val')))
        return None


def read_rpr(rpr):
    p = {}
    if rpr is None:
        return p
    for k in ('b', 'i', 'strike', 'dstrike'):
        v = onoff(val(rpr, k))
        if v is not None:
            p[k] = v
    u = val(rpr, 'u')
    if u is not None:
        p['u'] = u not in ('none', '0')
    c = val(rpr, 'color')
    if c is not None:
        p['color'] = c
    h = val(rpr, 'highlight')
    if h is not None:
        p['hl'] = None if h == 'none' else h
    return p


class Numbering:
    def __init__(self, root, styles):
        self.abs = {}
        for a in root.findall('w:abstractNum', NS):
            self.abs[a.get(q('abstractNumId'))] = a
        self.num = {}
        self.overrides = {}
        for n in root.findall('w:num', NS):
            nid = n.get(q('numId'))
            self.num[nid] = n.find('w:abstractNumId', NS).get(q('val'))
            ov = {}
            for o in n.findall('w:lvlOverride', NS):
                so = o.find('w:startOverride', NS)
                if so is not None:
                    ov[int(o.get(q('ilvl')))] = int(so.get(q('val')))
            self.overrides[nid] = ov
        self.styles = styles
        self.counters = {}
        self.used_nums = set()

    def abstract_for(self, num_id):
        aid = self.num.get(num_id)
        a = self.abs.get(aid)
        if a is not None and a.find('w:numStyleLink', NS) is not None:
            link = a.find('w:numStyleLink', NS).get(q('val'))
            nid, _ = self.styles.numpr(link)
            if nid:
                aid = self.num.get(nid, aid)
                a = self.abs.get(aid)
        return aid, a

    def lvl(self, a, ilvl):
        for l in a.findall('w:lvl', NS):
            if int(l.get(q('ilvl'))) == ilvl:
                return l
        return None

    def next_label(self, num_id, ilvl):
        if not num_id or num_id == '0' or num_id not in self.num:
            return None
        aid, a = self.abstract_for(num_id)
        if a is None:
            return None
        cnt = self.counters.setdefault(aid, {})
        if num_id not in self.used_nums:
            self.used_nums.add(num_id)
            for l, s in self.overrides.get(num_id, {}).items():
                cnt[l] = s - 1
        lv = self.lvl(a, ilvl)
        if lv is None:
            return None
        start = int(val(lv, 'start') or 1) if val(lv, 'start') not in (None, '__on__') else 1
        cnt[ilvl] = cnt.get(ilvl, start - 1) + 1
        for deeper in list(cnt):
            if deeper > ilvl:
                del cnt[deeper]
        fmt = val(lv, 'numFmt') or 'decimal'
        text = val(lv, 'lvlText') or ''
        if fmt == 'bullet':
            return '-'
        if fmt == 'none':
            return text if text and '%' not in text else None

        def render(m):
            k = int(m.group(1)) - 1
            l2 = self.lvl(a, k)
            f = (val(l2, 'numFmt') if l2 is not None else None) or 'decimal'
            s2 = val(l2, 'start') if l2 is not None else None
            s2 = int(s2) if s2 not in (None, '__on__') else 1
            n = cnt.get(k, s2)
            return fmt_num(n, f)
        return re.sub(r'%(\d)', render, text)


def fmt_num(n, f):
    if f in ('lowerLetter', 'upperLetter'):
        s = ''
        while n > 0:
            n, r = divmod(n - 1, 26)
            s = chr(97 + r) + s
        return s.upper() if f == 'upperLetter' else s
    if f in ('lowerRoman', 'upperRoman'):
        vals = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'),
                (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
        s = ''
        for v, r in vals:
            while n >= v:
                s += r
                n -= v
        return s.upper() if f == 'upperRoman' else s
    if f == 'ordinal':
        return '%dº' % n
    return str(n)


def esc(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # evita que colchetes/asteriscos do modelo virem sintaxe Markdown
    return t.replace('*', '\\*').replace('_', '\\_')


def plain(html):
    t = re.sub(r'<br>', ' ', html)
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('\\*', '*').replace('\\_', '_').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    return re.sub(r'\s+', ' ', t).strip()


class Converter:
    def __init__(self, path):
        z = zipfile.ZipFile(path)
        self.styles = Styles(ET.fromstring(z.read('word/styles.xml')))
        numxml = z.read('word/numbering.xml') if 'word/numbering.xml' in z.namelist() else None
        self.numbering = Numbering(ET.fromstring(numxml), self.styles) if numxml else None
        self.doc = ET.fromstring(z.read('word/document.xml'))
        self.comments_xml = z.read('word/comments.xml') if 'word/comments.xml' in z.namelist() else None
        self.out = []
        self.anchors = {}  # id do comentário -> (item do modelo, trecho do texto)
        self.last_label = None
        self.last_heading = None

    # ---- runs -------------------------------------------------------------
    def runs(self, el, base):
        """Gera (texto, props) para cada trecho de texto do parágrafo, em ordem."""
        for ch in el:
            tag = ch.tag
            if tag == q('r'):
                rpr = ch.find('w:rPr', NS)
                props = dict(base)
                rs = rpr.find('w:rStyle', NS) if rpr is not None else None
                if rs is not None:
                    props.update(self.styles.rpr(rs.get(q('val'))))
                props.update(read_rpr(rpr))
                for c in ch:
                    if c.tag == q('t'):
                        yield c.text or '', props
                    elif c.tag == q('tab'):
                        yield ' ', props
                    elif c.tag in (q('br'), q('cr')):
                        yield '\n', props
                    elif c.tag == q('noBreakHyphen'):
                        yield '-', props
                    elif c.tag == q('sym'):
                        yield '•', props
            elif tag in (q('del'), q('moveFrom'), q('pPr'), q('rPr')):
                continue
            elif tag == '{%s}AlternateContent' % MC:
                choice = ch.find('{%s}Choice' % MC)
                if choice is not None:
                    yield from self.runs(choice, base)
            elif tag in (q('drawing'), q('pict'), q('object')):
                continue
            else:
                yield from self.runs(ch, base)

    def render_runs(self, p, base, drop_bold=False):
        segs = []
        for text, props in self.runs(p, base):
            if not text:
                continue
            key = self.fmt_key(props, drop_bold)
            if segs and segs[-1][1] == key:
                segs[-1][0] += text
            else:
                segs.append([text, key])
        parts = []
        for text, key in segs:
            parts.append(self.wrap(text, key))
        s = ''.join(parts)
        return re.sub(r'[ \t]+', ' ', s).strip()

    @staticmethod
    def fmt_key(props, drop_bold):
        color = props.get('color')
        color = COLOR_MAP.get((color or '').upper()) if color and color not in ('auto',) else None
        hl = props.get('hl')
        hl = HL_MAP.get(hl) if hl else None
        return (bool(props.get('b')) and not drop_bold, bool(props.get('i')), bool(props.get('u')),
                bool(props.get('strike') or props.get('dstrike')), color, hl)

    @staticmethod
    def wrap(text, key):
        b, i, u, s, color, hl = key
        m = re.match(r'^(\s*)(.*?)(\s*)$', text, re.S)
        lead, core, trail = m.groups()
        if not core:
            return text
        core = esc(core).replace('\n', '<br>')
        if s:
            core = '<s>%s</s>' % core
        if u:
            core = '<u>%s</u>' % core
        if i:
            core = '<i>%s</i>' % core
        if b:
            core = '<b>%s</b>' % core
        style = []
        if color:
            style.append('color:%s' % color)
        if hl:
            style.append('background:%s' % hl)
        if style:
            core = '<span style="%s">%s</span>' % (';'.join(style), core)
        return lead + core + trail

    # ---- blocos -----------------------------------------------------------
    def para_style(self, p):
        ps = p.find('w:pPr/w:pStyle', NS)
        return ps.get(q('val')) if ps is not None else self.styles.default_p

    def paragraph(self, p, in_table=False):
        sid = self.para_style(p)
        base = self.styles.rpr(sid)
        num_id, ilvl = self.styles.numpr(sid)
        np = p.find('w:pPr/w:numPr', NS)
        if np is not None:
            if np.find('w:numId', NS) is not None:
                num_id = np.find('w:numId', NS).get(q('val'))
            if np.find('w:ilvl', NS) is not None:
                ilvl = np.find('w:ilvl', NS).get(q('val'))
        ilvl = int(ilvl or 0)
        # rPr da marca de parágrafo não afeta o texto; ignorada.
        outline = self.styles.outline(sid)
        is_title = num_id not in (None, '0') and ilvl == 0 and outline == 0
        body = self.render_runs(p, base, drop_bold=is_title)
        label = None
        if self.numbering and num_id not in (None, '0'):
            # Word numera parágrafos vazios também, mas eles não aparecem no texto.
            label = self.numbering.next_label(num_id, ilvl) if body else None
        if label and label != '-':
            self.last_label = label
        if is_title:
            self.last_heading = '%s %s' % (label or '', plain(body))
        self.record_anchors(p, label, body)
        if not body:
            return None
        if in_table:
            return (label + ' ' if label else '') + body
        if is_title:
            return '## %s %s' % (label, body) if label else '## ' + body
        if label is None and outline in (1,) and len(re.sub(r'<[^>]+>', '', body)) < 160:
            return '### ' + body
        if label == '-':
            return '- ' + body
        if label:
            return '%s %s' % (label, body)
        return body

    def record_anchors(self, p, label, body):
        ids = [e.get(q('id')) for e in p.iter() if e.tag in (q('commentRangeStart'), q('commentReference'))]
        for cid in ids:
            if cid in self.anchors:
                continue
            if label and label != '-':
                where = 'item %s' % label
            elif self.last_label:
                where = 'após o item %s' % self.last_label
            else:
                where = 'cabeçalho do modelo'
            snippet = plain(body)
            if len(snippet) > 140:
                snippet = snippet[:140].rsplit(' ', 1)[0] + ' …'
            self.anchors[cid] = (where, snippet)

    def notas(self):
        """Notas explicativas (comentários do Word), na ordem do documento, com o item a que se referem."""
        if not self.out:
            self.convert()
        if self.comments_xml is None:
            return ''
        root = ET.fromstring(self.comments_xml)
        texts = {}
        for c in root.findall('w:comment', NS):
            paras = []
            for cp in c.iter(q('p')):
                t = ''.join(x.text or '' for x in cp.iter(q('t'))).strip()
                if t:
                    paras.append(t)
            texts[c.get(q('id'))] = paras
        out = []
        for cid, (where, snippet) in self.anchors.items():
            paras = texts.get(cid)
            if not paras:
                continue
            head = '### %s' % where[0].upper() + where[1:]
            if snippet:
                head += ' — “%s”' % snippet
            out.append(head + '\n\n' + '\n\n'.join(esc(x) for x in paras))
        return '\n\n'.join(out) + '\n'

    def table(self, tbl):
        rows = []
        for tr in tbl.findall('w:tr', NS):
            cells = []
            for tc in tr.findall('w:tc', NS):
                vm = tc.find('w:tcPr/w:vMerge', NS)
                if vm is not None and vm.get(q('val')) != 'restart':
                    txt = ''
                else:
                    ps = [self.paragraph(p, in_table=True) for p in tc.iter(q('p'))]
                    txt = '<br>'.join(x for x in ps if x)
                txt = txt.replace('|', '\\|').replace('\n', '<br>')
                cells.append(txt)
                gs = tc.find('w:tcPr/w:gridSpan', NS)
                for _ in range(int(gs.get(q('val'))) - 1 if gs is not None else 0):
                    cells.append('')
            rows.append(cells)
        if not rows:
            return None
        width = max(len(r) for r in rows)
        rows = [r + [''] * (width - len(r)) for r in rows]
        if width == 1:
            return '\n\n'.join('> ' + r[0] for r in rows if r[0])
        lines = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * width]
        lines += ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
        return '\n'.join(lines)

    def convert(self):
        body = self.doc.find('w:body', NS)
        self.block(body)
        return '\n\n'.join(self.out) + '\n'

    def block(self, el):
        for ch in el:
            if ch.tag == q('p'):
                r = self.paragraph(ch)
                if r:
                    self.out.append(r)
            elif ch.tag == q('tbl'):
                r = self.table(ch)
                if r:
                    self.out.append(r)
            elif ch.tag in (q('sdt'), q('sdtContent'), q('customXml')):
                self.block(ch)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    conv = Converter(args[0])
    print(conv.notas() if '--notas' in sys.argv else conv.convert(), end='')
