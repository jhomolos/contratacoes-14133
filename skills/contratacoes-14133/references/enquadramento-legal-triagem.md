# Triagem de enquadramento legal — descobrir a modalidade e o dispositivo aplicável

Fonte: texto literal dos arts. 6º (XIII, XIV, XV), 28 a 32 e 72 a 75 da Lei nº 14.133/2021, conferido em `lei-14133-2021.md` (conversão do texto do Planalto).

## Para que serve este arquivo

O usuário desta skill quase nunca sabe, de antemão, se sua contratação é pregão, concorrência, dispensa ou inexigibilidade — e muito menos qual dos 5 incisos do art. 74 ou dos 18 incisos do art. 75 se aplica. **Ele não precisa saber: é a skill que deve descobrir, fazendo perguntas de fato.**

A divisão de trabalho entre os arquivos de referência é esta:

| Arquivo | Responde |
|---|---|
| **este arquivo** | *Qual* dispositivo se aplica ao caso — a partir de perguntas sobre fatos, não sobre direito |
| `parecer-tecnico-topicos.md` | Uma vez conhecido o dispositivo, *que prova documental* juntar e *que seção* escrever no Parecer Técnico |

Nunca pergunte ao usuário "qual é o enquadramento legal?" como primeira pergunta. Pergunte os **fatos** desta triagem e apresente a conclusão para ele confirmar.

## Por que a triagem vem no início do ETP, e não depois

Três razões, todas de ordem prática:

1. **É no ETP que se define a modalidade.** O ETP é o documento em que a Administração entende o que está contratando; o enquadramento é consequência desse entendimento, e o tópico 5 do ETP exige a declaração expressa do dispositivo quando houver contratação direta.
2. **Sem ETP não há TR.** O Termo de Referência escolhe o modelo da AGU e as alternativas "OU" internas em função da modalidade — não é possível redigi-lo antes.
3. **A própria exigibilidade do ETP depende do resultado da triagem.** Pelo art. 14 da IN SEGES/ME nº 58/2022, o ETP é dispensável nas hipóteses dos **incisos I, II, III, VII e VIII do art. 75**, do **§7º do art. 90**, e nas **prorrogações de contratos de serviços e fornecimentos contínuos** — em todos os casos exigindo justificativa expressa nos autos. Se a triagem cair num desses incisos, pergunte ao usuário se ele pretende usar a faculdade: pode não haver ETP a elaborar, e sim uma justificativa a juntar aos autos. Do mesmo modo, o art. 72, I, admite que o ETP, a análise de riscos e o TR entrem "se for o caso" na contratação direta.

Conduza a triagem **antes** dos Blocos 1 a 8 da entrevista do ETP. As respostas também definem quais desses blocos fazem sentido.

## Etapa 1 — Natureza do objeto

Quatro perguntas que condicionam todo o resto (inclusive qual arquivo de ETP e de TR usar):

1. **É compra (bem), serviço, ou obra/serviço de engenharia?** Se for serviço, é serviço comum ou obra/serviço de engenharia disfarçado? Reforma, instalação, adaptação predial e manutenção predial estrutural costumam ser serviço de engenharia — o que muda o limite de valor da dispensa (art. 75, I, e não II) e proíbe o pregão.
2. **É de Tecnologia da Informação e Comunicação (TIC)?** Define `etp-tic-topicos.md` vs. `etp-topicos.md` e qual dos quatro modelos de TR usar.
3. **Se for serviço: há dedicação exclusiva de mão de obra** (pessoas alocadas nas dependências do contratante)? E é **serviço contínuo** (necessidade permanente ou prolongada, art. 6º, XV) ou por escopo?
4. **Os padrões de desempenho e qualidade do objeto podem ser definidos objetivamente por especificações usuais de mercado?**
   - Sim → **bem ou serviço comum** (art. 6º, XIII).
   - Não, por alta heterogeneidade ou complexidade → **bem ou serviço especial** (art. 6º, XIV), e a lei **exige justificativa prévia do contratante** para essa classificação. Registre-a no ETP.

Esta quarta pergunta é a que decide pregão vs. concorrência mais adiante — faça-a sempre, mesmo que pareça óbvia.

## Etapa 2 — Triagem de contratação direta

Percorra as baterias abaixo na ordem. Elas vão do mais objetivo e frequente (valor, quem é o contratado) ao mais especializado. **Pare quando encontrar uma hipótese que se aplique, mas continue a leitura das demais baterias** — mais de uma pode caber, e a Etapa 4 diz como escolher.

Se **nenhuma** hipótese se aplicar, a contratação é por licitação: vá para a Etapa 3.

### Bateria A — Valor (art. 75, I e II)

- **Qual o valor total estimado da contratação?**
- **É obra ou serviço de engenharia, ou serviço de manutenção de veículo automotor do órgão?**
  - Sim, e abaixo do limite → **art. 75, I** (valor nominal na lei: R$ 100.000,00).
  - Não (compra ou outro serviço), e abaixo do limite → **art. 75, II** (valor nominal na lei: R$ 50.000,00).

Cuidados obrigatórios antes de fechar por valor:

- **Os limites são atualizados periodicamente por decreto** (a lei registra Decretos nº 10.922/2021, 11.317/2022, 11.871/2023, 12.343/2024 e 12.807/2025). **Nunca use o valor nominal da lei como se fosse o vigente** — pergunte ao usuário o limite atualizado ou avise que é preciso confirmar o decreto em vigor na data da contratação.
- **Fracionamento (art. 75, §1º) — este é o erro mais comum e o mais penalizado.** Pergunte sempre: *"quanto a sua unidade gestora já gastou neste exercício financeiro com objetos de mesma natureza (mesmo ramo de atividade)?"* O limite se afere pelo **somatório do exercício**, não pelo valor desta contratação isolada. Se o somatório estourar o limite, a dispensa por valor **não está disponível** e a contratação vai para licitação (ou para outra hipótese de dispensa, se houver).
- **Consórcio público, autarquia ou fundação qualificada como agência executiva** têm os limites **duplicados** (§2º). Pergunte a natureza jurídica do órgão.
- **Manutenção de veículo do próprio órgão até R$ 8.000,00, incluído fornecimento de peças, não entra no somatório do §1º** (§7º).
- Estas contratações são **preferencialmente precedidas de aviso em sítio eletrônico oficial por no mínimo 3 dias úteis** com manifestação de interesse em propostas adicionais (§3º), e **preferencialmente pagas por cartão de pagamento** com extrato divulgado no PNCP (§4º). Registre no ETP se o aviso será ou não publicado — e justifique a omissão.

### Bateria B — Quem é o contratado

Pergunte **quem** será contratado, em termos de natureza jurídica. Um usuário leigo raramente percebe que a identidade do contratado, por si só, pode autorizar a contratação direta:

- **Órgão ou entidade da própria Administração Pública, criado especificamente para produzir aquele bem ou prestar aquele serviço**, e o preço é compatível com o mercado → **art. 75, IX**.
- **Ente federativo ou entidade de sua Administração indireta**, em contrato de programa para serviço público prestado de forma associada (autorizado em consórcio público ou convênio de cooperação) → **art. 75, XI**.
- **Associação de pessoas com deficiência**, sem fins lucrativos, de comprovada idoneidade, com serviços prestados **exclusivamente** por pessoas com deficiência e preço de mercado → **art. 75, XIV**.
- **Instituição brasileira sem fins lucrativos** cuja finalidade estatutária seja apoiar, captar e executar ensino, pesquisa, extensão, desenvolvimento institucional, científico e tecnológico e inovação (inclusive gerir administrativa e financeiramente essas atividades) — a clássica **fundação de apoio** — ou **instituição dedicada à recuperação social de pessoa presa**, em ambos os casos com inquestionável reputação ética e profissional → **art. 75, XV**.
- **Produtor público de produtos estratégicos para a saúde, por intermédio de fundação de apoio criada para esse fim antes da vigência da Lei**, com preço de mercado → **art. 75, XVI**. Atenção: este inciso teve redações sucessivas (MP nº 1.166/2023 com vigência encerrada, Lei nº 14.628/2023 e Lei nº 15.471/2026) — confirme a redação vigente antes de citar.
- **Entidade privada sem fins lucrativos**, para implementar cisternas ou outras tecnologias sociais de acesso à água para famílias rurais de baixa renda atingidas pela seca ou falta regular de água → **art. 75, XVII**.
- **Entidade privada sem fins lucrativos**, para implementar o **Programa Cozinha Solidária** → **art. 75, XVIII**.
- **ICT pública ou agência de fomento** (seu próprio órgão) contratando transferência de tecnologia ou licenciamento de direito de uso ou exploração de criação protegida, com vantagem demonstrada → **art. 75, IV, "d"**.
- Contratação para cumprir os **arts. 3º, 3º-A, 4º, 5º ou 20 da Lei de Inovação (nº 10.973/2004)** → **art. 75, V**.

### Bateria C — Urgência e situação excepcional

- **Há guerra, estado de defesa, estado de sítio, intervenção federal ou grave perturbação da ordem?** → **art. 75, VII**.
- **Há emergência ou calamidade pública, com urgência de atendimento de situação que possa ocasionar prejuízo ou comprometer a continuidade dos serviços públicos ou a segurança de pessoas, obras, serviços, equipamentos e outros bens?** → **art. 75, VIII**. Se sim, faça estas perguntas de controle, porque o inciso é o mais restritivo da lei:
  - A contratação se limita **aos bens necessários ao atendimento da situação** e **às parcelas de obras e serviços concluíveis em até 1 ano** contado da ocorrência? Além disso não cabe.
  - O contrato **não será prorrogado** e a empresa **não foi contratada antes com base neste mesmo inciso**? Ambas são vedações expressas.
  - O objetivo é **manter a continuidade do serviço público** e os preços observam o art. 23 (§6º)? A emergência **não dispensa pesquisa de preços**.
  - Estão sendo adotadas as providências para **concluir o processo licitatório** regular? O §6º ressalva expressamente a **apuração de responsabilidade dos agentes públicos que deram causa à situação emergencial** — se a urgência decorre de desídia no planejamento (contrato que venceu sem substituto), avise o usuário desse risco.
- **A contratação pode acarretar comprometimento da segurança nacional**, em caso estabelecido pelo Ministro de Estado da Defesa mediante demanda dos comandos das Forças Armadas ou de ministérios? → **art. 75, VI**.
- **A União precisa intervir no domínio econômico para regular preços ou normalizar o abastecimento?** → **art. 75, X**.

### Bateria D — Licitação anterior que não deu resultado

- **Houve licitação para este mesmo objeto há menos de 1 ano?** Se sim:
  - **Não apareceram licitantes interessados ou não houve propostas válidas** (licitação deserta) → **art. 75, III, "a"**.
  - **As propostas trouxeram preços manifestamente superiores aos de mercado ou incompatíveis com os fixados por órgãos oficiais** (licitação fracassada por preço) → **art. 75, III, "b"**.
  - Pergunta de controle indispensável: **a contratação vai manter todas as condições definidas naquele edital?** Se as condições mudarem, o inciso III não se aplica — é caso de nova licitação.

### Bateria E — Natureza específica do objeto (art. 75, IV)

Pergunte se o objeto é um destes. São hipóteses fechadas e pouco intuitivas; vale ler a lista ao usuário em vez de esperar que ele se lembre:

| Alínea | Pergunta a fazer |
|---|---|
| **"a"** | São peças, componentes ou bens (nacionais ou estrangeiros) para **manutenção de equipamento**, comprados do **fornecedor original**, **durante o período de garantia técnica**, porque comprar de terceiro **faria perder a garantia**? A condição de exclusividade tem de ser *indispensável para a vigência da garantia* — fora do período de garantia, esta alínea não serve |
| **"b"** | A contratação decorre de **acordo internacional específico aprovado pelo Congresso Nacional**, com condições manifestamente vantajosas? |
| **"c"** | São **produtos para pesquisa e desenvolvimento**? (limite nominal de R$ 300.000,00 quando se tratar de obras e serviços de engenharia, também sujeito a atualização por decreto; §5º remete a procedimentos especiais de regulamentação própria) |
| **"d"** | Ver Bateria B (ICT/agência de fomento) |
| **"e"** | São **hortifrutigranjeiros, pães ou outros gêneros perecíveis**, pelo período necessário até concluir a licitação, contratados **com base no preço do dia**? |
| **"f"** | É bem ou serviço produzido/prestado no País que envolve, **cumulativamente**, **alta complexidade tecnológica e defesa nacional**? |
| **"g"** | É **material de uso das Forças Armadas** (exceto material de uso pessoal e administrativo), para manter a **padronização exigida pelo apoio logístico** de meios navais, aéreos ou terrestres, **mediante autorização do comandante da força**? |
| **"h"** | São bens e serviços para **contingente militar brasileiro em operação de paz no exterior**? (exige justificativa de preço e de escolha do fornecedor, **ratificada pelo comandante da força**) |
| **"i"** | É **abastecimento ou suprimento de efetivo militar em estada eventual de curta duração** em porto, aeroporto ou localidade diferente da sede, por movimentação operacional ou adestramento? |
| **"j"** | É **coleta, processamento e comercialização de resíduos sólidos urbanos recicláveis**, em área com coleta seletiva, por **associação ou cooperativa formada exclusivamente por pessoas físicas de baixa renda reconhecidas como catadores**, com equipamentos compatíveis com as normas técnicas, ambientais e de saúde pública? |
| **"k"** | É **aquisição ou restauração de obra de arte ou objeto histórico**, de **autenticidade certificada**, inerente ou compatível com as finalidades do órgão? |
| **"l"** | São serviços especializados ou aquisição/locação de equipamentos para **rastreamento e obtenção de provas** (art. 3º, II e V, da Lei nº 12.850/2013), com **necessidade justificada de sigilo sobre a investigação**? |
| **"m"** | São **medicamentos destinados exclusivamente ao tratamento de doenças raras** definidas pelo Ministério da Saúde? |

Outras duas hipóteses de objeto específico, fora do inciso IV:

- **Transferência de tecnologia de produto estratégico para o SUS**, listado em ato da direção nacional do SUS — inclusive na aquisição durante as etapas de absorção tecnológica, em valores compatíveis com o instrumento de transferência → **art. 75, XII**.
- **Profissional técnico de notória especialização para compor comissão de avaliação de critérios de técnica** (em licitação por técnica e preço) → **art. 75, XIII**. Cuidado: este é **dispensa**, não inexigibilidade, embora mencione notória especialização. Não o confunda com o art. 74, III.

### Bateria F — Inviabilidade de competição (art. 74)

O art. 74 tem lógica diferente do art. 75: aqui não é a lei que autoriza pular a disputa, é a **realidade do mercado que torna a disputa impossível**. O rol é **exemplificativo** ("em especial nos casos de") — se o caso não couber em nenhum dos cinco incisos mas a competição for genuinamente inviável, o enquadramento é no **caput do art. 74**, com fundamentação reforçada.

- **Existe mais de um fornecedor capaz de entregar este objeto?** Se a resposta é não:
  - → **art. 74, I**. Pergunta de controle decisiva: *"não existe outro fornecedor no mercado, ou você prefere esta marca?"* O §1º **veda a preferência por marca específica**. Exclusividade é do fornecedor, comprovada por atestado de exclusividade, contrato de exclusividade, declaração do fabricante ou outro documento idôneo. Preferência de marca disfarçada de exclusividade é a irregularidade mais apontada pelos órgãos de controle neste inciso.
- **É serviço técnico especializado de natureza predominantemente intelectual, e você precisa de um profissional ou empresa cujo reconhecimento no ramo torna o trabalho dele o adequado para este objeto?** Se sim, confirme que o serviço está em **uma das oito alíneas**: a) estudos técnicos, planejamentos, projetos básicos ou executivos; b) pareceres, perícias e avaliações em geral; c) assessorias ou consultorias técnicas e auditorias financeiras ou tributárias; d) fiscalização, supervisão ou gerenciamento de obras ou serviços; e) patrocínio ou defesa de causas judiciais ou administrativas; f) treinamento e aperfeiçoamento de pessoal; g) restauração de obras de arte e de bens de valor histórico; h) controles de qualidade e tecnológico, análises, testes e ensaios de campo e laboratoriais, instrumentação e monitoramento de parâmetros de obras e do meio ambiente e demais serviços de engenharia que se enquadrem no inciso.
  - → **art. 74, III**, com a alínea identificada. Perguntas de controle: o serviço **não é de publicidade ou divulgação** (vedação expressa)? **Haverá subcontratação ou atuação de profissionais diferentes dos que justificaram a escolha?** O §4º veda — e isso invalida o enquadramento, então pergunte antes de fechar o parecer.
  - Note que a alínea "f" (treinamento e aperfeiçoamento de pessoal) alcança cursos e capacitações: contratação de curso **pode** ser inexigibilidade por notória especialização, mas também pode ser dispensa por valor (art. 75, II) ou pregão, se houver vários fornecedores equivalentes. Não presuma.
- **É profissional do setor artístico?** → **art. 74, II**, desde que **consagrado pela crítica especializada ou pela opinião pública**. Perguntas de controle: a contratação é direta com o artista ou por empresário? Se por empresário, ele tem **exclusividade permanente e contínua** de representação no País ou em Estado específico? O §2º **afasta expressamente** a inexigibilidade quando a representação é **restrita a um evento ou local específico**.
- **O objeto será contratado por credenciamento** — vários prestadores habilitados, em condições padronizadas, todos contratáveis, sem disputa entre eles? → **art. 74, IV**. Aqui não há fornecedor exclusivo: o que se justifica é a **adequação da sistemática de credenciamento ao objeto**. O credenciamento é também procedimento auxiliar do art. 78.
- **É aquisição ou locação de imóvel cujas instalações e localização tornam necessária aquela escolha específica?** → **art. 74, V**. O §5º impõe três requisitos cumulativos, que viram pedidos de documento ao usuário: (I) **avaliação prévia** do bem, estado de conservação, custos de adaptações imprescindíveis e prazo de amortização dos investimentos; (II) **certificação da inexistência de imóveis públicos vagos e disponíveis** que atendam ao objeto; (III) **justificativas de singularidade** do imóvel e de **vantagem** para a Administração.

## Etapa 3 — Se é licitação: qual das cinco modalidades

O art. 28 lista cinco modalidades e o §2º **veda criar outras ou combiná-las**. Escolha assim:

- **Concurso** (art. 30) — a Administração quer **escolher um trabalho** técnico, científico ou artístico mediante **prêmio ou remuneração**, e não contratar execução. Se for concurso para elaboração de projeto, o vencedor **cede todos os direitos patrimoniais** e autoriza a execução (art. 30, parágrafo único, e art. 93).
- **Leilão** (art. 31) — **alienação de bens** da Administração, não aquisição. Se o usuário descreve venda de bens inservíveis, veículos baixados ou imóveis, o caso é leilão e a cadeia DFD → ETP → TR desta skill não é a adequada; avise-o.
- **Diálogo competitivo** (art. 32) — restrito a contratações que envolvam, **cumulativamente**: (a) inovação tecnológica ou técnica; (b) impossibilidade de o órgão ter sua necessidade satisfeita **sem adaptar soluções disponíveis** no mercado; e (c) impossibilidade de as **especificações técnicas serem definidas com precisão suficiente** pela Administração. Também cabe quando a Administração precisa definir e identificar os meios e alternativas que satisfaçam sua necessidade, com destaque para a solução técnica mais adequada, os requisitos técnicos aptos a concretizá-la, ou a estrutura jurídica/financeira do contrato (art. 32, II). As três condições do inciso I são cumulativas — não é modalidade para objeto meramente complexo. Se o usuário não consegue especificar o objeto, investigue primeiro se é falta de estudo (que o ETP resolve) e não impossibilidade real.
- **Pregão** (art. 29) — **regra geral** sempre que o objeto tiver padrões de desempenho e qualidade **objetivamente definíveis por especificações usuais de mercado**, ou seja, sempre que for **bem ou serviço comum** (art. 6º, XIII). Mas o **parágrafo único do art. 29 proíbe o pregão** para: **serviços técnicos especializados de natureza predominantemente intelectual** e **obras e serviços de engenharia**, exceto os **serviços comuns de engenharia** (art. 6º, XXI, "a").
- **Concorrência** (art. 29) — o que resta: **bens e serviços especiais** (art. 6º, XIV, com justificativa prévia obrigatória da classificação), **obras e serviços de engenharia** que não sejam serviços comuns de engenharia, e **serviços técnicos especializados de natureza predominantemente intelectual**.

Pergunte também o **critério de julgamento**: se for **melhor técnica ou técnica e preço** (arts. 36 a 38), a lei exige **banca técnica de no mínimo 3 membros** — obrigatória, não facultativa, nas hipóteses do art. 36, §1º (serviços intelectuais especializados, tecnologia sofisticada de domínio restrito, TIC especial, obras/serviços especiais de engenharia, objetos com soluções técnicas alternativas mensuráveis) — e essa avaliação da banca é o que faz as vezes de parecer técnico neste contexto. Ver `parecer-tecnico-topicos.md`, seção "Parecer técnico em licitação (pregão/concorrência)".

Pregão e concorrência seguem o **mesmo rito procedimental comum** do art. 17 — a escolha entre os dois é consequência da natureza do objeto, não uma opção discricionária de conveniência.

Note a simetria útil para conferência: um serviço técnico especializado de natureza predominantemente intelectual **nunca** é pregão. Se há um único profissional de notória especialização, é art. 74, III; se há vários, é concorrência.

## Etapa 4 — Quando mais de uma hipótese se aplica

É comum. Exemplos: curso de R$ 30.000 com fornecedor único (art. 75, II por valor **e** art. 74, I por exclusividade); peça de manutenção em garantia por R$ 20.000 (art. 75, IV, "a" **e** art. 75, II).

Regras de conduta:

1. **Registre no ETP todas as hipóteses cabíveis e justifique a escolhida.** A motivação da escolha é o que protege o gestor — não a escolha em si.
2. **Não use a dispensa por valor para contornar o fracionamento.** Se o somatório do exercício (art. 75, §1º) já estourou o limite, a dispensa por valor está fora, ainda que esta contratação isolada caiba.
3. **Inexigibilidade e dispensa não são intercambiáveis.** Inexigibilidade pressupõe competição **inviável**; dispensa pressupõe competição **possível**, mas legalmente afastada. Se houver dois fornecedores no mercado, não há inexigibilidade — mesmo que um deles seja melhor.
4. **Na dúvida entre dois incisos, é decisão jurídica, não técnica.** Apresente ao usuário as duas leituras com os fatos que sustentam cada uma e recomende que leve a dúvida à consultoria jurídica (art. 53), em vez de escolher por ele.

## Erros de enquadramento que a triagem existe para evitar

Todos já custaram responsabilização. O art. 73 é expresso: **contratação direta indevida com dolo, fraude ou erro grosseiro gera responsabilidade solidária do contratado e do agente público pelo dano ao erário**.

- **Preferência por marca apresentada como exclusividade** (art. 74, §1º, veda).
- **Fracionamento de despesa** para caber no limite de dispensa por valor (art. 75, §1º).
- **Empresário de artista com exclusividade apenas para o evento** (art. 74, §2º, afasta).
- **Subcontratação em contrato de notória especialização** (art. 74, §4º, veda).
- **Emergência criada pela própria desídia no planejamento** (art. 75, §6º, ressalva a apuração de responsabilidade).
- **Recontratar a mesma empresa com base no art. 75, VIII**, ou prorrogar contrato emergencial (vedações expressas do inciso).
- **Citar só o artigo, sem o inciso e a alínea.** "Dispensa nos termos do art. 75" não é enquadramento — é lacuna.
- **Usar pregão para serviço técnico de natureza predominantemente intelectual ou para obra** (art. 29, parágrafo único, proíbe).
- **Classificar o objeto como especial para fugir do pregão sem a justificativa prévia** exigida pelo art. 6º, XIV.

## O que registrar, e onde

Depois de concluída a triagem, apresente ao usuário a conclusão em uma frase — *"pelo que você descreveu, isto é inexigibilidade com base no art. 74, III, alínea 'f', da Lei nº 14.133/2021; confirma?"* — e só então prossiga. Registre:

- **ETP, tópico 5** (descrição da solução como um todo): a declaração do dispositivo aplicável, com artigo, inciso e alínea.
- **ETP, tópico 4** (levantamento de mercado): os fatos que sustentam o enquadramento — quantos fornecedores existem, o que a pesquisa encontrou. É aqui que a inviabilidade de competição do art. 74 se comprova, não no parecer.
- **Mapa de Riscos**: o risco de questionamento do enquadramento, quando a triagem tiver ficado entre duas hipóteses.
- **Parecer Técnico**: a seção "DA MODALIDADE DA LICITAÇÃO" e a seção extra específica do inciso — ver as tabelas de `parecer-tecnico-topicos.md`, que dizem qual documento comprobatório pedir ao usuário para o inciso identificado aqui.

Se a conclusão desta etapa for **pregão ou concorrência** (não contratação direta), pergunte também se será **Registro de Preços (SRP) ou contrato único** — ver "Bloco 0.5" em `etp-topicos.md`. Registre a resposta no mesmo tópico do dispositivo aplicável (ETP, tópico 5, ou tópico 15 no ETP de TIC), porque ela também condiciona as alternativas "OU" do Termo de Referência (Passo 3 do `SKILL.md`).

Se a contratação for direta, lembre o usuário de que o art. 72 exige que o processo seja instruído com: DFD e, se for o caso, ETP, análise de riscos e TR (I); estimativa de despesa na forma do art. 23 (II); parecer jurídico e pareceres técnicos, se for o caso (III); demonstração de compatibilidade orçamentária (IV); comprovação de habilitação e qualificação mínima do contratado (V); razão da escolha do contratado (VI); justificativa de preço (VII); e autorização da autoridade competente (VIII) — além da **divulgação do ato que autoriza a contratação direta ou do extrato do contrato em sítio eletrônico oficial** (parágrafo único).

Além dos oito documentos do art. 72, a contratação direta atrai deveres que não estão nos arts. 74 e 75 e que a triagem não resolve sozinha: as vedações de participação do art. 14 (que alcançam a **execução do contrato**, não só a disputa), a consulta a Ceis/Cnep e as certidões do art. 91, §4º, a habilitação mínima do art. 72, V, a escolha do instrumento contratual do art. 95, e o prazo de **10 dias úteis** de divulgação no PNCP de que depende a **eficácia** do contrato (art. 94, II). Estão detalhados nas seções finais de `parecer-tecnico-topicos.md`.
