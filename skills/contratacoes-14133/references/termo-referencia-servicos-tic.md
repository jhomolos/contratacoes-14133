# Modelo de Termo de Referência — Serviços de TIC

Fonte: modelo oficial da Advocacia-Geral da União (AGU) para a Lei nº 14.133/2021, versão de abril/2026, fornecido pelo usuário. Cobre licitação e contratação direta (alternativas "OU" no texto).

## Quando usar este arquivo

Use este modelo quando o objeto da contratação for **serviços de Tecnologia da Informação e Comunicação (TIC)** — desenvolvimento de sistemas, sustentação, suporte técnico, serviços em nuvem, etc. Não use os modelos genéricos de serviços (`termo-referencia-servicos-obras.md`) para objetos de TIC — este modelo tem seções próprias (alinhamento a PDTIC e à Estratégia de Governo Digital, requisitos organizados por categoria, propriedade intelectual e transferência de conhecimento) que o modelo genérico não tem.

## Como preencher

- O texto contém alternativas separadas por "OU". Escolha a alternativa compatível com o caso (modalidade, regime, características do objeto) e **risque as não escolhidas com `<s>…</s>`, sem apagá-las** (Regra de ouro do `SKILL.md`). O "OU" que separa a alternativa descartada também é riscado. Trechos de realce (turquesa, rosa, azul-petróleo etc.) que não se aplicam ao objeto seguem a mesma regra: riscados, não removidos. Preencha os campos entre `<colchetes>`/`[colchetes]` com o código de cores do `SKILL.md`.
- A seção "Requisitos da Contratação" é organizada em categorias — não pule categorias sem justificar por que não se aplicam ao objeto.
- O alinhamento ao PDTIC e à Estratégia de Governo Digital do órgão precisa dos dados reais desses planos — pergunte ao usuário, não invente objetivos estratégicos.
- Não invente fundamentação legal, percentuais, prazos, índices de reajuste ou critérios de ANS/SLA que o modelo deixa em aberto — pergunte ao usuário ou extraia do ETP.

## Como ler este arquivo: numeração, cores e formatação do modelo

O corpo abaixo da linha horizontal reproduz o `.docx` oficial (`modelos-tr-tic/modelo-de-termo-de-referencia-servicos-tic-lei-no-14-133-abr-26.docx`) com a **numeração automática**, a **hierarquia dos parágrafos**, as **cores de fonte**, os **realces** e o **negrito/itálico/sublinhado** originais, em HTML embutido no Markdown (`<span style="color:red">`, `<span style="background:cyan">`, `<b>`, `<i>`, `<u>`). A conversão foi feita por `scripts/modelo_docx_para_md.py` e conferida contra o Microsoft Word: a numeração de todos os parágrafos é idêntica à exibida no Word. Quando a AGU publicar versão nova, gere este corpo de novo com o mesmo script em vez de editar à mão.

Legenda da própria AGU ("Orientações para uso do modelo – leitura obrigatória"):

| No modelo | Significado |
|---|---|
| Texto preto (sem itálico) | Redação que se espera invariável. **Qualquer alteração exige justificativa nos autos.** |
| <span style="color:red"><i>Vermelho itálico</i></span> | Texto a preencher ou adotar conforme oportunidade e conveniência, de acordo com o objeto. São as previsões "feitas para variar"; inclui as alternativas "OU" e os campos entre colchetes. |
| Realce <span style="background:yellow">amarelo</span> | Alterado em relação à versão anterior do modelo (informativo; não muda a aplicabilidade). |
| Realce <span style="background:cyan">turquesa</span> | Aplicável **exclusivamente ao Sistema de Registro de Preços (SRP)**. Fora de SRP, riscar. |
| Realce <span style="background:lime">verde brilhante</span> | Cláusulas de **margem de preferência** (Decreto nº 11.890/2024). |

As **notas explicativas** do modelo (comentários do Word) estão em `termo-referencia-servicos-tic-notas.md`, organizadas pelo número do item. Consulte a nota do item antes de escolher entre alternativas "OU", riscar uma cláusula ou alterar texto preto. Segundo a AGU, notas explicativas e realces são removidos só na **versão final**: na minuta que vai à análise jurídica, mantenha-os.

**Ao produzir o TR**, siga a seção "Regra de ouro" do `SKILL.md`: mantenha a numeração, a hierarquia, as cores, os realces e a formatação do modelo, e aplique por cima o código de alterações do IPP (vermelho = inclusão, verde = ajuste de redação, azul = só prazo numérico escrito por extenso, `<s>` = supressão).

## Orientações do IPP da AGU para o TR

Detalhamento completo em `references/ipp-agu-orientacoes.md`, seção "Termo de Referência". Pontos decisivos:

- **Prazo de vigência não é número arbitrário**: deve decorrer da **soma** dos prazos de execução, de substituição ou reparo, recebimento provisório, recebimento definitivo e pagamento. Serviços de **operação continuada de sistemas estruturantes de TIC** admitem até 15 anos (art. 114).
- **Garantia do serviço ≠ garantia de execução do contrato**: a primeira (CDC ou convencional) trata da higidez e qualidade do serviço; a segunda (arts. 96 a 102) assegura a regular execução. São campos distintos.
- **Medição por resultado**: a unidade de medida deve permitir mensurar resultados e **eliminar a remuneração por horas de serviço ou por postos de trabalho** — hipótese **excepcional** que exige método de cálculo definido. Em serviços de TIC, essa é a principal fonte de glosa: contratos remunerados por alocação de pessoal, e não por entrega.
- **Indicadores e ANS/SLA**: objetivamente mensuráveis, de coleta fácil, relevantes e adequados; **evitar indicadores complexos ou sobrepostos**; prever fatores fora do controle do prestador; metas realistas; **faixa de tolerância** com menor ou nenhuma margem para atividades críticas; **simples notificação nas primeiras ocorrências** quando o descumprimento for ínfimo e o indicador não crítico. Forma de cálculo da multa **"a mais simples possível"**; sanções **relacionadas às obrigações do modelo de execução**.
- **IMR**: quando utilizado, deve operar preferencialmente por **ferramentas informatizadas** e ser específico à contratação, "evitando-se um mecanismo de controle apenas de modo textual/protocolar". Se elaborado, é **anexo dos Estudos Preliminares**.
- **Ordem de Serviço**: identificação do pedido e da contratada, especificação dos serviços, estimativa de horas quando for a única opção viável, local, recursos financeiros, critérios de avaliação e **responsáveis pela solicitação, avaliação e ateste — sem vínculo com a contratada**.
- **Propriedade intelectual e transferência de conhecimento**: o modelo já traz a cessão de direitos sobre artefatos e a transição contratual com transferência de conhecimento, tecnologia e técnicas — confirme a coerência com o ETP.
- **Habilitação**: critérios justificados nos autos, à luz dos riscos. Fixar **preços máximos aceitáveis globais e unitários**.
- **Contratação direta**: fundamentos de fato e de direito, observado o art. 7º da IN SEGES/ME nº 65/2021, inclusive a vedação do §3º (inexigibilidade incompatível com possibilidade de competição).
- **Mapa de Riscos**: atualizado e juntado **ao final da elaboração do TR**.
- **Divulgação**: o TR vai ao **PNCP na mesma data** da divulgação do edital ou do aviso de contratação direta.
- **Registre a data de extração deste modelo**: exigida na **Declaração de utilização de modelos AGU/MGI**.

---

<b>MODELO DE TERMO DE REFERÊNCIA<br>Lei nº 14.133, de 1º de abril de 2021<br>LICITAÇÃO E CONTRATAÇÃO DIRETA</b>

<span style="color:red"><b><i>ÓRGÃO OU ENTIDADE PÚBLICA</i></b></span>

(Processo Administrativo n° <span style="color:red"><i>xxxxx</i></span>.<span style="color:red"><i>xxxxxx</i></span>/<span style="color:red"><i>xxxx</i></span>-<span style="color:red"><i>xx</i></span>)

<b>TERMO DE REFERÊNCIA</b>

## 1. CONDIÇÕES GERAIS DA CONTRATAÇÃO

1.1. Contratação de <span style="color:red">&lt;definição do objeto da contratação</span> <span style="color:red"><i>de</i></span> <span style="color:red">forma precisa, suficiente e clara, vedadas especificações que, por excessivas, irrelevantes ou desnecessárias, limitem ou frustrem a competição ou a realização do fornecimento da solução</span> <span style="color:red">de TIC&gt;</span>, nos termos da tabela abaixo, conforme condições e exigências estabelecidas neste instrumento.

| <b>Item</b> | <b>Especificação</b> | <b>CATSER</b> | <b>Métrica ou Unidade de Medida</b> | <b>CÓD.</b> <br><b>PMC-TIC</b> | <b>Quantidade</b> | <b>Valor Unitário</b> | <b>Valor Total</b> |
|---|---|---|---|---|---|---|---|
| <b>1</b> |  |  |  |  |  |  |  |
| <b>2</b> |  |  |  |  |  |  |  |
| <b>3</b> |  |  |  |  |  |  |  |
| <b>...</b> |  |  |  |  |  |  |  |

1.2. <span style="color:red;background:cyan"><i>Estimativas de consumo individualizadas, do órgão gerenciador e órgão(s) e entidade(s) participante(s).</i></span>

| <span style="color:red;background:cyan"><b><i>Órgão Gerenciador:</i></b></span> |  |  |  |  |  |
|---|---|---|---|---|---|
| <span style="color:red;background:cyan"><i>Item</i></span> | <span style="color:red;background:cyan"><i>Descrição/ especificação</i></span> | <span style="color:red;background:cyan"><i>Unidade de medida</i></span> | <span style="color:red;background:cyan"><i>Requisição mínima</i></span> | <span style="color:red;background:cyan"><i>Requisição máxima</i></span> | <span style="color:red;background:cyan"><i>Quantidade total</i></span> |
|  |  |  |  |  |  |

| <span style="color:red;background:cyan"><b><i>Órgão Participante:</i></b></span> |  |  |  |  |  |
|---|---|---|---|---|---|
| <span style="color:red;background:cyan"><i>Item</i></span> | <span style="color:red;background:cyan"><i>Descrição/ especificação</i></span> | <span style="color:red;background:cyan"><i>Unidade de medida</i></span> | <span style="color:red;background:cyan"><i>Requisição mínima</i></span> | <span style="color:red;background:cyan"><i>Requisição máxima</i></span> | <span style="color:red;background:cyan"><i>Quantidade total</i></span> |
|  |  |  |  |  |  |

| <span style="color:red;background:cyan"><b><i>Órgão Participante:</i></b></span> |  |  |  |  |  |
|---|---|---|---|---|---|
| <span style="color:red;background:cyan"><i>Item</i></span> | <span style="color:red;background:cyan"><i>Descrição/ especificação</i></span> | <span style="color:red;background:cyan"><i>Unidade de medida</i></span> | <span style="color:red;background:cyan"><i>Requisição mínima</i></span> | <span style="color:red;background:cyan"><i>Requisição máxima</i></span> | <span style="color:red;background:cyan"><i>Quantidade total</i></span> |
|  |  |  |  |  |  |

### <b>Classificação do objeto quanto à heterogeneidade ou complexidade</b>

1.3. <span style="color:red"><i>O(s) serviço(s) objeto desta contratação são caracterizados como</i></span> <span style="color:red"><b><i>comum(ns),</i></b></span> <span style="color:red"><i>conforme justificativa constante do Estudo Técnico Preliminar.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.4. <span style="color:red"><i>O objeto da contratação tem a natureza de</i></span> <span style="color:red"><b><i>serviço(s) especial(is)</i></b></span><span style="color:red"><i>, conforme justificativa constante do Estudo Técnico Preliminar.</i></span>

### <b>Classificação do objeto quanto ao modelo de execução</b>

1.5. <span style="color:red"><i>O serviço é enquadrado como não contínuo.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.6. <span style="color:red"><i>O serviço é enquadrado como continuado tendo em vista que [...], sendo a vigência plurianual mais vantajosa considerando [...]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[o Estudo Técnico Preliminar]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[os termos da Nota Técnica .../...];</i></span>

### <b>Prazo de vigência</b>

1.7. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, na forma do artigo 105 da Lei n° 14.133, de 2021.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.8. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo, limitado a 5 anos]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, prorrogável por até 10 anos, na forma dos artigos 106 e 107 da Lei n° 14.133, de 2021.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.9. <span style="color:red"><i>Tratando-se de contratação que prevê operação continuada de sistemas estruturantes de tecnologia da informação, o prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo]</i></b></span><span style="color:red"><i>, prorrogável para até 15 anos (máximo de 15 anos, incluindo prorrogações), contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, na forma do artigo 114 da Lei n° 14.133, de 2021.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.10. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo, limitado a um ano da ocorrência da emergência ou calamidade]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, improrrogável, na forma do art. 75, inciso VIII, da Lei n° 14.133/2021.</i></span>

1.11. O contrato ou outro instrumento hábil que o substitua oferece maior detalhamento das regras que serão aplicadas em relação à vigência da contratação.

## 2. FUNDAMENTAÇÃO E DESCRIÇÃO DA NECESSIDADE DA CONTRATAÇÃO

2.1. A presente contratação justifica-se <span style="color:red"><i>[a justificativa deve ser clara, precisa e suficiente, sendo vedadas justificativas genéricas, incapazes de demonstrar as reais necessidades da contratação, devendo-se</i></span> <span style="color:red"><b><i>evidenciar a relação entre a necessidade da contratação e os respectivos volumes e características do objeto</i></b></span><span style="color:red"><i>, assim como a</i></span> <span style="color:red"><b><i>forma de cálculo</i></b></span> <span style="color:red"><i>utilizada para a definição do quantitativo de bens e serviços que compõem a solução de TIC e os resultados e</i></span> <span style="color:red"><b><i>benefícios a serem alcançados.</i></b></span> <span style="color:red"><i>Caso o processo de contratação resulte na formação de Ata de Registro de Preços que permita adesões por órgãos não participes,</i></span> <span style="color:red"><b><i>é necessário registrar a motivação para tal permissão</i></b></span><span style="color:red"><i>]</i></span>.

2.2. <span style="color:red"><i>O objeto da contratação está previsto no Plano de Contratações Anual [</i></span><span style="color:red"><b><i>ANO</i></b></span><span style="color:red"><i>], conforme detalhamento a seguir:</i></span>

I) <span style="color:red"><i>ID PCA no PNCP: [...];</i></span>

II) <span style="color:red"><i>Data de publicação no PNCP: [...];</i></span>

III) <span style="color:red"><i>Id do item no PCA: [...];</i></span>

IV) <span style="color:red"><i>Classe/Grupo: [...];</i></span>

V) <span style="color:red"><i>Identificador da Futura Contratação: [...];</i></span>

<span style="color:red"><b><i>OU</i></b></span>

2.3. <span style="color:red"><i>O objeto da contratação está previsto no Plano de Contratações Anual [</i></span><span style="color:red"><b><i>ANO</i></b></span><span style="color:red"><i>], conforme consta das informações básicas desse Termo de Referência.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

2.4. <span style="color:red"><i>O objeto da contratação está previsto no Plano de Contratações Anual [ANO], conforme consta das informações básicas deste termo de referência.</i></span>

2.5. O objeto da contratação também está alinhado com a Estratégia de Governo Digital <span style="color:red"><i>&lt;ANO&gt;</i></span> e em consonância com o Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC) <span style="color:red"><i>&lt;ANO&gt;</i></span> do <span style="color:red"><i>&lt;NOME DO ÓRGÃO&gt;</i></span>, conforme demonstrado abaixo:

| <b>ALINHAMENTO AOS PLANOS ESTRATÉGICOS</b> |  |
|---|---|
| <b>ID</b> | <b>Objetivos Estratégicos</b> |
| <span style="color:red"><b><i>N1</i></b></span> | <span style="color:red"><i>&lt;Objetivo Estratégico N1 do Plano Estratégico Institucional &lt;ANO&gt;&gt;</i></span> |
| <span style="color:red"><b><i>…</i></b></span> | <span style="color:red"><i>&lt;Objetivo Estratégico NN do Plano Estratégico Institucional &lt;ANO&gt;&gt;</i></span> |
| <span style="color:red"><b><i>M1</i></b></span> | <span style="color:red"><i>&lt;Objetivo Estratégico M1 da Estratégia de Governança Digital &lt;ANO&gt;&gt;</i></span> |
| <span style="color:red"><b><i>…</i></b></span> | <span style="color:red"><i>&lt;Objetivo Estratégico MM da Estratégia de Governança Digital &lt;ANO&gt;&gt;</i></span> |

| <b>ALINHAMENTO AO PDTIC</b> <span style="color:red"><b><i>&lt;ANO&gt;</i></b></span> |  |  |  |
|---|---|---|---|
| <b>ID</b> | <b>Ação do PDTIC</b> | <b>ID</b> | <b>Meta do PDTIC associada</b> |
| <span style="color:red"><b><i>A1</i></b></span> | <span style="color:red"><i>&lt;Ação X1 do Plano de Metas e Ações&gt;</i></span> | <span style="color:red"><b><i>M1</i></b></span> | <span style="color:red"><i>&lt;Meta M1 do Plano de Metas e Ações&gt;</i></span> |
| <span style="color:red"><b><i>…</i></b></span> | <span style="color:red"><i>&lt;Ação XN do Plano de Metas e Ações&gt;</i></span> | <span style="color:red"><b><i>…</i></b></span> | <span style="color:red"><i>&lt;Meta MN do Plano de Metas e Ações&gt;</i></span> |

2.6. Por tratar de oferta de serviços públicos digitais, o objeto da contratação será integrado à Plataforma Gov.br, nos termos do Decreto nº 8.936, de 19 de dezembro de 2016, e suas atualizações, de acordo com as especificações deste Termo de Referência.

## 3. DESCRIÇÃO DA SOLUÇÃO COMO UM TODO CONSIDERADO O CICLO DE VIDA DO OBJETO

3.1. A descrição da solução como um todo encontra-se pormenorizada em tópico específico dos Estudos Técnicos Preliminares, apêndice deste Termo de Referência.

3.2. A solução de TIC consiste em [<span style="color:red"><i>descrever de forma</i></span> <span style="color:red"><b><i>detalhada</i></b></span><span style="color:red"><i>,</i></span> <span style="color:red"><b><i>motivada</i></b></span> <span style="color:red"><i>e</i></span> <span style="color:red"><b><i>justificada</i></b></span><span style="color:red"><i>, incluindo o</i></span> <span style="color:red"><b><i>quantitativo</i></b></span> <span style="color:red"><i>de bens e serviços necessários para a composição da solução de TIC</i></span>].

## 4. REQUISITOS DA CONTRATAÇÃO

### <b>Requisitos de Negócio:</b>

4.1. A presente contratação orienta-se pelos seguintes requisitos de negócio:

4.1.1 <span style="color:red"><i>[...];</i></span>

4.1.2 <span style="color:red"><i>[...]; e</i></span>

4.1.3 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos de Capacitação</b>

4.2. <span style="color:red"><i>Será necessário treinamento à equipe que atuará com a solução. O treinamento deverá ser de no mínimo</i></span> <span style="color:red"><b><i>[XX]</i></b></span> <span style="color:red"><i>horas de duração.</i></span>

4.2.1 <span style="color:red"><i>[...].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.3. <span style="color:red"><i>Não faz parte do escopo da contratação a realização de capacitação técnica na utilização dos recursos relacionados ao objeto da presente contratação;</i></span>

4.3.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos Legais</b>

4.4. O presente processo de contratação deve estar aderente à Constituição Federal, à Lei nº 14.133, de 2021, à Instrução Normativa SGD/ME nº 94, de 2022, Instrução Normativa SEGES/ME nº 65, de 7 de julho de 2021, Lei nº 13.709, de 2018 (Lei Geral de Proteção de Dados Pessoais – LGPD) e a outras legislações aplicáveis;

### <b>Requisitos de Manutenção</b>

4.5. Devido às características da solução, há necessidade de realização de manutenções <span style="color:red"><b><i>[corretivas/preventivas/adaptativa/evolutiva]</i></b></span> pela Contratada, visando à manutenção da disponibilidade da solução <span style="color:red">e ao aperfeiçoamento de suas funcionalidades</span>;

4.5.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos Temporais</b>

4.6. Os serviços devem ser prestados no prazo máximo de <span style="color:red"><b><i>[XX]</i></b></span> dias corridos <span style="color:red">para as capitais dos estados e de</span> <span style="color:red"><b><i>[XX]</i></b></span> <span style="color:red">dias corridos para as demais localidades</span>, a contar do recebimento da abertura da Ordem de Serviço (OS), emitida pela Contratante, podendo ser prorrogada, excepcionalmente, por <span style="color:red">até igual período</span>, desde que justificado previamente pelo Contratado e autorizado pela Contratante;

4.7. Na contagem dos prazos estabelecidos neste Termo de Referência, quando não expressados de forma contrária, excluir-se-á o dia do início e incluir-se-á o do vencimento.

4.8. Todos os prazos citados, quando não expresso de forma contrária, serão considerados em dias corridos. Ressaltando que serão contados os dias a partir da hora em que ocorrer o incidente até a mesma hora do último dia, conforme os prazos.

4.9. Na execução dos serviços, deverão ser observados os seguintes prazos:

| <span style="color:red"><b><i>Atividade, Tarefa ou Serviço</i></b></span> | <span style="color:red"><b><i>Prazo máximo de início de atendimento</i></b></span> | <span style="color:red"><b><i>Prazo máximo de solução de problema</i></b></span> |
|---|---|---|
| <span style="color:red"><i>(.........)</i></span> | <span style="color:red"><i>(.........) dias</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>horas</i></span> | <span style="color:red"><i>(.........) dias</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>horas</i></span> |
| <span style="color:red"><i>(.........)</i></span> | <span style="color:red"><i>(.........) dias</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>horas</i></span> | <span style="color:red"><i>(.........) dias</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>horas</i></span> |

4.9.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos de Segurança e Privacidade</b>

4.10. A solução deverá atender aos princípios e procedimentos elencados na Política de Segurança da Informação do Contratante, e <span style="color:red">[....]</span>

4.10.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos Sociais, Ambientais e Culturais</b>

4.11. Os serviços devem estar aderentes às seguintes diretrizes sociais, ambientais e culturais:

4.11.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos da Arquitetura Tecnológica</b>

4.12. Os serviços deverão ser executados observando-se as diretrizes de arquitetura tecnológica estabelecidas pela área técnica da Contratante.

4.13. A adoção de tecnologia ou arquitetura diversa deverá ser autorizada previamente pela Contratante. Caso não seja autorizada, é vedado à Contratada adotar arquitetura, componentes ou tecnologias diferentes daquelas definidas pela Contratante.

4.13.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos de Projeto e de Implementação</b>

4.14. Os serviços deverão observar integralmente os requisitos de projeto e de implementação descritos a seguir:

4.14.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos de Implantação</b>

4.15. Os serviços deverão observar integralmente os requisitos de implantação, instalação e fornecimento descritos a seguir:

4.15.1 <span style="color:red"><i>[...].</i></span>

### <b>Requisitos de Garantia e Manutenção</b>

4.16. <span style="color:red"><i>O prazo de garantia é aquele estabelecido na Lei nº 8.078, de 11 de setembro de 1990 (Código de Defesa do Consumidor), e suas atualizações.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.17. <span style="color:red"><i>O prazo de garantia contratual dos serviços, complementar à garantia legal, será de, no mínimo, \_\_\_ (\_\_\_\_) meses, contado a partir do primeiro dia útil subsequente à data do recebimento definitivo do objeto.</i></span>

### <b>Requisitos de Experiência Profissional</b>

4.18. <span style="color:red"><i>Os serviços de &lt;assistência técnica, suporte, garantia, ....&gt; deverão ser prestados por técnicos devidamente capacitados nos produtos em questão, bem como com todos os recursos ferramentais necessários para a prestação dos serviços;</i></span>

4.19. <span style="color:red"><i>[...].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.20. <span style="color:red"><i>Não serão exigidos requisitos de experiência profissional para a presente a contratação.</i></span>

### <b>Requisitos de Formação da Equipe</b>

4.21. <span style="color:red"><i>Os serviços deverão ser prestados por técnicos devidamente capacitados, de acordo com os critérios estabelecidos a seguir:</i></span>

4.22. <span style="color:red"><i>[...].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.23. <span style="color:red"><i>Não serão exigidos requisitos de formação da equipe para a presente a contratação.</i></span>

### <b>Requisitos de Metodologia de Trabalho</b>

4.24. A execução dos serviços está condicionada ao recebimento pelo Contratado de Ordem de Serviço (OS) emitida pela Contratante.

4.25. A OS indicará o serviço, a quantidade e a localidade na qual os deverão ser prestados.

4.26. O Contratado deve fornecer meios para contato e registro de ocorrências da seguinte forma: com funcionamento <span style="color:red"><b><i>[XX]</i></b></span> horas por dia e <span style="color:red"><b><i>[XX]</i></b></span> dias por semana de maneira eletrônica e <span style="color:red"><b><i>[XX]</i></b></span> horas por dia e <span style="color:red"><b><i>[XX]</i></b></span> dias por semana por via telefônica.

4.27. A execução do serviço dever ser acompanhada pelo Contratado, que dará ciência de eventuais acontecimentos à Contratante.

4.28. <span style="color:red"><i>[...].</i></span>

### <b>Requisitos de Segurança da Informação e Privacidade</b>

4.29. O Contratado deverá observar integralmente os requisitos de Segurança da Informação e Privacidade descritos a seguir:

4.30. <span style="color:red"><i>[...].</i></span>

### <b>Vistoria</b>

4.31. <span style="color:red"><i>Não há necessidade de realização de avaliação prévia do local de execução dos serviços.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.32. <span style="color:red"><i>A avaliação prévia do local de execução dos serviços é imprescindível para o conhecimento pleno das condições e peculiaridades do objeto a ser contratado, sendo assegurado ao interessado o direito de realização de vistoria prévia, acompanhado por servidor designado para esse fim, de segunda à sexta-feira, das</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>horas às</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>horas.</i></span>

4.33. <span style="color:red"><i>Serão disponibilizados data e horário diferentes aos interessados em realizar a vistoria prévia.</i></span>

4.34. <span style="color:red"><i>Para a vistoria, o representante legal da empresa ou responsável técnico deverá estar devidamente identificado, apresentando documento de identidade civil e documento expedido pela empresa comprovando sua habilitação para a realização da vistoria.</i></span>

4.34.1 <span style="color:red"><b><i>... [incluir outras instruções sobre vistoria]</i></b></span><span style="color:red"><i>;</i></span>

4.34.2 <span style="color:red"><b><i>... [incluir outras instruções sobre vistoria]</i></b></span><span style="color:red"><i>.</i></span>

4.35. <span style="color:red"><i>Caso o interessado opte por não realizar a vistoria, deverá prestar declaração formal assinada pelo seu responsável técnico acerca do conhecimento pleno das condições e peculiaridades da contratação.</i></span>

4.36. <span style="color:red"><i>A não realização da vistoria não poderá embasar posteriores alegações de desconhecimento das instalações, dúvidas ou esquecimentos de quaisquer detalhes dos locais da prestação dos serviços, devendo o Contratado assumir os ônus dos serviços decorrentes.</i></span>

### <span style="color:red"><b><i>Outros Requisitos Aplicáveis</i></b></span>

4.37. <span style="color:red"><i>[...];</i></span>

4.38. <span style="color:red"><i>[...]; e</i></span>

4.39. <span style="color:red"><i>[...].</i></span>

### <b>Sustentabilidade</b>

4.40. Além dos critérios de sustentabilidade eventualmente inseridos na descrição do objeto, devem ser atendidos os seguintes requisitos, que se baseiam no Guia Nacional de Contratações Sustentáveis:

4.40.1 <span style="color:red"><i>[...];</i></span>

4.40.2 <span style="color:red"><i>[...]; e</i></span>

4.40.3 <span style="color:red"><i>[...].</i></span>

### <span style="color:red"><b><i>Indicação de marcas ou modelos</i></b></span>

4.41. <span style="color:red"><i>Na presente contratação será admitida a indicação da(s) seguinte(s) marca(s), característica(s) ou modelo(s), de acordo com as justificativas contidas nos Estudos Técnicos Preliminares: (...).</i></span>

### <span style="color:red"><b><i>Da vedação de utilização de marca/produto na execução do serviço</i></b></span>

4.42. <span style="color:red"><i>Diante das conclusões extraídas do processo administrativo nº</i></span> <span style="color:red"><b><i>xxxxx.xxxxxx/xxxx-xx</i></b></span><span style="color:red"><i>, a Administração não aceitará o fornecimento dos seguintes produtos/marcas:</i></span>

4.42.1 <span style="color:red"><i>[...];</i></span>

4.42.2 <span style="color:red"><i>[...]; e</i></span>

4.42.3 <span style="color:red"><i>[...].</i></span>

### <span style="color:red"><b><i>Da exigência de carta de solidariedade</i></b></span>

4.43. <span style="color:red"><i>Em caso de fornecedor, revendedor ou distribuidor, será exigida do licitante/interessado provisoriamente classificado em primeiro lugar, nos termos do edital ou do aviso de contratação direta, carta de solidariedade emitida pelo fabricante, que assegure a execução do contrato.</i></span>

### <b>Subcontratação</b>

4.44. <span style="color:red"><i>Não será admitida a subcontratação do objeto contratual.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.45. <span style="color:red"><i>É permitida a subcontratação parcial do objeto, até o limite de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor total do contrato, nas seguintes condições:</i></span>

4.46. <span style="color:red"><i>É vedada a subcontratação completa ou da parcela principal da obrigação, abaixo discriminada:</i></span>

4.46.1 <span style="color:red"><i>[...];</i></span>

4.46.2 <span style="color:red"><i>[...]; e</i></span>

4.46.3 <span style="color:red"><i>[...].</i></span>

4.47. <span style="color:red"><i>Poderão ser subcontratadas as seguintes parcelas do objeto:</i></span>

4.47.1 <span style="color:red"><i>[...];</i></span>

4.47.2 <span style="color:red"><i>[...]; e</i></span>

4.47.3 <span style="color:red"><i>[...].</i></span>

4.48. <span style="color:red"><i>Em qualquer hipótese de subcontratação, permanece a responsabilidade integral do Contratado pela perfeita execução contratual, cabendo-lhe realizar a supervisão e coordenação das atividades do subcontratado, bem como responder perante o Contratante pelo rigoroso cumprimento das obrigações contratuais correspondentes ao objeto da subcontratação.</i></span>

4.49. <span style="color:red"><i>A subcontratação depende de autorização prévia do Contratante, a quem incumbe avaliar se o subcontratado cumpre os requisitos de qualificação técnica necessários para a execução do objeto.</i></span>

4.50. <span style="color:red"><i>O Contratado apresentará à Administração documentação que comprove a capacidade técnica do subcontratado, que será avaliada e juntada aos autos do processo correspondente.</i></span>

4.51. <span style="color:red"><i>É vedada a subcontratação de pessoa física ou jurídica, se aquela ou os dirigentes desta mantiverem vínculo de natureza técnica, comercial, econômica, financeira, trabalhista ou civil com dirigente do órgão ou entidade contratante ou com agente público que desempenhe função na contratação ou atue na fiscalização ou na gestão do contrato, ou se deles forem cônjuge, companheiro ou parente em linha reta, colateral, ou por afinidade, até o terceiro grau.</i></span>

### <span style="color:red"><b><i>Da exigência de amostra</i></b></span>

4.52. <span style="color:red"><i>Havendo o aceite da proposta quanto ao valor, o interessado classificado provisoriamente em primeiro lugar deverá apresentar amostra, que terá data, local e horário de sua realização divulgados por mensagem no sistema, cuja presença será facultada a todos os interessados, incluindo os demais fornecedores interessados.</i></span>

4.53. <span style="color:red"><i>Serão exigidas amostras dos seguintes itens:</i></span>

4.53.1 <span style="color:red"><i>[...];</i></span>

4.53.2 <span style="color:red"><i>[...]; e</i></span>

4.53.3 <span style="color:red"><i>[...].</i></span>

4.54. <span style="color:red"><i>As amostras poderão ser entregues no endereço [</i></span><span style="color:red"><b><i>indicar o endereço</i></b></span><span style="color:red"><i>]</i></span><span style="color:red;background:lime"><i>,</i></span> <span style="color:red"><i>no prazo limite de [</i></span><span style="color:red"><b><i>indicar o prazo</i></b></span><span style="color:red"><i>], sendo que a empresa assume total responsabilidade pelo envio e por eventual atraso na entrega.</i></span>

4.55. <span style="color:red"><i>É facultada prorrogação o prazo estabelecido, a partir de solicitação fundamentada no chat pelo interessado, antes de findo o prazo.</i></span>

4.56. <span style="color:red"><i>No caso de não haver entrega da amostra ou ocorrer atraso na entrega, sem justificativa aceita, ou havendo entrega de amostra fora das especificações previstas, a proposta será recusada.</i></span>

4.57. <span style="color:red"><i>Serão avaliados os seguintes aspectos e padrões mínimos de aceitabilidade:</i></span>

4.57.1 <span style="color:red"><i>Itens (....): ...........;</i></span>

4.57.2 <span style="color:red"><i>Itens (....): ............</i></span>

4.58. <span style="color:red"><i>Os resultados das avaliações serão divulgados por meio de mensagem no sistema.</i></span>

4.59. <span style="color:red"><i>Se a(s) amostra(s) apresentada(s) pelo primeiro classificado não for(em) aceita(s), será analisada a aceitabilidade da proposta ou lance ofertado pelo segundo classificado. Seguir-se-á com a verificação da(s) amostra(s) e, assim, sucessivamente, até a verificação de uma que atenda às especificações constantes neste Termo de Referência.</i></span>

4.60. <span style="color:red"><i>Os exemplares colocados à disposição da Administração serão tratados como protótipos, podendo ser manuseados e desmontados pela equipe técnica responsável pela análise, não gerando direito a ressarcimento.</i></span>

4.61. <span style="color:red"><i>Após a divulgação do resultado final do certame, as amostras entregues deverão ser recolhidas pelos fornecedores no prazo de</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) dias, após o qual poderão ser descartadas pela Administração, sem direito a ressarcimento.</i></span>

4.62. <span style="color:red"><i>Os interessados deverão colocar à disposição da Administração todas as condições indispensáveis à realização de testes e fornecer, sem ônus, os manuais impressos em língua portuguesa, necessários ao seu perfeito manuseio, quando for o caso.</i></span>

### <b>Garantia da contratação</b>

4.63. <span style="color:red"><i>Não haverá exigência da garantia da contratação dos art. 96 e seguintes da Lei nº 14.133, de 2021, pelas razões constantes do Estudo Técnico Preliminar.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.64. <span style="color:red"><i>Será exigida a garantia da contratação de que tratam os arts. 96 e seguintes da Lei nº 14.133, de 2021, com validade durante a execução do contrato e 90 (noventa) dias após término da vigência contratual, podendo o Contratado optar pela caução em dinheiro ou em títulos da dívida pública, seguro-garantia, fiança bancária ou título de capitalização, em valor correspondente a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor</i></span> <span style="color:red"><b><i>[total]</i></b></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><b><i>[anual]</i></b></span> <span style="color:red"><i>da contratação.</i></span>

4.65. <span style="color:red"><i>Em caso de opção pelo seguro-garantia, a parte adjudicatária deverá apresentá-la, no máximo, até a data de assinatura do contrato.</i></span>

4.65.1 <span style="color:red"><i>A apólice de seguro-garantia permanecerá em vigor mesmo que o Contratado não pague o prêmio nas datas convencionadas.</i></span>

4.65.2 <span style="color:red"><i>Caso o adjudicatário não apresente a apólice de seguro de garantia antes da assinatura do contrato, ocorrerá a preclusão do direito de escolha dessa modalidade de garantia.</i></span>

4.65.3 <span style="color:red"><i>A apólice de seguro-garantia deverá acompanhar as modificações referentes à vigência do contrato principal mediante a emissão do respectivo endosso pela seguradora.</i></span>

4.65.4 <span style="color:red"><i>Será permitida a substituição da apólice de seguro-garantia na data de renovação ou de aniversário, desde que mantidas as condições e coberturas da apólice vigente e nenhum período fique descoberto, ressalvados os períodos de suspensão contratual.</i></span>

4.65.5 <span style="color:red"><i>Caso o adjudicatário não opte pelo seguro-garantia ou não apresente a apólice de seguro de garantia antes da assinatura do contrato, deverá apresentar, no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, a critério do Contratante, contado da assinatura do contrato, comprovante de prestação de garantia nas modalidades de caução em dinheiro ou títulos da dívida pública, fiança bancária ou títulos de capitalização.</i></span>

4.66. <span style="color:red"><i>Caso seja a garantia em dinheiro a modalidade de garantia escolhida pelo Contratado, deverá ser efetuada em favor do Contratante, em conta específica na Caixa Econômica Federal, com correção monetária.</i></span>

4.67. <span style="color:red"><i>Caso a opção seja por utilizar títulos da dívida pública, estes devem ter sido emitidos sob a forma escritural, mediante registro em sistema centralizado de liquidação e de custódia autorizado pelo Banco Central do Brasil, e avaliados pelos seus valores econômicos, conforme definido pelo Ministério competente.</i></span>

4.68. <span style="color:red"><i>No caso de garantia na modalidade de fiança bancária, deverá ser emitida por banco ou instituição financeira devidamente autorizada a operar no País pelo Banco Central do Brasil, e deverá constar expressa renúncia do fiador aos benefícios do artigo 827 do Código Civil.</i></span>

4.69. <span style="color:red"><i>Na hipótese de opção pelo título de capitalização, a garantia deverá ser custeada por pagamento único, com resgate pelo valor total, sob a modalidade de instrumento de garantia, emitido por sociedades de capitalização regulamente constituídas e autorizadas pelo Governo Federal.</i></span>

4.69.1 <span style="color:red"><i>O título de capitalização deverá ser apresentado ao Contratante juntamente com as condições gerais e o número do processo administrativo sob o qual o plano de capitalização foi aprovado pela Susep (art. 8º, III, da Circular SUSEP nº 656, de 11 de março de 2022).</i></span>

4.70. <span style="color:red"><i>A garantia assegurará, qualquer que seja a modalidade escolhida, sob pena de não aceitação, o pagamento de:</i></span>

4.70.1 <span style="color:red"><i>prejuízos advindos do não cumprimento do objeto do contrato e do não adimplemento das demais obrigações nele previstas;</i></span>

4.70.2 <span style="color:red"><i>multas moratórias e punitivas aplicadas pela Administração à contratada; e</i></span>

4.70.3 <span style="color:red"><i>obrigações trabalhistas e previdenciárias de qualquer natureza e para com o FGTS, não adimplidas pelo Contratado.</i></span>

4.71. <span style="color:red"><i>Em caso de seguro-garantia, a apólice deverá ter cobertura para pagamento direto ao empregado após decisão definitiva em processo administrativo que apure montante líquido e certo a ele devido em razão de inadimplência do Contratado, independentemente de trânsito em julgado de decisão judicial.</i></span>

4.72. <span style="color:red"><i>No caso de alteração do valor do contrato, ou prorrogação de sua vigência, a garantia deverá ser ajustada ou renovada, no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, contado da data de assinatura do termo aditivo ou da emissão do apostilamento, seguindo os mesmos parâmetros utilizados quando da contratação.</i></span>

4.73. <span style="color:red"><i>Na hipótese de suspensão do contrato por ordem ou inadimplemento da Administração, o Contratado ficará desobrigado de renovar a garantia ou de endossar a apólice de seguro até a ordem de reinício da execução ou o adimplemento pela Administração.</i></span>

4.74. <span style="color:red"><i>Se o valor da garantia for utilizado total ou parcialmente em pagamento de qualquer obrigação, o Contratado obriga-se a fazer a respectiva reposição no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, a critério do Contratante, contados da data em que for notificada.</i></span>

4.75. <span style="color:red"><i>O Contratante executará a garantia na forma prevista na legislação que rege a matéria.</i></span>

4.75.1 <span style="color:red"><i>O emitente da garantia ofertada pelo Contratado deverá ser notificado pelo Contratante quanto ao início de processo administrativo para apuração de descumprimento de cláusulas contratuais.</i></span>

4.75.2 <span style="color:red"><i>Caso se trate da modalidade seguro-garantia, ocorrido o sinistro durante a vigência da apólice, sua caracterização e comunicação poderão ocorrer fora desta vigência, não caracterizando fato que justifique a negativa do sinistro, desde que respeitados os prazos prescricionais aplicados ao contrato de seguro, nos termos do art. 20 da Circular Susep n° 662, de 11 de abril de 2022.</i></span>

4.76. <span style="color:red"><i>Extinguir-se-á a garantia com a restituição da carta fiança, autorização para a liberação de importâncias depositadas em dinheiro a título de garantia ou anuência ao resgate do título de capitalização, acompanhada de declaração do Contratante, mediante termo circunstanciado, de que o Contratado cumpriu todas as cláusulas do contrato.</i></span>

4.76.1 <span style="color:red"><i>A extinção da garantia na modalidade seguro-garantia observará a regulamentação da Susep.</i></span>

4.76.2 <span style="color:red"><i>A Administração deverá apurar se há alguma pendência contratual antes do término da vigência da apólice.</i></span>

4.77. <span style="color:red"><i>A garantia somente será liberada ou restituída após a fiel execução do contrato ou após a sua extinção por culpa exclusiva da Administração e, quando em dinheiro, será atualizada monetariamente.</i></span>

4.78. <span style="color:red"><i>O Contratado autoriza o Contratante a reter, a qualquer tempo, a garantia, na forma prevista neste Termo de Referência.</i></span>

4.79. <span style="color:red"><i>O garantidor não é parte para figurar em processo administrativo instaurado pelo Contratante com o objetivo de apurar prejuízos e/ou aplicar sanções à contratada.</i></span>

4.80. <span style="color:red"><i>A garantia de execução é independente de eventual garantia do produto ou serviço prevista neste Termo de Referência.</i></span>

### <span style="color:red"><b><i>Instalação de escritório</i></b></span>

4.81. <span style="color:red"><i>Considera-se imprescindível para a adequada execução dos serviços contratados que o fornecedor possua ou venha a instalar escritório contendo estrutura administrativa mínima, no município de</i></span> <span style="color:red"><b><i>[indicar o Município/UF]</i></b></span><span style="color:red"><i>, pelas razões constantes do Estudo Técnico Preliminar.</i></span>

### <span style="color:red"><b><i>Margem de Preferência</i></b></span>

4.82. <span style="color:red"><i>O objeto da contratação enquadra-se na margem de preferência .............</i></span> <span style="color:red"><b><i>[normal]</i></b></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><b><i>[adicional]</i></b></span> <span style="color:red"><i>de ........ %, prevista no Decreto n.º....................., conforme disposto na Resolução n.º ......................... da Comissão Interministerial de Contratações Públicas para o Desenvolvimento Sustentável – CICS.</i></span>

### <b>Informações relevantes para o [dimensionamento</b> <b><u>E/OU</u></b> <b>apresentação] da proposta</b>

4.83. <span style="color:red"><i>A demanda do órgão tem como base as seguintes características:</i></span>

4.83.1 <span style="color:red"><i>[...];</i></span>

4.83.2 <span style="color:red"><i>[...]; e</i></span>

4.83.3 <span style="color:red"><i>[...].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.84. <span style="color:red"><i>A demanda dos órgãos partícipes tem como base as seguintes características:</i></span>

4.84.1 <span style="color:red"><i>[...];</i></span>

4.84.2 <span style="color:red"><i>[...]; e</i></span>

4.84.3 <span style="color:red"><i>[...].</i></span>

## 5. PAPÉIS E RESPONSABILIDADES

5.1. São obrigações da CONTRATANTE:

5.1.1 nomear Gestor e Fiscais Técnico, Administrativo e Requisitante do contrato para acompanhar e fiscalizar a execução dos contratos;

5.1.2 encaminhar formalmente a demanda por meio de Ordem de Serviço ou de Fornecimento de Bens, de acordo com os critérios estabelecidos no Termo de Referência;

5.1.3 receber o objeto fornecido pelo contratado que esteja em conformidade com a proposta aceita, conforme inspeções realizadas;

5.1.4 aplicar à contratada as sanções administrativas regulamentares e contratuais cabíveis, comunicando ao órgão gerenciador da Ata de Registro de Preços, quando aplicável;

5.1.5 liquidar o empenho e efetuar o pagamento à contratada, dentro dos prazos preestabelecidos em contrato;

5.1.6 comunicar à contratada todas e quaisquer ocorrências relacionadas com o fornecimento da solução de TIC;

5.1.7 definir produtividade ou capacidade mínima de fornecimento da solução de TIC por parte do contratado, com base em pesquisas de mercado, quando aplicável;

5.1.8 prever que os direitos de propriedade intelectual e direitos autorais da solução de TIC sobre os diversos artefatos e produtos cuja criação ou alteração seja objeto da relação contratual pertençam à Administração, incluindo a documentação, o código-fonte de aplicações, os modelos de dados e as bases de dados, justificando os casos em que isso não ocorrer.

5.2. São obrigações do CONTRATADO:

5.2.1 indicar formalmente preposto apto a representá-la junto à contratante, que deverá responder pela fiel execução do contrato;

5.2.2 atender prontamente quaisquer orientações e exigências da Equipe de Fiscalização do Contrato, inerentes à execução do objeto contratual;

5.2.3 reparar quaisquer danos diretamente causados à contratante ou a terceiros por culpa ou dolo de seus representantes legais, prepostos ou empregados, em decorrência da relação contratual, não excluindo ou reduzindo a responsabilidade da fiscalização ou o acompanhamento da execução dos serviços pela contratante;

5.2.4 propiciar todos os meios necessários à fiscalização do contrato pela contratante, cujo representante terá poderes para sustar o fornecimento, total ou parcial, em qualquer tempo, desde que motivadas as causas e justificativas desta decisão;

5.2.5 manter, durante toda a execução do contrato, as mesmas condições da habilitação;

5.2.6 quando especificada, manter, durante a execução do contrato, equipe técnica composta por profissionais devidamente habilitados, treinados e qualificados para fornecimento da solução de TIC;

5.2.7 quando especificado, manter a produtividade ou a capacidade mínima de fornecimento da solução de TIC durante a execução do contrato;

5.2.8 ceder os direitos de propriedade intelectual e direitos autorais da solução de TIC sobre os diversos artefatos e produtos produzidos em decorrência da relação contratual, incluindo a documentação, os modelos de dados e as bases de dados à Administração;

5.2.9 fazer a transição contratual, quando for o caso.

5.3. São obrigações do órgão gerenciador do registro de preços:

5.3.1 efetuar o registro do licitante fornecedor e firmar a correspondente Ata de Registro de Preços;

5.3.2 conduzir os procedimentos relativos a eventuais renegociações de condições, produtos ou preços registrados;

5.3.3 definir mecanismos de comunicação com os órgãos participantes e não participantes, contendo:

5.3.4 as formas de comunicação entre os envolvidos, a exemplo de ofício, telefone, e-mail, ou sistema informatizado, quando disponível; e

5.3.5 definição dos eventos a serem reportados ao órgão gerenciador, com a indicação de prazo e responsável;

5.3.6 definir mecanismos de controle de fornecimento da solução de TIC, observando, dentre outros:

5.3.7 a definição da produtividade ou da capacidade mínima de fornecimento da solução de TIC;

5.3.8 as regras para gerenciamento da fila de fornecimento da solução de TIC aos órgãos participantes e não participantes, contendo prazos e formas de negociação e redistribuição da demanda, quando esta ultrapassar a produtividade definida ou a capacidade mínima de fornecimento e for requerida pelo contratado; e

5.3.9 as regras para a substituição da solução registrada na Ata de Registro de Preços, garantida a verificação de Amostra do Objeto, observado o disposto no inciso III, alínea "c", item 2 do art. 17 da Instrução Normativa SGS/ME nº 94, de 2022, em função de fatores supervenientes que tornem necessária e imperativa a substituição da solução tecnológica.

## 6. MODELO DE EXECUÇÃO DO OBJETO

### <b>Condições de execução</b>

6.1. <span style="color:red"><i>A execução do objeto seguirá a seguinte dinâmica:</i></span>

6.1.1 Início da execução do objeto: <span style="color:red"><i>XX</i></span> dias <span style="color:red"><i>[da assinatura do contrato]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[da emissão da ordem de serviço]</i></span>.

6.1.2 Descrição detalhada dos métodos, rotinas, etapas, tecnologias procedimentos, frequência e periodicidade de execução do trabalho: <span style="color:red"><i>[...]</i></span>.

6.1.3 <span style="color:red"><i>Cronograma de realização dos serviços: [...];</i></span>

6.1.4 <span style="color:red"><i>Etapa ... Período / a partir de / após concluído ...</i></span>

### <b>Local e horário da prestação dos serviços</b>

6.2. Os serviços serão prestados no seguinte endereço: <span style="color:red"><i>[...]</i></span>;

6.3. Os serviços serão prestados no seguinte horário: <span style="color:red"><i>[...].</i></span>

### <b>Rotinas a serem cumpridas</b>

6.3.1 A execução contratual observará as rotinas <span style="color:red"><i>[abaixo] / [em anexo]</i></span>:

### <b>Materiais a serem disponibilizados</b>

6.4. <span style="color:red"><i>Para a perfeita execução dos serviços, o Contratado deverá disponibilizar os materiais, equipamentos, ferramentas e utensílios necessários, nas quantidades estimadas e qualidades a seguir estabelecidas, promovendo sua substituição quando necessário:</i></span>

6.4.1 <span style="color:red"><i>[...];</i></span>

6.4.2 <span style="color:red"><i>[...]; e</i></span>

6.4.3 <span style="color:red"><i>[...].</i></span>

### <b>Informações relevantes para o dimensionamento da proposta</b>

6.5. <span style="color:red"><i>A demanda do órgão tem como base as seguintes características:</i></span>

6.5.1 <span style="color:red"><i>[...];</i></span>

6.5.2 <span style="color:red"><i>[...]; e</i></span>

6.5.3 <span style="color:red"><i>[...].</i></span>

### <b>Formas de transferência de conhecimento</b>

6.6. <span style="color:red"><i>A transferência do conhecimento deverá ser realizada observando-se o que segue:</i></span>

6.6.1 <span style="color:red"><i>[...];</i></span>

6.6.2 <span style="color:red"><i>[...]; e</i></span>

6.6.3 <span style="color:red"><i>[...].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

6.7. <span style="color:red"><i>Não será necessária transferência de conhecimento devido às características do objeto.</i></span>

### <b>Procedimentos de transição e finalização do contrato</b>

6.8. <span style="color:red"><i>Os procedimentos de transição e finalização do contrato constituem-se das seguintes etapas:</i></span>

6.8.1 <span style="color:red"><i>[...];</i></span>

6.8.2 <span style="color:red"><i>[...]; e</i></span>

6.8.3 <span style="color:red"><i>[...].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

6.9. <span style="color:red"><i>Não serão necessários procedimentos de transição e finalização do contrato devido às características do objeto.</i></span>

### <b>Quantidade mínima de serviços para comparação e controle</b>

6.10. Cada OS conterá o volume de serviços demandados, incluindo a sua localização e o prazo, conforme modelo descrito no [Anexo].

6.11. <span style="color:red"><i>[...]</i></span>

### <b>Mecanismos formais de comunicação</b>

6.12. São definidos como mecanismos formais de comunicação, entre a Contratante e o Contratado, os seguintes:

I) Ordem de Serviço;

II) Ata de Reunião;

III) Ofício;

IV) Sistema de abertura de chamados;

V) E-mails e Cartas;

VI) <span style="color:red">[...].</span>

### <b>Manutenção de Sigilo e Normas de Segurança</b>

6.13. O Contratado deverá manter sigilo absoluto sobre quaisquer dados e informações contidos em quaisquer documentos e mídias, incluindo os equipamentos e seus meios de armazenamento, de que venha a ter conhecimento durante a execução dos serviços, não podendo, sob qualquer pretexto, divulgar, reproduzir ou utilizar, sob pena de lei, independentemente da classificação de sigilo conferida pelo Contratante a tais documentos.

6.14. O Termo de Compromisso e Manutenção de Sigilo, contendo declaração de manutenção de sigilo e respeito às normas de segurança vigentes na entidade, a ser assinado pelo representante legal do Contratado, e Termo de Ciência, a ser assinado por todos os empregados do Contratado diretamente envolvidos na contratação, encontram-se nos ANEXOS [....] e [...].

## 7. MODELO DE GESTÃO DO CONTRATO

7.1. O contrato deverá ser executado fielmente pelas partes, de acordo com as cláusulas avençadas e as normas da Lei nº 14.133, de 2021, e cada parte responderá pelas consequências de sua inexecução total ou parcial.

7.2. Em caso de impedimento, ordem de paralisação ou suspensão do contrato, o cronograma de execução será prorrogado automaticamente pelo tempo correspondente, anotadas tais circunstâncias mediante simples apostila.

7.3. As comunicações entre o órgão ou entidade e o Contratado devem ser realizadas por escrito sempre que o ato exigir tal formalidade, admitindo-se o uso de mensagem eletrônica para esse fim.

7.4. O órgão ou entidade poderá convocar o preposto da empresa para adoção de providências que devam ser cumpridas de imediato.

### <b>Preposto</b>

7.5. O Contratado designará formalmente o preposto da empresa, antes do início da prestação dos serviços, indicando no instrumento os poderes e deveres em relação à execução do objeto Contratado.

7.6. O Contratado <span style="color:red"><i>[deverá]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[não necessitará]</i></span> manter preposto da empresa no local da execução do objeto <span style="color:red"><i>durante o período [definir o período].</i></span>

7.7. O Contratante poderá recusar, desde que justificadamente, a indicação ou a manutenção do preposto da empresa, hipótese em que o Contratado designará outro para o exercício da atividade.

### <b>Reunião Inicial</b>

7.8. Após a assinatura do Contrato e a nomeação do Gestor e Fiscais do Contrato, será realizada a Reunião Inicial de alinhamento com o objetivo de nivelar os entendimentos acerca das condições estabelecidas no Contrato, Edital e seus anexos, e esclarecer possíveis dúvidas acerca da execução dos serviços.

7.9. A reunião será realizada em conformidade com o previsto no inciso I do Art. 31 da IN SGD/ME nº 94, de 2022, e ocorrerá em até .....(....) dias úteis da assinatura do Contrato, podendo ser prorrogada a critério da Contratante.

7.10. A pauta desta reunião observará, pelo menos:

7.10.1 Presença do representante legal da contratada, que apresentará o seu preposto;

7.10.2 Entrega, por parte da Contratada, do Termo de Compromisso e dos Termos de Ciência;

7.10.3 esclarecimentos relativos a questões operacionais, administrativas e de gestão do contrato;

7.10.4 A Carta de apresentação do Preposto deverá conter no mínimo o nome completo e CPF do funcionário da empresa designado para acompanhar a execução do contrato e atuar como interlocutor principal junto à Contratante, incumbido de receber, diligenciar, encaminhar e responder as principais questões técnicas, legais e administrativas referentes ao andamento contratual;

7.10.5 Apresentação das declarações/certificados do fabricante, comprovando que o produto ofertado possui a garantia solicitada neste termo de referência.

### <b>Rotinas de Fiscalização</b>

7.11. A execução do contrato deverá ser acompanhada e fiscalizada pelo(s) fiscal(is) do contrato, ou pelos respectivos substitutos, nos termos do art. 33 da IN SGD nº 94, de 2022, observando-se, em especial, as rotinas a seguir.

### <b>Fiscalização Técnica</b>

7.12. O fiscal técnico do contrato acompanhará a execução do contrato, para que sejam cumpridas todas as condições estabelecidas no contrato, de modo a assegurar os melhores resultados para a Administração.

7.13. O fiscal técnico do contrato anotará no histórico de gerenciamento do contrato todas as ocorrências relacionadas à execução do contrato, com a descrição do que for necessário para a regularização das faltas ou dos defeitos observados.

7.14. Identificada qualquer inexatidão ou irregularidade, o fiscal técnico do contrato emitirá notificações para a correção da execução do contrato, determinando prazo para a correção.

7.15. O fiscal técnico do contrato informará ao gestor do contato, em tempo hábil, a situação que demandar decisão ou adoção de medidas que ultrapassem sua competência, para que adote as medidas necessárias e saneadoras, se for o caso.

7.16. No caso de ocorrências que possam inviabilizar a execução do contrato nas datas aprazadas, o fiscal técnico do contrato comunicará o fato imediatamente ao gestor do contrato.

7.17. O fiscal técnico do contrato comunicará ao gestor do contrato, em tempo hábil, o término do contrato sob sua responsabilidade, com vistas à tempestiva renovação ou à prorrogação contratual.

7.18. <span style="color:red"><i>A fiscalização da execução dos serviços abrange, ainda, as seguintes rotinas:</i></span>

7.18.1 <span style="color:red"><i>[...];</i></span>

7.18.2 <span style="color:red"><i>[...]; e</i></span>

7.18.3 <span style="color:red"><i>[...].</i></span>

7.19. A fiscalização de que trata esta cláusula não exclui nem reduz a responsabilidade do Contratado, inclusive perante terceiros, por qualquer irregularidade, ainda que resultante de imperfeições técnicas, vícios redibitórios, ou emprego de material inadequado ou de qualidade inferior e, na ocorrência desta, não implica corresponsabilidade do Contratante ou de seus agentes, gestores e fiscais, de conformidade.

### <b>Fiscalização Administrativa</b>

7.20. O fiscal administrativo do contrato, além de exercer as atribuições previstas no art. 33, IV, da IN SGD nº 94, de 2022, verificará a manutenção das condições de habilitação da contratada, acompanhará o empenho, o pagamento, as garantias, as glosas e a formalização de apostilamento e termos aditivos, solicitando quaisquer documentos comprobatórios pertinentes, caso necessário.

7.21. Caso ocorra descumprimento das obrigações contratuais, o fiscal administrativo do contrato atuará tempestivamente na solução do problema, reportando ao gestor do contrato para que tome as providências cabíveis, quando ultrapassar a sua competência.

7.22. <span style="color:red"><i>Além do disposto acima, a fiscalização contratual obedecerá às seguintes rotinas:</i></span>

7.22.1 <span style="color:red"><i>[...];</i></span>

7.22.2 <span style="color:red"><i>[...]; e</i></span>

7.22.3 <span style="color:red"><i>[...].</i></span>

### <b>Gestor do Contrato</b>

7.23. Cabe ao gestor do contrato, além de exercer as atribuições previstas no art. 33, I, da IN SGD nº 94, de 2022:

7.23.1 coordenar a atualização do processo de acompanhamento e fiscalização do contrato contendo todos os registros formais da execução no histórico de gerenciamento do contrato, a exemplo da ordem de serviço, do registro de ocorrências, das alterações e das prorrogações contratuais, elaborando relatório com vistas à verificação da necessidade de adequações do contrato para fins de atendimento da finalidade da administração.

7.23.2 acompanhar os registros realizados pelos fiscais do contrato, de todas as ocorrências relacionadas à execução do contrato e as medidas adotadas, informando, se for o caso, à autoridade superior àquelas que ultrapassarem a sua competência.

7.23.3 acompanhar a manutenção das condições de habilitação da contratada, para fins de empenho de despesa e pagamento, e anotará os problemas que obstem o fluxo normal da liquidação e do pagamento da despesa no relatório de riscos eventuais.

7.23.4 emitir documento comprobatório da avaliação realizada pelos fiscais técnico, administrativo e setorial quanto ao cumprimento de obrigações assumidas pelo Contratado, com menção ao seu desempenho na execução contratual, baseado nos indicadores objetivamente definidos e aferidos, e a eventuais penalidades aplicadas, devendo constar do cadastro de atesto de cumprimento de obrigações.

7.23.5 tomar providências para a formalização de processo administrativo de responsabilização para fins de aplicação de sanções, a ser conduzido pela comissão de que trata o art. 158 da Lei nº 14.133, de 2021, ou pelo agente ou pelo setor com competência para tal, conforme o caso.

7.23.6 elaborar relatório final com informações sobre a consecução dos objetivos que tenham justificado a contratação e eventuais condutas a serem adotadas para o aprimoramento das atividades da Administração.

7.23.7 enviar a documentação pertinente ao setor de contratos para a formalização dos procedimentos de liquidação e pagamento, com a indicação expressa de que o valor da Nota Fiscal emitida pela contratada confere com o valor dimensionado pela fiscalização e gestão no recebimento definitivo do serviço.

7.23.8 receber e dar encaminhamento imediato:

7.23.8.1. às denúncias de discriminação, violência e assédio no ambiente de trabalho, conforme o art. 2º, inciso III, do Decreto n.º 12.174/2024;

7.23.8.2. à notificação formal de que a empresa contratada está descumprindo suas obrigações trabalhistas, enviada pelo trabalhador, sindicato, Ministério do Trabalho, Ministério Público, Defensoria Pública ou por qualquer outro meio idôneo.

## 8. CRITÉRIOS DE MEDIÇÃO E PAGAMENTO

8.1. <span style="color:red"><i>A avaliação da execução do objeto utilizará o [Instrumento de Medição de Resultado (IMR), conforme previsto no [Anexo XXX]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[outro instrumento substituto para aferição da qualidade da prestação dos serviços]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[o disposto nesta seção].</i></span>

| <span style="color:red"><b><i>IAP – ÍNDICE DE ATENDIMENTO NO PRAZO</i></b></span> |  |
|---|---|
| <span style="color:red"><b><i>Tópico</i></b></span> | <span style="color:red"><b><i>Descrição</i></b></span> |
| <span style="color:red"><b><i>Finalidade</i></b></span> | <span style="color:red"><i>Medir o tempo de atraso na prestação dos serviços constantes na Ordem de Serviço.</i></span> |
| <span style="color:red"><b><i>Meta a cumprir</i></b></span> | <span style="color:red"><i>IAP igual ou superior a (....) %.</i></span> |
| <span style="color:red"><b><i>Instrumento de medição</i></b></span> | <span style="color:red"><i>Deve ser aferido por meio de ferramentas, procedimentos de amostragem ou outros procedimentos de inspeção.</i></span> |
| <span style="color:red"><b><i>Forma de acompanhamento</i></b></span> | <span style="color:red"><i>É apurado pelos fiscais do contrato avaliando a quantidade atendida dentro do prazo em relação à quantidade total atendida no período de referência.</i></span> |
| <span style="color:red"><b><i>Periodicidade</i></b></span> | <span style="color:red"><i>Mensal</i></span> |
| <span style="color:red"><b><i>Mecanismo de Cálculo (métrica)</i></b></span> | <span style="color:red"><b><i>IAP = 100 \* (ΣQtap / ΣQtr)</i></b></span><br><span style="color:red"><i>Onde:</i></span><br><span style="color:red"><i>IAP = Indicador de atendimento aos prazos do serviço;</i></span><br><span style="color:red"><i>ΣQtap = Somatório do quantitativo atendido no prazo máximo estabelecido no TR com previsão de encerramento para o período de referência;</i></span><br><span style="color:red"><i>ΣQtr = Somatório do quantitativo total registrado com previsão de encerramento para o período de referência.</i></span> |
| <span style="color:red"><b><i>Observações</i></b></span> | <span style="color:red"><i>Obs1: Serão utilizados dias corridos na medição.</i></span><br><span style="color:red"><i>Obs2: Os dias com expediente parcial no órgão/entidade serão considerados como dias corridos no cômputo do indicador.</i></span> |
| <span style="color:red"><b><i>Início de Vigência</i></b></span> | <span style="color:red"><i>A partir da emissão da OS.</i></span> |
| <span style="color:red"><b><i>Faixas de ajuste no pagamento e Sanções</i></b></span> | <span style="color:red"><i>IAP &gt;= 90%: sem descontos sobre o valor da fatura mensal.</i></span><br><span style="color:red"><i>IAP &gt;= 80% e &lt; 90%: 10% de desconto sobre o valor da fatura mensal.</i></span><br><span style="color:red"><i>IAP &gt;= 70% e &lt; 80%: 20% de desconto sobre o valor da fatura mensal.</i></span><br><span style="color:red"><i>IAP &lt; 70%: 30% de desconto sobre o valor da fatura mensal.</i></span> |

8.2. Será indicada a retenção ou glosa no pagamento, proporcional à irregularidade verificada, sem prejuízo das sanções cabíveis, caso se constate que o Contratado:

8.2.1 não produziu os resultados acordados,

8.2.2 deixou de executar, ou não executou com a qualidade mínima exigida as atividades contratadas; ou

8.2.3 deixou de utilizar materiais e recursos humanos exigidos para a execução do serviço, ou os utilizou com qualidade ou quantidade inferior à demandada.

8.3. <span style="color:red"><i>A utilização do IMR não impede a aplicação concomitante de outros mecanismos para a avaliação da prestação dos serviços.</i></span>

8.4. <span style="color:red"><i>A aferição da execução contratual para fins de pagamento considerará os seguintes critérios:</i></span>

8.4.1 <span style="color:red"><i>[...];</i></span>

8.4.2 <span style="color:red"><i>[...]; e</i></span>

8.4.3 <span style="color:red"><i>[...].</i></span>

### <b>Recebimento</b>

8.5. Os serviços serão recebidos provisoriamente, no prazo de <span style="color:red"><i>XXX (xxxxx)</i></span> dias, pelos fiscais técnico e administrativo, mediante termos detalhados, quando verificado o cumprimento das exigências de caráter técnico e administrativo.

8.6. O prazo para recebimento provisório será contado do recebimento de comunicação de cobrança oriunda do Contratado com a comprovação da prestação dos serviços a que se referem a parcela a ser paga.

8.7. O fiscal técnico do contrato realizará o recebimento provisório do objeto do contrato mediante termo detalhado que comprove o cumprimento das exigências de caráter técnico.

8.8. O fiscal administrativo do contrato realizará o recebimento provisório do objeto do contrato mediante termo detalhado que comprove o cumprimento das exigências de caráter administrativo.

8.9. O fiscal setorial do contrato, quando houver, realizará o recebimento provisório sob o ponto de vista técnico e administrativo.

8.10. Para efeito de recebimento provisório, será considerado para fins de faturamento o período <span style="color:red"><i>[indicar o período]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[indicar os eventos ou etapas para fins de faturamento].</i></span>

8.11. Ao final de cada período/evento de faturamento:

8.11.1 o fiscal técnico do contrato deverá apurar o resultado das avaliações da execução do objeto e, se for o caso, a análise do desempenho e qualidade da prestação dos serviços realizados em consonância com os indicadores previstos no ato convocatório, que poderá resultar no redimensionamento de valores a serem pagos à contratada, registrando em relatório a ser encaminhado ao gestor do contrato;

8.12. Será considerado como ocorrido o recebimento provisório com a entrega do termo detalhado ou, em havendo mais de um a ser feito, com a entrega do último.

8.13. O Contratado fica obrigado a reparar, corrigir, remover, reconstruir ou substituir, às suas expensas, no todo ou em parte, o objeto em que se verificarem vícios, defeitos ou incorreções resultantes da execução ou materiais empregados, cabendo à fiscalização não atestar a última e/ou única medição de serviços até que sejam sanadas todas as eventuais pendências que possam vir a ser apontadas no recebimento provisório.

8.14. A fiscalização não efetuará o ateste da última e/ou única medição de serviços até que sejam sanadas todas as eventuais pendências que possam vir a ser apontadas no recebimento provisório.

8.15. O recebimento provisório também ficará sujeito, quando cabível, à conclusão de todos os testes de campo e à entrega dos Manuais e Instruções exigíveis.

8.16. Os serviços poderão ser rejeitados, no todo ou em parte, quando em desacordo com as especificações constantes neste Termo de Referência e na proposta, sem prejuízo da aplicação das penalidades.

8.17. Quando a fiscalização for exercida por um único servidor, o Termo Detalhado deverá conter o registro, a análise e a conclusão acerca das ocorrências na execução do contrato, em relação à fiscalização técnica e administrativa e demais documentos que julgar necessários, devendo encaminhá-los ao gestor do contrato para recebimento definitivo.

8.18. Os serviços serão recebidos definitivamente no prazo de <span style="color:red"><i>XX</i></span> (<span style="color:red"><i>xxxxx</i></span>) dias, contados do recebimento provisório, por servidor ou comissão designada pela autoridade competente, após a verificação da qualidade e quantidade do serviço e consequente aceitação mediante termo detalhado, obedecendo os seguintes procedimentos:

8.18.1 Emitir documento comprobatório da avaliação realizada pelos fiscais técnico, administrativo e setorial, quando houver, no cumprimento de obrigações assumidas pelo Contratado, com menção ao seu desempenho na execução contratual, baseado em indicadores objetivamente definidos e aferidos, e a eventuais penalidades aplicadas, devendo constar do cadastro de atesto de cumprimento de obrigações, conforme regulamento.

8.18.2 Realizar a análise dos relatórios e de toda a documentação apresentada pela fiscalização e, caso haja irregularidades que impeçam a liquidação e o pagamento da despesa, indicar as cláusulas contratuais pertinentes, solicitando ao Contratado, por escrito, as respectivas correções;

8.18.3 Emitir Termo Detalhado para efeito de recebimento definitivo dos serviços prestados, com base nos relatórios e documentações apresentadas; e

8.18.4 Comunicar a empresa para que emita a Nota Fiscal ou Fatura, com o valor exato dimensionado pela fiscalização.

8.18.5 Enviar a documentação pertinente ao setor de contratos para a formalização dos procedimentos de liquidação e pagamento, no valor dimensionado pela fiscalização e gestão.

8.19. No caso de controvérsia sobre a execução do objeto, quanto à dimensão, qualidade e quantidade, deverá ser observado o teor do art. 143 da Lei nº 14.133, de 2021, comunicando-se à empresa para emissão de Nota Fiscal quanto à parcela incontroversa da execução do objeto, para efeito de liquidação e pagamento.

8.20. Nenhum prazo de recebimento ocorrerá enquanto pendente a solução, pelo Contratado, de inconsistências verificadas na execução do objeto ou no instrumento de cobrança.

8.21. O recebimento provisório ou definitivo não excluirá a responsabilidade civil pela solidez e pela segurança do serviço nem a responsabilidade ético-profissional pela perfeita execução do contrato.

### <b>Procedimentos de Teste e Inspeção</b>

8.22. Serão adotados como procedimentos de teste e inspeção, para fins de elaboração dos Termos de Recebimento Provisório e Definitivo:

8.22.1 <span style="color:red"><i>[...];</i></span>

8.22.2 <span style="color:red"><i>[...]; e</i></span>

8.22.3 <span style="color:red"><i>[...].</i></span>

### <b>Liquidação</b>

8.23. Recebida a Nota Fiscal ou documento de cobrança equivalente, correrá o prazo de dez dias úteis para fins de liquidação, na forma desta seção, prorrogáveis por igual período, nos termos do art. 7º, §3º da Instrução Normativa SEGES/ME nº 77/2022.

8.24. O prazo de que trata o item anterior será reduzido à metade, mantendo-se a possibilidade de prorrogação, nos casos de contratações decorrentes de despesas cujos valores não ultrapassem o limite de que trata o inciso II do art. 75 da Lei nº 14.133, de 2021.

8.25. Para fins de liquidação, o setor competente deve verificar se a Nota Fiscal ou Fatura apresentada expressa os elementos necessários e essenciais do documento, tais como:

I) o prazo de validade;

II) a data da emissão;

III) os dados do contrato e do órgão contratante;

IV) o período respectivo de execução do contrato;

V) o valor a pagar; e

VI) eventual destaque do valor de retenções tributárias cabíveis.

8.26. Havendo erro na apresentação da Nota Fiscal/Fatura, ou circunstância que impeça a liquidação da despesa, esta ficará sobrestada até que o Contratado providencie as medidas saneadoras, reiniciando-se o prazo após a comprovação da regularização da situação, sem ônus ao Contratante.

8.27. A Nota Fiscal ou Fatura deverá ser obrigatoriamente acompanhada da comprovação da regularidade fiscal, constatada por meio de consulta on-line ao SICAF ou, na impossibilidade de acesso ao referido Sistema, mediante consulta aos sítios eletrônicos oficiais ou à documentação mencionada no art. 68 da Lei nº 14.133/2021.

8.28. A Administração deverá realizar consulta ao SICAF para:

8.28.1 verificar a manutenção das condições de habilitação exigidas;

8.28.2 identificar possível razão que impeça a participação em licitação/contratação no âmbito do órgão ou entidade, tais como a proibição de contratar com a Administração ou com o Poder Público, bem como ocorrências impeditivas indiretas.

8.29. Constatando-se, junto ao SICAF, a situação de irregularidade do Contratado, será providenciada sua notificação, por escrito, para que, no prazo de 5 (cinco) dias úteis, regularize sua situação ou, no mesmo prazo, apresente sua defesa. O prazo poderá ser prorrogado uma vez, por igual período, a critério do Contratante.

8.30. Não havendo regularização ou sendo a defesa considerada improcedente, o Contratante deverá comunicar aos órgãos responsáveis pela fiscalização da regularidade fiscal quanto à inadimplência do Contratado, bem como quanto à existência de pagamento a ser efetuado, para que sejam acionados os meios pertinentes e necessários para garantir o recebimento de seus créditos.

8.31. Persistindo a irregularidade, o Contratante deverá adotar as medidas necessárias à rescisão contratual nos autos do processo administrativo correspondente, assegurada ao Contratado a ampla defesa.

8.32. Havendo a efetiva execução do objeto, os pagamentos serão realizados normalmente, até que se decida pela rescisão do contrato, caso o Contratado não regularize sua situação junto ao SICAF.

### <b>Prazo de pagamento</b>

8.33. O pagamento será efetuado no prazo máximo de até dez dias úteis, contados da finalização da liquidação da despesa, conforme seção anterior, nos termos da Instrução Normativa SEGES/ME nº 77, de 2022.

8.34. No caso de atraso pelo Contratante, os valores devidos ao Contratado serão atualizados monetariamente entre o termo final do prazo de pagamento até a data de sua efetiva realização, mediante aplicação do índice <span style="color:red"><i>[definir o índice]</i></span> de correção monetária.

### <b>Forma de pagamento</b>

8.35. O pagamento será realizado por meio de ordem bancária, para crédito em banco, agência e conta corrente indicados pelo Contratado.

8.36. Será considerada data do pagamento o dia em que constar como emitida a ordem bancária para pagamento.

8.37. Quando do pagamento, será efetuada a retenção tributária prevista na legislação aplicável.

8.37.1 Independentemente do percentual de tributo inserido na planilha, quando houver, serão retidos na fonte, quando da realização do pagamento, os percentuais estabelecidos na legislação vigente.

8.38. O Contratado regularmente optante pelo Simples Nacional, nos termos da Lei Complementar nº 123, de 2006, não sofrerá a retenção tributária quanto aos impostos e contribuições abrangidos por aquele regime. No entanto, o pagamento ficará condicionado à apresentação de comprovação, por meio de documento oficial, de que faz jus ao tratamento tributário favorecido previsto na referida Lei Complementar.

### <span style="color:red"><b><i>Antecipação de pagamento</i></b></span>

8.39. <span style="color:red"><i>A presente contratação permite a antecipação de pagamento [</i></span><span style="color:red"><b><i>parcial</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>total</i></b></span><span style="color:red"><i>], conforme as regras previstas no presente tópico.</i></span>

8.40. <span style="color:red"><i>O Contratado emitirá [recibo]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[nota fiscal]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[fatura]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[documento idôneo] correspondente ao valor da antecipação de pagamento de R$</i></span> <span style="color:red"><b><i>X.XXX,XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>valor em extenso</i></b></span><span style="color:red"><i>), tão logo [</i></span><span style="color:red"><b><i>incluir condicionante – ex: seja assinado o termo de contrato, ou seja, prestada a garantia etc.</i></b></span><span style="color:red"><i>], para que o Contratante efetue o pagamento antecipado.</i></span>

8.41. <span style="color:red"><i>Para as etapas seguintes do contrato, a antecipação do pagamento ocorrerá da seguinte forma:</i></span>

8.41.1 <span style="color:red"><i>R$</i></span> <span style="color:red"><b><i>X.XXX,XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>valor em extenso</i></b></span><span style="color:red"><i>) quando do início da segunda etapa;</i></span>

8.41.2 <span style="color:red"><i>(...).</i></span>

8.42. <span style="color:red"><i>Fica o Contratado obrigado a devolver, com correção monetária, a integralidade do valor antecipado na hipótese de inexecução do objeto.</i></span>

8.42.1 <span style="color:red"><i>No caso de inexecução parcial, deverá haver a devolução do valor relativo à parcela não-executada do contrato.</i></span>

8.42.2 <span style="color:red"><i>O valor relativo à parcela antecipada e não executada do contrato será atualizado monetariamente pela variação acumulada do</i></span> <span style="color:red"><b><i>[especificar o índice de correção monetária a ser adotado]</i></b></span><span style="color:red"><i>, ou outro índice que venha a substituí-lo, desde a data do pagamento da antecipação até a data da devolução.</i></span>

8.43. <span style="color:red"><i>A liquidação ocorrerá de acordo com as regras do tópico respectivo deste instrumento.</i></span>

8.44. <span style="color:red"><i>O pagamento antecipado será efetuado no prazo máximo de até</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) dias, contados do recebimento do [recibo]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[nota fiscal]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[fatura]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[documento idôneo].</i></span>

8.45. <span style="color:red"><i>A antecipação de pagamento dispensa o ateste ou recebimento prévios do objeto, os quais deverão ocorrer após a regular execução da parcela contratual a que se refere o valor antecipado.</i></span>

8.46. <span style="color:red"><i>O pagamento de que trata este item está condicionado à tomada das seguintes providências pelo Contratado:</i></span>

8.46.1 <span style="color:red"><i>comprovação da execução da etapa imediatamente anterior do objeto pelo Contratado, para a antecipação do valor remanescente;</i></span>

8.46.2 <span style="color:red"><i>prestação da garantia adicional nas modalidades de que trata o art. 96 da Lei nº 14.133, de 2021, no percentual de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento).</i></span>

8.47. <span style="color:red"><i>O pagamento do valor a ser antecipado ocorrerá respeitando eventuais retenções tributárias incidentes.</i></span>

### <b>Reajuste</b>

8.48. Os preços inicialmente contratados são fixos e irreajustáveis no prazo de um ano contado da data do orçamento estimado, em <span style="color:red"><i>[DD/MM/AAAA]</i></span>.

8.49. Após o interregno de um ano, e independentemente de pedido do Contratado, os preços iniciais serão reajustados, mediante a aplicação, pelo Contratante, do Índice de Custos de Tecnologia da Informação - ICTI, mantido pela Fundação Instituto de Pesquisa Econômica Aplicada - IPEA, exclusivamente para as obrigações iniciadas e concluídas após a ocorrência da anualidade.

8.50. Nos reajustes subsequentes ao primeiro, o interregno mínimo de um ano será contado a partir dos efeitos financeiros do último reajuste.

8.51. No caso de atraso ou não divulgação do(s) índice (s) de reajustamento, o Contratante pagará ao Contratado a importância calculada pela última variação conhecida, liquidando a diferença correspondente tão logo seja(m) divulgado(s) o(s) índice(s) definitivo(s).

8.52. Nas aferições finais, o(s) índice(s) utilizado(s) para reajuste será(ão), obrigatoriamente, o(s) definitivo(s).

8.53. Caso o(s) índice(s) estabelecido(s) para reajustamento venha(m) a ser extinto(s) ou de qualquer forma não possa(m) mais ser utilizado(s), será(ão) adotado(s), em substituição, o(s) que vier(em) a ser determinado(s) pela legislação então em vigor.

8.54. Na ausência de previsão legal quanto ao índice substituto, as partes elegerão novo índice oficial, para reajustamento do preço do valor remanescente, por meio de termo aditivo.

8.55. O reajuste será realizado por apostilamento.

### <b>Cessão de Crédito</b>

8.56. As cessões de crédito dependerão de prévia aprovação do Contratante.

8.56.1 A eficácia da cessão de crédito, em relação à Administração, está condicionada à celebração de termo aditivo ao contrato administrativo.

8.56.2 Sem prejuízo do regular atendimento da obrigação contratual de cumprimento de todas as condições de habilitação por parte do Contratado (cedente), a celebração do aditamento de cessão de crédito e a realização dos pagamentos respectivos também se condicionam à regularidade fiscal e trabalhista do cessionário, bem como à certificação de que o cessionário não se encontra impedido de licitar e contratar com o Poder Público, conforme a legislação em vigor, ou de receber benefícios ou incentivos fiscais ou creditícios, direta ou indiretamente, conforme o art. 12 da Lei nº 8.429, de 1992, nos termos do Parecer JL-01, de 18 de maio de 2020.

8.56.3 O crédito a ser pago à cessionária é exatamente aquele que seria destinado à cedente (Contratado) pela execução do objeto contratual, restando absolutamente incólumes todas as defesas e exceções ao pagamento e todas as demais cláusulas exorbitantes ao direito comum aplicáveis no regime jurídico de direito público incidente sobre os contratos administrativos, incluindo a possibilidade de pagamento em conta vinculada ou de pagamento pela efetiva comprovação do fato gerador, quando for o caso, e o desconto de multas, glosas e prejuízos causados à Administração.

8.56.4 A cessão de crédito não afetará a execução do objeto contratado, que continuará sob a integral responsabilidade do Contratado.

8.57. O disposto nesta seção não afeta as operações de crédito de que trata a Instrução Normativa SEGES/MGI nº 82, de 21 de fevereiro de 2025, as quais ficam por esta regidas.

## 9. Sanções Administrativas e Procedimentos para retenção ou glosa no pagamento

9.1. Nos casos de inadimplemento na execução do objeto, as ocorrências serão registradas pela contratante, conforme a tabela abaixo:

| <span style="color:red"><b><i>Id</i></b></span> | <span style="color:red"><b><i>Ocorrência</i></b></span> | <span style="color:red"><b><i>Glosa / Sanção</i></b></span> |
|---|---|---|
| <span style="color:red"><i>1</i></span> | <span style="color:red"><i>Não prestar os esclarecimentos imediatamente, referente à execução dos serviços, salvo quando implicarem em indagações de caráter técnico, hipótese em que serão respondidos no prazo máximo de (.....) horas úteis.</i></span> | <span style="color:red"><i>Multa de (.....) % sobre o valor total do Contrato por dia útil de atraso em prestar as informações por escrito, ou por outro meio quando autorizado pela contratante, até o limite de (.....) dias úteis.</i></span> |
|  |  | <span style="color:red"><i>Após o limite de (.....) dias úteis, aplicar-se-á multa de (.....) % do valor total do Contrato.</i></span> |
| <span style="color:red"><i>2</i></span> | <span style="color:red"><i>Não atender ao indicador de nível de serviço IAP (Índice de Atendimento no Prazo)</i></span> | <span style="color:red"><i>IAP &gt;= 90%: sem descontos sobre o valor da fatura mensal.</i></span> |
|  |  | <span style="color:red"><i>IAP &gt;= 80% e &lt; 90%: 10% de desconto sobre o valor da fatura mensal.</i></span> |
|  |  | <span style="color:red"><i>IAP &gt;= 70% e &lt; 80%: 20% de desconto sobre o valor da fatura mensal.</i></span> |
|  |  | <span style="color:red"><i>IAP &lt; 70%: 30% de desconto sobre o valor da fatura mensal.</i></span> |
| <span style="color:red"><i>…</i></span> | <span style="color:red"><i>…</i></span> | <span style="color:red"><i>…</i></span> |
| <span style="color:red"><i>N</i></span> | <span style="color:red"><i>Não cumprir qualquer outra obrigação contratual não citada nesta tabela.</i></span> | <span style="color:red"><i>Advertência.</i></span><br><span style="color:red"><i>Em caso de reincidência ou configurado prejuízo aos resultados pretendidos com a contratação, aplica-se multa de (.....) % do valor total do Contrato.</i></span> |

9.2. Nos termos do art. 19, inciso III da Instrução Normativa SGD/ME nº 94, de 2022, será efetuada a retenção ou glosa no pagamento, proporcional à irregularidade verificada, sem prejuízo das sanções cabíveis, nos casos em que p contratado:

9.2.1 não atingir os valores mínimos aceitáveis fixados nos critérios de aceitação, não produzir os resultados ou deixar de executar as atividades contratadas; ou

9.2.2 deixar de utilizar materiais e recursos humanos exigidos para fornecimento da solução de TIC, ou utilizá-los com qualidade ou quantidade inferior à demandada;

9.3. Comete infração administrativa, nos termos da Lei nº 14.133, de 2021, o Contratado que:

a) der causa à inexecução parcial do contrato;

b) der causa à inexecução parcial do contrato que cause grave dano à Administração ou ao funcionamento dos serviços públicos ou ao interesse coletivo;

c) der causa à inexecução total do contrato;

d) ensejar o retardamento da execução ou da entrega do objeto da contratação sem motivo justificado;

e) apresentar documentação falsa ou prestar declaração falsa durante a execução do contrato;

f) praticar ato fraudulento na execução do contrato;

g) comportar-se de modo inidôneo ou cometer fraude de qualquer natureza;

h) praticar ato lesivo previsto no art. 5º da Lei nº 12.846, de 1º de agosto de 2013.

9.4. Serão aplicadas ao Contratado que incorrer nas infrações acima descritas as seguintes sanções:

9.4.1 Advertência, quando o Contratado der causa à inexecução parcial do contrato, sempre que não se justificar a imposição de penalidade mais grave;

9.4.2 Impedimento de licitar e contratar, quando praticadas as condutas descritas nas alíneas “b”, “c” e “d” do subitem acima, sempre que não se justificar a imposição de penalidade mais grave;

9.4.3 Declaração de inidoneidade para licitar e contratar, quando praticadas as condutas descritas nas alíneas “e”, “f”, “g” e “h” do subitem acima, bem como nas alíneas “b”, “c” e “d”, que justifiquem a imposição de penalidade mais grave.

9.4.4 Multa:

9.4.4.1. <span style="color:red"><i>Moratória, para as infrações descritas no item “d”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) por dia de atraso injustificado sobre o valor da parcela inadimplida, até o limite de</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) dias.</i></span>

9.4.4.2. <span style="color:red"><i>Moratória de 0,07% (sete centésimos por cento) por dia de atraso injustificado sobre o valor total do contrato, até o máximo de 2% (dois por cento), pela inobservância do prazo fixado para apresentação, suplementação ou reposição da garantia;</i></span>

9.4.4.2.1. <span style="color:red"><i>O atraso superior a 25 (vinte e cinco) dias para apresentação, suplementação ou reposição da garantia autoriza a Administração a promover a extinção do contrato por descumprimento ou cumprimento irregular de suas cláusulas, conforme dispõe o inciso I do art. 137 da Lei n. 14.133, de 2021.</i></span>

9.4.4.3. <span style="color:red"><i>Compensatória, para as infrações descritas acima alíneas “</i></span><span style="color:red"><b><i>e</i></b></span><span style="color:red"><i>” a “</i></span><span style="color:red"><b><i>h</i></b></span><span style="color:red"><i>” de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

9.4.4.4. <span style="color:red"><i>Compensatória, para a inexecução total do contrato prevista acima na alínea “</i></span><span style="color:red"><b><i>c</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

9.4.4.5. <span style="color:red"><i>Compensatória, para a infração descrita acima na alínea “</i></span><span style="color:red"><b><i>b</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

9.4.4.6. <span style="color:red"><i>Compensatória, em substituição à multa moratória para a infração descrita acima na alínea “d”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

9.4.4.7. <span style="color:red"><i>Compensatória, para a infração descrita acima na alínea “</i></span><span style="color:red"><b><i>a</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação [, ressalvadas as seguintes infrações também enquadráveis nessa alínea:]</i></span>

9.4.4.7.1. <span style="color:red"><i>[INDICAR ITENS ESPECÍFICOS DE INEXECUÇÃO PARCIAL QUE JUSTIFIQUEM PENALIDADE DIVERSA</i></span><span style="color:red">];</span>

9.5. A aplicação das sanções previstas neste Termo de Referência não exclui, em hipótese alguma, a obrigação de reparação integral do dano causado ao Contratante.

9.6. Todas as sanções previstas neste Termo de Referência poderão ser aplicadas cumulativamente com a multa.

9.7. Antes da aplicação da multa será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis, contado da data de sua intimação.

9.8. Se a multa aplicada e as indenizações cabíveis forem superiores ao valor do pagamento eventualmente devido pelo Contratante ao Contratado, além da perda desse valor, a diferença será descontada da garantia prestada ou será cobrada judicialmente.

9.9. A multa poderá ser recolhida administrativamente no prazo máximo de <span style="color:red"><i>XX</i></span> (<span style="color:red"><i>xxxxx</i></span>) dias, a contar da data do recebimento da comunicação enviada pela autoridade competente.

9.10. A aplicação das sanções realizar-se-á em processo administrativo que assegure o contraditório e a ampla defesa ao Contratado, observando-se o procedimento previsto no caput e parágrafos do art. 158 da Lei nº 14.133, de 2021, para as penalidades de impedimento de licitar e contratar e de declaração de inidoneidade para licitar ou contratar.

9.10.1 Para a garantia da ampla defesa e contraditório, as notificações serão enviadas eletronicamente para os endereços de e-mail informados na proposta comercial, bem como os cadastrados pela empresa no SICAF.

9.10.2 Os endereços de e-mail informados na proposta comercial e/ou cadastrados no SICAF serão considerados de uso contínuo da empresa, não cabendo alegação de desconhecimento das comunicações a eles comprovadamente enviadas.

9.11. Na aplicação das sanções serão considerados:

9.11.1 a natureza e a gravidade da infração cometida;

9.11.2 as peculiaridades do caso concreto;

9.11.3 as circunstâncias agravantes ou atenuantes;

9.11.4 os danos que dela provierem para o Contratante; e

9.11.5 a implantação ou o aperfeiçoamento de programa de integridade, conforme normas e orientações dos órgãos de controle.

9.12. Os atos previstos como infrações administrativas na Lei nº 14.133, de 2021, ou em outras leis de licitações e contratos da Administração Pública que também sejam tipificados como atos lesivos na Lei nº 12.846, de 2013, serão apurados e julgados conjuntamente, nos mesmos autos, observados o rito procedimental e autoridade competente definidos na referida Lei.

9.13. A personalidade jurídica do Contratado poderá ser desconsiderada sempre que utilizada com abuso do direito para facilitar, encobrir ou dissimular a prática dos atos ilícitos previstos neste Termo de Referência ou para provocar confusão patrimonial, e, nesse caso, todos os efeitos das sanções aplicadas à pessoa jurídica serão estendidos aos seus administradores e sócios com poderes de administração, à pessoa jurídica sucessora ou à empresa do mesmo ramo com relação de coligação ou controle, de fato ou de direito, com o Contratado, observados, em todos os casos, o contraditório, a ampla defesa e a obrigatoriedade de análise jurídica prévia.

9.14. O Contratante deverá, no prazo máximo de 15 (quinze) dias úteis, contado da data de aplicação da sanção, informar e manter atualizados os dados relativos às sanções por ela aplicadas, para fins de publicidade no Cadastro Nacional de Empresas Inidôneas e Suspensas (CEIS) e no Cadastro Nacional de Empresas Punidas (CNEP), instituídos no âmbito do Poder Executivo Federal.

9.14.1 As penalidades serão obrigatoriamente registradas no SICAF.

9.15. As sanções de impedimento de licitar e contratar e declaração de inidoneidade para licitar ou contratar são passíveis de reabilitação na forma do art. 163 da Lei nº 14.133, de 2021.

9.16. Os débitos do Contratado para com a Administração Contratante, resultantes de multa administrativa e/ou indenizações, não inscritos em dívida ativa, poderão ser compensados, total ou parcialmente, com os créditos devidos pelo referido órgão decorrentes deste mesmo contrato ou de outros contratos administrativos que o Contratado possua com o mesmo órgão ora Contratante, na forma da Instrução Normativa SEGES/ME nº 26, de 13 de abril de 2022.

## 10. FORMA E CRITÉRIOS DE SELEÇÃO DO FORNECEDOR E REGIME DE EXECUÇÃO

### <b>Forma de seleção e critério de julgamento da proposta</b>

10.1. <span style="color:red"><i>O fornecedor será selecionado por meio da realização de procedimento de LICITAÇÃO, na modalidade [PREGÃO]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[CONCORRÊNCIA], sob a forma ELETRÔNICA, com adoção do critério de julgamento pelo [MENOR PREÇO]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[MAIOR DESCONTO]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[TÉCNICA E PREÇO].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

10.2. <span style="color:red"><i>O fornecedor será selecionado por meio de contratação direta com fundamento no art. [</i></span><span style="color:red"><b><i>74 OU 75</i></b></span><span style="color:red"><i>], inciso [</i></span><span style="color:red"><b><i>indicar o inciso</i></b></span><span style="color:red"><i>], da Lei nº 14.133, de 1º de abril de 2021, com base no seguinte fundamento: [</i></span><span style="color:red"><b><i>descrever a fundamentação da contratação para enquadramento no dispositivo legal indicado</i></b></span><span style="color:red"><i>]</i></span>

### <b>Regime de Execução</b>

10.3. O regime de execução do contrato será por <span style="color:red">[....].</span>

### <b>Exigências de habilitação</b>

10.4. Para fins de habilitação, deverá o interessado comprovar os seguintes requisitos:

### <b>Habilitação jurídica</b>

10.5. Pessoa física: cédula de identidade (RG) ou documento equivalente que, por força de lei, tenha validade para fins de identificação em todo o território nacional;

10.6. Empresário individual: inscrição no Registro Público de Empresas Mercantis, a cargo da Junta Comercial da respectiva sede;

10.7. Microempreendedor Individual - MEI: Certificado da Condição de Microempreendedor Individual - CCMEI, cuja aceitação ficará condicionada à verificação da autenticidade no sítio https://www.gov.br/empresas-e-negocios/pt-br/empreendedor;

10.8. Sociedade empresária, sociedade limitada unipessoal – SLU ou sociedade identificada como empresa individual de responsabilidade limitada - EIRELI: inscrição do ato constitutivo, estatuto ou contrato social no Registro Público de Empresas Mercantis, a cargo da Junta Comercial da respectiva sede, acompanhada de documento comprobatório de seus administradores;

10.9. Sociedade empresária estrangeira: portaria de autorização de funcionamento no Brasil, publicada no Diário Oficial da União e arquivada na Junta Comercial da unidade federativa onde se localizar a filial, agência, sucursal ou estabelecimento, a qual será considerada como sua sede, conforme Instrução Normativa DREI/ME n.º 77, de 18 de março de 2020.

10.10. Sociedade simples: inscrição do ato constitutivo no Registro Civil de Pessoas Jurídicas do local de sua sede, acompanhada de documento comprobatório de seus administradores;

10.11. Filial, sucursal ou agência de sociedade simples ou empresária: inscrição do ato constitutivo da filial, sucursal ou agência da sociedade simples ou empresária, respectivamente, no Registro Civil das Pessoas Jurídicas ou no Registro Público de Empresas Mercantis onde opera, com averbação no Registro onde tem sede a matriz;

10.12. Sociedade cooperativa: ata de fundação e estatuto social, com a ata da assembleia que o aprovou, devidamente arquivado na Junta Comercial ou inscrito no Registro Civil das Pessoas Jurídicas da respectiva sede, além do registro de que trata o art. 107 da Lei nº 5.764, de 16 de dezembro 1971.

10.13. Consórcio de empresas: contrato de consórcio devidamente arquivado no Registro Civil das Pessoas Jurídicas ou no Registro Público de Empresas Mercantis (art. 279 da Lei nº 6.404, de 15 de dezembro de 1976) ou compromisso público ou particular de constituição, subscrito pelos consorciados, com a indicação da empresa líder, responsável por sua representação perante a Administração (art. 15, caput, I e II, da Lei nº 14.133, de 2021).

10.14. <span style="color:red"><i>Ato de autorização para o exercício da atividade de ............ (especificar a atividade contratada sujeita à autorização), expedido por ....... (especificar o órgão competente) nos termos do art. ..... da (Lei/Decreto) n° ........</i></span>

10.15. Os documentos apresentados deverão estar acompanhados de todas as alterações ou da consolidação respectiva.

### <b>Habilitação fiscal, social e trabalhista</b>

10.16. Prova de inscrição no Cadastro Nacional de Pessoas Jurídicas ou no Cadastro de Pessoas Físicas, conforme o caso;

10.17. Prova de regularidade fiscal perante a Fazenda Nacional, mediante apresentação de certidão expedida conjuntamente pela Secretaria da Receita Federal do Brasil (RFB) e pela Procuradoria-Geral da Fazenda Nacional (PGFN), referente a todos os créditos tributários federais e à Dívida Ativa da União (DAU) por elas administrados, inclusive aqueles relativos à Seguridade Social, nos termos da Portaria Conjunta nº 1.751, de 02 de outubro de 2014, do Secretário da Receita Federal do Brasil e da Procuradora-Geral da Fazenda Nacional.

10.18. Prova de regularidade com o Fundo de Garantia do Tempo de Serviço (FGTS);

10.19. Prova de inexistência de débitos inadimplidos perante a Justiça do Trabalho, mediante a apresentação de certidão negativa ou positiva com efeito de negativa, nos termos do Título VII-A da Consolidação das Leis do Trabalho, aprovada pelo Decreto-Lei nº 5.452, de 1º de maio de 1943;

10.20. Prova de inscrição no cadastro de contribuintes Distrital ou Municipal relativo ao domicílio ou sede do fornecedor, pertinente ao seu ramo de atividade e compatível com o objeto contratual;

10.21. Prova de regularidade com a Fazenda Distrital ou Municipal do domicílio ou sede do fornecedor, relativa à atividade em cujo exercício contrata ou concorre;

10.22. Caso o fornecedor seja considerado isento dos tributos relacionados ao objeto contratual, deverá comprovar tal condição mediante a apresentação de declaração da Fazenda respectiva do seu domicílio ou sede, ou outra equivalente, na forma da lei.

10.23. O fornecedor enquadrado como microempreendedor individual que pretenda auferir os benefícios do tratamento diferenciado previstos na Lei Complementar n. 123, de 2006, estará dispensado da prova de inscrição nos cadastros de contribuintes estadual e municipal.

### <b>Qualificação Econômico-Financeira</b>

10.24. certidão negativa de insolvência civil expedida pelo distribuidor do domicílio ou sede do interessado, caso se trate de pessoa física, desde que admitida a sua participação na licitação/contratação, ou de sociedade simples;

10.25. certidão negativa de falência expedida pelo distribuidor da sede do fornecedor;

10.26. balanço patrimonial, demonstração de resultado de exercício e demais demonstrações contábeis <span style="color:red"><i>................... [do último exercício social]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[dos dois últimos exercícios sociais]</i></span><i>,</i> já exigíveis e apresentados na forma da lei, comprovando, índices de Liquidez Geral (LG), Liquidez Corrente (LC), e Solvência Geral (SG) superiores a 1 (um), obtidos por meio da aplicação das seguintes fórmulas:

| LG = | Ativo Circulante + Realizável a Longo Prazo |
|---|---|
|  | Passivo Circulante + Passivo Não Circulante |

| SG = | Ativo Total |
|---|---|
|  | Passivo Circulante + Passivo Não Circulante |

| LC = | Ativo Circulante |
|---|---|
|  | Passivo Circulante |

10.27. <span style="color:red"><i>Caso a empresa apresente resultado inferior ou igual a 1 (um) em qualquer dos índices de Liquidez Geral (LG), Solvência Geral (SG) e Liquidez Corrente (LC), será exigido, para fins de habilitação, [</i></span><span style="color:red"><b><i>capital mínimo</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>patrimônio líquido mínimo</i></b></span><span style="color:red"><i>] de [</i></span><span style="color:red"><b><i>definir percentual, limitado a 10%</i></b></span><span style="color:red"><i>] do [</i></span><span style="color:red"><b><i>valor total estimado da contratação</i></b></span> <span style="color:red;background:yellow"><b><i>– aplicável para o contrato de escopo</i></b></span><span style="color:red;background:yellow"><i>]</i></span> <span style="color:red;background:yellow"><b><i><u>OU</u></i></b></span> <span style="color:red;background:yellow"><i>[</i></span><span style="color:red;background:yellow"><b><i>valor total estimado da contratação para o período de doze meses – aplicável para o contrato de serviço continuado</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>valor total estimado da parcela pertinente</i></b></span><span style="color:red"><i>].</i></span>

10.28. <span style="color:red"><i>Os indicadores fixados acima deverão ser atingidos em cada um dos dois últimos exercícios sociais, sob pena de inabilitação;</i></span>

10.29. Os documentos referidos acima limitar-se-ão ao último exercício no caso de a pessoa jurídica ter sido constituída há menos de 2 (dois) anos;

10.30. Os documentos referidos acima deverão ser exigidos com base no limite definido pela Receita Federal do Brasil para transmissão da Escrituração Contábil Digital - ECD ao Sped.

10.31. <span style="color:red"><i>O atendimento dos índices econômicos previstos neste termo de referência deverá ser atestado mediante declaração assinada por profissional habilitado da área contábil, apresentada pelo fornecedor.</i></span>

10.32. As empresas criadas no exercício financeiro da licitação/contratação deverão atender a todas as exigências da habilitação e poderão substituir os demonstrativos contábeis pelo balanço de abertura.

### <b>Qualificação Técnica</b>

10.33. <span style="color:red"><i>Declaração de que o fornecedor tomou conhecimento de todas as informações e das condições locais para o cumprimento das obrigações objeto da contratação.</i></span>

10.33.1 <span style="color:red"><i>Essa declaração poderá ser substituída por declaração formal assinada pelo responsável técnico do interessado acerca do conhecimento pleno das condições e peculiaridades da contratação.</i></span>

10.34. <span style="color:red"><i>Registro ou inscrição da empresa na entidade profissional competente</i></span> <span style="color:red"><b><i>.........(escrever por extenso, se for o caso</i></b></span><span style="color:red"><i>), em plena validade;</i></span>

10.34.1 <span style="color:red"><i>Sociedades empresárias estrangeiras atenderão à exigência por meio da apresentação, no momento da assinatura do contrato ou do aceite de instrumento equivalente, da solicitação de registro perante a entidade profissional competente no Brasil.</i></span>

10.35. <span style="color:red"><i>Prova de atendimento aos requisitos ........, previstos na lei ............:</i></span>

10.36. Comprovação de aptidão para execução de serviço similar, de complexidade tecnológica e operacional equivalente ou superior à do objeto desta contratação, ou do item pertinente, por meio da apresentação de certidões ou atestados emitidos por pessoas jurídicas de direito público ou privado, ou pelo conselho profissional competente, quando for o caso.

10.36.1 Para fins da comprovação de que trata este subitem, os atestados deverão dizer respeito a contrato(s) executado(s) com as seguintes características mínimas:

10.36.1.1. <span style="color:red"><i>contrato(s) que comprove(m) a experiência mínima de XXX (XXX) anos do fornecedor na prestação dos serviços, em períodos sucessivos ou não, sendo aceito o somatório de atestados de períodos diferentes;</i></span>

10.36.1.2. <span style="color:red"><i>... [INSERIR, SE FOR O CASO, OUTRAS CARACTERÍSTICAS MÍNIMAS DOS SERVIÇOS A SEREM COMPROVADAS POR MEIO DOS ATESTADOS]</i></span>

10.36.2 <span style="color:red"><i>Serão admitidos, para fins de comprovação de quantitativo mínimo de serviço, a apresentação e o somatório de diferentes atestados de serviços executados de forma concomitante.</i></span>

10.36.3 Os atestados de capacidade técnica poderão ser apresentados em nome da matriz ou da filial do fornecedor.

10.36.4 O fornecedor disponibilizará todas as informações necessárias à comprovação da legitimidade dos atestados, apresentando, quando solicitado pela Administração, cópia do contrato que deu suporte à contratação, endereço atual do Contratante e local em que foram prestados os serviços, entre outros documentos.

10.36.5 Os atestados deverão referir-se a serviços prestados no âmbito de sua atividade econômica principal ou secundária especificadas no contrato social vigente.

10.37. <span style="color:red"><i>Declaração de que o fornecedor possui ou instalará escritório no município de ..................., o que deverá ser comprovado no prazo máximo de 60 (sessenta) dias, contado a partir da vigência do contrato.</i></span>

10.38. Serão aceitos atestados ou outros documentos hábeis emitidos por entidades estrangeiras quando acompanhados de tradução para o português, salvo se comprovada a inidoneidade da entidade emissora.

10.39. A apresentação, pelo fornecedor, de certidões ou atestados de desempenho anterior emitido em favor de consórcio do qual tenha feito parte será admitida, desde que atendidos os requisitos do art. 67, §§ 10 e 11, da Lei nº 14.133/2021 e regulamentos sobre o tema.

### <b>Disposições gerais sobre habilitação</b>

10.40. Quando permitida a participação na licitação/contratação de empresas estrangeiras que não funcionem no País, as exigências de habilitação serão atendidas mediante documentos equivalentes, inicialmente apresentados em tradução livre.

10.41. Na hipótese de o fornecedor ser empresa estrangeira que não funcione no País, para assinatura do contrato ou da ata de registro de preços ou do aceite do instrumento equivalente, os documentos exigidos para a habilitação serão traduzidos por tradutor juramentado no País e apostilados nos termos do disposto no Decreto nº 8.660, de 29 de janeiro de 2016, ou de outro que venha a substituí-lo, ou consularizados pelos respectivos consulados ou embaixadas.

10.42. Não serão aceitos documentos de habilitação com indicação de CNPJ/CPF diferentes, salvo aqueles legalmente permitidos.

10.43. Se o fornecedor for a matriz, todos os documentos deverão estar em nome da matriz, e se o fornecedor for a filial, todos os documentos deverão estar em nome da filial, exceto para atestados de capacidade técnica, e no caso daqueles documentos que, pela própria natureza, comprovadamente, forem emitidos somente em nome da matriz.

10.44. Serão aceitos registros de CNPJ de fornecedor matriz e filial com diferenças de números de documentos pertinentes ao CND e ao CRF/FGTS, quando for comprovada a centralização do recolhimento dessas contribuições.

### <b>Documentação complementar para cooperativas</b>

10.45. Caso admitida a participação de cooperativas, será exigida a seguinte documentação complementar:

10.45.1 A relação dos cooperados que atendem aos requisitos técnicos exigidos para a contratação e que executarão o contrato, com as respectivas atas de inscrição e a comprovação de que estão domiciliados na localidade da sede da cooperativa, respeitado o disposto nos arts. 4º, inciso XI, 21, inciso I e 42, §§2º a 6º da Lei n. 5.764, de 1971;

10.45.2 A declaração de regularidade de situação do contribuinte individual – DRSCI, para cada um dos cooperados indicados;

10.45.3 A comprovação do capital social proporcional ao número de cooperados necessários à prestação do serviço;

10.45.4 O registro previsto na Lei n. 5.764, de 1971, art. 107;

10.45.5 A comprovação de integração das respectivas quotas-partes por parte dos cooperados que executarão o contrato;

10.45.6 Os seguintes documentos para a comprovação da regularidade jurídica da cooperativa:

10.45.6.1. ata de fundação;

10.45.6.2. estatuto social com a ata da assembleia que o aprovou;

10.45.6.3. regimento dos fundos instituídos pelos cooperados, com a ata da assembleia;

10.45.6.4. editais de convocação das três últimas assembleias gerais extraordinárias;

10.45.6.5. três registros de presença dos cooperados que executarão o contrato em assembleias gerais ou nas reuniões seccionais;

10.45.6.6. ata da sessão que os cooperados autorizaram a cooperativa a contratar o objeto da contratação; e

10.45.6.7. última auditoria contábil-financeira da cooperativa, conforme dispõe o art. 112 da Lei n. 5.764, de 1971, ou uma declaração, sob as penas da lei, de que tal auditoria não foi exigida pelo órgão fiscalizador.

## 11. ESTIMATIVAS DO VALOR DA CONTRATAÇÃO

11.1. <span style="color:red"><i>O custo estimado total da contratação, que é o máximo aceitável, é de R$... (por extenso), conforme custos unitários apostos na [</i></span><span style="color:red"><b><i>tabela contida no item 1.1 acima</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>em anexo</i></b></span><span style="color:red"><i>].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

11.2. <span style="color:red"><i>O valor de referência para aplicação do maior desconto corresponde a R$.....</i></span>

<span style="color:red"><b><i>OU</i></b></span>

11.3. <span style="color:red"><i>O custo estimado da contratação possui caráter sigiloso e será tornado público apenas e imediatamente após o julgamento das propostas.</i></span>

11.3.1 <span style="color:red"><i>Quando as propostas permanecerem com preços acima do orçamento estimado, o custo estimado da contratação será tornado público após a fase de lances.</i></span>

11.4. <span style="color:red"><i>A estimativa de custo levou em consideração o risco envolvido na contratação e sua alocação entre Contratante e Contratado, conforme especificado na matriz de risco constante do Contrato.</i></span>

11.5. <span style="color:red;background:cyan"><i>Em caso de Registro de Preços, os preços registrados poderão ser alterados ou atualizados em decorrência de eventual redução dos preços praticados no mercado ou de fato que eleve o custo dos bens, das obras ou dos serviços registrados, nas seguintes situações:</i></span>

11.5.1 <span style="color:red;background:cyan"><i>em caso de força maior, caso fortuito ou fato do príncipe ou em decorrência de fatos imprevisíveis ou previsíveis de consequências incalculáveis, que inviabilizem a execução da ata tal como pactuada, nos termos do disposto na alínea “d” do inciso II do capu</i></span><span style="color:red;background:cyan"><b><i>t</i></b></span> <span style="color:red;background:cyan"><i>do art. 124 da Lei nº 14.133, de 2021;</i></span>

11.5.2 <span style="color:red;background:cyan"><i>em caso de criação, alteração ou extinção de quaisquer tributos ou encargos legais ou superveniência de disposições legais, com comprovada repercussão sobre os preços registrados;</i></span>

11.5.3 <span style="color:red;background:cyan"><i>serão reajustados os preços registrados, respeitada a contagem da anualidade e o índice previsto para a contratação; ou</i></span>

11.5.4 <span style="color:red;background:cyan"><i>poderão ser repactuados, a pedido do interessado, conforme critérios definidos para a contratação.</i></span>

## 12. ADEQUAÇÃO ORÇAMENTÁRIA

12.1. <span style="color:red"><i>As despesas decorrentes da presente contratação correrão à conta de recursos específicos consignados no Orçamento Geral da União.</i></span>

12.2. <span style="color:red"><i>A contratação será atendida pela seguinte dotação:</i></span>

I) <span style="color:red"><i>Gestão/unidade: [...];</i></span>

II) <span style="color:red"><i>Fonte de recursos: [...];</i></span>

III) <span style="color:red"><i>Programa de trabalho: [...];</i></span>

IV) <span style="color:red"><i>Elemento de despesa: [...]; e</i></span>

V) <span style="color:red"><i>Plano interno: [...].</i></span>

12.3. <span style="color:red"><i>A dotação relativa aos exercícios financeiros subsequentes será indicada após aprovação da Lei Orçamentária respectiva e liberação dos créditos correspondentes, mediante apostilamento.</i></span>

12.4. <span style="color:red;background:cyan"><i>A indicação da dotação orçamentária fica postergada para o momento da assinatura do contrato ou instrumento equivalente.</i></span>

## 13. DISPOSIÇÕES FINAIS

13.1. As informações contidas neste Termo de Referência não são classificadas como sigilosas <span style="color:red"><b>[</b></span><span style="color:red"><b><i>exceto o custo estimado da contratação, que possui caráter sigiloso até o julgamento das propostas</i></b></span><span style="color:red"><b>]</b></span>.

### <b>Cronograma Físico Financeiro</b>

| Evento | Prazo estimado | Valor |
|---|---|---|
| Evento 1 | (.../.../...) a (.../.../...)<br>ou<br>(....) dias após a emissão da OS | R$ ......... |
| Evento 2 | [....] | R$ ......... |
| .... | [....] | R$ ......... |
| Evento N | [....] | R$ ......... |

| <b>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</b><br><b>Integrante</b><br><b>Requisitante</b><br><span style="color:red"><i>&lt;Nome&gt;</i></span><br><span style="color:red"><i>&lt;Cargo&gt;</i></span><br><span style="color:red"><i>&lt;Matrícula&gt;</i></span> | <b>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</b><br><b>Integrante</b><br><b>Técnico</b><br><span style="color:red"><i>&lt;Nome&gt;</i></span><br><span style="color:red"><i>&lt;Cargo&gt;</i></span><br><span style="color:red"><i>&lt;Matrícula&gt;</i></span> | <b>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</b><br><b>Integrante</b><br><b>Administrativo</b><br><span style="color:red"><i>&lt;Nome&gt;</i></span><br><span style="color:red"><i>&lt;Cargo&gt;</i></span><br><span style="color:red"><i>&lt;Matrícula&gt;</i></span> |
|---|---|---|

> <b>Autoridade Máxima da Área de TIC</b>

> <b>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</b><br><span style="color:red"><i>&lt;Nome&gt;</i></span><br><span style="color:red"><i>&lt;Cargo&gt;</i></span><br><span style="color:red"><i>&lt;Matrícula&gt;</i></span>

<span style="color:red"><i>[Local]</i></span><i>,</i> <span style="color:red"><i>[dia]</i></span> <i>de</i> <span style="color:red"><i>[mês]</i></span> <i>de</i> <span style="color:red"><i>[ano].</i></span>

Aprovo,

> <b>Autoridade Competente</b>

> <b>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</b><br><span style="color:red"><i>&lt;Nome&gt;</i></span><br><span style="color:red"><i>&lt;Cargo&gt;</i></span><br><span style="color:red"><i>&lt;Matrícula&gt;</i></span>
