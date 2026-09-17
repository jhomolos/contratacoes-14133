# Tópicos do Estudo Técnico Preliminar (ETP)

Base legal: art. 18, §1º, da Lei 14.133/2021. A numeração e a redação abaixo seguem o modelo real usado pelo órgão do usuário (confirmado por um ETP preenchido de exemplo), que numera os tópicos a partir de 2 — o item 1 é reservado às "Informações Básicas" (número do TR vinculado). Use esta numeração ao produzir o ETP para o usuário.

> **Status**: estrutura confirmada tanto pelo texto de lei quanto por um ETP real do órgão — não é mais placeholder.

0. **Informações Básicas** — número do Termo de Referência ao qual o ETP está vinculado (o TR recebe numeração própria mesmo sendo produzido depois do ETP, porque o número é reservado no início do processo).
1. **Descrição da necessidade da contratação**, considerado o problema a ser resolvido sob a perspectiva do interesse público. Não descreva a solução aqui — só o problema. Reaproveite a "Justificativa da necessidade" do DFD em vez de reescrever do zero.
2. **Área requisitante** — unidade/setor/departamento que demanda a contratação (não previsto expressamente no art. 18 §1º, mas exigido pelo modelo do órgão).
3. **Descrição dos Requisitos da Contratação**, incluindo prazos de garantia, vida útil do bem, regime de execução (contínuo/não contínuo), vedação de subcontratação quando aplicável, exigência ou dispensa de garantia contratual, e enquadramento no Catálogo Eletrônico de Padronização (CATMAT/CATSER) quando existir item padronizado correspondente.
4. **Levantamento de Soluções / Mercado**, com a análise das alternativas possíveis e a justificativa técnica e econômica da escolha da solução — inclua evidências concretas (ex.: registros oficiais, páginas de referência) quando a escolha recair sobre um fornecedor específico. **É aqui que se comprova a inviabilidade de competição** que fundamenta uma inexigibilidade do art. 74: quantos fornecedores foram procurados, o que a pesquisa encontrou. O Parecer Técnico depois invoca esse levantamento — ele não substitui a prova.
5. **Descrição da solução como um todo**, inclusive das exigências relacionadas à manutenção e à assistência técnica, quando for o caso. Declare aqui a **modalidade e o enquadramento legal** definidos na triagem do Bloco 0 (ver `references/enquadramento-legal-triagem.md`), com **artigo, inciso e alínea** quando houver — ex.: "inexigibilidade, art. 74, III, 'f', da Lei nº 14.133/2021". Citar só o artigo é lacuna, não enquadramento.
6. **Estimativa das Quantidades a Serem Contratadas**, acompanhada das memórias de cálculo e dos documentos que lhe dão suporte.
7. **Estimativa do Valor da Contratação**, acompanhada dos preços unitários referenciais e do detalhamento de todos os custos incidentes.
8. **Justificativa para o Parcelamento ou não da Solução.**
9. **Contratações Correlatas e/ou Interdependentes.**
10. **Alinhamento entre a Contratação e o Planejamento** — demonstração da previsão no Plano de Contratações Anual (PCA) e conformidade com a Lei de Responsabilidade Fiscal (art. 16, Lei Complementar nº 101/2000), quando aplicável.
11. **Benefícios a serem alcançados com a contratação** — este é o "demonstrativo dos resultados pretendidos" da lei (economicidade, melhor aproveitamento de recursos), descrito em termos concretos do que a Administração ganha com a contratação.
12. **Providências a Serem Adotadas** pela Administração previamente à celebração do contrato, inclusive quanto à capacitação de servidores para fiscalização e gestão contratual, e à divisão de responsabilidades entre unidades (ex.: fase interna vs. fase externa da contratação).
13. **Possíveis Impactos Ambientais** e respectivas medidas de tratamento, mitigação ou compensação, se for o caso. Se não aplicável, diga isso explicitamente com justificativa breve, em vez de omitir o tópico.
14. **Declaração de Viabilidade** — a Equipe de Planejamento declara viável a contratação com base neste ETP; cite o dispositivo normativo do órgão que rege a declaração (ex.: inciso XIII do art. 9º da IN SEGES/ME nº 58/2022). Este é o "posicionamento conclusivo" da lei e só deve ser escrito depois que todos os outros tópicos estiverem fechados — é uma síntese, não uma introdução.
15. **Responsáveis** — tabela com CPF, nome/posto-graduação e e-mail de cada integrante da Equipe de Planejamento da Contratação. **Peça esses dados ao usuário para cada novo processo** — nunca reaproveite nomes/CPFs de um ETP ou DFD anterior desta conversa.
16. **Anexos** — documentos comprobatórios citados no corpo do ETP (ex.: registros oficiais, páginas de referência, tabelas de preços).

## Entrevista inicial — faça estas perguntas ANTES de redigir

O DFD quase nunca traz contexto suficiente para um ETP defensável. Antes de escrever qualquer tópico, conduza esta entrevista com o usuário. Não presuma respostas: o IPP da AGU (ver `references/ipp-agu-orientacoes.md`) é explícito em que a necessidade "pode inclusive ser distinta a depender da finalidade do órgão, ainda que o objeto indicado pelo setor requisitante seja o mesmo" — ou seja, o mesmo objeto justifica-se de formas diferentes em contextos diferentes, e só o usuário conhece o dele.

**Os blocos abaixo não são um checklist fixo a percorrer identicamente em toda contratação.** Vários itens só fazem sentido para determinada natureza de objeto — estão marcados como condicionais entre parênteses. Antes de entrevistar, identifique com o usuário se o objeto é bem ou serviço e, sendo serviço, de que natureza (curso/treinamento/capacitação, mão de obra dedicada, TI, obra, locação, etc.), e pule as perguntas cuja condição não se aplica. Perguntar sobre material didático ou certificado de conclusão numa aquisição de equipamentos, por exemplo, é sinal de entrevista mal calibrada — o objetivo é uma entrevista enxuta e pertinente, não exaustiva por hábito.

**Bloco 0 — Modalidade e enquadramento legal (faça ANTES de todos os outros blocos)**

Conduza a triagem completa de `references/enquadramento-legal-triagem.md`. Ela faz perguntas **de fato** (o que é o objeto, quanto vale, quantos fornecedores existem, quem é o contratado, há urgência) e conclui qual modalidade e qual dispositivo se aplicam — pregão, concorrência, concurso, leilão, diálogo competitivo, ou contratação direta com o inciso exato do art. 74 ou 75.

Este bloco vem primeiro por três razões:

- **O usuário não tem obrigação de conhecer a lei.** Nunca abra perguntando "qual é o enquadramento legal?" ou "é dispensa ou inexigibilidade?" — ele frequentemente não sabe, e um chute aqui contamina todos os documentos seguintes. Pergunte os fatos e apresente a conclusão para ele confirmar.
- **É no ETP que a modalidade se define**, e o tópico 5 exige a declaração expressa do dispositivo. O TR (Passo 3) escolhe o modelo da AGU e as alternativas "OU" em função dessa definição, então não há como redigi-lo antes.
- **O resultado da triagem pode dispensar o próprio ETP** — ver a seção "Quando o ETP pode ser dispensado" abaixo. Descobrir isso depois de conduzir a entrevista inteira é desperdício de trabalho do usuário.

A triagem também define qual arquivo de referência usar (TIC vs. genérico) e quais dos blocos seguintes são pertinentes.

**Bloco 1 — Necessidade e resultado pretendido** (alimenta os tópicos 1, 11 e 14)
- Como você chegou à conclusão de que precisa do produto desta contratação? O que aconteceu (ou deixou de acontecer) que evidenciou essa necessidade?
- Qual problema, exatamente, esta contratação resolve?
- Qual é a aplicação prática do objeto no dia a dia da área? No caso de capacitação: o que os capacitados farão depois que não conseguem fazer hoje?
- O que se pretende alcançar após a conclusão/entrega — que resultado concreto e verificável?
- Há beneficiários indiretos (outras unidades, outros órgãos, o cidadão)? Como eles se beneficiam?
- O que acontece se a contratação não ocorrer?

**Bloco 2 — Quantidades** (alimenta o tópico 6)
- Qual método foi usado para chegar à quantidade? Há série histórica, dimensionamento de equipe, cálculo de demanda?
- **As quantidades podem ser alteradas?** Confirme os quantitativos do DFD com o usuário em vez de simplesmente copiá-los — o DFD é um ponto de partida, e o ETP é o momento de revisá-lo com base em dados concretos.
- Há interdependência com outras contratações que permita economia de escala?

**Bloco 3 — Composição do objeto e requisitos** (alimenta os tópicos 3 e 5)
- Há fornecimento de insumos, equipamentos, licenças ou qualquer item acessório embutido no objeto? Isso precisa estar explícito.
- (Se o objeto for curso, treinamento, capacitação ou especialização) Haverá fornecimento de material didático, ainda que em formato digital?
- (Se o serviço envolver mão de obra alocada nas dependências do contratante) Haverá fornecimento de uniformes?
- Há exigência de garantia ou assistência técnica?
- Há questões de frete, entrega ou deslocamento?
- Cabe subcontratação?
- Existe item no Catálogo Eletrônico de Padronização (CATMAT/CATSER) que corresponda ao objeto? Se não for usado, é preciso justificar.

**Bloco 4 — Medição do resultado** (alimenta o tópico 11 e o modelo de gestão do TR)
- Como o produto da contratação será medido/aferido? Qual a unidade de medida que permite verificar o resultado?
- Há um modelo de relatório, termo de aceite ou instrumento equivalente que comprove a entrega?
- (Se o objeto for curso, treinamento, capacitação ou especialização) Haverá emissão de certificado de conclusão? Para quem (todos os inscritos ou só aprovados?), e com que requisito de frequência ou aproveitamento?
- Será elaborado Instrumento de Medição de Resultados (IMR)? Se sim, ele deve constar como **anexo do ETP** (IN SEGES/MP nº 05/2017, Anexos V-B e VIII-A).

**Bloco 5 — Garantia** (alimenta o tópico 3)
- Há garantia contratual de execução do serviço (arts. 96 a 102 da Lei nº 14.133/2021)? Se não haverá, é preciso justificar.
- Atenção: a garantia legal do produto/serviço (Código de Defesa do Consumidor) **sempre se aplica** e não se confunde com a garantia de execução do contrato. Registre as duas de forma distinta.

**Bloco 6 — Pagamento** (alimenta os tópicos 7 e 12)
- Há necessidade de antecipação de pagamento? Em caso positivo, quais as condicionantes e garantias adicionais?
- O pagamento será único ou por etapas/parcelas vinculadas a marcos do cronograma?

**Bloco 7 — Sustentabilidade e impactos ambientais** (alimenta o tópico 13)
- Sempre busque enquadramento no **Guia Nacional de Contratações Sustentáveis** da AGU, mesmo em objetos aparentemente neutros (serviços online, capacitação). O IPP exige que critérios de sustentabilidade sejam veiculados como especificação técnica do objeto ou como obrigação da contratada; **se não forem aplicáveis, a decisão precisa ser justificada pela área técnica** — não basta escrever "não se aplica".
- Pergunte: há consumo de energia, material impresso, deslocamento, descarte de equipamentos, logística reversa? Há impacto ambiental positivo (ex.: substituição de deslocamento presencial por solução remota)?

**Bloco 8 — Planejamento e providências** (alimenta os tópicos 10 e 12)
- A contratação está prevista no PCA? Em qual item? Se não estiver, qual medida será adotada para suprir a omissão?
- Há alinhamento com Planejamento Estratégico, PDI ou Plano Diretor de Logística Sustentável do órgão?
- É preciso adequar o ambiente (infraestrutura, sistemas, capacitação de fiscais) antes da contratação surtir efeito? Se sim, isso vira cronograma no tópico 12 **e** um risco no Mapa de Riscos.

## Como preencher cada tópico

- Peça ao usuário os dados que só ele tem (quantitativos, valores de mercado já levantados, prazos, dados dos responsáveis). Não estime valores por conta própria.
- Reaproveite diretamente o que já foi levantado no DFD para os tópicos 1 (necessidade) e 6-7 (quantidades e valor), em vez de pedir de novo ou reescrever do zero.
- O tópico 14 (Declaração de Viabilidade) só deve ser escrito por último.
- Os tópicos 6 e 7 (Estimativa das Quantidades e Estimativa do Valor) da lei aparecem como uma dupla no modelo do órgão — mantenha essa proximidade na redação, já que um normalmente referencia o outro.

## Quando o ETP pode ser dispensado

Art. 14 da IN SEGES/ME nº 58/2022: (a) nas hipóteses dos **incisos I, II, VII e VIII do art. 75** e do **§7º do art. 90** da Lei nº 14.133/2021; (b) na hipótese do **inciso III do art. 75**; e (c) nas **prorrogações de contratos de serviços e fornecimentos contínuos**. Em qualquer caso, **o gestor deve justificar expressamente nos autos a posição adotada** — por exemplo, que a elaboração é incompatível com a urgência da contratação.

Antes de elaborar um ETP completo, verifique se o caso se enquadra em alguma dessas hipóteses e pergunte ao usuário se ele pretende usar a faculdade. Se usar, o que entra nos autos é a justificativa da dispensa, não um ETP abreviado.

Essa verificação é resultado direto do **Bloco 0** da entrevista: como as hipóteses dependem do inciso do art. 75 aplicável, só a triagem de enquadramento revela se o ETP é exigível. Na contratação direta, o art. 72, I, também admite o ETP, a análise de riscos e o TR apenas "se for o caso".

## Estimativa do valor: o ETP não encerra a pesquisa de preços

O tópico 7 do ETP traz a estimativa, mas a **pesquisa de preços é artefato próprio**, regida pelo art. 23 da Lei nº 14.133/2021 e pela **IN SEGES/ME nº 65/2021**, e se materializa em dois documentos que precisam estar nos autos:

1. a **planilha com os preços pesquisados** (com todos os preços coletados, indicando quais compuseram a cesta e quais foram desconsiderados e por quê); e
2. o **Relatório da Pesquisa de Preços / Nota Técnica**, com a análise crítica (conteúdo mínimo no art. 3º da IN 65/2021).

Parâmetros, metodologia (média/mediana/menor), cuidados na pesquisa direta com fornecedores e o regime especial das contratações diretas estão detalhados em `references/ipp-agu-orientacoes.md`, seções "Pesquisa de preços" e "Relatório da Pesquisa de Preços / Nota Técnica". Dois pontos que o ETP costuma deixar passar:

- é obrigatório registrar **a listagem dos fornecedores consultados, a justificativa da escolha de cada um e quais deixaram de responder**;
- as memórias de cálculo e documentos de suporte **podem constar de anexo classificado**, se a Administração optar por preservar o sigilo do orçamento até a conclusão da licitação (art. 24).

## Ligação com o Mapa de Riscos

Se o tópico 12 (Providências a serem Adotadas) apontar necessidade de adequação do ambiente — infraestrutura, sistemas, capacitação de fiscais —, o IPP determina que essa providência seja **incluída no Mapa de Riscos como fator de risco** ao sucesso da contratação, caso não seja implementada a tempo. Além disso, o Mapa de Riscos deve ser **atualizado e juntado ao final da elaboração do ETP** (e novamente ao final do TR).

## Instrumento de Medição de Resultados (IMR)

Em contratações de serviços, quando houver IMR ou instrumento substituto, ele deve constar como **anexo dos Estudos Preliminares** (IN SEGES/MP nº 05/2017, Anexos V-B e VIII-A) — não apenas ser mencionado no TR. O IPP observa que os resultados pretendidos devem ser **constantemente revisitados até a elaboração final do TR**, porque é a clareza deles que permite estipular níveis de qualidade e as respectivas adequações de pagamento.
