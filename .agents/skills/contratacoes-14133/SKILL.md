---
name: contratacoes-14133
description: Elabora e revisa toda a documentação técnica exigida para contratações públicas federais sob a Lei 14.133/2021 (Nova Lei de Licitações e Contratos) — Estudo Técnico Preliminar (ETP), Mapa de Riscos, Termo de Referência (TR) e Parecer Técnico — a partir de um Documento de Formalização de Demanda (DFD) enviado pelo usuário. Também avalia a completude e a conformidade legal de documentação de contratação já elaborada (própria, de outra área, ou de um processo inteiro) frente aos requisitos da modalidade. Use esta skill sempre que o usuário mencionar DFD, ETP, Estudo Técnico Preliminar, Mapa de Riscos, Termo de Referência, TR, Parecer Técnico, licitação, contratação pública, Lei 14.133, pregão, dispensa de licitação, inexigibilidade, ou pedir para revisar, conferir ou montar a documentação de uma contratação — mesmo que não cite o nome exato do documento ou da lei.
---

# Documentação de Contratações Públicas — Lei 14.133/2021

Esta skill ajuda requisitantes, equipe técnica e equipe administrativa de contratações da Administração Pública Federal a transformar um Documento de Formalização de Demanda (DFD) na cadeia de documentos técnicos exigidos pela Lei 14.133/2021, e a conferir se essa documentação está completa e coerente.

## Regra de ouro: nunca apague texto de modelo

Ao adaptar um modelo da AGU/SEGES ao caso concreto, **não remova nada**. A AGU orienta (IPP, p. 54-55) que as alternativas não escolhidas permaneçam visíveis e riscadas, e que a motivação das alterações fique na própria minuta — isso acelera a análise pela consultoria jurídica e evidencia que o gestor ponderou cada opção, em vez de entregar um texto "limpo" que esconde as escolhas feitas.

Use este código de formatação visual em todo documento derivado de modelo:

| Ação | Formatação | Uso |
|---|---|---|
| Inclusão | Fonte **vermelha** | Texto novo, inexistente no modelo |
| Ajustes | Fonte **verde** | Alteração de redação de texto já existente |
| Preenchimento | Fonte **azul** | Lacunas do modelo preenchidas com dados do caso |
| Supressão | ~~Tachado~~ | Trecho do modelo que não se aplica — permanece visível, riscado |

Em Markdown, use `~~texto~~` para supressão e marcação explícita para as cores (ex.: `<span style="color:blue">15 (quinze) dias úteis</span>`), ou entregue em formato que preserve cor quando o usuário pedir .docx. Quando o modelo oferece alternativas "OU" no mesmo tópico, risque a não escolhida e mantenha-a — nunca a delete.

Detalhes e literalidade das regras: `references/ipp-agu-orientacoes.md`.

## Por que o fluxo importa

Cada documento desta cadeia é insumo do seguinte: o ETP interpreta a necessidade descrita no DFD e a transforma em solução técnica justificada; o Mapa de Riscos nasce junto com o ETP porque os riscos identificados ali (e as ações de mitigação) alimentam diretamente o modelo de gestão do contrato; o TR só pode ser redigido com solidez depois que o ETP definiu a solução, os requisitos e as quantidades; e o Parecer Técnico, quando exigido pela modalidade, avalia essa cadeia já pronta. Gerar um documento sem ter o anterior como base é o erro mais comum e o que mais gera glosa/questionamento por controle interno ou órgãos de controle — por isso, sempre que possível, produza os documentos nessa ordem e reaproveite as decisões já tomadas (não repita a análise do zero a cada etapa).

## Fluxo de trabalho

```
DFD → Estudo Técnico Preliminar (ETP) + Mapa de Riscos (anexo do ETP) → Termo de Referência (TR) → Parecer Técnico (quando a modalidade exigir)
```

### Passo 0: Ler e validar o DFD e a publicação da Equipe de Planejamento

Peça dois documentos de início, antes de começar a elaborar qualquer coisa:

1. **O DFD** — leia `references/dfd-topicos.md` para a estrutura esperada. Ao recebê-lo, extraia:
   - A necessidade que motiva a contratação (o problema, não a solução já pré-definida)
   - Quantitativos e prazos estimados, se já informados
   - Área requisitante e responsável
   - Se há vinculação ao Plano de Contratações Anual (PCA)
2. **A publicação (Portaria) que designa a Equipe de Planejamento da Contratação** — é a fonte oficial dos nomes/CPFs dos integrantes (requisitante, técnico, administrativo) que devem assinar o ETP e o Mapa de Riscos, e compor a comissão nos demais documentos. Sem essa publicação, não preencha os campos de "Responsáveis" com nomes — pergunte ao usuário.
   - Ao receber a portaria, confira dois artigos que costumam faltar (o IPP traz modelo em `references/ipp-agu-orientacoes.md`): o que fixa **prazo para conclusão do ETP** e o que estende a atuação da equipe **até a homologação da licitação ou a ratificação da contratação direta**. A ausência deles não impede prosseguir, mas vale apontar ao usuário.
   - Atenção à diferença entre **pedido de designação** (ofício que solicita) e **portaria de designação** (ato que designa). Só a segunda é fonte oficial dos nomes.

Se o DFD estiver incompleto para permitir um ETP consistente (falta a descrição da necessidade, por exemplo), pergunte ao usuário antes de prosseguir — não invente a necessidade da contratação. Nunca reaproveite nomes, CPFs ou e-mails de um DFD/ETP/Portaria anterior desta conversa para preencher os campos de identificação de outro processo — são pessoas e processos diferentes; peça os dados de novo ou peça a publicação correspondente.

### Passo 1: Estudo Técnico Preliminar (ETP)

**Comece pela triagem de enquadramento legal.** Leia `references/enquadramento-legal-triagem.md` e conduza-a antes de qualquer outra pergunta do ETP. O usuário desta skill é requisitante ou equipe técnica, não advogado: ele raramente sabe se o caso é pregão, concorrência, dispensa ou inexigibilidade, e quase nunca sabe qual dos 5 incisos do art. 74 ou dos 18 incisos do art. 75 se aplica. **Nunca pergunte "qual é o enquadramento legal?" nem "é dispensa ou inexigibilidade?" de saída** — pergunte os fatos que a triagem lista (natureza do objeto, valor estimado e somatório do exercício, quantos fornecedores existem, quem é o contratado, se há urgência ou licitação anterior fracassada) e **apresente a conclusão para ele confirmar**, com artigo, inciso e alínea.

Essa triagem vem primeiro porque é no ETP que a modalidade se define (o tópico 5 exige a declaração do dispositivo), porque o TR do Passo 3 depende dela para escolher o modelo da AGU e as alternativas "OU", e porque o resultado dela pode **dispensar o próprio ETP** (art. 14 da IN SEGES/ME nº 58/2022 — incisos I, II, III, VII e VIII do art. 75; e art. 72, I, que exige ETP na contratação direta apenas "se for o caso").

Definido o objeto: se **não** for de TIC, leia `references/etp-topicos.md` para os tópicos obrigatórios e a numeração usada pelo órgão. Se **for** de TIC, use `references/etp-tic-topicos.md` em vez do genérico — a estrutura de TIC é substancialmente mais detalhada (levantamento e análise comparativa de soluções alternativas, registro de soluções inviáveis, TCO) e não deve ser substituída pela genérica.

**Depois da triagem, conduza a entrevista inicial** descrita em `references/etp-topicos.md` (seção "Entrevista inicial", Blocos 1 a 8). O DFD quase nunca traz contexto suficiente: é preciso entender como o usuário concluiu que precisa do objeto, qual problema exatamente ele resolve, qual a aplicação prática, o que se pretende alcançar depois, e quem são os beneficiários indiretos. Trate também insumos, forma de medição do resultado, garantia, antecipação de pagamento e sustentabilidade. **As quantidades do DFD são ponto de partida, não dado fechado** — confirme-as com o usuário.

**A entrevista deve se adaptar à natureza do objeto — nunca é um checklist fixo.** Identifique primeiro se é bem ou serviço e, se serviço, de que natureza (curso/treinamento, mão de obra dedicada, TI, obra etc.), e faça só as perguntas pertinentes a essa natureza. Exemplo do que evitar: perguntar sobre material didático ou certificado de conclusão numa aquisição de equipamentos — esses itens só cabem quando o objeto é curso, treinamento, capacitação ou especialização.

Percorra cada tópico interagindo com o usuário sempre que a informação não estiver disponível — não preencha tópicos como estimativa de valor, levantamento de mercado ou análise comparativa de soluções com dados fictícios; peça a fonte ou marque o tópico como pendente.

Consulte `references/ipp-agu-orientacoes.md` para saber o que a AGU espera em cada campo. Regra central: **campo não preenchido exige justificativa expressa** (art. 18, §2º) — nunca omita um tópico em silêncio; escreva por que não se aplica. Sustentabilidade em particular: mesmo objetos aparentemente neutros exigem enquadramento no Guia Nacional de Contratações Sustentáveis, e a inaplicabilidade precisa ser justificada pela área técnica.

### Passo 2: Mapa de Riscos

**Antes de elaborar, verifique se ele é exigível**: nas contratações diretas, o gerenciamento de riscos pode ser dispensado (art. 72, I, da Lei nº 14.133/2021), **exceto quanto à fase de gestão do contrato**, e desde que a justificativa seja juntada aos autos. Pergunte ao usuário se ele quer usar essa faculdade antes de produzir um mapa completo.

Leia `references/mapa-riscos-modelo.md`. Contém a estrutura real do órgão (introdução, escala de probabilidade/impacto, tabela-síntese de riscos, um bloco de avaliação por risco, aprovação e assinatura), além de riscos-exemplo observados em contratações reais — use-os como inspiração de nível de detalhe, não como lista fechada a copiar. O IPP é expresso ao exigir pertinência com as especificidades do caso e **vedar indicações genéricas e meramente protocolares**.

O Mapa de Riscos não é documento único: deve ser **atualizado e juntado ao final do ETP, ao final do TR, após a seleção do fornecedor e após eventos relevantes**. Ele também **não se confunde com a matriz de risco** da minuta de contrato, que trata do equilíbrio econômico-financeiro — elaborar um não dispensa o outro.

Os riscos identificados aqui devem alimentar o "modelo de gestão do contrato" do TR (Passo 3) — não trate como um documento isolado.

### Passo 3: Termo de Referência (TR)

O TR segue o modelo disponibilizado pela Advocacia-Geral da União (AGU), que é atualizado periodicamente. A AGU publica um modelo por **tipo de objeto**, e cada modelo já cobre tanto licitação (pregão/concorrência) quanto contratação direta (dispensa/inexigibilidade) na mesma peça, com alternativas marcadas "OU" no texto para cada caso (confirmado por comparação byte a byte dos arquivos publicados nas duas seções do site da AGU):

- `references/termo-referencia-compras.md` — aquisição de bens (compras), exceto TIC.
- `references/termo-referencia-servicos-obras.md` — serviços (com ou sem dedicação exclusiva de mão de obra), obras e serviços de engenharia, exceto TIC. Também serve para contratação integrada/semi-integrada.
- `references/termo-referencia-compras-tic.md` — aquisição de bens de Tecnologia da Informação e Comunicação (TIC).
- `references/termo-referencia-servicos-tic.md` — serviços de Tecnologia da Informação e Comunicação (TIC).

Os modelos de TIC têm seções próprias que os modelos genéricos não têm (alinhamento a PDTIC e à Estratégia de Governo Digital, requisitos organizados por categoria, propriedade intelectual, transferência de conhecimento) — nunca use o modelo genérico de compras/serviços para um objeto de TIC, e vice-versa. Se não estiver claro se o objeto é ou não de TIC, pergunte ao usuário.

Note também que a AGU publica, separadamente, um **Termo de Contrato** para serviços (dividido em com/sem dedicação exclusiva de mão de obra) — esse é o instrumento contratual que cita o TR como anexo, não o TR em si. Está fora do escopo atual desta skill; se o usuário pedir ajuda com o Termo de Contrato, avise que ainda não há suporte para esse documento e pergunte se ele quer que seja adicionado.

Para redigir o TR: identifique o tipo de objeto (compras vs. serviços/obras, TIC vs. não-TIC) para escolher o arquivo certo dentre os quatro acima. A modalidade e o dispositivo legal **já vêm definidos pela triagem do Passo 1** (`references/enquadramento-legal-triagem.md`) — reaproveite-os em vez de perguntar de novo; se o usuário chegou direto ao TR sem ETP, conduza a triagem agora, porque sem ela não é possível escolher as alternativas "OU" do modelo. Pergunte ainda **se a contratação será feita por Sistema de Registro de Preços (SRP)** — isso muda alternativas "OU" do próprio modelo (ex.: critério de aceitabilidade de preços unitários máximos por grupo de itens, e a adequação orçamentária, exigível no SRP apenas antes da assinatura do contrato, não na elaboração do TR) — e as características do caso (regime de execução, dedicação exclusiva de mão de obra, etc.) para saber quais alternativas "OU" do modelo usar. **Risque as alternativas não escolhidas, não as apague** — ver "Regra de ouro" acima.

Consulte `references/ipp-agu-orientacoes.md` (seção "Termo de Referência — como preencher") para o detalhamento do que a AGU espera em cada elemento, especialmente: o prazo de vigência deve ser a **soma** dos prazos de execução, reparo, recebimento provisório, definitivo e pagamento (não um número arbitrário); a diferença entre **garantia do produto/serviço (CDC)** e **garantia de execução do contrato** (arts. 96 a 102), que devem aparecer separadamente; e a definição da forma de aferição/medição do serviço para pagamento com base em resultado, com unidade de medida que evite remunerar por horas ou postos de trabalho.

Como esses modelos são atualizados periodicamente pela AGU, se em algum momento o usuário indicar uma versão mais nova, substitua o arquivo de referência correspondente em vez de tentar mesclar as duas versões.

Reaproveite diretamente do ETP: descrição da solução, requisitos, quantidades, estimativa de valor e resultado do levantamento de mercado. Não peça essas informações de novo ao usuário se já estiverem no ETP gerado nesta mesma conversa — apenas encaixe-as na estrutura do modelo AGU vigente.

### Passo 4: Parecer Técnico (quando aplicável)

Antes de redigir, determine se o Parecer Técnico é exigido para a modalidade em questão:

- **Dispensa ou inexigibilidade de licitação**: exigido.
- **Pregão**: não exigido — não ofereça para elaborar um Parecer Técnico neste caso.
- **Concorrência**: incerto (o próprio usuário não soube confirmar) — pergunte a ele antes de assumir que é ou não exigido; não decida sozinho.

Se exigido, leia `references/parecer-tecnico-topicos.md`, que traz a estrutura comum e, na seção "Enquadramento legal", uma tabela com cada um dos 5 incisos do art. 74 (inexigibilidade) e dos 18 incisos do art. 75 (dispensa) — cada inciso pede uma prova documental e uma seção extra do parecer diferentes (ex.: notória especialização exige currículo/portfólio e seção própria; exclusividade de fornecedor exige atestado de exclusividade; imóvel exige laudo de singularidade).

O inciso exato já deve estar definido pela triagem do Passo 1 e declarado no tópico 5 do ETP — reaproveite-o. Se o usuário chegou direto ao Parecer Técnico, ou se o ETP cita só o artigo sem o inciso, **conduza antes a triagem de `references/enquadramento-legal-triagem.md`**: não pergunte "qual o inciso?" a quem pode não saber responder, e nunca invente o enquadramento nem generalize "dispensa"/"inexigibilidade" sem o inciso. Lembre também o art. 72, que lista os oito documentos de instrução do processo de contratação direta, e o art. 73, que responsabiliza solidariamente contratado e agente público pela contratação direta indevida com dolo, fraude ou erro grosseiro.

### Passo 5: Documentos de menor importância

Se o usuário mencionar outros documentos com template próprio (não cobertos acima), pergunte qual é o template e, se ainda não estiver salvo em `references/`, ofereça para criar um novo arquivo de referência para reutilização futura.

## Avaliação de completude e conformidade

Esta skill também analisa documentação já pronta, em três modos possíveis — pergunte ao usuário qual se aplica quando não estiver óbvio pelo pedido:

1. **Conferência de documento próprio recém-gerado**: releia o documento produzido nesta conversa contra o arquivo de referência correspondente e aponte tópicos faltantes ou rasos.
2. **Revisão de documento de terceiros**: o usuário envia um ETP, TR, Mapa de Riscos ou Parecer já pronto (de outra área/pessoa). Compare tópico a tópico com o arquivo de referência correspondente e com a Lei 14.133/2021, e aponte tanto ausências quanto inconsistências (ex.: TR que contradiz o ETP).
3. **Checklist processual completo**: o usuário quer saber se, para a modalidade da contratação, todos os documentos obrigatórios existem e estão presentes no processo. Use `references/checklist-completude.md` como roteiro. Lembre-o de que esse roteiro é ferramenta de trabalho e **não substitui a Lista de Verificação oficial da AGU**, exigida antes do envio à análise jurídica (Enunciado BPC nº 06 e art. 36 da IN SEGES nº 05/2017) — e que nela **não basta marcar "SIM"/"NÃO"**: é preciso indicar a folha ou o sequencial do sistema onde está cada documento.

Em qualquer um dos três modos, estruture a resposta como uma lista de achados (o que falta, o que está incompleto, o que está conforme) — não como um parecer solto em prosa. Isso facilita a correção pelo usuário.

## Referência transversal: enquadramento legal

`references/enquadramento-legal-triagem.md` é o roteiro de perguntas que descobre **a modalidade e o dispositivo aplicáveis** a partir de fatos que o usuário conhece, sem exigir que ele conheça a lei. Use-o no Passo 1 e sempre que a modalidade ou o inciso não estiverem definidos com artigo, inciso e alínea — inclusive ao revisar documentação de terceiros que cite apenas "art. 75" ou "dispensa". Ele cobre as cinco modalidades do art. 28 (critérios dos arts. 29 a 32), os 5 incisos do art. 74, os 18 incisos do art. 75, e os erros de enquadramento que geram responsabilização pelo art. 73.

O texto integral da lei está em `lei-14133-2021.md` (raiz do projeto), para conferir literalidade quando a triagem não bastar.

## Referência transversal: IPP da AGU

`references/ipp-agu-orientacoes.md` destila o *Instrumento de Padronização dos Procedimentos de Contratação* (AGU/MGI), que é a referência oficial sobre **como preencher** cada artefato — enquanto os modelos de TR dizem *o que* escrever, o IPP diz *como e por quê*. Consulte-o ao elaborar ou revisar qualquer documento, e especialmente quando surgir a dúvida "esse campo pode ficar em branco?" (a resposta quase sempre é não: exige justificativa expressa).

A versão integral do IPP está em `IPP-AGU-fev-2024.md` (raiz do projeto) e cobre também DFD, Portaria de designação da equipe de planejamento, gerenciamento de riscos, pesquisa de preços, declarações orçamentárias, minuta de edital (seção 11), minuta de contrato (seção 12) e adoção do Sistema de Registro de Preços (seção 13) — os três últimos fora do escopo atual de produção desta skill (ver nota sobre o Termo de Contrato no Passo 3), mas úteis para dúvidas pontuais. É uma conversão mais resumida que `ipp-agu-orientacoes.md`: para as seções que este último já distila (DFD, Portaria de EPC, ETP, Mapa de Riscos, Pesquisa de Preços, TR, Autorização, Checklist), prefira sempre `ipp-agu-orientacoes.md`; consulte o arquivo integral apenas para Edital, Contrato ou Registro de Preços.

## Nota sobre os arquivos de referência

Todos os arquivos de `references/` já refletem modelos e exemplos reais fornecidos pelo usuário (TR de compras, serviços/obras e suas variantes de TIC; Mapa de Riscos; Parecer Técnico de dispensa e inexigibilidade; DFD; ETP) — nenhum está mais em estado de placeholder genérico. Ainda assim, trate-os como uma base viva: se o usuário indicar uma versão mais nova de algum modelo AGU, ou fornecer templates adicionais (ex.: para outros documentos de menor importância), atualize o arquivo de referência correspondente.

Os exemplos de DFD, ETP e Parecer Técnico usados para construir `dfd-topicos.md`, `etp-topicos.md` e `parecer-tecnico-topicos.md` continham dados pessoais reais (nomes, CPFs, e-mails) que foram removidos ao generalizar a estrutura — nunca reintroduza dados pessoais de exemplos anteriores desta conversa em um novo documento; sempre peça os dados atuais ao usuário.
