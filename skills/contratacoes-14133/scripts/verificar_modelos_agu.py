#!/usr/bin/env python3
"""Verifica se os modelos de Termo de Referência da AGU salvos em references/ são a versão vigente.

Consulta as páginas de listagem do site da AGU (pregão/concorrência e bens/serviços de TIC) e
compara a data de cada modelo publicado com a versão registrada no cabeçalho do arquivo local
correspondente (linha "**Versão local**: mês/ano · verificada no site da AGU em AAAA-MM-DD").
A página de contratação direta não é consultada porque replica os mesmos arquivos de
pregão/concorrência (conferido por hash em 2026-09-16 — ver memória do projeto).

**A checagem é mensal, não a cada execução.** Para cada modelo, se a data "verificada em"
tiver menos de 30 dias, o script não acessa a rede para ele — só informa que já foi conferido
recentemente. Só os modelos com mais de 30 dias (ou sem essa data) disparam a consulta ao site
da AGU. Se nenhum modelo precisar de checagem, o script inteiro não faz nenhuma chamada de
rede. Use --forcar para ignorar esse prazo (ex.: quando o usuário pedir uma checagem imediata).

Ao concluir a consulta de um modelo com sucesso (independentemente do resultado: atual ou
desatualizado), a data "verificada em" desse arquivo é atualizada para hoje — isso reinicia a
contagem dos 30 dias. Se a consulta falhar (erro de rede), a data não é alterada, para que a
tentativa seja repetida na próxima execução.

Não depende de bibliotecas externas (usa só `urllib` e `datetime`, da biblioteca padrão).

Uso:
  python verificar_modelos_agu.py                # respeita o prazo mensal por modelo
  python verificar_modelos_agu.py --forcar       # ignora o prazo e confere todos agora
  python verificar_modelos_agu.py --baixar       # confere e baixa os desatualizados para
                                                  # modelos-tr-pregao-conc/ ou modelos-tr-tic/
                                                  # (implica --forcar)

Baixar o .docx não regenera o .md sozinho — depois de baixar, siga o Passo 3 (Termo de
Referência) do SKILL.md para reconverter o arquivo com scripts/modelo_docx_para_md.py
(corpo, --notas e --legenda) e atualizar a linha "**Versão local**" e a frase "Fonte:" do
cabeçalho com o novo mês/ano.

Saída: ATUAL, DESATUALIZADO (com a URL de download), OK-RECENTE (dentro do prazo mensal,
não verificado agora) ou AVISO/ERRO (falha de rede ou de parsing).
Código de saída: 0 se nada precisar de atenção; 1 se houver desatualizado, aviso ou erro.
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
INTERVALO_DIAS = 30

# slug no nome do arquivo da AGU -> (arquivo de referência local, pasta onde salvar o .docx baixado, rótulo)
MODELOS = {
    "compras": ("termo-referencia-compras.md", "modelos-tr-pregao-conc", "Compras (exceto TIC)"),
    "servicos-e-obras": ("termo-referencia-servicos-obras.md", "modelos-tr-pregao-conc", "Serviços e obras (exceto TIC)"),
    "compras-tic": ("termo-referencia-compras-tic.md", "modelos-tr-tic", "Compras de TIC"),
    "servicos-tic": ("termo-referencia-servicos-tic.md", "modelos-tr-tic", "Serviços de TIC"),
}

PAGINAS = [
    "https://www.gov.br/agu/pt-br/composicao/cgu/cgu/modelos/licitacoesecontratos/14133/pregao-e-concorrencia",
    "https://www.gov.br/agu/pt-br/composicao/cgu/cgu/modelos/licitacoesecontratos/14133/bens-e-servicos-de-tic",
]

LINK_RE = re.compile(
    r'href="(https://www\.gov\.br/agu/[^"]*?modelo-de-termo-de-referencia-'
    r'(compras-tic|servicos-tic|compras|servicos-e-obras)-lei-no-14-133-'
    r'(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)-(\d{2,4})\.docx)"'
)

MARCADOR_RE = re.compile(
    r'\*\*Versão local\*\*:\s*(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)/(\d{2,4})'
    r'(?:\s*·\s*verificada no site da AGU em\s*(\d{4}-\d{2}-\d{2}))?'
)


def data_chave(mes, ano):
    ano = int(ano)
    if ano < 100:
        ano += 2000
    return (ano, MESES.index(mes) + 1)


def baixar_pagina(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", errors="replace")


def encontrar_versoes_agu(erros):
    """Retorna {slug: (chave, mes, ano, url)} com a versão mais recente encontrada de cada modelo."""
    achados = {}
    for pagina in PAGINAS:
        try:
            html = baixar_pagina(pagina)
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            erros.append(f"Não consegui acessar {pagina}: {e}")
            continue
        for m in LINK_RE.finditer(html):
            url, slug, mes, ano = m.groups()
            chave = data_chave(mes, ano)
            if slug not in achados or chave > achados[slug][0]:
                achados[slug] = (chave, mes, ano, url)
    return achados


def ler_marcador(caminho_md):
    """Retorna (mes, ano, data_verificacao_ou_None) ou None se o arquivo/a linha não existir."""
    if not caminho_md.exists():
        return None
    texto = caminho_md.read_text(encoding="utf-8")
    m = MARCADOR_RE.search(texto)
    if not m:
        return None
    mes, ano, data_str = m.groups()
    verificado_em = datetime.strptime(data_str, "%Y-%m-%d").date() if data_str else None
    return mes, ano, verificado_em


def atualizar_verificado_em(caminho_md, hoje):
    """Atualiza só a data 'verificada em' da linha do marcador, mantendo o mês/ano da versão."""
    texto = caminho_md.read_text(encoding="utf-8")

    def sub(m):
        mes, ano = m.group(1), m.group(2)
        return f"**Versão local**: {mes}/{ano} · verificada no site da AGU em {hoje.isoformat()}"

    novo = MARCADOR_RE.sub(sub, texto, count=1)
    if novo != texto:
        caminho_md.write_text(novo, encoding="utf-8", newline="\n")


def baixar_docx(url, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        destino.write_bytes(r.read())


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # evita acentos corrompidos no console do Windows
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baixar", action="store_true", help="baixa os modelos desatualizados (implica --forcar)")
    ap.add_argument("--forcar", action="store_true", help="ignora o prazo mensal e confere todos agora")
    ap.add_argument("--raiz", help="raiz do repositório (padrão: calculada a partir deste script)")
    a = ap.parse_args()
    forcar = a.forcar or a.baixar

    script_dir = Path(__file__).resolve().parent
    refs = script_dir.parent / "references"
    raiz = Path(a.raiz) if a.raiz else script_dir.parents[2]
    hoje = date.today()

    # Passo 1: decide, sem tocar na rede, quais modelos precisam de checagem agora.
    pendentes = {}
    houve_problema = False
    for slug, (arquivo_md, pasta_local, rotulo) in MODELOS.items():
        caminho_md = refs / arquivo_md
        marcador = ler_marcador(caminho_md)
        if marcador is None:
            print(f"[AVISO] {rotulo}: não encontrei a linha \"**Versão local**\" em {arquivo_md} — não é possível "
                  f"comparar nem controlar o prazo mensal. Adicione a linha manualmente.")
            houve_problema = True
            continue
        loc_mes, loc_ano, verificado_em = marcador
        dias = (hoje - verificado_em).days if verificado_em else None
        if not forcar and dias is not None and dias < INTERVALO_DIAS:
            print(f"[OK-RECENTE] {rotulo}: verificado há {dias} dia(s) (dentro do prazo de {INTERVALO_DIAS} dias) "
                  f"— não conferido agora. Use --forcar para verificar mesmo assim.")
            continue
        pendentes[slug] = (arquivo_md, pasta_local, rotulo, loc_mes, loc_ano, caminho_md)

    if not pendentes:
        print(f"Nenhum modelo com mais de {INTERVALO_DIAS} dias desde a última checagem — nada a fazer.")
        sys.exit(1 if houve_problema else 0)

    print(f"Consultando o site da AGU para {len(pendentes)} modelo(s) "
          f"(pregão/concorrência e bens/serviços de TIC)...")
    erros = []
    agu = encontrar_versoes_agu(erros)
    for e in erros:
        print(f"[ERRO] {e}")
    houve_problema = houve_problema or bool(erros)

    for slug, (arquivo_md, pasta_local, rotulo, loc_mes, loc_ano, caminho_md) in pendentes.items():
        rem = agu.get(slug)

        if rem is None:
            print(f"[AVISO] {rotulo}: modelo não encontrado nas páginas consultadas da AGU — confira manualmente.")
            houve_problema = True
            continue

        rem_chave, rem_mes, rem_ano, rem_url = rem
        loc_chave = data_chave(loc_mes, loc_ano)

        if loc_chave == rem_chave:
            print(f"[ATUAL] {rotulo}: {loc_mes}/{loc_ano} (igual ao site da AGU).")
            atualizar_verificado_em(caminho_md, hoje)
        elif loc_chave < rem_chave:
            print(f"[DESATUALIZADO] {rotulo}: local {loc_mes}/{loc_ano} × AGU {rem_mes}/{rem_ano}.")
            print(f"    Baixar em: {rem_url}")
            houve_problema = True
            atualizar_verificado_em(caminho_md, hoje)  # o fato de estar desatualizado já foi registrado acima
            if a.baixar:
                destino = raiz / pasta_local / rem_url.rsplit("/", 1)[-1]
                try:
                    baixar_docx(rem_url, destino)
                    print(f"    Baixado para {destino}")
                    print(f"    Próximo passo: reconverta com scripts/modelo_docx_para_md.py "
                          f"(corpo, --notas e --legenda) e atualize a linha \"**Versão local**\" (para "
                          f"{rem_mes}/{rem_ano}) e a frase \"Fonte:\" em {arquivo_md}.")
                except (urllib.error.URLError, TimeoutError) as e:
                    print(f"    [ERRO] Falha ao baixar: {e}")
        else:
            print(f"[AVISO] {rotulo}: versão local ({loc_mes}/{loc_ano}) é mais recente que a encontrada "
                  f"no site da AGU ({rem_mes}/{rem_ano}) — confira manualmente, pode ser link desatualizado da AGU.")
            houve_problema = True
            atualizar_verificado_em(caminho_md, hoje)

    sys.exit(1 if houve_problema else 0)


if __name__ == "__main__":
    main()
