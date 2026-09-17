# Tópicos do Estudo Técnico Preliminar (ETP) — Tecnologia da Informação e Comunicação (TIC)

Fonte: ETP real do órgão do usuário (aquisição de software especializado), com base na Instrução Normativa SGD/ME nº 94/2022. É substancialmente mais detalhado que o ETP genérico (`references/etp-topicos.md`) — use este arquivo, não o genérico, quando o objeto for de TIC. Dados pessoais e o conteúdo dos anexos do exemplo original (páginas de fornecedor, e-mails com representantes comerciais) foram removidos; mantenha apenas a estrutura de tópicos.

## Estrutura

0. **Informações Básicas** — número do processo.
1. **Descrição da necessidade** — o problema institucional a ser resolvido, não a solução. Reaproveite do DFD.
2. **Área requisitante** — unidade/setor e responsável.
3. **Necessidades de Negócio** — por que, do ponto de vista do negócio/missão institucional, a solução é necessária (não é sobre tecnologia ainda, é sobre o problema organizacional).
4. **Necessidades Tecnológicas** — os requisitos técnicos que a solução de TIC precisa atender (protocolos, interoperabilidade, customização, tipo de licenciamento, etc.).
5. **Demais requisitos necessários e suficientes à escolha da solução de TIC** — lista de itens que ainda serão detalhados no TR: qualificação técnica exigida, forma de composição do preço estimado, classificação e forma de seleção do fornecedor, minuta do termo de contrato, prazos/duração/forma de pagamento, declarações de ciência, obrigações da contratada/contratante, sanções cabíveis.
6. **Requisitos de Sustentabilidade** — com base no Guia Nacional de Contratações Sustentáveis, mesmo quando o objeto (ex.: software) aparenta não ter impacto ambiental direto — justifique a aplicabilidade ou não.
7. **Indicação de marcas ou modelos** (art. 41, inciso I, da Lei nº 14.133/2021) — quando a contratação admitir indicação de marca específica, justifique tecnicamente por que apenas aquela marca/produto atende à necessidade.
8. **Vistoria** — se aplicável ao objeto (normalmente não aplicável a soluções fornecidas remotamente/online).
9. **Condições de execução** — dinâmica de entrega, incluindo cronograma detalhado (tabela Etapa / Descrição / Prazo, com marcos relativos à data de assinatura do contrato, ex. "t0 + 30 dias").
10. **Estimativa da demanda — quantidade de bens e serviços** — quantitativos de cada item da solução (licenças, suporte, treinamento, etc.), com a vigência de cada um.
11. **Levantamento de soluções** — liste as alternativas de solução consideradas (tipicamente: solução open source/pronta no mercado; desenvolvimento próprio; contratação de solução especializada de mercado), não apenas a escolhida.
12. **Análise comparativa de soluções** — para cada alternativa do tópico anterior, uma análise do que ela envolveria.
13. **Registro de soluções consideradas inviáveis** — para cada alternativa descartada, documente a razão concreta (limitação técnica, falta de interoperabilidade, custo/complexidade de desenvolvimento próprio, etc.), citando evidências em anexo quando houver (pesquisa em catálogo público, resposta de fornecedor, ficha técnica).
14. **Análise comparativa de custos (TCO — Total Cost of Ownership)** — metodologia de precificação (ex.: média de preços pesquisados, conforme art. 23 da Lei 14.133/2021 e IN SEGES/ME nº 65/2021), valores unitários e total, índice de reajuste aplicável (ex.: Índice de Custo da Tecnologia da Informação — ICTI).
15. **Descrição da solução de TIC a ser contratada** — a solução escolhida, com justificativa objetiva de por que foi selecionada frente às alternativas do levantamento.
16. **Estimativa de custo total da contratação** — detalhamento de valores por item e total.
17. **Justificativa técnica da escolha da solução** — por que a solução escolhida é tecnicamente superior às alternativas (menor risco, suporte especializado, atualizações contínuas, conformidade com normas, escalabilidade/interoperabilidade).
18. **Justificativa econômica da escolha da solução** — por que compensa financeiramente frente a alternativas gratuitas ou de desenvolvimento próprio.
19. **Benefícios a serem alcançados com a contratação** — em termos concretos (produtividade, conformidade normativa, redução de custos, etc.).
20. **Providências a serem Adotadas** — o que precisa ser feito antes da contratação (infraestrutura já disponível ou a preparar, designação de equipes de recebimento/fiscalização).
21. **Declaração de Viabilidade** + **Justificativa da Viabilidade** — síntese conclusiva; só escrever por último.
22. **Responsáveis** — equipe de planejamento/comissão de contratação e autoridade competente. **Peça esses dados ao usuário para cada novo processo**; nunca reaproveite nomes de um ETP anterior.
23. **Anexos** — evidências citadas ao longo do documento (pesquisas de mercado, comprovação de soluções descartadas, cotações, prints de catálogos oficiais). Referencie-os pelo número (Anexo I, II, III...) mas não é necessário reproduzir o conteúdo do anexo dentro do ETP.

## Como preencher

- Os tópicos 11-14 (levantamento de soluções, análise comparativa, registro de soluções inviáveis, TCO) são o núcleo do ETP de TIC e o que mais diferencia esse modelo do genérico — não os trate como opcionais nem os resuma demais; a ausência de uma comparação real de alternativas é o motivo mais comum de glosa em contratações de TIC.
- Peça ao usuário os valores de mercado, protocolos técnicos exigidos e nomes de soluções concorrentes reais — não invente concorrentes ou valores para preencher a análise comparativa.
- Reaproveite do DFD a descrição da necessidade (tópico 1) e do TR de TIC (se já elaborado) os requisitos técnicos, e vice-versa — não peça a mesma informação duas vezes.

## Orientações do IPP da AGU aplicáveis também ao ETP de TIC

O IPP (`references/ipp-agu-orientacoes.md`) não tem seção específica de TIC, mas suas regras de preenchimento do ETP incidem integralmente aqui. As mais relevantes para este modelo:

- **Necessidade (tópico 1)**: deve abordar obrigatoriamente três coisas — o **problema identificado**, a **real necessidade gerada por ele** e **o que se almeja alcançar**. Ainda que já conste do DFD, a justificativa deve ser **robustecida**, não copiada.
- **Necessidades de Negócio e Tecnológicas (tópicos 3 e 4)**: correspondem ao tópico "Requisitos da contratação" do ETP genérico. Se o levantamento indicar **número restrito de fornecedores**, o IPP manda **verificar se os requisitos eleitos são realmente indispensáveis**, avaliando retirá-los ou flexibilizá-los (art. 9º, I, §2º, da IN SEGES/ME nº 58/2022). Em TIC, requisitos técnicos excessivos são a principal causa de direcionamento involuntário — revise-os com esse filtro antes de fechar o documento.
- **Sustentabilidade (tópico 6)**: critérios devem ser veiculados **como especificação técnica do objeto ou como obrigação da contratada**, observado o Guia Nacional de Contratações Sustentáveis; **a inaplicabilidade deve ser justificada pela área técnica**, não apenas afirmada.
- **Indicação de marca (tópico 7)**: qualquer direcionamento de marca exige **justificativa técnica**, sob pena de enquadramento como restrição indevida à competitividade. Em software, certifique-se também de que o objeto **não se enquadra como bem de luxo** (art. 20 da Lei nº 14.133/2021 e Decreto nº 10.818/2021) e verifique a existência de item padronizado no **Catálogo Eletrônico de Padronização** (PNCP) — se não usar o catálogo, justifique.
- **Estimativa da demanda (tópico 10)**: indicar **o método** de apuração, com memórias de cálculo e documentos de suporte; o processo deve ser **autoexplicativo**, porque "a memória sobre as circunstâncias envolvidas nas decisões vai se perdendo ao longo do tempo".
- **TCO e estimativa de custo (tópicos 14 e 16)**: regidos pela **IN SEGES/ME nº 65/2021**. Registrar obrigatoriamente a **lista de fornecedores consultados, a justificativa da escolha de cada um e quais não responderam**; justificar a metodologia (média, mediana, menor ou outra) e a **desconsideração de valores inexequíveis, inconsistentes ou excessivamente elevados**. Se a contratação for direta, aplica-se o regime do **art. 7º da IN 65/2021** — inclusive a regra de que **é vedada a inexigibilidade se a justificativa de preços demonstrar a possibilidade de competição** (§3º). Em TIC, onde o levantamento de soluções (tópicos 11-13) mapeia concorrentes explicitamente, essa contradição é fácil de surgir: se o tópico 13 descartou concorrentes por não atenderem a requisitos, a fundamentação precisa ser técnica e robusta, não uma preferência.
- **Providências (tópico 20)**: se houver necessidade de adequação do ambiente (infraestrutura, capacitação de fiscais), elaborar **cronograma com atividades e responsáveis** e **incluir essa providência no Mapa de Riscos como fator de risco** caso não seja implementada a tempo.
- **Transferência de conhecimento**: o IPP arrola a eventual necessidade de **transição contratual com transferência de conhecimento, tecnologia e técnicas empregadas** como obrigação da contratada a ser avaliada nos requisitos — particularmente relevante em TIC e já presente no modelo de TR de TIC da AGU.
- **Anexos (tópico 23)**: vão na aba "Anexos" do ETP Digital. Avaliar a necessidade de **classificar o ETP** nos termos da Lei nº 12.527/2011.
- **Dispensa do ETP**: as hipóteses do art. 14 da IN SEGES/ME nº 58/2022 valem também para TIC — ver `references/etp-topicos.md`, seção "Quando o ETP pode ser dispensado".
