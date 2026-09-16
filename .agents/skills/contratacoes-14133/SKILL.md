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

Se o DFD estiver incompleto para permitir um ETP consistente (falta a descrição da necessidade, por exemplo), pergunte ao usuário antes de prosseguir — não invente a necessidade da contratação. Nunca reaproveite nomes, CPFs ou e-mails de um DFD/ETP/Portaria anterior desta conversa para preencher os campos de identificação de outro processo — são pessoas e processos diferentes; peça os dados de novo ou peça a publicação correspondente.

### Passo 1: Estudo Técnico Preliminar (ETP)

Se o objeto **não** for de TIC, leia `references/etp-topicos.md` para os tópicos obrigatórios e a numeração usada pelo órgão. Se o objeto **for** de TIC, use `references/etp-tic-topicos.md` em vez do genérico — a estrutura de TIC é substancialmente mais detalhada (levantamento e análise comparativa de soluções alternativas, registro de soluções inviáveis, TCO) e não deve ser substituída pela genérica.

**Antes de redigir, conduza a entrevista inicial** descrita em `references/etp-topicos.md` (seção "Entrevista inicial"). O DFD quase nunca traz contexto suficiente: é preciso entender como o usuário concluiu que precisa do objeto, qual problema exatamente ele resolve, qual a aplicação prática, o que se pretende alcançar depois, e quem são os beneficiários indiretos. Trate também insumos/material didático, forma de medição do resultado, garantia, antecipação de pagamento e sustentabilidade. **As quantidades do DFD são ponto de partida, não dado fechado** — confirme-as com o usuário.

Percorra cada tópico interagindo com o usuário sempre que a informação não estiver disponível — não preencha tópicos como estimativa de valor, levantamento de mercado ou análise comparativa de soluções com dados fictícios; peça a fonte ou marque o tópico como pendente.

Consulte `references/ipp-agu-orientacoes.md` para saber o que a AGU espera em cada campo. Regra central: **campo não preenchido exige justificativa expressa** (art. 18, §2º) — nunca omita um tópico em silêncio; escreva por que não se aplica. Sustentabilidade em particular: mesmo objetos aparentemente neutros exigem enquadramento no Guia Nacional de Contratações Sustentáveis, e a inaplicabilidade precisa ser justificada pela área técnica.

### Passo 2: Mapa de Riscos

Leia `references/mapa-riscos-modelo.md`. Contém a estrutura real do órgão (introdução, escala de probabilidade/impacto, tabela-síntese de riscos, um bloco de avaliação por risco, aprovação e assinatura), além de riscos-exemplo observados em contratações reais — use-os como inspiração de nível de detalhe, não como lista fechada a copiar.

Os riscos identificados aqui devem alimentar o "modelo de gestão do contrato" do TR (Passo 3) — não trate como um documento isolado.

### Passo 3: Termo de Referência (TR)

O TR segue o modelo disponibilizado pela Advocacia-Geral da União (AGU), que é atualizado periodicamente. A AGU publica um modelo por **tipo de objeto**, e cada modelo já cobre tanto licitação (pregão/concorrência) quanto contratação direta (dispensa/inexigibilidade) na mesma peça, com alternativas marcadas "OU" no texto para cada caso (confirmado por comparação byte a byte dos arquivos publicados nas duas seções do site da AGU):

- `references/termo-referencia-compras.md` — aquisição de bens (compras), exceto TIC.
- `references/termo-referencia-servicos-obras.md` — serviços (com ou sem dedicação exclusiva de mão de obra), obras e serviços de engenharia, exceto TIC. Também serve para contratação integrada/semi-integrada.
- `references/termo-referencia-compras-tic.md` — aquisição de bens de Tecnologia da Informação e Comunicação (TIC).
- `references/termo-referencia-servicos-tic.md` — serviços de Tecnologia da Informação e Comunicação (TIC).

Os modelos de TIC têm seções próprias que os modelos genéricos não têm (alinhamento a PDTIC e à Estratégia de Governo Digital, requisitos organizados por categoria, propriedade intelectual, transferência de conhecimento) — nunca use o modelo genérico de compras/serviços para um objeto de TIC, e vice-versa. Se não estiver claro se o objeto é ou não de TIC, pergunte ao usuário.

Note também que a AGU publica, separadamente, um **Termo de Contrato** para serviços (dividido em com/sem dedicação exclusiva de mão de obra) — esse é o instrumento contratual que cita o TR como anexo, não o TR em si. Está fora do escopo atual desta skill; se o usuário pedir ajuda com o Termo de Contrato, avise que ainda não há suporte para esse documento e pergunte se ele quer que seja adicionado.

Para redigir o TR: identifique o tipo de objeto (compras vs. serviços/obras, TIC vs. não-TIC) para escolher o arquivo certo dentre os quatro acima, depois pergunte a modalidade (licitação ou contratação direta) e as características do caso (regime de execução, dedicação exclusiva de mão de obra, etc.) para saber quais alternativas "OU" do modelo usar. **Risque as alternativas não escolhidas, não as apague** — ver "Regra de ouro" acima.

Consulte `references/ipp-agu-orientacoes.md` (seção "Termo de Referência — como preencher") para o detalhamento do que a AGU espera em cada elemento, especialmente: o prazo de vigência deve ser a **soma** dos prazos de execução, reparo, recebimento provisório, definitivo e pagamento (não um número arbitrário); a diferença entre **garantia do produto/serviço (CDC)** e **garantia de execução do contrato** (arts. 96 a 102), que devem aparecer separadamente; e a definição da forma de aferição/medição do serviço para pagamento com base em resultado, com unidade de medida que evite remunerar por horas ou postos de trabalho.

Como esses modelos são atualizados periodicamente pela AGU, se em algum momento o usuário indicar uma versão mais nova, substitua o arquivo de referência correspondente em vez de tentar mesclar as duas versões.

Reaproveite diretamente do ETP: descrição da solução, requisitos, quantidades, estimativa de valor e resultado do levantamento de mercado. Não peça essas informações de novo ao usuário se já estiverem no ETP gerado nesta mesma conversa — apenas encaixe-as na estrutura do modelo AGU vigente.

### Passo 4: Parecer Técnico (quando aplicável)

Antes de redigir, determine se o Parecer Técnico é exigido para a modalidade em questão:

- **Dispensa ou inexigibilidade de licitação**: exigido.
- **Pregão**: não exigido — não ofereça para elaborar um Parecer Técnico neste caso.
- **Concorrência**: incerto (o próprio usuário não soube confirmar) — pergunte a ele antes de assumir que é ou não exigido; não decida sozinho.

Se exigido, leia `references/parecer-tecnico-topicos.md`, que traz a estrutura comum e as diferenças específicas entre dispensa (fundamentação no art. 75) e inexigibilidade (fundamentação no art. 74, com seção adicional de comprovação de exclusividade). Pergunte a modalidade e o inciso legal aplicável ao usuário, ou deduza do ETP se ele já tiver essa análise — não invente o enquadramento legal.

### Passo 5: Documentos de menor importância

Se o usuário mencionar outros documentos com template próprio (não cobertos acima), pergunte qual é o template e, se ainda não estiver salvo em `references/`, ofereça para criar um novo arquivo de referência para reutilização futura.

## Avaliação de completude e conformidade

Esta skill também analisa documentação já pronta, em três modos possíveis — pergunte ao usuário qual se aplica quando não estiver óbvio pelo pedido:

1. **Conferência de documento próprio recém-gerado**: releia o documento produzido nesta conversa contra o arquivo de referência correspondente e aponte tópicos faltantes ou rasos.
2. **Revisão de documento de terceiros**: o usuário envia um ETP, TR, Mapa de Riscos ou Parecer já pronto (de outra área/pessoa). Compare tópico a tópico com o arquivo de referência correspondente e com a Lei 14.133/2021, e aponte tanto ausências quanto inconsistências (ex.: TR que contradiz o ETP).
3. **Checklist processual completo**: o usuário quer saber se, para a modalidade da contratação, todos os documentos obrigatórios existem e estão presentes no processo. Use `references/checklist-completude.md` como roteiro.

Em qualquer um dos três modos, estruture a resposta como uma lista de achados (o que falta, o que está incompleto, o que está conforme) — não como um parecer solto em prosa. Isso facilita a correção pelo usuário.

## Referência transversal: IPP da AGU

`references/ipp-agu-orientacoes.md` destila o *Instrumento de Padronização dos Procedimentos de Contratação* (AGU/MGI), que é a referência oficial sobre **como preencher** cada artefato — enquanto os modelos de TR dizem *o que* escrever, o IPP diz *como e por quê*. Consulte-o ao elaborar ou revisar qualquer documento, e especialmente quando surgir a dúvida "esse campo pode ficar em branco?" (a resposta quase sempre é não: exige justificativa expressa).

O PDF completo (93 páginas) está em `modelos-outros/IPP-AGU-fev-2024.pdf` e cobre também DFD, Portaria de designação da equipe de planejamento (com modelo), gerenciamento de riscos, pesquisa de preços, declarações orçamentárias, minuta de edital, minuta de contrato, registro de preços e a Lista de Verificação (checklist) da AGU. Consulte-o diretamente quando precisar de um desses temas.

## Nota sobre os arquivos de referência

Todos os arquivos de `references/` já refletem modelos e exemplos reais fornecidos pelo usuário (TR de compras, serviços/obras e suas variantes de TIC; Mapa de Riscos; Parecer Técnico de dispensa e inexigibilidade; DFD; ETP) — nenhum está mais em estado de placeholder genérico. Ainda assim, trate-os como uma base viva: se o usuário indicar uma versão mais nova de algum modelo AGU, ou fornecer templates adicionais (ex.: para outros documentos de menor importância), atualize o arquivo de referência correspondente.

Os exemplos de DFD, ETP e Parecer Técnico usados para construir `dfd-topicos.md`, `etp-topicos.md` e `parecer-tecnico-topicos.md` continham dados pessoais reais (nomes, CPFs, e-mails) que foram removidos ao generalizar a estrutura — nunca reintroduza dados pessoais de exemplos anteriores desta conversa em um novo documento; sempre peça os dados atuais ao usuário.
