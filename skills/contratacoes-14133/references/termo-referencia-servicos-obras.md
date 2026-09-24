# Modelo de Termo de Referência — Serviços e Obras, Exceto TIC

Fonte: modelo oficial da Advocacia-Geral da União (AGU) para a Lei nº 14.133/2021, versão de maio/2026, fornecido pelo usuário. Também aplicável a contratação integrada e semi-integrada. Confirmado (por comparação de hash dos arquivos) que a AGU disponibiliza o mesmo arquivo tanto na seção de licitação quanto na de contratação direta do site — este único modelo cobre **licitação (pregão/concorrência) e contratação direta (dispensa/inexigibilidade)**, com a escolha feita através das alternativas "OU" presentes no próprio texto.

## Quando usar este arquivo

Use este modelo quando o objeto da contratação for **serviço** (contínuo ou não, com ou sem dedicação exclusiva de mão de obra), **obra** ou **serviço de engenharia** — e não for Tecnologia da Informação e Comunicação (TIC), que tem modelo próprio da AGU não incluído aqui. Se a contratação for de serviços de TIC, pergunte ao usuário se ele possui o modelo específico.

## Como preencher

- O texto contém alternativas separadas por "OU". Escolha a alternativa compatível com o caso (licitação vs. contratação direta; regime de execução — empreitada por preço global/unitário, integral, tarefa, contratação integrada/semi-integrada, fornecimento e prestação de serviço associado; com ou sem dedicação exclusiva de mão de obra; obra/serviço de engenharia vs. serviço comum) e **risque as não escolhidas com `<s>…</s>`, sem apagá-las** (Regra de ouro do `SKILL.md`). O "OU" que separa a alternativa descartada também é riscado. Trechos de realce (turquesa, rosa, azul-petróleo etc.) que não se aplicam ao objeto seguem a mesma regra: riscados, não removidos.
- Preste atenção especial às cláusulas que só existem por causa da dedicação exclusiva de mão de obra (realce **rosa**: garantia adicional, conta-depósito vinculada ou pagamento por fato gerador, repactuação por acordo/convenção/dissídio coletivo, uniformes, obrigações trabalhistas detalhadas) e às de obras e serviços de engenharia (realce **azul-petróleo**). Se a contratação não tiver esse regime ou natureza, **risque essas cláusulas inteiras**, mantendo-as visíveis.
- Substitua todos os campos entre colchetes pelo conteúdo do caso, marcado com o código de cores do `SKILL.md` (vermelho; azul só para prazo numérico por extenso), com as informações da contratação em questão obtidas do ETP e do DFD já elaborados ou perguntadas diretamente ao usuário.
- Não invente fundamentação legal, percentuais de multa, prazos, índices de reajuste ou parâmetros do IMR (Instrumento de Medição de Resultado) que o modelo deixa em aberto — pergunte ao usuário ou extraia do ETP.

## Como ler este arquivo: numeração, cores e formatação do modelo

O corpo abaixo da linha horizontal reproduz o `.docx` oficial (`modelos-tr-pregao-conc/modelo-de-termo-de-referencia-servicos-e-obras-lei-no-14-133-mai-26.docx`) com a **numeração automática**, a **hierarquia dos parágrafos**, as **cores de fonte**, os **realces** e o **negrito/itálico/sublinhado** originais, em HTML embutido no Markdown (`<span style="color:red">`, `<span style="background:cyan">`, `<b>`, `<i>`, `<u>`). A conversão foi feita por `scripts/modelo_docx_para_md.py` e conferida contra o Microsoft Word: a numeração de todos os parágrafos é idêntica à exibida no Word. Quando a AGU publicar versão nova, gere este corpo de novo com o mesmo script em vez de editar à mão.

Legenda da própria AGU ("Orientações para uso do modelo – leitura obrigatória"):

| No modelo | Significado |
|---|---|
| Texto preto (sem itálico) | Redação que se espera invariável. **Qualquer alteração exige justificativa nos autos.** |
| <span style="color:red"><i>Vermelho itálico</i></span> | Texto a preencher ou adotar conforme oportunidade e conveniência, de acordo com o objeto. São as previsões "feitas para variar"; inclui as alternativas "OU" e os campos entre colchetes. |
| Realce <span style="background:yellow">amarelo</span> | Alterado em relação à versão anterior do modelo (informativo; não muda a aplicabilidade). |
| Realce <span style="background:cyan">turquesa</span> | Aplicável **exclusivamente ao Sistema de Registro de Preços (SRP)**. Fora de SRP, riscar. |
| Realce <span style="background:magenta">rosa</span> | Serviços com **dedicação exclusiva de mão de obra**. Sem esse regime, riscar. |
| Realce <span style="background:darkcyan;color:white">azul-petróleo</span> | **Obras e serviços de engenharia**. Para serviço comum, riscar. |
| Realce <span style="background:lightgray">cinza</span> | Pela Nota Explicativa 3 do modelo, trechos para **dedicação exclusiva de mão de obra** (a legenda geral do modelo, item 5, indica rosa para esse mesmo fim; o cinza aparece em poucos trechos). |

As **notas explicativas** do modelo (comentários do Word) estão em `termo-referencia-servicos-obras-notas.md`, organizadas pelo número do item. Consulte a nota do item antes de escolher entre alternativas "OU", riscar uma cláusula ou alterar texto preto. Segundo a AGU, notas explicativas e realces são removidos só na **versão final**: na minuta que vai à análise jurídica, mantenha-os.

**Ao produzir o TR**, siga a seção "Regra de ouro" do `SKILL.md`: mantenha a numeração, a hierarquia, as cores, os realces e a formatação do modelo, e aplique por cima o código de alterações do IPP (vermelho = inclusão, verde = ajuste de redação, azul = só prazo numérico escrito por extenso, `<s>` = supressão).

## Orientações do IPP da AGU para o TR

Detalhamento completo em `references/ipp-agu-orientacoes.md`, seção "Termo de Referência". Pontos decisivos:

- **Prazo de vigência não é número arbitrário**: deve decorrer da **soma** dos prazos de execução, de substituição ou reparo (quando necessários), recebimento provisório, recebimento definitivo e pagamento.
- **Garantia do serviço ≠ garantia de execução do contrato**: a primeira (CDC ou convencional) relaciona-se à higidez e qualidade do serviço prestado; a segunda (arts. 96 a 102) assegura a regular execução do contrato. São campos distintos, e dispensar uma não afeta a outra.
- **Medição por resultado**: a unidade de medida deve permitir mensurar resultados e **eliminar a possibilidade de remunerar por quantidade de horas de serviço ou por postos de trabalho** — que é hipótese **excepcional** e exige método de cálculo definido. Adotada essa unidade, admite-se flexibilizar a execução ao longo do expediente, **vedadas horas extras ou adicionais não previstos originariamente**.
- **Indicadores de desempenho**: objetivamente mensuráveis, compreensíveis, de coleta fácil, relevantes e adequados à natureza do serviço; **evitar indicadores complexos ou sobrepostos**; prever fatores fora do controle do prestador; metas realistas; **faixa de tolerância** com menor ou nenhuma margem para atividades críticas; possibilidade de **simples notificação nas primeiras ocorrências** quando o descumprimento for ínfimo e o indicador não for crítico. A forma de cálculo da multa deve ser **"a mais simples possível"**, e as sanções devem estar **relacionadas às obrigações do modelo de execução**.
- **IMR**: quando utilizado, deve operar preferencialmente por **ferramentas informatizadas** e ser específico à contratação, "evitando-se um mecanismo de controle apenas de modo textual/protocolar". Se elaborado, é **anexo dos Estudos Preliminares** (IN SEGES/MP nº 05/2017, Anexos V-B e VIII-A).
- **Ordem de Serviço**: o modelo deve conter, no mínimo, identificação do pedido e da contratada, especificação dos serviços, estimativa prévia de horas (quando for a única opção viável), local, recursos financeiros, critérios de avaliação e **identificação dos responsáveis pela solicitação, avaliação e ateste — que não podem ter vínculo com a contratada**.
- **Especificações vedadas**: as excessivas, irrelevantes ou desnecessárias que limitem a competitividade ou favoreçam prestador específico; as que não representem a real demanda de desempenho; e as defasadas tecnológica ou metodologicamente.
- **Habilitação**: critérios justificados nos autos, analisando qualificação econômico-financeira e técnica **à luz dos riscos da contratação**. Fixar **preços máximos aceitáveis globais e unitários**.
- **Contratação direta**: identificar a forma (dispensa ou inexigibilidade) com os **fundamentos de fato e de direito**, observando o regime de pesquisa de preços do art. 7º da IN SEGES/ME nº 65/2021.
- **Mapa de Riscos**: deve ser atualizado e juntado **ao final da elaboração do TR**.
- **Divulgação**: o TR vai ao **PNCP na mesma data** da divulgação do edital ou do aviso de contratação direta (art. 12 da IN SEGES/ME nº 81/2022).
- **Registre a data de extração deste modelo**: exigida na **Declaração de utilização de modelos AGU/MGI**.

---

<b>MODELO DE TERMO DE REFERÊNCIA<br>Lei nº 14.133, de 1º de abril de 2021<br>SERVIÇOS COM E SEM DEDICAÇÃO EXCLUSIVA DE MÃO DE OBRA, OBRAS E SERVIÇOS DE ENGENHARIA, EXCETO TIC</b>

<b>[TAMBÉM APLICÁVEL PARA CONTRATAÇÃO INTEGRADA E SEMI-INTEGRADA]</b>

<b>LICITAÇÃO E CONTRATAÇÃO DIRETA</b>

<span style="color:red"><b><i>ÓRGÃO OU ENTIDADE PÚBLICA</i></b></span>

(Processo Administrativo n° <span style="color:red"><i>xxxxx</i></span>.<span style="color:red"><i>xxxxxx</i></span>/<span style="color:red"><i>xxxx</i></span>-<span style="color:red"><i>xx</i></span>)

<b>TERMO DE REFERÊNCIA</b>

## 1. CONDIÇÕES GERAIS DA CONTRATAÇÃO

1.1. Contratação <span style="color:red">de</span> <span style="color:red;background:darkcyan">[</span><span style="color:red;background:darkcyan"><i>obras</i></span><span style="color:red;background:darkcyan">]</span> <span style="color:red"><b>OU</b></span> <span style="color:red">[</span><span style="color:red"><i>serviços</i></span><span style="color:red">]</span> <span style="color:red;background:darkcyan">[</span><span style="color:red;background:darkcyan"><i>de engenharia</i></span><span style="color:red;background:darkcyan">]</span> <span style="color:red">[</span><span style="color:red"><i>contínuos</i></span><span style="color:red">]</span> <span style="color:red">de [</span><span style="color:red"><b><i>INSERIR OBJETO</i></b></span><span style="color:red">],</span> <span style="background:magenta">[</span><span style="background:magenta"><i>a serem executados com regime de dedicação exclusiva de mão de obra</i></span><span style="background:magenta">]</span><span style="color:red">,</span> nos termos da tabela abaixo, conforme condições e exigências estabelecidas neste instrumento.

| <b>ITEM</b> | <b>ESPECIFICAÇÃO</b> | <b>CATSER</b> | <b>UNIDADE DE MEDIDA</b> | <b>QUANTIDADE</b> | <b>VALOR UNITÁRIO</b> | <b>VALOR TOTAL</b> |
|---|---|---|---|---|---|---|
| <b>1</b> |  |  |  |  | <span style="color:red">R$ .... OU SIGILOSO</span> | <span style="color:red">R$ .... OU SIGILOSO</span> |
| <b>2</b> |  |  |  |  |  |  |
| <b>3</b> |  |  |  |  |  |  |
| <b>...</b> |  |  |  |  |  |  |

1.1.1. <span style="color:red;background:cyan"><i>Estimativas de consumo individualizadas, do órgão gerenciador e órgão(s) e entidade(s) participante(s)</i></span><span style="background:cyan"><i>.</i></span>

| <span style="color:red;background:cyan"><b><i>Órgão Gerenciador:</i></b></span> |  |  |  |  |  |
|---|---|---|---|---|---|
| <span style="color:red;background:cyan"><b><i>item</i></b></span> | <span style="color:red;background:cyan"><b><i>DESCRIÇÃO/ ESPECIF.</i></b></span> | <span style="color:red;background:cyan"><b><i>UNIDADE</i></b></span><br><span style="color:red;background:cyan"><b><i>DE</i></b></span><br><span style="color:red;background:cyan"><b><i>MEDIDA</i></b></span> | <span style="color:red;background:cyan"><i>REQUISIÇÃO</i></span><br><span style="color:red;background:cyan"><i>MÍNIMA</i></span> | <span style="color:red;background:cyan"><i>REQUISIÇÃO</i></span><br><span style="color:red;background:cyan"><i>Máxima</i></span> | <span style="color:red;background:cyan"><b><i>Quantidade</i></b></span><br><span style="color:red;background:cyan"><b><i>total</i></b></span> |
|  |  |  |  |  |  |

| <span style="color:red;background:cyan"><b><i>Órgão Participante:</i></b></span> |  |  |  |  |  |
|---|---|---|---|---|---|
| <span style="color:red;background:cyan"><b><i>Item</i></b></span> | <span style="color:red;background:cyan"><b><i>DESCRIÇÃO/ ESPECIF.</i></b></span> | <span style="color:red;background:cyan"><b><i>UNIDADE</i></b></span><br><span style="color:red;background:cyan"><b><i>DE</i></b></span><br><span style="color:red;background:cyan"><b><i>MEDIDA</i></b></span> | <span style="color:red;background:cyan"><i>REQUISIÇÃO</i></span><br><span style="color:red;background:cyan"><i>MÍNIMA</i></span> | <span style="color:red;background:cyan"><i>REQUISIÇÃO</i></span><br><span style="color:red;background:cyan"><i>Máxima</i></span> | <span style="color:red;background:cyan"><b><i>Quantidade</i></b></span><br><span style="color:red;background:cyan"><b><i>total</i></b></span> |
|  |  |  |  |  |  |

| <span style="color:red;background:cyan"><b><i>Órgão Participante:</i></b></span> |  |  |  |  |  |
|---|---|---|---|---|---|
| <span style="color:red;background:cyan"><b><i>Item</i></b></span> | <span style="color:red;background:cyan"><b><i>DESCRIÇÃO/ ESPECIF.</i></b></span> | <span style="color:red;background:cyan"><b><i>UNIDADE</i></b></span><br><span style="color:red;background:cyan"><b><i>DE</i></b></span><br><span style="color:red;background:cyan"><b><i>MEDIDA</i></b></span> | <span style="color:red;background:cyan"><i>REQUISIÇÃO</i></span><br><span style="color:red;background:cyan"><i>MÍNIMA</i></span> | <span style="color:red;background:cyan"><i>REQUISIÇÃO</i></span><br><span style="color:red;background:cyan"><i>Máxima</i></span> | <span style="color:red;background:cyan"><b><i>Quantidade</i></b></span><br><span style="color:red;background:cyan"><b><i>total</i></b></span> |
|  |  |  |  |  |  |

### <b>Classificação do objeto quanto à heterogeneidade ou complexidade</b>

1.2. <span style="color:red"><i>O(s) serviço(s) objeto desta contratação são caracterizados como</i></span> <span style="color:red"><b><i>comum(ns),</i></b></span> <span style="color:red"><i>conforme justificativa constante do Estudo Técnico Preliminar.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.3. <span style="color:red"><i>O objeto da contratação tem a natureza de [</i></span><span style="color:red"><b><i>obra</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>serviços especiais</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>serviços especiais de engenharia</i></b></span><span style="color:red"><i>], conforme justificativa constante do Estudo Técnico Preliminar.</i></span>

### <b>Classificação do objeto quanto ao modelo de execução</b>

1.4. <span style="color:red"><i>O serviço é enquadrado como não contínuo ou contratados por escopo.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.5. <span style="color:red"><i>O serviço é enquadrado como continuado tendo em vista que [...], sendo a vigência plurianual mais vantajosa considerando [...]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[o Estudo Técnico Preliminar]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[os termos da Nota Técnica .../...];</i></span>

### <b>Prazo de vigência</b>

1.6. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, na forma do artigo 105 da Lei n° 14.133, de 2021.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.7. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo, limitado a 5 anos]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, prorrogável por até 10 anos, na forma dos artigos 106 e 107 da Lei n° 14.133, de 2021.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.8. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo, limitado a um ano da ocorrência da emergência ou calamidade]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, improrrogável, na forma do art. 75, inciso VIII, da Lei n° 14.133/2021.</i></span>

1.9. O contrato ou outro instrumento hábil que o substitua oferece maior detalhamento das regras que serão aplicadas em relação à vigência da contratação.

## 2. FUNDAMENTAÇÃO E DESCRIÇÃO DA NECESSIDADE DA CONTRATAÇÃO

2.1. <span style="color:red"><i>A Fundamentação da Contratação e de seus quantitativos encontra-se pormenorizada em tópico específico dos Estudos Técnicos Preliminares, apêndice deste Termo de Referência.</i></span>

2.2. <span style="color:red"><i>O objeto da contratação está previsto no Plano de Contratações Anual [</i></span><span style="color:red"><b><i>ANO</i></b></span><span style="color:red"><i>], conforme detalhamento a seguir:</i></span>

I) <span style="color:red"><i>ID PCA no PNCP: [...];</i></span>

II) <span style="color:red"><i>Data de publicação no PNCP: [...];</i></span>

III) <span style="color:red"><i>Id do item no PCA: [...];</i></span>

IV) <span style="color:red"><i>Classe/Grupo: [...];</i></span>

V) <span style="color:red"><i>Identificador da Futura Contratação: [...];</i></span>

<span style="color:red"><b><i>OU</i></b></span>

2.3. <span style="color:red"><i>O objeto da contratação está previsto no Plano de Contratações Anual [</i></span><span style="color:red"><b><i>ANO</i></b></span><span style="color:red"><i>], conforme consta das informações básicas desse Termo de Referência.</i></span>

## 3. DESCRIÇÃO DA SOLUÇÃO COMO UM TODO CONSIDERADO O CICLO DE VIDA DO OBJETO

3.1. <span style="color:red"><i>A descrição da solução como um todo encontra-se pormenorizada em tópico específico dos Estudos Técnicos Preliminares, apêndice deste Termo de Referência.</i></span>

## 4. REQUISITOS DA CONTRATAÇÃO

### <span style="color:red"><b><i>Sustentabilidade</i></b></span>

4.1. <span style="color:red"><i>Além dos critérios de sustentabilidade eventualmente inseridos na descrição do objeto, devem ser atendidos os seguintes requisitos, que se baseiam no Guia Nacional de Contratações Sustentáveis:</i></span>

4.1.1 <span style="color:red"><i>[...];</i></span>

4.1.2 <span style="color:red"><i>[...]; e</i></span>

4.1.3 <span style="color:red"><i>[...].</i></span>

### <span style="color:red"><b><i>Indicação de marcas ou modelos</i></b></span>

4.2. <span style="color:red"><i>Na presente contratação será admitida a indicação da(s) seguinte(s) marca(s), característica(s) ou modelo(s), de acordo com as justificativas contidas nos Estudos Técnicos Preliminares: (...).</i></span>

### <span style="color:red"><b><i>Da vedação de utilização de marca/produto na execução do serviço</i></b></span>

4.3. <span style="color:red"><i>Diante das conclusões extraídas do processo administrativo nº</i></span> <span style="color:red"><b><i>xxxxx.xxxxxx/xxxx-xx</i></b></span><span style="color:red"><i>, a Administração não aceitará o fornecimento dos seguintes produtos/marcas:</i></span>

4.3.1 <span style="color:red"><i>[...];</i></span>

4.3.2 <span style="color:red"><i>[...]; e</i></span>

4.3.3 <span style="color:red"><i>[...].</i></span>

### <span style="color:red"><b><i>Da exigência de carta de solidariedade</i></b></span>

4.4. <span style="color:red"><i>Em caso de fornecedor, revendedor ou distribuidor, será exigida do licitante/interessado provisoriamente classificado em primeiro lugar, nos termos do edital ou do aviso de contratação direta, carta de solidariedade emitida pelo fabricante, que assegure a execução do contrato.</i></span>

<b>Subcontratação</b>

4.5. <span style="color:red"><i>Não será admitida a subcontratação do objeto contratual.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.6. <span style="color:red"><i>É permitida a subcontratação parcial do objeto, até o limite de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor total do contrato, nas seguintes condições:</i></span>

4.7. <span style="color:red"><i>É vedada a subcontratação completa ou da parcela principal da obrigação, abaixo discriminada:</i></span>

4.7.1 <span style="color:red"><i>[...];</i></span>

4.7.2 <span style="color:red"><i>[...]; e</i></span>

4.7.3 <span style="color:red"><i>[...].</i></span>

4.8. <span style="color:red"><i>Poderão ser subcontratadas as seguintes parcelas do objeto:</i></span>

4.8.1 <span style="color:red"><i>[...];</i></span>

4.8.2 <span style="color:red"><i>[...]; e</i></span>

4.8.3 <span style="color:red"><i>[...].</i></span>

4.9. <span style="color:red"><i>Em qualquer hipótese de subcontratação, permanece a responsabilidade integral do Contratado pela perfeita execução contratual, cabendo-lhe realizar a supervisão e coordenação das atividades do subcontratado, bem como responder perante o Contratante pelo rigoroso cumprimento das obrigações contratuais correspondentes ao objeto da subcontratação.</i></span>

4.10. <span style="color:red"><i>A subcontratação depende de autorização prévia do Contratante, a quem incumbe avaliar se o subcontratado cumpre os requisitos de qualificação técnica necessários para a execução do objeto.</i></span>

4.11. <span style="color:red"><i>O Contratado apresentará à Administração documentação que comprove a capacidade técnica do subcontratado, que será avaliada e juntada aos autos do processo correspondente.</i></span>

4.12. <span style="color:red"><i>É vedada a subcontratação de pessoa física ou jurídica, se aquela ou os dirigentes desta mantiverem vínculo de natureza técnica, comercial, econômica, financeira, trabalhista ou civil com dirigente do órgão ou entidade contratante ou com agente público que desempenhe função na contratação ou atue na fiscalização ou na gestão do contrato, ou se deles forem cônjuge, companheiro ou parente em linha reta, colateral, ou por afinidade, até o terceiro grau.</i></span>

4.13. <span style="background:magenta">Em se tratando de serviços contínuos com regime de dedicação exclusiva de mão de obra, o Contratado terá responsabilidade solidária por atos e omissões do subcontratado que resultem em descumprimento da legislação trabalhista (art. 2º, inciso IV, do Decreto nº 12.174, de 2024).</span>

### <b>Garantia da contratação</b>

4.14. <span style="color:red"><i>Não haverá exigência da garantia da contratação dos art. 96 e seguintes da Lei nº 14.133, de 2021, pelas razões constantes do Estudo Técnico Preliminar.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.15. <span style="color:red"><i>Será exigida a garantia da contratação de que tratam os arts. 96 e seguintes da Lei nº 14.133, de 2021, com validade durante a execução do contrato e 90 (noventa) dias após término da vigência contratual, podendo o Contratado optar pela caução em dinheiro ou em títulos da dívida pública, seguro-garantia, fiança bancária ou título de capitalização, em valor correspondente a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor</i></span> <span style="color:red"><b><i>[total]</i></b></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><b><i>[anual]</i></b></span> <span style="color:red"><i>da contratação.</i></span>

4.15.1 <span style="color:red;background:darkcyan"><i>Tratando-se de obra ou serviço de engenharia, será exigida garantia adicional do fornecedor cuja proposta for inferior a 85% (oitenta e cinco por cento) do valor orçado pela Administração, equivalente à diferença entre este último e o valor da proposta.</i></span>

4.16. <span style="color:red"><i>Em caso de opção pelo seguro-garantia, a parte adjudicatária deverá apresentá-la, no máximo, até a data de assinatura do contrato.</i></span>

4.16.1 <span style="color:red"><i>A apólice de seguro-garantia permanecerá em vigor mesmo que o Contratado não pague o prêmio nas datas convencionadas.</i></span>

4.16.2 <span style="color:red"><i>Caso o adjudicatário não apresente a apólice de seguro de garantia antes da assinatura do contrato, ocorrerá a preclusão do direito de escolha dessa modalidade de garantia.</i></span>

4.16.3 <span style="color:red"><i>A apólice de seguro-garantia deverá acompanhar as modificações referentes à vigência do contrato principal mediante a emissão do respectivo endosso pela seguradora.</i></span>

4.16.4 <span style="color:red"><i>Será permitida a substituição da apólice de seguro-garantia na data de renovação ou de aniversário, desde que mantidas as condições e coberturas da apólice vigente e nenhum período fique descoberto, ressalvados os períodos de suspensão contratual.</i></span>

4.16.5 <span style="color:red"><i>Caso o adjudicatário não opte pelo seguro-garantia ou não apresente a apólice de seguro de garantia antes da assinatura do contrato, deverá apresentar, no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, a critério do Contratante, contado da assinatura do contrato, comprovante de prestação de garantia nas modalidades de caução em dinheiro ou títulos da dívida pública, fiança bancária ou títulos de capitalização.</i></span>

4.17. <span style="color:red"><i>Caso seja a garantia em dinheiro a modalidade de garantia escolhida pelo Contratado, deverá ser efetuada em favor do Contratante, em conta específica na Caixa Econômica Federal, com correção monetária.</i></span>

4.18. <span style="color:red"><i>Caso a opção seja por utilizar títulos da dívida pública, estes devem ter sido emitidos sob a forma escritural, mediante registro em sistema centralizado de liquidação e de custódia autorizado pelo Banco Central do Brasil, e avaliados pelos seus valores econômicos, conforme definido pelo Ministério competente.</i></span>

4.19. <span style="color:red"><i>No caso de garantia na modalidade de fiança bancária, deverá ser emitida por banco ou instituição financeira devidamente autorizada a operar no País pelo Banco Central do Brasil, e deverá constar expressa renúncia do fiador aos benefícios do artigo 827 do Código Civil.</i></span>

4.20. <span style="color:red"><i>Na hipótese de opção pelo título de capitalização, a garantia deverá ser custeada por pagamento único, com resgate pelo valor total, sob a modalidade de instrumento de garantia, emitido por sociedades de capitalização regulamente constituídas e autorizadas pelo Governo Federal.</i></span>

4.20.1 <span style="color:red"><i>O título de capitalização deverá ser apresentado ao Contratante juntamente com as condições gerais e o número do processo administrativo sob o qual o plano de capitalização foi aprovado pela Susep (art. 8º, III, da Circular SUSEP nº 656, de 11 de março de 2022).</i></span>

4.21. <span style="color:red"><i>A garantia assegurará, qualquer que seja a modalidade escolhida, sob pena de não aceitação, o pagamento de:</i></span>

4.21.1 <span style="color:red"><i>prejuízos advindos do não cumprimento do objeto do contrato e do não adimplemento das demais obrigações nele previstas;</i></span>

4.21.2 <span style="color:red"><i>multas moratórias e punitivas aplicadas pela Administração à contratada; e</i></span>

4.21.3 <span style="background:magenta">obrigações trabalhistas e previdenciárias de qualquer natureza e para com o FGTS, não adimplidas pelo Contratado, quando se tratar de serviços contínuos com regime de dedicação exclusiva de mão de obra.</span>

4.22. <span style="background:magenta">Nos contratos de serviços contínuos com regime de dedicação exclusiva de mão de obra, a apólice do seguro-garantia ou a fiança bancária deverá ter cobertura para o pagamento direto ao empregado das verbas devidas em razão da inadimplência do Contratado.</span>

4.22.1 <span style="background:magenta">Nos casos referidos no item anterior, o pagamento direto não pode estar condicionado ao trânsito em julgado de decisão judicial, sendo suficiente decisão definitiva em processo administrativo, que apure o montante devido.</span>

4.23. <span style="color:red"><i>No caso de alteração do valor do contrato, ou prorrogação de sua vigência, a garantia deverá ser ajustada ou renovada, no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, contado da data de assinatura do termo aditivo ou da emissão do apostilamento, seguindo os mesmos parâmetros utilizados quando da contratação.</i></span>

4.24. <span style="color:red"><i>Na hipótese de suspensão do contrato por ordem ou inadimplemento da Administração, o Contratado ficará desobrigado de renovar a garantia ou de endossar a apólice de seguro até a ordem de reinício da execução ou o adimplemento pela Administração.</i></span>

4.25. <span style="color:red"><i>Se o valor da garantia for utilizado total ou parcialmente em pagamento de qualquer obrigação, o Contratado obriga-se a fazer a respectiva reposição no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, a critério do Contratante, contados da data em que for notificada.</i></span>

4.26. <span style="color:red"><i>O Contratante executará a garantia na forma prevista na legislação que rege a matéria.</i></span>

4.26.1 <span style="color:red"><i>O emitente da garantia ofertada pelo Contratado deverá ser notificado pelo Contratante quanto ao início de processo administrativo para apuração de descumprimento de cláusulas contratuais.</i></span>

4.26.2 <span style="color:red"><i>Caso se trate da modalidade seguro-garantia, ocorrido o sinistro durante a vigência da apólice, sua caracterização e comunicação poderão ocorrer fora desta vigência, não caracterizando fato que justifique a negativa do sinistro, desde que respeitados os prazos prescricionais aplicados ao contrato de seguro, nos termos do art. 20 da Circular Susep n° 662, de 11 de abril de 2022.</i></span>

4.27. <span style="color:red"><i>Extinguir-se-á a garantia com a restituição da carta fiança, autorização para a liberação de importâncias depositadas em dinheiro a título de garantia ou anuência ao resgate do título de capitalização, acompanhada de declaração do Contratante, mediante termo circunstanciado, de que o Contratado cumpriu todas as cláusulas do contrato.</i></span>

4.27.1 <span style="color:red"><i>A extinção da garantia na modalidade seguro-garantia observará a regulamentação da Susep.</i></span>

4.27.2 <span style="color:red"><i>A Administração deverá apurar se há alguma pendência contratual antes do término da vigência da apólice.</i></span>

4.28. <span style="color:red"><i>A garantia somente será liberada ou restituída após a fiel execução do contrato ou após a sua extinção por culpa exclusiva da Administração e, quando em dinheiro, será atualizada monetariamente.</i></span>

4.28.1 <span style="background:magenta">Em se tratando de serviços executados com dedicação exclusiva de mão de obra, a garantia somente será liberada ante a comprovação de que o Contratado pagou todas as verbas rescisórias decorrentes da contratação, sendo que, caso esse pagamento não ocorra até o fim do segundo mês após o encerramento da vigência contratual, a garantia deverá ser utilizada para o pagamento dessas verbas trabalhistas, incluindo suas repercussões previdenciárias e relativas ao FGTS, observada a legislação que rege a matéria;</span>

4.28.2 <span style="background:magenta">Também poderá haver liberação da garantia se a empresa comprovar que os empregados serão realocados em outra atividade de prestação de serviços, sem que ocorra a interrupção do contrato de trabalho;</span>

4.28.3 <span style="background:magenta">Por ocasião do encerramento da prestação dos serviços Contratados, a Administração Contratante poderá utilizar o valor da garantia prestada para o pagamento direto aos trabalhadores vinculados ao contrato no caso da não comprovação: (1) do pagamento das respectivas verbas rescisórias ou (2) da realocação dos trabalhadores em outra atividade de prestação de serviços.</span>

4.29. <span style="color:red"><i>O Contratado autoriza o Contratante a reter, a qualquer tempo, a garantia, na forma prevista neste Termo de Referência.</i></span>

4.30. <span style="color:red"><i>O garantidor não é parte para figurar em processo administrativo instaurado pelo Contratante com o objetivo de apurar prejuízos e/ou aplicar sanções à contratada.</i></span>

4.31. <span style="color:red"><i>A garantia de execução é independente de eventual garantia do produto ou serviço prevista neste Termo de Referência.</i></span>

### <b>Vistoria</b>

4.32. <span style="color:red"><i>Não há necessidade de realização de avaliação prévia do local de execução dos serviços.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.33. <span style="color:red"><i>A avaliação prévia do local de execução dos serviços é imprescindível para o conhecimento pleno das condições e peculiaridades do objeto a ser contratado, sendo assegurado ao interessado o direito de realização de vistoria prévia, acompanhado por servidor designado para esse fim, de segunda à sexta-feira, das</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>horas às</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>horas.</i></span>

4.34. <span style="color:red"><i>Serão disponibilizados data e horário diferentes aos interessados em realizar a vistoria prévia.</i></span>

4.35. <span style="color:red"><i>Para a vistoria, o representante legal da empresa ou responsável técnico deverá estar devidamente identificado, apresentando documento de identidade civil e documento expedido pela empresa comprovando sua habilitação para a realização da vistoria.</i></span>

4.35.1 <span style="color:red"><b><i>... [incluir outras instruções sobre vistoria]</i></b></span><span style="color:red"><i>;</i></span>

4.35.2 <span style="color:red"><b><i>... [incluir outras instruções sobre vistoria]</i></b></span><span style="color:red"><i>.</i></span>

4.36. <span style="color:red"><i>Caso o interessado opte por não realizar a vistoria, deverá prestar declaração formal assinada pelo seu responsável técnico acerca do conhecimento pleno das condições e peculiaridades da contratação.</i></span>

4.37. <span style="color:red"><i>A não realização da vistoria não poderá embasar posteriores alegações de desconhecimento das instalações, dúvidas ou esquecimentos de quaisquer detalhes dos locais da prestação dos serviços, devendo o Contratado assumir os ônus dos serviços decorrentes.</i></span>

### <span style="color:red"><b><i>Instalação de escritório</i></b></span>

4.38. <span style="color:red"><i>Considera-se imprescindível para a adequada execução dos serviços contratados que o fornecedor possua ou venha a instalar escritório contendo estrutura administrativa mínima, no município de</i></span> <span style="color:red"><b><i>[indicar o Município/UF]</i></b></span><span style="color:red"><i>, pelas razões constantes do Estudo Técnico Preliminar.</i></span>

### <span style="color:red"><b><i>Margem de Preferência</i></b></span>

4.39. <span style="color:red"><i>O objeto da contratação enquadra-se na margem de preferência .............</i></span> <span style="color:red"><b><i>[normal]</i></b></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><b><i>[adicional]</i></b></span> <span style="color:red"><i>de ........ %, prevista no Decreto n.º....................., conforme disposto na Resolução n.º ......................... da Comissão Interministerial de Contratações Públicas para o Desenvolvimento Sustentável – CICS.</i></span>

## 5. MODELO DE EXECUÇÃO DO OBJETO

### <b>Condições de execução</b>

5.1. <span style="color:red"><i>A execução do objeto seguirá a seguinte dinâmica:</i></span>

5.1.1 Início da execução do objeto: <span style="color:red"><i>XX</i></span> dias <span style="color:red"><i>[da assinatura do contrato]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[da emissão da ordem de serviço]</i></span>.

5.1.2 Descrição detalhada dos métodos, rotinas, etapas, tecnologias procedimentos, frequência e periodicidade de execução do trabalho: <span style="color:red"><i>[...]</i></span>.

5.1.3 <span style="color:red"><i>Cronograma de realização dos serviços: [...];</i></span>

5.1.4 <span style="color:red"><i>Etapa ... Período / a partir de / após concluído ...</i></span>

### <b>Local e horário da prestação dos serviços</b>

5.2. Os serviços serão prestados no seguinte endereço: <span style="color:red"><i>[...]</i></span>;

5.3. Os serviços serão prestados no seguinte horário: <span style="color:red"><i>[...].</i></span>

### <b>Rotinas a serem cumpridas</b>

5.3.1 A execução contratual observará as rotinas <span style="color:red"><i>[abaixo] / [em anexo]</i></span>:

### <b>Materiais a serem disponibilizados</b>

5.4. <span style="color:red"><i>Para a perfeita execução dos serviços, o Contratado deverá disponibilizar os materiais, equipamentos, ferramentas e utensílios necessários, nas quantidades estimadas e qualidades a seguir estabelecidas, promovendo sua substituição quando necessário:</i></span>

5.4.1 <span style="color:red"><i>[...];</i></span>

5.4.2 <span style="color:red"><i>[...]; e</i></span>

5.4.3 <span style="color:red"><i>[...].</i></span>

### <b>Informações relevantes para o dimensionamento da proposta</b>

5.5. <span style="color:red"><i>A demanda do órgão tem como base as seguintes características:</i></span>

5.5.1 <span style="color:red"><i>[...];</i></span>

5.5.2 <span style="color:red"><i>[...]; e</i></span>

5.5.3 <span style="color:red"><i>[...].</i></span>

### <span style="color:red"><b><i>Disposições específicas para contratações integradas e semi-integradas</i></b></span>

5.6. <span style="color:red"><i>Providências necessárias para a efetivação de desapropriação autorizada pelo poder público:</i></span>

5.6.1 <span style="color:red"><i>[...];</i></span>

5.6.2 <span style="color:red"><i>[...]; e</i></span>

5.6.3 <span style="color:red"><i>[...].</i></span>

5.7. <span style="color:red"><i>Responsabilidade por cada fase do procedimento expropriatório:</i></span>

5.7.1 <span style="color:red"><i>[...];</i></span>

5.7.2 <span style="color:red"><i>[...]; e</i></span>

5.7.3 <span style="color:red"><i>[...].</i></span>

5.8. <span style="color:red"><i>Responsabilidade pelo pagamento das indenizações devidas:</i></span>

5.8.1 <span style="color:red"><i>[...];</i></span>

5.8.2 <span style="color:red"><i>[...]; e</i></span>

5.8.3 <span style="color:red"><i>[...].</i></span>

5.9. <span style="color:red"><i>Estimativa do valor a ser pago a título de indenização pelos bens expropriados, incluindo custos correlatos:</i></span>

5.9.1 <span style="color:red"><i>[...];</i></span>

5.9.2 <span style="color:red"><i>[...]; e</i></span>

5.9.3 <span style="color:red"><i>[...].</i></span>

5.10. <span style="color:red"><i>Distribuição objetiva de riscos entre as partes:</i></span>

5.10.1 <span style="color:red"><i>Risco pela diferença entre o custo da desapropriação e a estimativa de valor: [Contratante][e][Contratado]</i></span>

5.10.2 <span style="color:red"><i>Risco pelos eventuais danos e prejuízos ocasionados por atraso na disponibilização dos bens expropriados: [Contratante][e][Contratado]</i></span>

5.10.3 <span style="color:red"><i>[...]</i></span>

5.10.4 <span style="color:red"><i>O registro de imissão provisória na posse e/ou o registro de propriedade dos bens a serem desapropriados deverá ser efetuado em nome de [......]</i></span>

5.11. <span style="color:red;background:darkcyan"><i>Na contratação semi-integrada, mediante prévia autorização do Contratante, o projeto básico poderá ser alterado, desde que demonstrada a superioridade das inovações propostas pelo Contratado em termos de redução de custos, de aumento da qualidade, de redução do prazo de execução ou de facilidade de manutenção ou operação, assumindo o Contratado a responsabilidade integral pelos riscos associados à alteração do projeto básico.</i></span>

5.12. <span style="color:red;background:darkcyan"><i>Nas hipóteses em que for adotada a contratação integrada ou semi-integrada, é vedada a alteração dos valores contratuais, exceto nos seguintes casos:</i></span>

5.12.1 <span style="color:red;background:darkcyan"><i>para restabelecimento do equilíbrio econômico-financeiro decorrente de caso fortuito ou força maior;</i></span>

5.12.2 <span style="color:red;background:darkcyan"><i>por necessidade de alteração do projeto ou das especificações para melhor adequação técnica aos objetivos da contratação, a pedido do Contratante, desde que não decorrente de erros ou omissões por parte do Contratado, observados os limites estabelecidos no art. 125 da Lei nº 14.133, de 2021;</i></span>

5.12.3 <span style="color:red;background:darkcyan"><i>por necessidade de alteração do projeto nas contratações semi-integradas, nos termos do §5º do art. 46 da Lei nº 14.133, de 2021; e</i></span>

5.12.4 <span style="color:red;background:darkcyan"><i>por ocorrência de evento superveniente alocado na matriz de riscos como de responsabilidade do Contratante.</i></span>

5.13. <span style="color:red;background:darkcyan"><i>Na contratação integrada, após a elaboração do projeto básico pelo Contratado, o conjunto de desenhos, especificações, memoriais e cronograma físico-financeiro deverá ser submetido à aprovação do Contratante, que avaliará sua adequação em relação aos parâmetros definidos no edital e conformidade com as normas técnicas, vedadas alterações que reduzam a qualidade ou a vida útil do empreendimento e mantida a responsabilidade integral do Contratado pelos riscos associados ao projeto básico.</i></span>

### <b>Especificação da garantia do serviço</b>

5.14. <span style="color:red"><i>O prazo de garantia dos serviços é aquele estabelecido na Lei nº 8.078, de 11 de setembro de 1990 (Código de Defesa do Consumidor).</i></span>

<span style="color:red"><b><i>OU</i></b></span>

5.15. <span style="color:red"><i>O prazo de garantia contratual dos serviços, complementar à garantia legal da Lei nº 8.078, de 11 de setembro de 1990 (Código de Defesa do Consumidor), será de, no mínimo</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) meses, contado a partir do primeiro dia útil subsequente à data do recebimento definitivo do objeto.</i></span>

### <span style="color:red;background:lightgray"><b><i>Uniformes</i></b></span>

5.16. <span style="background:magenta">Os uniformes a serem fornecidos pelo Contratado a seus empregados deverão ser condizentes com a atividade a ser desempenhada no órgão Contratante, compreendendo peças para todas as estações climáticas do ano, sem qualquer repasse do custo para o empregado, observando o disposto nos itens seguintes:</span>

5.16.1 <span style="background:magenta">O uniforme deverá compreender as seguintes peças do vestuário:</span>

5.16.1.1. <span style="background:magenta">[...];</span>

5.16.1.2. <span style="background:magenta">[...] ..... (....) conjuntos completos ao empregado no início da execução do contrato, devendo ser substituído 01 (um) conjunto completo de uniforme a cada 06 (seis) meses, ou a qualquer época, no prazo máximo de ...... (.......) horas, após comunicação escrita do Contratante, sempre que não atendam as condições mínimas de apresentação;</span>

5.16.2 <span style="background:magenta">As peças devem ser confeccionadas com tecido e material de qualidade, seguindo os seguintes parâmetros mínimos:</span>

5.16.2.1. <span style="background:magenta">[...];</span>

5.16.2.2. <span style="background:magenta">[...].</span>

5.16.3 <span style="background:magenta">No caso de empregada gestante, os uniformes deverão ser apropriados para a situação, substituindo-os sempre que estiverem apertados;</span>

5.16.4 <span style="background:magenta">Os uniformes deverão ser entregues mediante recibo, cuja cópia, devidamente acompanhada do original para conferência, deverá ser enviada ao servidor responsável pela fiscalização do contrato.</span>

### <span style="color:red"><b><i>Procedimentos de transição e finalização do contrato</i></b></span>

5.17. <span style="color:red"><i>Os procedimentos de transição e finalização do contrato constituem-se das seguintes etapas:</i></span>

5.17.1 <span style="color:red"><i>[...];</i></span>

5.17.2 <span style="color:red"><i>[...]; e</i></span>

5.17.3 <span style="color:red"><i>[...].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

5.18. <span style="color:red"><i>Não serão necessários procedimentos de transição e finalização do contrato devido às características do objeto.</i></span>

## 6. MODELO DE GESTÃO DO CONTRATO

6.1. O contrato deverá ser executado fielmente pelas partes, de acordo com as cláusulas avençadas e as normas da Lei nº 14.133, de 2021, e cada parte responderá pelas consequências de sua inexecução total ou parcial.

6.2. Em caso de impedimento, ordem de paralisação ou suspensão do contrato, o cronograma de execução será prorrogado automaticamente pelo tempo correspondente, anotadas tais circunstâncias mediante simples apostila.

6.3. As comunicações entre o órgão ou entidade e o Contratado devem ser realizadas por escrito sempre que o ato exigir tal formalidade, admitindo-se o uso de mensagem eletrônica para esse fim.

6.4. O órgão ou entidade poderá convocar o preposto da empresa para adoção de providências que devam ser cumpridas de imediato.

6.5. <span style="color:red"><i>Após a assinatura do contrato ou instrumento equivalente, o órgão ou entidade poderá convocar o representante da empresa contratada para reunião inicial para apresentação do plano de fiscalização, que conterá informações acerca das obrigações contratuais, dos mecanismos de fiscalização, das estratégias para execução do objeto, do plano complementar de execução do Contratado, quando houver, do método de aferição dos resultados e das sanções aplicáveis, dentre outros.</i></span>

### <b>Preposto</b>

6.6. O Contratado designará formalmente o preposto da empresa, antes do início da prestação dos serviços, indicando no instrumento os poderes e deveres em relação à execução do objeto Contratado.

6.7. O Contratado <span style="color:red"><i>[deverá]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[não necessitará]</i></span> manter preposto da empresa no local da execução do objeto <span style="color:red"><i>durante o período [definir o período].</i></span>

6.8. O Contratante poderá recusar, desde que justificadamente, a indicação ou a manutenção do preposto da empresa, hipótese em que o Contratado designará outro para o exercício da atividade.

### <b>Rotinas de Fiscalização</b>

6.9. A execução do contrato deverá ser acompanhada e fiscalizada pelo(s) fiscal(is) do contrato, ou pelos respectivos substitutos.

### <b>Fiscalização Técnica</b>

6.10. O fiscal técnico do contrato acompanhará a execução do contrato, para que sejam cumpridas todas as condições estabelecidas no contrato, de modo a assegurar os melhores resultados para a Administração.

6.11. O fiscal técnico do contrato anotará no histórico de gerenciamento do contrato todas as ocorrências relacionadas à execução do contrato, com a descrição do que for necessário para a regularização das faltas ou dos defeitos observados.

6.12. Identificada qualquer inexatidão ou irregularidade, o fiscal técnico do contrato emitirá notificações para a correção da execução do contrato, determinando prazo para a correção.

6.13. O fiscal técnico do contrato informará ao gestor do contato, em tempo hábil, a situação que demandar decisão ou adoção de medidas que ultrapassem sua competência, para que adote as medidas necessárias e saneadoras, se for o caso.

6.14. No caso de ocorrências que possam inviabilizar a execução do contrato nas datas aprazadas, o fiscal técnico do contrato comunicará o fato imediatamente ao gestor do contrato.

6.15. O fiscal técnico do contrato comunicará ao gestor do contrato, em tempo hábil, o término do contrato sob sua responsabilidade, com vistas à tempestiva renovação ou à prorrogação contratual.

6.16. <span style="color:red"><i>A fiscalização da execução dos serviços abrange, ainda, as seguintes rotinas:</i></span>

6.16.1 <span style="color:red"><i>[...];</i></span>

6.16.2 <span style="color:red"><i>[...]; e</i></span>

6.16.3 <span style="color:red"><i>[...].</i></span>

6.17. A fiscalização de que trata esta cláusula não exclui nem reduz a responsabilidade do Contratado, inclusive perante terceiros, por qualquer irregularidade, ainda que resultante de imperfeições técnicas, vícios redibitórios, ou emprego de material inadequado ou de qualidade inferior e, na ocorrência desta, não implica corresponsabilidade do Contratante ou de seus agentes, gestores e fiscais, de conformidade.

6.18. As disposições previstas neste Termo de Referência não excluem o disposto no Anexo VIII da Instrução Normativa SEGES/MP nº 05, de 2017, aplicável no que for pertinente à contratação, por força da Instrução Normativa Seges/ME nº 98, de 26 de dezembro de 2022.

6.19. <span style="background:magenta">Para a compensação da jornada prevista no Decreto 12.174, de 2024, e na Instrução Normativa SEGES/MGI nº 81, de 12 de setembro de 2024, na hipótese de os trabalhadores prestarem serviços para unidades distintas, caberá ao fiscal setorial fazer a interlocução com os responsáveis pelas unidades de execução onde o trabalhador presta os serviços, para o fim da avaliação sobre a compensação pretendida. Em não havendo designação de fiscal setorial, a competência recairá no fiscal técnico.</span>

6.20. <span style="background:magenta">O controle das horas compensadas será feito por meio de registros decorrentes do ponto eletrônico da contratada ou outros meios admitidos pela legislação trabalhista.</span>

6.21. <span style="background:magenta">O fiscal técnico deverá incluir no relatório mensal ou no termo de recebimento provisório a informação consolidada sobre compensação de jornada pelos trabalhadores alocados no contrato.</span>

6.22. <span style="background:magenta">Caso o período de ausência corresponda a um dia de trabalho, o fiscal observará se foi efetuado o desconto do pagamento do vale transporte na fatura apresentada pela contratada, exceto quando a compensação recair em um dia no qual o trabalhador não exerceria suas atividades.</span>

6.23. <span style="background:magenta">O desconto do valor referente ao vale-alimentação só deverá ser realizado se as horas de ausência não venham a ser compensadas posteriormente e a convenção coletiva ou o acordo coletivo aplicável estabelecer que o benefício está vinculado ao dia trabalhado.</span>

6.24. <span style="background:magenta">Caso a ausência seja parcialmente compensada, o desconto do valor do vale alimentação será proporcional ao período não compensado.</span>

6.25. <span style="background:magenta">Na hipótese de diminuição excepcional e temporária dos serviços, inclusive em razão de recesso de final de ano, o fiscal do contrato, apoiado na decisão do gestor de realizar escalas de revezamento dos trabalhadores, conferirá se a escala apresentada atende às necessidades de manutenção dos serviços de cada unidade, dando ciência ao gestor do contrato.</span>

6.26. <span style="background:magenta">O total de horas calculadas para o recesso deverá ser compensado a partir da fixação da escala de revezamento, com cumprimento integral até o mês subsequente ao do recesso.</span>

6.27. <span style="background:magenta">O fiscal técnico deverá elaborar o termo de recebimento provisório, com as seguintes informações:</span>

6.27.1 <span style="background:magenta">se o saldo de horas se encontra positivo, caso ainda não usufruído o recesso;</span>

6.27.2 <span style="background:magenta">se o recesso foi parcialmente compensado, caso o recesso tenha sido usufruído, mas a compensação não tenha sido concluída;</span>

6.27.3 <span style="background:magenta">se o recesso foi integralmente compensado, caso a compensação tenha sido concluída; ou</span>

6.27.4 <span style="background:magenta">se há saldo em aberto, com sugestão de glosa no pagamento da fatura, caso a compensação não tenha sido concluída até o mês imediatamente subsequente ao recesso.</span>

6.28. <span style="background:magenta">Quando o trabalhador manifestar interesse na compensação de jornada por necessidade de ausência eventual, deverão ser realizadas as seguintes ações:</span>

6.28.1 <span style="background:magenta">O trabalhador deverá informar previamente a sua intenção de compensar a jornada ao responsável pela unidade de execução onde desempenha suas atividades;</span>

6.28.2 <span style="background:magenta">O responsável pela unidade avaliará a viabilidade da compensação e, em caso de concordância, comunicará o fiscal do contrato;</span>

6.28.3 <span style="background:magenta">O fiscal do contrato informará o preposto da empresa sobre a compensação pretendida e a data prevista da ausência do trabalhador; e</span>

6.28.4 <span style="background:magenta">Após a formalização da compensação, o fiscal do contrato poderá efetuar o recebimento provisório, informando o saldo de horas a compensar para fins de controle, sem indicação de glosa.</span>

6.29. <span style="background:magenta">Neste caso, o fiscal do contrato poderá efetuar o recebimento provisório, informando o saldo de horas a compensar para fins de controle, sem indicação de glosa.</span>

6.30. <span style="background:magenta">O fiscal técnico deverá elaborar o termo de recebimento provisório com as seguintes informações:</span>

6.30.1 <span style="background:magenta">se o saldo de horas objeto do recebimento anterior foi integralmente compensado, caso a compensação tenha sido concluída; ou</span>

6.30.2 <span style="background:magenta">se o saldo de horas não foi integralmente compensado, com a sugestão de glosa no pagamento da fatura.</span>

### <b>Fiscalização Administrativa</b>

6.31. O fiscal administrativo do contrato verificará a manutenção das condições de habilitação da contratada, acompanhará o empenho, o pagamento, as garantias, as glosas e a formalização de apostilamento e termos aditivos, solicitando quaisquer documentos comprobatórios pertinentes, caso necessário.

6.32. Caso ocorra descumprimento das obrigações contratuais, o fiscal administrativo do contrato atuará tempestivamente na solução do problema, reportando ao gestor do contrato para que tome as providências cabíveis, quando ultrapassar a sua competência.

6.33. <span style="color:red"><i>Além do disposto acima, a fiscalização contratual obedecerá às seguintes rotinas:</i></span>

6.33.1 <span style="color:red"><i>[...]</i></span>

6.34. <span style="background:magenta">A fiscalização administrativa poderá ser efetivada com base em critérios estatísticos, levando-se em consideração falhas que impactem o contrato como um todo e não apenas erros e falhas eventuais no pagamento de alguma vantagem a um determinado empregado.</span>

6.35. <span style="background:magenta">Na fiscalização do cumprimento das obrigações trabalhistas e sociais exigir-se-á, dentre outras, as seguintes comprovações:</span>

6.35.1 <span style="background:magenta">No caso de empresas regidas pela Consolidação das Leis do Trabalho (CLT):</span>

6.35.1.1. <span style="background:magenta">no primeiro mês da prestação dos serviços, a contratada deverá apresentar a seguinte documentação:</span>

6.35.1.1.1. <span style="background:magenta">relação dos empregados, contendo nome completo, cargo ou função, horário do posto de trabalho, números da carteira de identidade (RG) e da inscrição no Cadastro de Pessoas Físicas (CPF), com indicação dos responsáveis técnicos pela execução dos serviços, quando for o caso;</span>

6.35.1.1.2. <span style="background:magenta">Carteira de Trabalho e Previdência Social (CTPS) dos empregados admitidos e dos responsáveis técnicos pela execução dos serviços, quando for o caso, devidamente assinada pela contratada;</span>

6.35.1.1.3. <span style="background:magenta">exames médicos admissionais dos empregados da contratada que prestarão os serviços; e</span>

6.35.1.2. <span style="background:magenta">entrega até o dia trinta do mês seguinte ao da prestação dos serviços ao setor responsável pela fiscalização do contrato dos seguintes documentos, quando não for possível a verificação da regularidade destes no Sistema de Cadastro de Fornecedores (SICAF):</span>

6.35.1.2.1. <span style="background:magenta">Certidão Negativa de Débitos relativos a Créditos Tributários Federais e à Dívida Ativa da União (CND);</span>

6.35.1.2.2. <span style="background:magenta">certidões que comprovem a regularidade perante as Fazendas Estadual, Distrital e Municipal do domicílio ou sede do Contratado;</span>

6.35.1.2.3. <span style="background:magenta">Certidão de Regularidade do FGTS (CRF); e</span>

6.35.1.2.4. <span style="background:magenta">Certidão Negativa de Débitos Trabalhistas (CNDT).</span>

6.35.1.3. <span style="background:magenta">entrega, quando solicitado pelo Contratante, de quaisquer dos seguintes documentos:</span>

6.35.1.3.1. <span style="background:magenta">extrato da conta do INSS e do FGTS de qualquer empregado, a critério da Administração Contratante;</span>

6.35.1.3.2. <span style="background:magenta">cópia da folha de pagamento analítica de qualquer mês da prestação dos serviços, em que conste como tomador a parte contratante;</span>

6.35.1.3.3. <span style="background:magenta">cópia dos contracheques dos empregados relativos a qualquer mês da prestação dos serviços ou, ainda, quando necessário, cópia de recibos de depósitos bancários;</span>

6.35.1.3.4. <span style="background:magenta">comprovantes de entrega de benefícios suplementares (vale-transporte, vale-alimentação, entre outros), a que estiver obrigada por força de lei ou de Convenção ou Acordo Coletivo de Trabalho, relativos a qualquer mês da prestação dos serviços e de qualquer empregado;</span>

6.35.1.3.5. <span style="background:magenta">comprovantes de realização de eventuais cursos de treinamento e reciclagem que forem exigidos por lei ou pelo contrato; e</span>

6.35.1.3.6. <span style="background:magenta">documentos comprobatórios de que o capital social integralizado da empresa é compatível com o número de empregados, na forma do art. 4º-B da Lei nº 6.019/1974.</span>

<span style="color:red"><b><i>OU</i></b></span>

6.35.1.3.7. <span style="background:magenta">documentos comprobatórios de que o capital social mínimo integralizado atende ao disposto no art. 14 da Lei n.º 14.967/2024.</span>

6.35.1.4. <span style="background:magenta">entrega de cópia da documentação abaixo relacionada, quando da extinção ou rescisão do contrato, após o último mês de prestação dos serviços, no prazo definido no contrato:</span>

6.35.1.4.1. <span style="background:magenta">termos de rescisão dos contratos de trabalho dos empregados prestadores de serviço, devidamente homologados, quando exigível pelo sindicato da categoria;</span>

6.35.1.4.2. <span style="background:magenta">guias de recolhimento da contribuição previdenciária e do FGTS, referentes às rescisões contratuais;</span>

6.35.1.4.3. <span style="background:magenta">extratos dos depósitos efetuados nas contas vinculadas individuais do FGTS de cada empregado dispensado;</span>

6.35.1.4.4. <span style="background:magenta">exames médicos demissionais dos empregados dispensados.</span>

6.36. <span style="background:magenta">Sempre que houver admissão de novos empregados pela contratada, os documentos elencados no item 6.35.1.1 acima deverão ser apresentados.</span>

6.37. <span style="background:magenta">A Administração deverá analisar a documentação solicitada no item 6.35.1.4 acima no prazo de 30 (trinta) dias após o recebimento dos documentos, prorrogáveis por mais 30 (trinta) dias, justificadamente.</span>

6.38. <span style="background:magenta">A cada período de 12 meses de vigência do contrato de trabalho, a contratada deverá encaminhar termo de quitação anual das obrigações trabalhistas, na forma do art. 507-B da CLT, ou comprovar a adoção de providências voltadas à sua obtenção, relativamente aos empregados alocados, em dedicação exclusiva, na prestação de serviços contratados.</span>

6.39. <span style="background:magenta">O termo de quitação anual efetivado deverá ser firmado junto ao respectivo Sindicato dos Empregados e obedecerá ao disposto no art. 507-B, parágrafo único, da CLT.</span>

6.40. <span style="background:magenta">Para fins de comprovação da adoção das providências a que se refere o presente item, será aceito qualquer meio de prova, tais como: recibo de convocação, declaração de negativa de negociação, ata de negociação, dentre outros.</span>

6.41. <span style="background:magenta">Não haverá pagamento adicional pela Contratante à Contratada em razão do cumprimento das obrigações previstas neste item.</span>

6.42. <span style="background:magenta">No caso de sociedades diversas, tais como as Organizações Sociais Civis de Interesse Público (Oscip’s) e as Organizações Sociais, será exigida a comprovação de atendimento a eventuais obrigações decorrentes da legislação que rege as respectivas organizações.</span>

6.43. <span style="background:magenta">Os documentos necessários à comprovação do cumprimento das obrigações sociais trabalhistas poderão ser apresentados em original ou por qualquer processo de cópia autenticada por cartório competente ou por servidor da Administração.</span>

6.44. <span style="background:magenta">Em caso de indício de irregularidade no recolhimento das contribuições previdenciárias, os fiscais ou gestores de contratos de serviços com regime de dedicação exclusiva de mão de obra deverão oficiar à Receita Federal do Brasil (RFB).</span>

6.45. <span style="background:magenta">Em caso de indício de irregularidade no recolhimento da contribuição para o FGTS, os fiscais ou gestores de contratos de serviços com regime de dedicação exclusiva de mão de obra deverão oficiar ao Ministério do Trabalho.</span>

6.46. <span style="background:magenta">O descumprimento das obrigações trabalhistas ou a não manutenção das condições de habilitação pelo Contratado poderá dar ensejo à rescisão contratual, sem prejuízo das demais sanções.</span>

6.47. <span style="background:magenta">A Administração Contratante poderá conceder um prazo para que o Contratado regularize suas obrigações trabalhistas ou suas condições de habilitação, sob pena de rescisão contratual, quando não identificar má-fé ou a incapacidade da empresa de corrigir.</span>

6.48. <span style="background:magenta">Caso não seja apresentada a documentação comprobatória do cumprimento das obrigações trabalhistas, previdenciárias e para com o FGTS, o Contratante comunicará o fato ao Contratado e reterá o pagamento da fatura mensal, em valor proporcional ao inadimplemento, até que a situação seja regularizada.</span>

6.49. <span style="background:magenta">Não havendo quitação das obrigações por parte do Contratado no prazo de quinze dias, o Contratante poderá efetuar o pagamento das obrigações diretamente aos empregados do Contratado que tenham participado da execução dos serviços objeto do contrato.</span>

6.50. <span style="background:magenta">O sindicato representante da categoria do trabalhador deverá ser notificado pelo Contratante para acompanhar o pagamento das verbas mencionadas.</span>

6.51. <span style="background:magenta">Tais pagamentos não configuram vínculo empregatício ou implicam a assunção de responsabilidade por quaisquer obrigações dele decorrentes entre o Contratante e os empregados do Contratado.</span>

6.52. <span style="background:magenta">O contrato só será considerado integralmente cumprido após a comprovação, pelo Contratado, do pagamento de todas as obrigações trabalhistas, sociais e previdenciárias e para com o FGTS referentes à mão de obra alocada em sua execução, inclusive quanto às verbas rescisórias.</span>

6.53. <span style="background:magenta">O Contratado é responsável pelos encargos trabalhistas, previdenciários, fiscais e comerciais resultantes da execução do contrato.</span>

6.54. <span style="background:magenta">A inadimplência do Contratado quanto aos encargos trabalhistas, fiscais e comerciais não transfere à Administração Pública a responsabilidade por seu pagamento.</span>

6.55. <span style="background:magenta">A fiscalização administrativa observará, ainda, as diretrizes relacionadas no item 10 do Anexo VIII-B da Instrução Normativa nº 5, de 26 de maio de 2017, cuja incidência se admite por força da Instrução Normativa Seges/Me nº 98, de 26 de dezembro de 2022.</span>

6.56. <span style="background:magenta">Para efeito de recebimento provisório, ao final de cada período mensal, o fiscal administrativo deverá verificar a efetiva realização dos dispêndios concernentes aos salários e às obrigações trabalhistas, previdenciárias e com o FGTS do mês anterior, dentre outros, emitindo relatório que será encaminhado ao gestor do contrato.</span>

6.57. <span style="background:magenta">A fiscalização administrativa verificará a possibilidade de compensação de jornada de trabalho, que poderá ser adotada nas seguintes hipóteses:</span>

6.57.1 <span style="background:magenta">diminuição excepcional e temporária da demanda de trabalho na unidade de execução, inclusive na hipótese de recesso de final de ano, quando houver; e</span>

6.57.2 <span style="background:magenta">necessidade eventual de caráter pessoal dos trabalhadores, em que não se mostre eficiente ou conveniente convocar trabalhadores substitutos.</span>

6.58. <span style="background:magenta">As compensações de jornada limitam-se:</span>

6.58.1 <span style="background:magenta">à jornada diária máxima de 10 (dez) horas; e</span>

6.58.2 <span style="background:magenta">ao acréscimo de 2 (duas) horas à jornada diária do trabalhador.</span>

6.59. <span style="background:magenta">A compensação de jornada depende do interesse manifestado pelo trabalhador e da avaliação do responsável pela unidade de execução.</span>

6.60. <span style="background:magenta">A fiscalização administrativa acompanhará o planejamento e a programação das férias dos colaboradores terceirizados alocados no contrato, a serem realizados pela contratada, a fim de assegurar a previsibilidade da época de gozo das férias, como previsto no inciso I do art. 3º do Decreto n.º 12.174, de 11 de setembro de 2024, nos termos da Instrução Normativa SEGES/MGI nº 213, de 29 de maio de 2025.</span>

6.61. <span style="background:magenta">A programação da fruição das férias será realizada com, no mínimo, sessenta dias de antecedência ao término do período aquisitivo, salvo quando o período aquisitivo se encerrar nos primeiros noventa dias da vigência contratual.</span>

6.62. <span style="background:magenta">A contratada poderá solicitar reunião com a fiscalização contratual, antes da definição da programação da fruição das férias, para dirimir eventuais dúvidas sobre as rotinas da prestação de serviço estabelecidas neste Termo de Referência.</span>

6.63. <span style="background:magenta">O planejamento será formalizado por meio do relatório de programação de férias, no qual será informada a época de fruição de férias de cada colaborador terceirizado.</span>

6.64. <span style="background:magenta">O relatório de programação das férias conterá a relação dos colaboradores terceirizados alocados no contrato, cargo ou função, data de admissão e alocação no posto e informações sobre as férias, incluindo as datas de início e fim do período aquisitivo, do período concessivo e da fruição das férias, caso já estejam programadas, bem como o parcelamento dos períodos de férias, se houver.</span>

6.65. <span style="background:magenta">A contratada deverá enviar à fiscalização administrativa:</span>

6.65.1 <span style="background:magenta">até o quinto dia útil de cada mês, a partir do segundo mês da execução contratual, o relatório de programação das férias dos colaboradores terceirizados, observados os prazos do art. 5º da Instrução Normativa SEGES/MGI nº 213, de 2025;</span>

6.65.2 <span style="background:magenta">em até 5 dias úteis após a ciência do colaborador terceirizado, o recibo de concessão de férias, conforme o art. 135 da CLT e o inciso IV do art. 50 da Lei nº 14.133, de 1º de abril de 2021.</span>

6.66. <span style="background:magenta">O planejamento e a programação deverão garantir que as férias sejam fruídas, sempre que a vigência contratual permitir, dentro de doze meses, contados a partir da data do direito adquirido, conforme o art. 134 da CLT, de modo a mitigar as ocorrências de pagamento indenizado, observado o disposto no art. 8º da Instrução Normativa SEGES/MGI nº 213, de 2025.</span>

6.67. <span style="background:magenta">Após a programação das férias, eventuais alterações deverão ser comunicadas à fiscalização administrativa com, no mínimo, noventa dias de antecedência do início da fruição das férias, mediante justificativa, indicando-se, para tanto, um dos motivos elencados no parágrafo único do art. 10 da Instrução Normativa SEGES/MGI nº 213, de 2025.</span>

### <b>Gestor do Contrato</b>

6.68. Cabe ao gestor do contrato:

6.68.1 coordenar a atualização do processo de acompanhamento e fiscalização do contrato contendo todos os registros formais da execução no histórico de gerenciamento do contrato, a exemplo da ordem de serviço, do registro de ocorrências, das alterações e das prorrogações contratuais, elaborando relatório com vistas à verificação da necessidade de adequações do contrato para fins de atendimento da finalidade da administração.

6.68.2 acompanhar os registros realizados pelos fiscais do contrato, de todas as ocorrências relacionadas à execução do contrato e as medidas adotadas, informando, se for o caso, à autoridade superior àquelas que ultrapassarem a sua competência.

6.68.3 acompanhar a manutenção das condições de habilitação da contratada, para fins de empenho de despesa e pagamento, e anotará os problemas que obstem o fluxo normal da liquidação e do pagamento da despesa no relatório de riscos eventuais.

6.68.4 emitir documento comprobatório da avaliação realizada pelos fiscais técnico, administrativo e setorial quanto ao cumprimento de obrigações assumidas pelo Contratado, com menção ao seu desempenho na execução contratual, baseado nos indicadores objetivamente definidos e aferidos, e a eventuais penalidades aplicadas, devendo constar do cadastro de atesto de cumprimento de obrigações.

6.68.5 tomar providências para a formalização de processo administrativo de responsabilização para fins de aplicação de sanções, a ser conduzido pela comissão de que trata o art. 158 da Lei nº 14.133, de 2021, ou pelo agente ou pelo setor com competência para tal, conforme o caso.

6.68.6 elaborar relatório final com informações sobre a consecução dos objetivos que tenham justificado a contratação e eventuais condutas a serem adotadas para o aprimoramento das atividades da Administração.

6.68.7 enviar a documentação pertinente ao setor de contratos para a formalização dos procedimentos de liquidação e pagamento, com a indicação expressa de que o valor da Nota Fiscal emitida pela contratada confere com o valor dimensionado pela fiscalização e gestão no recebimento definitivo do serviço.

6.68.8 receber e dar encaminhamento imediato:

6.68.8.1. às denúncias de discriminação, violência e assédio no ambiente de trabalho, conforme o art. 2º, inciso III, do Decreto n.º 12.174/2024;

6.68.8.2. à notificação formal de que a empresa contratada está descumprindo suas obrigações trabalhistas, enviada pelo trabalhador, sindicato, Ministério do Trabalho, Ministério Público, Defensoria Pública ou por qualquer outro meio idôneo.

6.69. <span style="background:magenta">Para os períodos de diminuição excepcional e temporária de trabalho, inclusive em razão de recesso de fim de ano, o gestor avaliará a conveniência e oportunidade de elaboração de escalas de revezamento dos trabalhadores, comunicando a todas as unidades sobre a possibilidade e os requisitos para concessão (artigo 11 da Instrução Normativa SEGES/MGI nº 81, de 12 de setembro de 2024).</span>

## 7. CRITÉRIOS DE MEDIÇÃO E PAGAMENTO

7.1. <span style="color:red"><i>A avaliação da execução do objeto utilizará o [Instrumento de Medição de Resultado (IMR), conforme previsto no [Anexo XXX]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[outro instrumento substituto para aferição da qualidade da prestação dos serviços]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[o disposto nesta seção].</i></span>

7.2. <span style="color:red;background:darkcyan"><i>Nos regimes de execução de empreitada por preço global, empreitada integral, contratação por tarefa, contratação integrada e contratação semi-integrada será adotada sistemática de medição e pagamento associada à execução de etapas do cronograma físico-financeiro vinculadas ao cumprimento de metas de resultado, vedada a adoção de sistemática de remuneração orientada por preços unitários ou referenciada pela execução de quantidades de itens unitários.</i></span>

7.3. Será indicada a retenção ou glosa no pagamento, proporcional à irregularidade verificada, sem prejuízo das sanções cabíveis, caso se constate que o Contratado:

7.3.1 não produziu os resultados acordados,

7.3.2 deixou de executar, ou não executou com a qualidade mínima exigida as atividades contratadas; ou

7.3.3 deixou de utilizar materiais e recursos humanos exigidos para a execução do serviço, ou os utilizou com qualidade ou quantidade inferior à demandada.

7.4. <span style="color:red"><i>A utilização do IMR não impede a aplicação concomitante de outros mecanismos para a avaliação da prestação dos serviços.</i></span>

7.5. <span style="color:red"><i>A aferição da execução contratual para fins de pagamento considerará os seguintes critérios:</i></span>

7.5.1 <span style="color:red"><i>[...];</i></span>

7.5.2 <span style="color:red"><i>[...]; e</i></span>

7.5.3 <span style="color:red"><i>[...].</i></span>

### <b>Recebimento</b>

7.6. Os serviços serão recebidos provisoriamente, no prazo de <span style="color:red"><i>XXX (xxxxx)</i></span> dias, pelos fiscais técnico e administrativo, mediante termos detalhados, quando verificado o cumprimento das exigências de caráter técnico e administrativo.

7.6.1 <span style="color:red;background:darkcyan"><i>Tratando-se de obra ou serviço de engenharia, ao final de cada etapa da execução contratual, conforme previsto no Cronograma Físico-Financeiro, o Contratado apresentará a medição prévia dos serviços executados no período, por meio de planilha e memória de cálculo detalhada.</i></span>

7.6.1.1. <span style="color:red;background:darkcyan"><i>Uma etapa será considerada efetivamente concluída quando os serviços previstos para aquela etapa, no Cronograma Físico-Financeiro, estiverem executados em sua totalidade.</i></span>

7.6.1.2. <span style="color:red;background:darkcyan"><i>O Contratado também apresentará, a cada medição, os documentos comprobatórios da procedência legal dos produtos e subprodutos florestais utilizados naquela etapa da execução contratual, quando for o caso.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

7.6.2 <span style="color:red"><i>Não se tratando de obra ou serviço de engenharia, para fins de recebimento provisório</i></span> <span style="color:red"><b><i>[descrever o fato que será considerado como conclusão do objeto ou etapa para fins de permitir o recebimento provisório]</i></b></span><span style="color:red"><i>.</i></span>

7.7. O prazo para recebimento provisório será contado do recebimento de comunicação de cobrança oriunda do Contratado com a comprovação da prestação dos serviços a que se referem a parcela a ser paga.

7.8. O fiscal técnico do contrato realizará o recebimento provisório do objeto do contrato mediante termo detalhado que comprove o cumprimento das exigências de caráter técnico.

7.9. O fiscal administrativo do contrato realizará o recebimento provisório do objeto do contrato mediante termo detalhado que comprove o cumprimento das exigências de caráter administrativo.

7.10. O fiscal setorial do contrato, quando houver, realizará o recebimento provisório sob o ponto de vista técnico e administrativo.

7.11. Para efeito de recebimento provisório, será considerado para fins de faturamento o período <span style="color:red"><i>[indicar o período]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[indicar os eventos ou etapas para fins de faturamento].</i></span>

7.12. Ao final de cada período/evento de faturamento:

7.12.1 o fiscal técnico do contrato deverá apurar o resultado das avaliações da execução do objeto e, se for o caso, a análise do desempenho e qualidade da prestação dos serviços realizados em consonância com os indicadores previstos no ato convocatório, que poderá resultar no redimensionamento de valores a serem pagos à contratada, registrando em relatório a ser encaminhado ao gestor do contrato;

7.12.2 <span style="background:magenta">o fiscal administrativo deverá verificar a efetiva realização dos dispêndios concernentes aos salários e às obrigações trabalhistas, previdenciárias e com o FGTS do mês anterior, dentre outros, emitindo relatório que será encaminhado ao gestor do contrato.</span>

7.13. Será considerado como ocorrido o recebimento provisório com a entrega do termo detalhado ou, em havendo mais de um a ser feito, com a entrega do último.

7.14. O Contratado fica obrigado a reparar, corrigir, remover, reconstruir ou substituir, às suas expensas, no todo ou em parte, o objeto em que se verificarem vícios, defeitos ou incorreções resultantes da execução ou materiais empregados, cabendo à fiscalização não atestar a última e/ou única medição de serviços até que sejam sanadas todas as eventuais pendências que possam vir a ser apontadas no recebimento provisório.

7.15. A fiscalização não efetuará o ateste da última e/ou única medição de serviços até que sejam sanadas todas as eventuais pendências que possam vir a ser apontadas no recebimento provisório.

7.16. O recebimento provisório também ficará sujeito, quando cabível, à conclusão de todos os testes de campo e à entrega dos Manuais e Instruções exigíveis.

7.17. Os serviços poderão ser rejeitados, no todo ou em parte, quando em desacordo com as especificações constantes neste Termo de Referência e na proposta, sem prejuízo da aplicação das penalidades.

7.18. Quando a fiscalização for exercida por um único servidor, o Termo Detalhado deverá conter o registro, a análise e a conclusão acerca das ocorrências na execução do contrato, em relação à fiscalização técnica e administrativa e demais documentos que julgar necessários, devendo encaminhá-los ao gestor do contrato para recebimento definitivo.

7.19. Os serviços serão recebidos definitivamente no prazo de <span style="color:red"><i>XX</i></span> (<span style="color:red"><i>xxxxx</i></span>) dias, contados do recebimento provisório, por servidor ou comissão designada pela autoridade competente, após a verificação da qualidade e quantidade do serviço e consequente aceitação mediante termo detalhado, obedecendo os seguintes procedimentos:

7.19.1 Emitir documento comprobatório da avaliação realizada pelos fiscais técnico, administrativo e setorial, quando houver, no cumprimento de obrigações assumidas pelo Contratado, com menção ao seu desempenho na execução contratual, baseado em indicadores objetivamente definidos e aferidos, e a eventuais penalidades aplicadas, devendo constar do cadastro de atesto de cumprimento de obrigações, conforme regulamento.

7.19.2 Realizar a análise dos relatórios e de toda a documentação apresentada pela fiscalização e, caso haja irregularidades que impeçam a liquidação e o pagamento da despesa, indicar as cláusulas contratuais pertinentes, solicitando ao Contratado, por escrito, as respectivas correções;

7.19.3 Emitir Termo Detalhado para efeito de recebimento definitivo dos serviços prestados, com base nos relatórios e documentações apresentadas; e

7.19.4 Comunicar a empresa para que emita a Nota Fiscal ou Fatura, com o valor exato dimensionado pela fiscalização.

7.19.5 Enviar a documentação pertinente ao setor de contratos para a formalização dos procedimentos de liquidação e pagamento, no valor dimensionado pela fiscalização e gestão.

7.20. No caso de controvérsia sobre a execução do objeto, quanto à dimensão, qualidade e quantidade, deverá ser observado o teor do art. 143 da Lei nº 14.133, de 2021, comunicando-se à empresa para emissão de Nota Fiscal quanto à parcela incontroversa da execução do objeto, para efeito de liquidação e pagamento.

7.21. Nenhum prazo de recebimento ocorrerá enquanto pendente a solução, pelo Contratado, de inconsistências verificadas na execução do objeto ou no instrumento de cobrança.

7.22. O recebimento provisório ou definitivo não excluirá a responsabilidade civil pela solidez e pela segurança do serviço nem a responsabilidade ético-profissional pela perfeita execução do contrato.

### <b>Liquidação</b>

7.23. Recebida a Nota Fiscal ou documento de cobrança equivalente, correrá o prazo de dez dias úteis para fins de liquidação, na forma desta seção, prorrogáveis por igual período, nos termos do art. 7º, §3º da Instrução Normativa SEGES/ME nº 77/2022.

7.24. O prazo de que trata o item anterior será reduzido à metade, mantendo-se a possibilidade de prorrogação, nos casos de contratações decorrentes de despesas cujos valores não ultrapassem o limite de que trata o inciso II do art. 75 da Lei nº 14.133, de 2021

7.25. Para fins de liquidação, o setor competente deve verificar se a Nota Fiscal ou Fatura apresentada expressa os elementos necessários e essenciais do documento, tais como:

I) o prazo de validade;

II) a data da emissão;

III) os dados do contrato e do órgão contratante;

IV) o período respectivo de execução do contrato;

V) o valor a pagar; e

VI) eventual destaque do valor de retenções tributárias cabíveis.

7.26. Havendo erro na apresentação da Nota Fiscal/Fatura, ou circunstância que impeça a liquidação da despesa, esta ficará sobrestada até que o Contratado providencie as medidas saneadoras, reiniciando-se o prazo após a comprovação da regularização da situação, sem ônus ao Contratante.

7.27. A Nota Fiscal ou Fatura deverá ser obrigatoriamente acompanhada da comprovação da regularidade fiscal, constatada por meio de consulta on-line ao SICAF ou, na impossibilidade de acesso ao referido Sistema, mediante consulta aos sítios eletrônicos oficiais ou à documentação mencionada no art. 68 da Lei nº 14.133/2021.

7.28. A Administração deverá realizar consulta ao SICAF para:

7.28.1 verificar a manutenção das condições de habilitação exigidas;

7.28.2 identificar possível razão que impeça a participação em licitação/contratação no âmbito do órgão ou entidade, tais como a proibição de contratar com a Administração ou com o Poder Público, bem como ocorrências impeditivas indiretas.

7.29. Constatando-se, junto ao SICAF, a situação de irregularidade do Contratado, será providenciada sua notificação, por escrito, para que, no prazo de 5 (cinco) dias úteis, regularize sua situação ou, no mesmo prazo, apresente sua defesa. O prazo poderá ser prorrogado uma vez, por igual período, a critério do Contratante.

7.30. Não havendo regularização ou sendo a defesa considerada improcedente, o Contratante deverá comunicar aos órgãos responsáveis pela fiscalização da regularidade fiscal quanto à inadimplência do Contratado, bem como quanto à existência de pagamento a ser efetuado, para que sejam acionados os meios pertinentes e necessários para garantir o recebimento de seus créditos.

7.31. Persistindo a irregularidade, o Contratante deverá adotar as medidas necessárias à rescisão contratual nos autos do processo administrativo correspondente, assegurada ao Contratado a ampla defesa.

7.32. Havendo a efetiva execução do objeto, os pagamentos serão realizados normalmente, até que se decida pela rescisão do contrato, caso o Contratado não regularize sua situação junto ao SICAF.

### <b>Prazo de pagamento</b>

7.33. O pagamento será efetuado no prazo máximo de até dez dias úteis, contados da finalização da liquidação da despesa, conforme seção anterior, nos termos da Instrução Normativa SEGES/ME nº 77, de 2022.

7.34. No caso de atraso pelo Contratante, os valores devidos ao Contratado serão atualizados monetariamente entre o termo final do prazo de pagamento até a data de sua efetiva realização, mediante aplicação do índice <span style="color:red"><i>[definir o índice]</i></span> de correção monetária.

### <b>Forma de pagamento</b>

7.35. O pagamento será realizado por meio de ordem bancária, para crédito em banco, agência e conta corrente indicados pelo Contratado.

7.36. Será considerada data do pagamento o dia em que constar como emitida a ordem bancária para pagamento.

7.37. Quando do pagamento, será efetuada a retenção tributária prevista na legislação aplicável.

7.37.1 Independentemente do percentual de tributo inserido na planilha, quando houver, serão retidos na fonte, quando da realização do pagamento, os percentuais estabelecidos na legislação vigente.

7.38. O Contratado regularmente optante pelo Simples Nacional, nos termos da Lei Complementar nº 123, de 2006, não sofrerá a retenção tributária quanto aos impostos e contribuições abrangidos por aquele regime. No entanto, o pagamento ficará condicionado à apresentação de comprovação, por meio de documento oficial, de que faz jus ao tratamento tributário favorecido previsto na referida Lei Complementar.

### <span style="color:red"><b><i>Antecipação de pagamento</i></b></span>

7.39. <span style="color:red"><i>A presente contratação permite a antecipação de pagamento [</i></span><span style="color:red"><b><i>parcial</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>total</i></b></span><span style="color:red"><i>], conforme as regras previstas no presente tópico.</i></span>

7.40. <span style="color:red"><i>O Contratado emitirá [recibo]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[nota fiscal]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[fatura]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[documento idôneo] correspondente ao valor da antecipação de pagamento de R$</i></span> <span style="color:red"><b><i>X.XXX,XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>valor em extenso</i></b></span><span style="color:red"><i>), tão logo [</i></span><span style="color:red"><b><i>incluir condicionante – ex: seja assinado o termo de contrato, ou seja, prestada a garantia etc.</i></b></span><span style="color:red"><i>], para que o Contratante efetue o pagamento antecipado.</i></span>

7.41. <span style="color:red"><i>Para as etapas seguintes do contrato, a antecipação do pagamento ocorrerá da seguinte forma:</i></span>

7.41.1 <span style="color:red"><i>R$</i></span> <span style="color:red"><b><i>X.XXX,XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>valor em extenso</i></b></span><span style="color:red"><i>) quando do início da segunda etapa;</i></span>

7.41.2 <span style="color:red"><i>(...).</i></span>

7.42. <span style="color:red"><i>Fica o Contratado obrigado a devolver, com correção monetária, a integralidade do valor antecipado na hipótese de inexecução do objeto.</i></span>

7.42.1 <span style="color:red"><i>No caso de inexecução parcial, deverá haver a devolução do valor relativo à parcela não-executada do contrato.</i></span>

7.42.2 <span style="color:red"><i>O valor relativo à parcela antecipada e não executada do contrato será atualizado monetariamente pela variação acumulada do</i></span> <span style="color:red"><b><i>[especificar o índice de correção monetária a ser adotado]</i></b></span><span style="color:red"><i>, ou outro índice que venha a substituí-lo, desde a data do pagamento da antecipação até a data da devolução.</i></span>

7.43. <span style="color:red"><i>A liquidação ocorrerá de acordo com as regras do tópico respectivo deste instrumento.</i></span>

7.44. <span style="color:red"><i>O pagamento antecipado será efetuado no prazo máximo de até</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) dias, contados do recebimento do [recibo]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[nota fiscal]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[fatura]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[documento idôneo].</i></span>

7.45. <span style="color:red"><i>A antecipação de pagamento dispensa o ateste ou recebimento prévios do objeto, os quais deverão ocorrer após a regular execução da parcela contratual a que se refere o valor antecipado.</i></span>

7.46. <span style="color:red"><i>O pagamento de que trata este item está condicionado à tomada das seguintes providências pelo Contratado:</i></span>

7.46.1 <span style="color:red"><i>comprovação da execução da etapa imediatamente anterior do objeto pelo Contratado, para a antecipação do valor remanescente;</i></span>

7.46.2 <span style="color:red"><i>prestação da garantia adicional nas modalidades de que trata o art. 96 da Lei nº 14.133, de 2021, no percentual de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento).</i></span>

7.47. <span style="color:red"><i>O pagamento do valor a ser antecipado ocorrerá respeitando eventuais retenções tributárias incidentes.</i></span>

### <span style="background:magenta"><b>Reoneração gradual da folha de pagamento</b></span>

7.48. <span style="background:magenta">A pedido do Contratado, o preço do contrato poderá ser revisto nos termos do art. 134 c/c art. 136, I, da Lei nº 14.133, de 2021, após efetiva majoração das alíquotas, conforme regime de transição previsto no art. 9º-A e 9º-B da Lei nº 12.546, de 2011, com a redação dada pela Lei nº 14.973, de 2024.</span>

7.48.1 <span style="background:magenta">O pedido de revisão em virtude dos efeitos da Lei nº 14.973, de 2024 deverá ser formulado durante a vigência do contrato e antes de eventual prorrogação ou encerramento contratual, sob pena de preclusão.</span>

7.48.2 <span style="background:magenta">A revisão prevista no acima, caso requerida pelo Contratado, deverá ser instruída com a comprovação da variação dos custos por meio de Planilha de Custos e Formação de Preços.</span>

### <span style="background:magenta"><b>Repactuação</b></span>

7.49. <span style="background:magenta">Os preços contratados serão repactuados para manutenção do equilíbrio econômico-financeiro, após o interregno de um ano, mediante solicitação do Contratado.</span>

7.50. <span style="background:magenta">O interregno mínimo de 1 (um) ano para a primeira repactuação será contado:</span>

7.50.1 <span style="background:magenta">Para os custos relativos à mão de obra, vinculados à data-base da categoria profissional: a partir da data de início dos efeitos financeiros do acordo, convenção ou dissídio coletivo de trabalho ao qual a proposta estiver vinculada, relativo a cada categoria profissional abrangida pelo contrato;</span>

7.50.2 <span style="background:magenta">Para os custos decorrentes do mercado: a partir da apresentação da proposta.</span>

7.51. <span style="background:magenta">Nas repactuações subsequentes à primeira, o interregno mínimo de 1 (um) ano será contado a partir da data da última repactuação correspondente à mesma parcela objeto da nova solicitação.</span>

7.51.1 <span style="background:magenta">Entende-se como última repactuação a data em que iniciados seus efeitos financeiros, independentemente daquela apostilada.</span>

7.52. <span style="background:magenta">A repactuação poderá ser dividida em tantas parcelas quantas forem necessárias, observado o princípio da anualidade do reajuste de preços da contratação, podendo ser realizada em momentos distintos para discutir a variação de custos que tenham sua anualidade resultante em datas diferenciadas, como os decorrentes de mão de obra e os decorrentes dos insumos necessários à execução dos serviços.</span>

7.53. <span style="background:magenta">Quando a contratação envolver mais de uma categoria profissional, a repactuação dos custos contratuais decorrentes da mão de obra poderá ser dividida em tantos quantos forem os acordos, convenções ou dissídios coletivos de trabalho das respectivas categorias.</span>

7.54. <span style="background:magenta">É vedada a inclusão, por ocasião da repactuação, de benefícios não previstos na proposta inicial, exceto quando se tornarem obrigatórios por força de lei, acordo, convenção ou dissídio coletivo de trabalho.</span>

7.55. <span style="background:magenta">Na repactuação, o Contratante não se vinculará às disposições contidas em acordos, convenções ou dissídios coletivos de trabalho que tratem de obrigações e direitos que somente se aplicam aos contratos com a Administração Pública, de matéria não trabalhista, de pagamento de participação dos trabalhadores nos lucros ou resultados do Contratado, ou que estabeleçam direitos não previstos em lei, como valores ou índices obrigatórios de encargos sociais ou previdenciários, bem como de preços para os insumos relacionados ao exercício da atividade.</span>

7.56. <span style="background:magenta">Quando a repactuação solicitada se referir aos custos da mão de obra, o Contratado efetuará a comprovação da variação dos custos por meio de Planilha de Custos e Formação de Preços, acompanhada da apresentação do novo acordo, convenção ou sentença normativa da categoria profissional abrangida pelo contrato.</span>

7.56.1 <span style="background:magenta">A repactuação para reajustamento do contrato em razão de novo Acordo, Convenção ou Dissídio Coletivo de Trabalho deve repassar integralmente o aumento de custos da mão de obra decorrente desses instrumentos.</span>

7.56.2 <span style="background:magenta">Deverão prevalecer os direitos mais benéficos ao trabalhador durante a execução contratual, caso o Acordo, Convenção Coletiva ou Dissídio Coletivo ao qual a empresa contratada está vinculada seja diferente do Acordo, Convenção Coletiva ou Dissídio Coletivo utilizado pela Administração como paradigma para definição dos custos unitários mínimos relevantes, para fins de repactuação.</span>

7.56.3 <span style="background:magenta">A correção dos valores mínimos de remuneração, incluindo salário base e adicionais, e dos benefícios estabelecidos, será realizada com base nas cláusulas de reajuste percentual do Acordo, Convenção Coletiva ou Dissídio Coletivo ao qual a empresa contratada está vinculada, quando este for diferente do Acordo, Convenção Coletiva ou Dissídio Coletivo paradigma utilizado pela Administração.</span>

7.56.4 <span style="background:magenta">A repactuação será realizada com base na apuração da diferença percentual entre os valores previstos no Acordo, Convenção Coletiva ou Dissídio Coletivo anterior e o que entrou em vigor quando inexistir cláusula de previsão de reajuste percentual no Acordo, Convenção Coletiva ou Dissídio Coletivo ao qual a empresa contratada está vinculada, ressalvado o subitem seguinte.</span>

7.56.5 <span style="background:magenta">Deverão prevalecer os valores que forem mais benéficos ao trabalhador caso o Acordo, Convenção Coletiva de Trabalho ou Dissídio Coletivo ao qual a empresa contratada está vinculada venha a estabelecer valores de remuneração, incluindo salário base e adicionais, de auxílio-alimentação e de benefícios superiores aos valores estabelecidos na contratação ou superiores à aplicação dos percentuais previstos nos subitens anteriores.</span>

7.56.6 <span style="background:magenta">A repactuação dos demais custos relativos à mão de obra, que não estejam discriminados como custos mínimos relevantes pela Administração, terá como base o acordo, convenção ou dissídio coletivo de trabalho ao qual a proposta estiver vinculada (ou seja, àquele instrumento apresentado pela empresa no momento da licitação).</span>

7.57. <span style="background:magenta">Quando a repactuação solicitada pelo Contratado se referir aos custos decorrentes do mercado, o respectivo aumento será apurado mediante a aplicação do índice de reajustamento [</span><span style="background:magenta"><b>indicar o índice a ser adotado]</b></span><span style="background:magenta">, com base na seguinte fórmula:</span>

<span style="background:magenta"><i>R = V (I – Iº) / Iº, onde:</i></span>

<span style="background:magenta"><i>R = Valor do reajustamento procurado;</i></span>

<span style="background:magenta"><i>V = Valor contratual correspondente à parcela dos custos decorrentes do mercado a ser reajustada;</i></span>

<span style="background:magenta"><i>Iº = índice inicial - refere-se ao índice de custos ou de preços correspondente à data de apresentação da proposta;</i></span>

<span style="background:magenta"><i>I = Índice relativo ao mês do reajustamento</i></span>

7.58. <span style="background:magenta">No caso de atraso ou não divulgação do índice de reajustamento, o Contratante pagará ao Contratado a importância calculada pela última variação conhecida, liquidando a diferença correspondente tão logo seja divulgado o índice definitivo; fica o Contratado obrigado a apresentar memória de cálculo referente ao reajustamento de preços do valor remanescente, sempre que este ocorrer.</span>

7.59. <span style="background:magenta">Nas aferições finais, o índice utilizado para a repactuação dos custos decorrentes do mercado será, obrigatoriamente, o definitivo.</span>

7.60. <span style="background:magenta">Caso o índice estabelecido venha a ser extinto ou de qualquer forma não possa mais ser utilizado, será adotado, em substituição, o que vier a ser determinado pela legislação então em vigor.</span>

7.61. <span style="background:magenta">Na ausência de previsão legal quanto ao índice substituto, as partes elegerão novo índice oficial, para reajustamento do preço do valor remanescente dos custos decorrentes do mercado, por meio de termo aditivo.</span>

7.62. <span style="background:magenta">Independentemente do requerimento de repactuação dos custos decorrentes do mercado, o Contratante verificará, a cada anualidade, se houve deflação do índice adotado que justifique o recálculo dos custos em valor menor, promovendo, em caso positivo, a redução dos valores correspondentes da planilha contratual.</span>

7.63. <span style="background:magenta">Os efeitos financeiros da repactuação decorrente da variação dos custos contratuais de mão de obra vinculados aos acordos, às convenções ou aos dissídios coletivos de trabalho retroagirão, quando for o caso, à data do início dos efeitos financeiros do novo acordo, convenção ou sentença normativa que fundamenta a repactuação.</span>

7.64. <span style="background:magenta">Os novos valores contratuais decorrentes das repactuações poderão se iniciar em data futura, desde que assim acordado entre as partes, sem prejuízo da contagem da anualidade para concessão das repactuações futuras.</span>

7.65. <span style="background:magenta">Os efeitos financeiros da repactuação ficarão restritos exclusivamente aos itens que a motivaram, e apenas em relação à diferença porventura existente.</span>

7.66. <span style="background:magenta">O pedido de repactuação deverá ser formulado durante a vigência do contrato e antes de eventual prorrogação ou encerramento contratual, sob pena de preclusão.</span>

7.67. <span style="background:magenta">Caso, na data da prorrogação contratual, ainda não tenha sido celebrado o novo acordo, convenção ou dissídio coletivo da categoria, ou ainda não tenha sido possível ao Contratante ou ao Contratado proceder aos cálculos devidos, deverá ser inserida cláusula no termo aditivo de prorrogação para resguardar o direito futuro à repactuação, a ser exercido tão logo se disponha dos valores reajustados, sob pena de preclusão.</span>

7.68. <span style="background:magenta">A extinção do contrato não configurará óbice para o deferimento da repactuação solicitada tempestivamente, hipótese em que será concedida por meio de termo indenizatório.</span>

7.69. <span style="background:magenta">O Contratante decidirá sobre o pedido de repactuação de preços em até [</span><span style="background:magenta"><b>indicar o prazo]</b></span><span style="background:magenta">, contado da data do fornecimento, pelo Contratado, da documentação comprobatória da variação dos custos a serem repactuados.</span>

7.70. <span style="background:magenta">O prazo referido no subitem anterior ficará suspenso enquanto o Contratado não cumprir os atos ou apresentar a documentação solicitada pelo Contratante para a comprovação da variação dos custos.</span>

7.71. <span style="background:magenta">A repactuação de preços será formalizada por apostilamento.</span>

7.72. <span style="background:magenta">As repactuações não interferem no direito das partes de solicitar, a qualquer momento, a manutenção do equilíbrio econômico dos contratos com base no disposto no art. 124, inciso II, alínea “d”, da Lei nº 14.133, de 2021.</span>

7.73. <span style="background:magenta">O Contratado deverá complementar a garantia contratual anteriormente prestada, de modo que se mantenha a proporção inicial em relação ao valor contratado.</span>

7.74. <span style="background:magenta">Caso o Contratado esteja sujeito ao regime de incidência não-cumulativa de PIS e COFINS, a comprovação das alíquotas médias efetivas de recolhimento deverá ser feita no momento da prorrogação contratual ou da repactuação de preços, a fim de que sejam promovidos os ajustes necessários decorrentes das oscilações dos custos efetivos dessas contribuições.</span>

7.75. <span style="background:magenta">A majoração da tarifa de transporte público gera a possibilidade de revisão do item relativo aos valores pagos a título de vale-transporte, constante da Planilha de Custos e Formação de Preços do presente Contrato, desde que comprovada pelo Contratado a sua efetiva repercussão sobre os preços contratados.</span>

7.75.1 <span style="background:magenta">A revisão dos custos relativos ao vale-transporte será formalizada por apostilamento.</span>

<span style="color:red"><b><i>OU</i></b></span>

### <span style="color:red"><b><i>Reajuste</i></b></span>

7.76. <span style="color:red"><i>Os preços inicialmente contratados são fixos e irreajustáveis no prazo de um ano contado da data do orçamento estimado, em [DD/MM/AAAA].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

7.77. <span style="color:red;background:darkcyan"><i>Os preços inicialmente contratados são fixos e irreajustáveis no prazo de um ano contado da data do orçamento estimado, considerando as planilhas referenciais [elaboradas com base no SINAPI/SICRO do mês</i></span> <span style="color:red;background:darkcyan"><b><i>MM</i></b></span> <span style="color:red;background:darkcyan"><i>do ano de</i></span> <span style="color:red;background:darkcyan"><b><i>AAAA</i></b></span><span style="color:red;background:darkcyan"><i>]</i></span> <span style="color:red;background:darkcyan"><b><i>OU</i></b></span> <span style="color:red;background:darkcyan"><i>[datadas de</i></span> <span style="color:red;background:darkcyan"><b><i>DD</i></b></span><span style="color:red;background:darkcyan"><i>/</i></span><span style="color:red;background:darkcyan"><b><i>MM</i></b></span><span style="color:red;background:darkcyan"><i>/</i></span><span style="color:red;background:darkcyan"><b><i>AAAA</i></b></span><span style="color:red;background:darkcyan"><i>].</i></span>

7.78. <span style="color:red"><i>Após o interregno de um ano, e independentemente de pedido do Contratado, os preços iniciais serão reajustados, mediante a aplicação, pelo Contratante, do</i></span> <span style="color:red"><b><i>[indicar o índice a ser adotado]</i></b></span><span style="color:red"><i>, exclusivamente para as obrigações iniciadas e concluídas após a ocorrência da anualidade.</i></span>

7.79. <span style="color:red"><i>Nos reajustes subsequentes ao primeiro, o interregno mínimo de um ano será contado a partir dos efeitos financeiros do último reajuste.</i></span>

7.80. <span style="color:red"><i>No caso de atraso ou não divulgação do(s) índice (s) de reajustamento, o Contratante pagará ao Contratado a importância calculada pela última variação conhecida, liquidando a diferença correspondente tão logo seja(m) divulgado(s) o(s) índice(s) definitivo(s).</i></span>

7.81. <span style="color:red"><i>Nas aferições finais, o(s) índice(s) utilizado(s) para reajuste será(ão), obrigatoriamente, o(s) definitivo(s).</i></span>

7.82. <span style="color:red"><i>Caso o(s) índice(s) estabelecido(s) para reajustamento venha(m) a ser extinto(s) ou de qualquer forma não possa(m) mais ser utilizado(s), será(ão) adotado(s), em substituição, o(s) que vier(em) a ser determinado(s) pela legislação então em vigor.</i></span>

7.83. <span style="color:red"><i>Na ausência de previsão legal quanto ao índice substituto, as partes elegerão novo índice oficial, para reajustamento do preço do valor remanescente, por meio de termo aditivo.</i></span>

7.84. <span style="color:red"><i>O reajuste será realizado por apostilamento.</i></span>

### <b>Cessão de Crédito</b>

7.85. As cessões de crédito dependerão de prévia aprovação do Contratante.

7.85.1 A eficácia da cessão de crédito, em relação à Administração, está condicionada à celebração de termo aditivo ao contrato administrativo.

7.85.2 Sem prejuízo do regular atendimento da obrigação contratual de cumprimento de todas as condições de habilitação por parte do Contratado (cedente), a celebração do aditamento de cessão de crédito e a realização dos pagamentos respectivos também se condicionam à regularidade fiscal e trabalhista do cessionário, bem como à certificação de que o cessionário não se encontra impedido de licitar e contratar com o Poder Público, conforme a legislação em vigor, ou de receber benefícios ou incentivos fiscais ou creditícios, direta ou indiretamente, conforme o art. 12 da Lei nº 8.429, de 1992, nos termos do Parecer JL-01, de 18 de maio de 2020.

7.85.3 O crédito a ser pago à cessionária é exatamente aquele que seria destinado à cedente (Contratado) pela execução do objeto contratual, restando absolutamente incólumes todas as defesas e exceções ao pagamento e todas as demais cláusulas exorbitantes ao direito comum aplicáveis no regime jurídico de direito público incidente sobre os contratos administrativos, incluindo a possibilidade de pagamento em conta vinculada ou de pagamento pela efetiva comprovação do fato gerador, quando for o caso, e o desconto de multas, glosas e prejuízos causados à Administração.

7.85.4 A cessão de crédito não afetará a execução do objeto contratado, que continuará sob a integral responsabilidade do Contratado.

7.86. O disposto nesta seção não afeta as operações de crédito de que trata a Instrução Normativa SEGES/MGI nº 82, de 21 de fevereiro de 2025, as quais ficam por esta regidas.

### <span style="background:magenta"><b>Conta-Depósito Vinculada ou Pagamento por Fato Gerador</b></span>

### <span style="background:magenta"><b>Conta-Depósito Vinculada</b></span>

7.87. <span style="background:magenta">Para tratamento do risco de descumprimento das obrigações trabalhistas, previdenciárias e com FGTS por parte do Contratado, as regras acerca da Conta-Depósito Vinculada a que se refere o Anexo XII da IN SEGES/MP n. 05/2017, aplicável por força do art. 1º da IN SEGES/ME nº 98, de 2022, são as estabelecidas neste Termo de Referência.</span>

7.88. <span style="background:magenta">Os custos estimados das tarifas bancárias são de responsabilidade do Contratado e correspondem ao valor estimado de R$</span> <span style="background:magenta"><b>X.XXX,XX</b></span> <span style="background:magenta">(</span><span style="background:magenta"><b>valor em extenso</b></span><span style="background:magenta">),por mês, podendo ser contemplados na proposta do interessado e devendo ser debitados dos valores depositados.</span>

<span style="background:magenta"><b><i>OU</i></b></span>

7.89. <span style="background:magenta">Na presente contratação, a conta-depósito vinculada é isenta de tarifas bancárias.</span>

7.90. <span style="background:magenta">O futuro Contratado deve autorizar a Administração Contratante, no momento da assinatura do contrato, a fazer o desconto nas faturas e realizar os pagamentos dos salários e demais verbas trabalhistas diretamente aos trabalhadores, bem como das contribuições previdenciárias e do FGTS, quando não demonstrado o cumprimento tempestivo e regular dessas obrigações, até o momento da regularização, sem prejuízo das sanções cabíveis.</span>

7.91. <span style="background:magenta">Quando não for possível a realização desses pagamentos pela própria Administração (ex.: por falta da documentação pertinente, tais como folha de pagamento, rescisões dos contratos e guias de recolhimento), os valores retidos cautelarmente serão depositados junto à Justiça do Trabalho, com o objetivo de serem utilizados exclusivamente no pagamento de salários e das demais verbas trabalhistas, bem como das contribuições sociais e FGTS decorrentes.</span>

7.92. <span style="background:magenta">O Contratado autorizará o provisionamento de valores para o pagamento das férias, 13º salário e rescisão contratual dos trabalhadores alocados à execução do contrato, bem como de suas repercussões trabalhistas, fundiárias e previdenciárias, que serão depositados pelo Contratante em conta-depósito vinculada específica, em nome do prestador dos serviços, bloqueada para movimentação, e que somente serão liberados para o pagamento direto dessas verbas aos trabalhadores, nas condições estabelecidas no item 1.5 do anexo VII-B da IN SEGES/MP n. 5/2017.</span>

7.93. <span style="background:magenta">O montante dos depósitos da conta vinculada, conforme item 2 do Anexo XII da IN SEGES/MP n. 5/2017 será igual ao somatório dos valores das provisões a seguir discriminadas, incidentes sobre a remuneração, cuja movimentação dependerá de autorização do órgão ou entidade promotora da contratação e será feita exclusivamente para o pagamento das respectivas obrigações:</span>

7.93.1 <span style="background:magenta">13º (décimo terceiro) salário;</span>

7.93.2 <span style="background:magenta">Férias e um terço constitucional de férias;</span>

7.93.3 <span style="background:magenta">Multa sobre o FGTS; e</span>

7.93.4 <span style="background:magenta">Encargos sobre férias e 13º (décimo terceiro) salário.</span>

7.94. <span style="background:magenta">Os percentuais de provisionamento e a forma de cálculo serão aqueles indicados no Anexo XII da IN SEGES/MP n. 5/2017.</span>

7.95. <span style="background:magenta">O saldo da conta-depósito será remunerado pelo índice de correção da poupança pro rata die, conforme definido em Termo de Cooperação Técnica firmado entre o promotor desta contratação e instituição financeira. Eventual alteração da forma de correção implicará a revisão do Termo de Cooperação Técnica.</span>

7.96. <span style="background:magenta">Os valores referentes às provisões mencionadas neste edital Termo de Referência que sejam retidos por meio da conta-depósito deixarão de compor o valor mensal a ser pago diretamente à empresa que vier a prestar os serviços.</span>

7.97. <span style="background:magenta">O Contratado poderá solicitar a autorização do órgão ou entidade contratante para utilizar os valores da conta-depósito para o pagamento dos encargos trabalhistas previstos nos subitens acima ou de eventuais indenizações trabalhistas aos empregados, decorrentes de situações ocorridas durante a vigência do contrato.</span>

7.98. <span style="background:magenta">Na situação do subitem acima, a empresa deverá apresentar os documentos comprobatórios da ocorrência das obrigações trabalhistas e seus respectivos prazos de vencimento. Somente após a confirmação da ocorrência da situação pela Administração, será expedida a autorização para a movimentação dos recursos creditados na conta-depósito vinculada, que será encaminhada à Instituição Financeira no prazo máximo de 5 (cinco) dias úteis, a contar da data da apresentação dos documentos comprobatórios pela empresa.</span>

7.99. <span style="background:magenta">A autorização de movimentação deverá especificar que se destina exclusivamente para o pagamento dos encargos trabalhistas ou de eventual indenização trabalhista aos trabalhadores favorecidos.</span>

7.100. <span style="background:magenta">O Contratado deverá apresentar ao Contratante, no prazo máximo de 3 (três) dias úteis, contados da movimentação, o comprovante das transferências bancárias realizadas para a quitação das obrigações trabalhistas.</span>

7.101. <span style="background:magenta">O saldo remanescente dos recursos depositados na conta-depósito será liberado à respectiva titular no momento do encerramento do contrato, na presença do sindicato da categoria correspondente aos serviços contratados, quando couber, e após a comprovação da quitação de todos os encargos trabalhistas e previdenciários relativos ao serviço contratado, conforme item 15 do Anexo XII da IN SEGES/MP n. 05/2017.</span>

<span style="background:magenta"><b><i>OU</i></b></span>

### <span style="background:magenta"><b>Pagamento pelo fato gerador</b></span>

7.102. <span style="background:magenta">No caso do Pagamento pelo Fato Gerador, o Contratante adotará os seguintes procedimentos:</span>

7.103. <span style="background:magenta">Serão objeto de pagamento mensal ao Contratado o somatório dos seguintes módulos que compõem a planilha de custos e formação de preços, disposta no Anexo VII-D da IN SEGES/MP n.º 5/2017:</span>

<span style="background:magenta"><i>1. Módulo 1: Composição da Remuneração;</i></span>

<span style="background:magenta"><i>2. Submódulo 2.2: Encargos Previdenciários e FGTS;</i></span>

<span style="background:magenta"><i>3. Submódulo 2.3: Benefícios Mensais e Diários;</i></span>

<span style="background:magenta"><i>4. Submódulo 4.2: Substituto na Intrajornada;</i></span>

<span style="background:magenta"><i>5. Módulo 5: Insumos; e</i></span>

<span style="background:magenta"><i>6. Módulo 6: Custos Indiretos, Tributos e Lucro (CITL), que será calculado tendo por base as alíneas acima.</i></span>

7.104. <span style="background:magenta">Os valores referentes a férias, 1/3 (um terço) de férias previsto na Constituição, 13º (décimo terceiro) salários, ausências legais, verbas rescisórias, devidos aos trabalhadores, bem como outros de evento futuro e incerto, não serão parte integrante dos pagamentos mensais ao Contratado, devendo ser pagos pela Administração ao Contratado somente na ocorrência do seu fato gerador;</span>

7.104.1 <span style="background:magenta">A não ocorrência dos fatos geradores discriminados neste item não gera direito adquirido para o Contratado das referidas verbas ao final da vigência do contrato, devendo o pagamento seguir as regras previstas no contrato.</span>

7.105. <span style="background:magenta">As verbas discriminadas no item anterior somente serão liberadas nas seguintes condições:</span>

7.105.1 <span style="background:magenta">pelo valor correspondente ao 13º (décimo terceiro) salário dos empregados vinculados ao contrato, quando devido;</span>

7.105.2 <span style="background:magenta">pelo valor correspondente às férias e a 1/3 (um terço) de férias previsto na Constituição, quando do gozo de férias pelos empregados vinculados ao contrato;</span>

7.105.3 <span style="background:magenta">pelo valor correspondente ao 13º (décimo terceiro) salário proporcional, férias proporcionais e à indenização compensatória porventura devida sobre o FGTS, quando da dispensa de empregado vinculado ao contrato;</span>

7.105.4 <span style="background:magenta">pelos valores correspondentes às ausências legais efetivamente ocorridas dos empregados vinculados ao contrato; e</span>

7.105.5 <span style="background:magenta">outras de evento futuro e incerto, após efetivamente ocorridas, pelos seus valores correspondentes.</span>

## 8. INFRAÇÕES E SANÇÕES ADMINISTRATIVAS

8.1. Comete infração administrativa, nos termos da Lei nº 14.133, de 2021, o Contratado que:

a) der causa à inexecução parcial do contrato;

b) der causa à inexecução parcial do contrato que cause grave dano à Administração ou ao funcionamento dos serviços públicos ou ao interesse coletivo;

c) der causa à inexecução total do contrato;

d) ensejar o retardamento da execução ou da entrega do objeto da contratação sem motivo justificado;

e) apresentar documentação falsa ou prestar declaração falsa durante a execução do contrato;

f) praticar ato fraudulento na execução do contrato;

g) comportar-se de modo inidôneo ou cometer fraude de qualquer natureza;

h) praticar ato lesivo previsto no art. 5º da Lei nº 12.846, de 1º de agosto de 2013.

8.2. Serão aplicadas ao Contratado que incorrer nas infrações acima descritas as seguintes sanções:

8.2.1 Advertência, quando o Contratado der causa à inexecução parcial do contrato, sempre que não se justificar a imposição de penalidade mais grave;

8.2.2 Impedimento de licitar e contratar, quando praticadas as condutas descritas nas alíneas “b”, “c” e “d” do subitem acima, sempre que não se justificar a imposição de penalidade mais grave;

8.2.3 Declaração de inidoneidade para licitar e contratar, quando praticadas as condutas descritas nas alíneas “e”, “f”, “g” e “h” do subitem acima, bem como nas alíneas “b”, “c” e “d”, que justifiquem a imposição de penalidade mais grave.

8.2.4 Multa:

8.2.4.1. <span style="color:red"><i>Moratória, para as infrações descritas no item “d”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) por dia de atraso injustificado sobre o valor da parcela inadimplida, até o limite de</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) dias.</i></span>

8.2.4.2. <span style="color:red"><i>Moratória de 0,07% (sete centésimos por cento) por dia de atraso injustificado sobre o valor total do contrato, até o máximo de 2% (dois por cento), pela inobservância do prazo fixado para apresentação, suplementação ou reposição da garantia;</i></span>

8.2.4.2.1. O atraso superior a 25 (vinte e cinco) dias para apresentação, suplementação ou reposição da garantia autoriza a Administração a promover a extinção do contrato por descumprimento ou cumprimento irregular de suas cláusulas, conforme dispõe o inciso I do art. 137 da Lei n. 14.133, de 2021.

8.2.4.3. <span style="color:red"><i>Compensatória, para as infrações descritas acima alíneas “</i></span><span style="color:red"><b><i>e</i></b></span><span style="color:red"><i>” a “</i></span><span style="color:red"><b><i>h</i></b></span><span style="color:red"><i>” de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

8.2.4.4. <span style="color:red"><i>Compensatória, para a inexecução total do contrato prevista acima na alínea “</i></span><span style="color:red"><b><i>c</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

8.2.4.5. <span style="color:red"><i>Compensatória, para a infração descrita acima na alínea “</i></span><span style="color:red"><b><i>b</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

8.2.4.6. <span style="color:red"><i>Compensatória, em substituição à multa moratória para a infração descrita acima na alínea “d”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

8.2.4.7. <span style="color:red"><i>Compensatória, para a infração descrita acima na alínea “</i></span><span style="color:red"><b><i>a</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação [, ressalvadas as seguintes infrações também enquadráveis nessa alínea:]</i></span>

8.2.4.7.1. [INDICAR ITENS ESPECÍFICOS DE INEXECUÇÃO PARCIAL QUE JUSTIFIQUEM PENALIDADE DIVERSA];

8.3. A aplicação das sanções previstas neste Termo de Referência não exclui, em hipótese alguma, a obrigação de reparação integral do dano causado ao Contratante.

8.4. Todas as sanções previstas neste Termo de Referência poderão ser aplicadas cumulativamente com a multa.

8.5. Antes da aplicação da multa será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis, contado da data de sua intimação.

8.6. Se a multa aplicada e as indenizações cabíveis forem superiores ao valor do pagamento eventualmente devido pelo Contratante ao Contratado, além da perda desse valor, a diferença será descontada da garantia prestada ou será cobrada judicialmente.

8.7. A multa poderá ser recolhida administrativamente no prazo máximo de <span style="color:red"><i>XX</i></span> (<span style="color:red"><i>xxxxx</i></span>) dias, a contar da data do recebimento da comunicação enviada pela autoridade competente.

8.8. A aplicação das sanções realizar-se-á em processo administrativo que assegure o contraditório e a ampla defesa ao Contratado, observando-se o procedimento previsto no caput e parágrafos do art. 158 da Lei nº 14.133, de 2021, para as penalidades de impedimento de licitar e contratar e de declaração de inidoneidade para licitar ou contratar.

8.8.1 Para a garantia da ampla defesa e contraditório, as notificações serão enviadas eletronicamente para os endereços de e-mail informados na proposta comercial, bem como os cadastrados pela empresa no SICAF.

8.8.2 Os endereços de e-mail informados na proposta comercial e/ou cadastrados no SICAF serão considerados de uso contínuo da empresa, não cabendo alegação de desconhecimento das comunicações a eles comprovadamente enviadas.

8.9. Na aplicação das sanções serão considerados:

8.9.1 a natureza e a gravidade da infração cometida;

8.9.2 as peculiaridades do caso concreto;

8.9.3 as circunstâncias agravantes ou atenuantes;

8.9.4 os danos que dela provierem para o Contratante; e

8.9.5 a implantação ou o aperfeiçoamento de programa de integridade, conforme normas e orientações dos órgãos de controle.

8.10. Os atos previstos como infrações administrativas na Lei nº 14.133, de 2021, ou em outras leis de licitações e contratos da Administração Pública que também sejam tipificados como atos lesivos na Lei nº 12.846, de 2013, serão apurados e julgados conjuntamente, nos mesmos autos, observados o rito procedimental e autoridade competente definidos na referida Lei.

8.11. A personalidade jurídica do Contratado poderá ser desconsiderada sempre que utilizada com abuso do direito para facilitar, encobrir ou dissimular a prática dos atos ilícitos previstos neste Termo de Referência ou para provocar confusão patrimonial, e, nesse caso, todos os efeitos das sanções aplicadas à pessoa jurídica serão estendidos aos seus administradores e sócios com poderes de administração, à pessoa jurídica sucessora ou à empresa do mesmo ramo com relação de coligação ou controle, de fato ou de direito, com o Contratado, observados, em todos os casos, o contraditório, a ampla defesa e a obrigatoriedade de análise jurídica prévia.

8.12. O Contratante deverá, no prazo máximo de 15 (quinze) dias úteis, contado da data de aplicação da sanção, informar e manter atualizados os dados relativos às sanções por ela aplicadas, para fins de publicidade no Cadastro Nacional de Empresas Inidôneas e Suspensas (CEIS) e no Cadastro Nacional de Empresas Punidas (CNEP), instituídos no âmbito do Poder Executivo Federal.

8.12.1 As penalidades serão obrigatoriamente registradas no SICAF.

8.13. As sanções de impedimento de licitar e contratar e declaração de inidoneidade para licitar ou contratar são passíveis de reabilitação na forma do art. 163 da Lei nº 14.133, de 2021.

8.14. Os débitos do Contratado para com a Administração Contratante, resultantes de multa administrativa e/ou indenizações, não inscritos em dívida ativa, poderão ser compensados, total ou parcialmente, com os créditos devidos pelo referido órgão decorrentes deste mesmo contrato ou de outros contratos administrativos que o Contratado possua com o mesmo órgão ora Contratante, na forma da Instrução Normativa SEGES/ME nº 26, de 13 de abril de 2022.

## 9. FORMA E CRITÉRIOS DE SELEÇÃO DO FORNECEDOR E REGIME DE EXECUÇÃO

### <b>Forma de seleção e critério de julgamento da proposta</b>

9.1. <span style="color:red"><i>O fornecedor será selecionado por meio da realização de procedimento de LICITAÇÃO, na modalidade [PREGÃO]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[CONCORRÊNCIA], sob a forma ELETRÔNICA, com adoção do critério de julgamento pelo [MENOR PREÇO]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[MAIOR DESCONTO]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[TÉCNICA E PREÇO].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

9.2. <span style="color:red"><i>O fornecedor será selecionado por meio de contratação direta com fundamento no art. [</i></span><span style="color:red"><b><i>74 OU 75</i></b></span><span style="color:red"><i>], inciso [</i></span><span style="color:red"><b><i>indicar o inciso</i></b></span><span style="color:red"><i>], da Lei nº 14.133, de 1º de abril de 2021, com base no seguinte fundamento: [</i></span><span style="color:red"><b><i>descrever a fundamentação da contratação para enquadramento no dispositivo legal indicado</i></b></span><span style="color:red"><i>]</i></span>

### <b>Regime de Execução</b>

9.3. <span style="color:red"><i>O regime de execução do objeto será de [empreitada por preço global] OU [empreitada por preço unitário] OU [empreitada integral] OU [contratação por tarefa] OU [contratação integrada] OU [contratação semi-integrada] OU [fornecimento e prestação de serviço associado].</i></span>

### <span style="color:red;background:darkcyan"><b><i>Critérios de aceitabilidade de preços</i></b></span>

9.4. <span style="color:red;background:darkcyan"><i>Tratando-se de obra ou serviço de engenharia, ressalvado o objeto ou parte dele sujeito ao regime de empreitada por preço unitário, o critério de aceitabilidade de preços será o valor global estimado para a contratação.</i></span>

9.4.1 <span style="color:red;background:darkcyan"><i>O interessado que estiver mais bem colocado na disputa deverá apresentar à Administração, por meio eletrônico, planilha que contenha o preço global, os quantitativos e os preços unitários tidos como relevantes, conforme modelo de planilha elaborada pela Administração, para efeito de avaliação de exequibilidade;</i></span>

9.5. <span style="color:red;background:darkcyan"><i>Para o objeto ou parte dele sujeito ao regime de empreitada por preço unitário o critério de aceitabilidade de preços será: (...)</i></span>

9.5.1 <span style="color:red;background:darkcyan"><i>valor global: conforme valor estimado da contratação;</i></span>

9.5.2 <span style="color:red;background:darkcyan"><i>custos unitários relevantes: itens...</i></span>

9.6. <span style="background:magenta">Em se tratando de serviços contínuos executados em regime de dedicação exclusiva de mão de obra, somente serão aceitas, nos termos do edital, propostas que adotem, na planilha de custos e formação de preços, valores iguais ou superiores aos orçados pela Administração para as seguintes parcelas, conforme estimativa baseada no(a) .............. (Acordo Coletiva de Trabalho OU Convenção Coletiva de Trabalho OU Dissídio Coletivo) nº XXXXX, utilizado(a) como paradigma:</span>

<span style="background:magenta"><i>a) salário-base e adicionais ................., no valor de R$ ...............;</i></span>

<span style="background:magenta"><i>b) auxílio-alimentação, no valor de R$ ...............; e</i></span>

<span style="background:magenta"><i>c) benefícios de natureza trabalhista ou social que contemplem todos os trabalhadores representados pelo sindicato laboral, a saber:</i></span>

<span style="background:magenta"><i>i) ..........., no valor de R$ ..........;</i></span>

<span style="background:magenta"><i>ii) .............., no valor de R$....... (especificar os benefícios e valores).</i></span>

9.6.1 <span style="background:magenta">Não serão considerados custos unitários mínimos relevantes quaisquer valores previstos em Acordo, Convenção Coletiva de Trabalho ou Dissídio Coletivo que não contemplem todos os trabalhadores representados pelo sindicato laboral;</span>

9.6.2 <span style="background:magenta">Em caso de divergência entre os valores considerados no orçamento da Administração e os valores constantes da norma coletiva do licitante, a proposta deverá considerar o maior valor entre ambos;</span>

9.6.3 <span style="background:magenta">Os valores orçados pela Administração constam ..... [da planilha / do Anexo...].</span>

9.7. <span style="color:red;background:cyan"><i>Em se tratando de contratação para registro de preços, caso adotado o critério de julgamento de menor preço ou de maior desconto por grupo de itens, o critério de aceitabilidade de preços unitários máximos será:</i></span>

9.7.1 <span style="color:red;background:cyan"><i>Valores unitários: conforme planilha de composição de preços anexa ao edital</i></span> <span style="color:red;background:cyan"><b><i><u>OU</u></i></b></span> <span style="color:red;background:cyan"><i>tabela constante no item XXXXXX deste Termo de Referência.</i></span>

### <b>Exigências de habilitação</b>

9.8. Para fins de habilitação, deverá o interessado comprovar os seguintes requisitos:

### <b>Habilitação jurídica</b>

9.9. Pessoa física: cédula de identidade (RG) ou documento equivalente que, por força de lei, tenha validade para fins de identificação em todo o território nacional;

9.10. Empresário individual: inscrição no Registro Público de Empresas Mercantis, a cargo da Junta Comercial da respectiva sede;

9.11. Microempreendedor Individual - MEI: Certificado da Condição de Microempreendedor Individual - CCMEI, cuja aceitação ficará condicionada à verificação da autenticidade no sítio https://www.gov.br/empresas-e-negocios/pt-br/empreendedor;

9.12. Sociedade empresária, sociedade limitada unipessoal – SLU ou sociedade identificada como empresa individual de responsabilidade limitada - EIRELI: inscrição do ato constitutivo, estatuto ou contrato social no Registro Público de Empresas Mercantis, a cargo da Junta Comercial da respectiva sede, acompanhada de documento comprobatório de seus administradores;

9.13. Sociedade empresária estrangeira: portaria de autorização de funcionamento no Brasil, publicada no Diário Oficial da União e arquivada na Junta Comercial da unidade federativa onde se localizar a filial, agência, sucursal ou estabelecimento, a qual será considerada como sua sede, conforme Instrução Normativa DREI/ME n.º 77, de 18 de março de 2020.

9.14. Sociedade simples: inscrição do ato constitutivo no Registro Civil de Pessoas Jurídicas do local de sua sede, acompanhada de documento comprobatório de seus administradores;

9.15. Filial, sucursal ou agência de sociedade simples ou empresária: inscrição do ato constitutivo da filial, sucursal ou agência da sociedade simples ou empresária, respectivamente, no Registro Civil das Pessoas Jurídicas ou no Registro Público de Empresas Mercantis onde opera, com averbação no Registro onde tem sede a matriz;

9.16. Sociedade cooperativa: ata de fundação e estatuto social, com a ata da assembleia que o aprovou, devidamente arquivado na Junta Comercial ou inscrito no Registro Civil das Pessoas Jurídicas da respectiva sede, além do registro de que trata o art. 107 da Lei nº 5.764, de 16 de dezembro 1971.

9.17. Consórcio de empresas: contrato de consórcio devidamente arquivado no Registro Civil das Pessoas Jurídicas ou no Registro Público de Empresas Mercantis (art. 279 da Lei nº 6.404, de 15 de dezembro de 1976) ou compromisso público ou particular de constituição, subscrito pelos consorciados, com a indicação da empresa líder, responsável por sua representação perante a Administração (art. 15, caput, I e II, da Lei nº 14.133, de 2021).

9.18. <span style="color:red"><i>Ato de autorização para o exercício da atividade de ............ (especificar a atividade contratada sujeita à autorização), expedido por ....... (especificar o órgão competente) nos termos do art. ..... da (Lei/Decreto) n° ........</i></span>

9.19. Os documentos apresentados deverão estar acompanhados de todas as alterações ou da consolidação respectiva.

### <b>Habilitação fiscal, social e trabalhista</b>

9.20. Prova de inscrição no Cadastro Nacional de Pessoas Jurídicas ou no Cadastro de Pessoas Físicas, conforme o caso;

9.21. Prova de regularidade fiscal perante a Fazenda Nacional, mediante apresentação de certidão expedida conjuntamente pela Secretaria da Receita Federal do Brasil (RFB) e pela Procuradoria-Geral da Fazenda Nacional (PGFN), referente a todos os créditos tributários federais e à Dívida Ativa da União (DAU) por elas administrados, inclusive aqueles relativos à Seguridade Social, nos termos da Portaria Conjunta nº 1.751, de 02 de outubro de 2014, do Secretário da Receita Federal do Brasil e da Procuradora-Geral da Fazenda Nacional.

9.22. Prova de regularidade com o Fundo de Garantia do Tempo de Serviço (FGTS);

9.23. Prova de inexistência de débitos inadimplidos perante a Justiça do Trabalho, mediante a apresentação de certidão negativa ou positiva com efeito de negativa, nos termos do Título VII-A da Consolidação das Leis do Trabalho, aprovada pelo Decreto-Lei nº 5.452, de 1º de maio de 1943;

9.24. Prova de inscrição no cadastro de contribuintes Distrital ou Municipal relativo ao domicílio ou sede do fornecedor, pertinente ao seu ramo de atividade e compatível com o objeto contratual;

9.25. Prova de regularidade com a Fazenda Distrital ou Municipal do domicílio ou sede do fornecedor, relativa à atividade em cujo exercício contrata ou concorre;

9.26. Caso o fornecedor seja considerado isento dos tributos relacionados ao objeto contratual, deverá comprovar tal condição mediante a apresentação de declaração da Fazenda respectiva do seu domicílio ou sede, ou outra equivalente, na forma da lei.

9.27. O fornecedor enquadrado como microempreendedor individual que pretenda auferir os benefícios do tratamento diferenciado previstos na Lei Complementar n. 123, de 2006, estará dispensado da prova de inscrição nos cadastros de contribuintes estadual e municipal.

### <b>Qualificação Econômico-Financeira</b>

9.28. certidão negativa de insolvência civil expedida pelo distribuidor do domicílio ou sede do interessado, caso se trate de pessoa física, desde que admitida a sua participação na licitação/contratação, ou de sociedade simples;

9.29. certidão negativa de falência expedida pelo distribuidor da sede do fornecedor;

9.30. balanço patrimonial, demonstração de resultado de exercício e demais demonstrações contábeis <span style="color:red"><i>................... [do último exercício social]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[dos dois últimos exercícios sociais]</i></span><i>,</i> já exigíveis e apresentados na forma da lei, comprovando, índices de Liquidez Geral (LG), Liquidez Corrente (LC), e Solvência Geral (SG) superiores a 1 (um), obtidos por meio da aplicação das seguintes fórmulas:

| LG = | Ativo Circulante + Realizável a Longo Prazo |
|---|---|
|  | Passivo Circulante + Passivo Não Circulante |

| SG = | Ativo Total |
|---|---|
|  | Passivo Circulante + Passivo Não Circulante |

| LC = | Ativo Circulante |
|---|---|
|  | Passivo Circulante |

9.31. <span style="color:red"><i>Caso a empresa apresente resultado inferior ou igual a 1 (um) em qualquer dos índices de Liquidez Geral (LG), Solvência Geral (SG) e Liquidez Corrente (LC), será exigido, para fins de habilitação, [</i></span><span style="color:red"><b><i>capital mínimo</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>patrimônio líquido mínimo</i></b></span><span style="color:red"><i>] de [</i></span><span style="color:red"><b><i>definir percentual, limitado a 10%</i></b></span><span style="color:red"><i>] do [</i></span><span style="color:red"><b><i>valor total estimado da contratação</i></b></span> <span style="color:red;background:yellow"><b><i>– aplicável para o contrato de escopo</i></b></span><span style="color:red;background:yellow"><i>]</i></span> <span style="color:red;background:yellow"><b><i><u>OU</u></i></b></span> <span style="color:red;background:yellow"><i>[</i></span><span style="color:red;background:yellow"><b><i>valor total estimado da contratação para o período de doze meses – aplicável para o contrato de serviço continuado</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>valor total estimado da parcela pertinente</i></b></span><span style="color:red"><i>].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

9.31.1 <span style="color:red"><i>Capital Circulante Líquido ou Capital de Giro (Ativo Circulante - Passivo Circulante) de, no mínimo, 16,66% (dezesseis inteiros e sessenta e seis centésimos por cento) do valor estimado da contratação para o período de doze meses, tendo por base o balanço patrimonial e as demonstrações contábeis do último exercício social; e</i></span>

9.31.2 <span style="color:red"><i>Patrimônio líquido de 10% (dez por cento) do valor estimado da contratação para o período de doze meses, por meio da apresentação do balanço patrimonial e demonstrações contábeis do último exercício social;</i></span>

9.32. <span style="color:red"><i>Os indicadores fixados acima deverão ser atingidos em cada um dos dois últimos exercícios sociais, sob pena de inabilitação;</i></span>

9.33. Os documentos referidos acima limitar-se-ão ao último exercício no caso de a pessoa jurídica ter sido constituída há menos de 2 (dois) anos;

9.34. Os documentos referidos acima deverão ser exigidos com base no limite definido pela Receita Federal do Brasil para transmissão da Escrituração Contábil Digital - ECD ao Sped.

9.35. <span style="color:red"><i>O atendimento dos índices econômicos previstos neste termo de referência deverá ser atestado mediante declaração assinada por profissional habilitado da área contábil, apresentada pelo fornecedor.</i></span>

9.36. <span style="background:magenta">Declaração do fornecedor, acompanhada da relação de compromissos assumidos, conforme modelo constante do Anexo</span> <span style="background:magenta"><b>XXX</b></span> <span style="background:magenta">deste Termo de Referência, de que um doze avos dos contratos firmados com a Administração Pública e/ou com a iniciativa privada vigentes na data apresentação da proposta não é superior ao patrimônio líquido do interessado, observados os seguintes requisitos:</span>

9.36.1 <span style="background:magenta">a declaração deve ser acompanhada da Demonstração do Resultado do Exercício (DRE), relativa ao último exercício social; e</span>

9.36.2 <span style="background:magenta">caso a diferença entre a declaração e a receita bruta discriminada na Demonstração do Resultado do Exercício (DRE) apresentada seja superior a 10% (dez por cento), para mais ou para menos, o fornecedor deverá apresentar justificativas.</span>

9.37. As empresas criadas no exercício financeiro da licitação/contratação deverão atender a todas as exigências da habilitação e poderão substituir os demonstrativos contábeis pelo balanço de abertura.

### <b>Qualificação Técnica</b>

9.38. <span style="color:red"><i>Declaração de que o fornecedor tomou conhecimento de todas as informações e das condições locais para o cumprimento das obrigações objeto da contratação.</i></span>

9.38.1 <span style="color:red"><i>Essa declaração poderá ser substituída por declaração formal assinada pelo responsável técnico do interessado acerca do conhecimento pleno das condições e peculiaridades da contratação.</i></span>

9.39. <span style="color:red"><i>Registro ou inscrição da empresa na entidade profissional competente</i></span> <span style="color:red"><b><i>.........(escrever por extenso, se for o caso</i></b></span><span style="color:red"><i>), em plena validade;</i></span>

9.39.1 <span style="color:red"><i>Sociedades empresárias estrangeiras atenderão à exigência por meio da apresentação, no momento da assinatura do contrato ou do aceite de instrumento equivalente, da solicitação de registro perante a entidade profissional competente no Brasil.</i></span>

9.40. <span style="color:red"><i>Prova de atendimento aos requisitos ........, previstos na lei ............:</i></span>

### <b>Qualificação Técnico-Operacional</b>

9.41. Comprovação de aptidão para execução de serviço similar, de complexidade tecnológica e operacional equivalente ou superior à do objeto desta contratação, ou do item pertinente, por meio da apresentação de certidões ou atestados emitidos por pessoas jurídicas de direito público ou privado, ou pelo conselho profissional competente, quando for o caso.

9.41.1 Para fins da comprovação de que trata este subitem, os atestados deverão dizer respeito a contrato(s) executado(s) com as seguintes características mínimas:

9.41.1.1. <span style="color:red"><i>contrato(s) que comprove(m) a experiência mínima de XXX (XXX) anos do fornecedor na prestação dos serviços, em períodos sucessivos ou não, sendo aceito o somatório de atestados de períodos diferentes;</i></span>

9.41.1.2. <span style="color:red;background:lightgray"><i>contrato(s) que comprove(m) a execução, pelo fornecedor, de serviços envolvendo</i></span> <span style="color:red;background:yellow"><i>até</i></span> <span style="color:red;background:lightgray"><i>50% (cinquenta por cento) do número de postos de trabalho a serem contratados</i></span><span style="color:red;background:lightgray"><b><i>;</i></b></span>

9.41.1.3. <span style="color:red"><i>... [INSERIR, SE FOR O CASO, OUTRAS CARACTERÍSTICAS MÍNIMAS DOS SERVIÇOS A SEREM COMPROVADAS POR MEIO DOS ATESTADOS]</i></span>

9.41.2 <span style="color:red"><i>Serão admitidos, para fins de comprovação de quantitativo mínimo de serviço, a apresentação e o somatório de diferentes atestados de serviços executados de forma concomitante, pois essa situação equivale, para fins de comprovação de capacidade técnico-operacional, a uma única contratação.</i></span>

9.41.3 Os atestados de capacidade técnica poderão ser apresentados em nome da matriz ou da filial do fornecedor.

9.41.4 O fornecedor disponibilizará todas as informações necessárias à comprovação da legitimidade dos atestados, apresentando, quando solicitado pela Administração, cópia do contrato que deu suporte à contratação, endereço atual do Contratante e local em que foram prestados os serviços, entre outros documentos.

9.41.5 Os atestados deverão referir-se a serviços prestados no âmbito de sua atividade econômica principal ou secundária especificadas no contrato social vigente.

9.42. <span style="color:red"><i>Declaração de que o fornecedor possui ou instalará escritório no município de ..................., o que deverá ser comprovado no prazo máximo de 60 (sessenta) dias, contado a partir da vigência do contrato.</i></span>

9.43. Serão aceitos atestados ou outros documentos hábeis emitidos por entidades estrangeiras quando acompanhados de tradução para o português, salvo se comprovada a inidoneidade da entidade emissora.

9.44. A apresentação, pelo fornecedor, de certidões ou atestados de desempenho anterior emitido em favor de consórcio do qual tenha feito parte será admitida, desde que atendidos os requisitos do art. 67, §§ 10 e 11, da Lei nº 14.133/2021 e regulamentos sobre o tema.

### <b>Qualificação Técnico-Profissional</b>

9.45. Apresentação do(s) profissional(is), abaixo indicado(s), devidamente registrado(s) no conselho profissional competente, detentor(es) de atestado de responsabilidade técnica por execução de serviço de características semelhantes, também abaixo indicado(s):

9.45.1 <span style="color:red"><i>Para o (indicar o profissional): serviços de: (...)</i></span>

9.45.2 <span style="color:red"><i>Para o (indicar o profissional): serviços de (...)</i></span>

9.45.3 O(s) profissional(is) acima indicado(s) deverá(ão) participar do serviço objeto do contrato, e será admitida a sua substituição por profissionais de experiência equivalente ou superior, desde que aprovada pela Administração (§ 6º do art. 67 da Lei nº 14.133, de 2021)

9.46. <span style="color:red"><i>Apresentação da relação de compromissos assumidos e pendentes de cumprimento pelo fornecedor, que importem em diminuição da disponibilidade dos profissionais indicados no item anterior, conforme modelo constante no Anexo XXXX.</i></span>

9.47. Não serão admitidos atestados de responsabilidade técnica de profissionais que, na forma de regulamento, tenham dado causa à aplicação das sanções previstas nos incisos III e IV do <b>caput</b> do art. 156 da Lei n.º 14.133, de 2021, em decorrência de orientação proposta, de prescrição técnica ou de qualquer ato profissional de sua responsabilidade.

9.48. Os atestados de capacidade técnica poderão ser apresentados em nome da matriz ou da filial do fornecedor.

### <b>Disposições gerais sobre habilitação</b>

9.49. Quando permitida a participação na licitação/contratação de empresas estrangeiras que não funcionem no País, as exigências de habilitação serão atendidas mediante documentos equivalentes, inicialmente apresentados em tradução livre.

9.50. Na hipótese de o fornecedor ser empresa estrangeira que não funcione no País, para assinatura do contrato ou da ata de registro de preços ou do aceite do instrumento equivalente, os documentos exigidos para a habilitação serão traduzidos por tradutor juramentado no País e apostilados nos termos do disposto no Decreto nº 8.660, de 29 de janeiro de 2016, ou de outro que venha a substituí-lo, ou consularizados pelos respectivos consulados ou embaixadas.

9.51. Não serão aceitos documentos de habilitação com indicação de CNPJ/CPF diferentes, salvo aqueles legalmente permitidos.

9.52. Se o fornecedor for a matriz, todos os documentos deverão estar em nome da matriz, e se o fornecedor for a filial, todos os documentos deverão estar em nome da filial, exceto para atestados de capacidade técnica, e no caso daqueles documentos que, pela própria natureza, comprovadamente, forem emitidos somente em nome da matriz.

9.53. Serão aceitos registros de CNPJ de fornecedor matriz e filial com diferenças de números de documentos pertinentes ao CND e ao CRF/FGTS, quando for comprovada a centralização do recolhimento dessas contribuições.

### <b>Documentação complementar para cooperativas</b>

9.54. Caso admitida a participação de cooperativas, será exigida a seguinte documentação complementar:

9.54.1 A relação dos cooperados que atendem aos requisitos técnicos exigidos para a contratação e que executarão o contrato, com as respectivas atas de inscrição e a comprovação de que estão domiciliados na localidade da sede da cooperativa, respeitado o disposto nos arts. 4º, inciso XI, 21, inciso I e 42, §§2º a 6º da Lei n. 5.764, de 1971;

9.54.2 A declaração de regularidade de situação do contribuinte individual – DRSCI, para cada um dos cooperados indicados;

9.54.3 A comprovação do capital social proporcional ao número de cooperados necessários à prestação do serviço;

9.54.4 O registro previsto na Lei n. 5.764, de 1971, art. 107;

9.54.5 A comprovação de integração das respectivas quotas-partes por parte dos cooperados que executarão o contrato;

9.54.6 Os seguintes documentos para a comprovação da regularidade jurídica da cooperativa:

9.54.6.1. ata de fundação;

9.54.6.2. estatuto social com a ata da assembleia que o aprovou;

9.54.6.3. regimento dos fundos instituídos pelos cooperados, com a ata da assembleia;

9.54.6.4. editais de convocação das três últimas assembleias gerais extraordinárias;

9.54.6.5. três registros de presença dos cooperados que executarão o contrato em assembleias gerais ou nas reuniões seccionais;

9.54.6.6. ata da sessão que os cooperados autorizaram a cooperativa a contratar o objeto da contratação; e

9.54.6.7. última auditoria contábil-financeira da cooperativa, conforme dispõe o art. 112 da Lei n. 5.764, de 1971, ou uma declaração, sob as penas da lei, de que tal auditoria não foi exigida pelo órgão fiscalizador.

## 10. ESTIMATIVAS DO VALOR DA CONTRATAÇÃO

10.1. <span style="color:red"><i>O custo estimado total da contratação, que é o máximo aceitável, é de R$... (por extenso), conforme custos unitários apostos na [</i></span><span style="color:red"><b><i>tabela contida no item 1.1 acima</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>em anexo</i></b></span><span style="color:red"><i>].</i></span>

<span style="color:red"><b><i>OU</i></b></span>

10.2. <span style="color:red"><i>O custo estimado da contratação possui caráter sigiloso e será tornado público apenas e imediatamente após o julgamento das propostas.</i></span>

10.2.1 <span style="color:red"><i>Quando as propostas permanecerem com preços acima do orçamento estimado, o custo estimado da contratação será tornado público após a fase de lances.</i></span>

10.3. <span style="color:red"><i>A estimativa de custo levou em consideração o risco envolvido na contratação e sua alocação entre Contratante e Contratado, conforme especificado na matriz de risco constante do Contrato.</i></span>

10.4. <span style="color:red;background:cyan"><i>Em caso de Registro de Preços, os preços registrados poderão ser alterados ou atualizados em decorrência de eventual redução dos preços praticados no mercado ou de fato que eleve o custo dos bens, das obras ou dos serviços registrados, nas seguintes situações:</i></span>

10.4.1 <span style="color:red;background:cyan"><i>em caso de força maior, caso fortuito ou fato do príncipe ou em decorrência de fatos imprevisíveis ou previsíveis de consequências incalculáveis, que inviabilizem a execução da ata tal como pactuada, nos termos do disposto na alínea “d” do inciso II do capu</i></span><span style="color:red;background:cyan"><b><i>t</i></b></span> <span style="color:red;background:cyan"><i>do art. 124 da Lei nº 14.133, de 2021;</i></span>

10.4.2 <span style="color:red;background:cyan"><i>em caso de criação, alteração ou extinção de quaisquer tributos ou encargos legais ou superveniência de disposições legais, com comprovada repercussão sobre os preços registrados;</i></span>

10.4.3 <span style="color:red;background:cyan"><i>serão reajustados os preços registrados, respeitada a contagem da anualidade e o índice previsto para a contratação; ou</i></span>

10.4.4 <span style="color:red;background:cyan"><i>poderão ser repactuados, a pedido do interessado, conforme critérios definidos para a contratação.</i></span>

## 11. ADEQUAÇÃO ORÇAMENTÁRIA

11.1. <span style="color:red"><i>As despesas decorrentes da presente contratação correrão à conta de recursos específicos consignados no Orçamento Geral da União.</i></span>

11.2. <span style="color:red"><i>A contratação será atendida pela seguinte dotação:</i></span>

I) <span style="color:red"><i>Gestão/unidade: [...];</i></span>

II) <span style="color:red"><i>Fonte de recursos: [...];</i></span>

III) <span style="color:red"><i>Programa de trabalho: [...];</i></span>

IV) <span style="color:red"><i>Elemento de despesa: [...]; e</i></span>

V) <span style="color:red"><i>Plano interno: [...].</i></span>

11.3. <span style="color:red"><i>A dotação relativa aos exercícios financeiros subsequentes será indicada após aprovação da Lei Orçamentária respectiva e liberação dos créditos correspondentes, mediante apostilamento.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

11.4. <span style="color:red;background:cyan"><i>A indicação da dotação orçamentária fica postergada para o momento da assinatura do contrato ou instrumento equivalente.</i></span>

## 12. DISPOSIÇÕES FINAIS

12.1. As informações contidas neste Termo de Referência não são classificadas como sigilosas <span style="color:red"><b>[</b></span><span style="color:red"><b><i>exceto o custo estimado da contratação, que possui caráter sigiloso até o julgamento das propostas</i></b></span><span style="color:red"><b>]</b></span>.

<span style="color:red"><i>[Local]</i></span><i>,</i> <span style="color:red"><i>[dia]</i></span> <i>de</i> <span style="color:red"><i>[mês]</i></span> <i>de</i> <span style="color:red"><i>[ano].</i></span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Identificação e assinatura do servidor (ou equipe) responsável

<b>ANEXO I</b>

<b>Regras aplicáveis ao instrumento substitutivo ao contrato</b>

<b>(Contratações de pequeno valor - art. 95, inciso I, da Lei n. 14.133/2021, Orientação Normativa nº 84, de 17 de maio de 2024)</b>

## 1. FORMALIZAÇÃO DA CONTRATAÇÃO

1.1. O adjudicatário terá o <span style="color:red"><i>prazo de ...............,</i></span> contado a partir da data de sua convocação, para aceitar o instrumento equivalente ao contrato ............ <span style="color:red"><i>[Nota de Empenho/Carta Contrato/Autorização]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[constante neste Anexo]</i></span>, sob pena de decair do direito à contratação, sem prejuízo das sanções previstas.

1.2. O prazo poderá ser prorrogado, por igual período, por solicitação justificada do adjudicatário e aceita pela Administração.

1.3. O aceite do instrumento equivalente pelo adjudicatário implica no reconhecimento de que:

1.3.1 referido instrumento substitui o termo de contrato, sendo-lhe aplicáveis as disposições da Lei nº 14.133/2021;

1.3.2 o Contratado se vincula à sua proposta e às previsões contidas no <span style="color:red"><i>Edital</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>na Autorização de Contratação Direta e/ou no Aviso de Dispensa Eletrônica,</i></span> no Termo de Referência e em seus anexos, conforme Termo de Ciência e Concordância (Anexo II).

## 2. VIGÊNCIA E PRORROGAÇÃO

2.1. <span style="color:red"><i>O prazo de vigência da contratação é aquele estabelecido no Termo de Referência, na forma do artigo 105 da Lei n° 14.133, de 2021.</i></span>

2.2. <span style="color:red"><i>O prazo de vigência será automaticamente prorrogado, independentemente de termo aditivo, quando o objeto não for concluído no período firmado acima, ressalvadas as providências cabíveis no caso de culpa do Contratado, previstas neste instrumento.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

2.3. <span style="color:red"><i>O prazo de vigência da contratação é aquele estabelecido no Termo de Referência, prorrogável por até 10 anos, na forma dos artigos 106 e 107 da Lei n° 14.133, de 2021.</i></span>

2.4. <span style="color:red"><i>A prorrogação de que trata este item é condicionada ao ateste, pela autoridade competente, de que as condições e os preços permanecem vantajosos para a Administração, permitida a negociação com o Contratado, atentando, ainda, para o cumprimento dos seguintes requisitos:</i></span>

2.4.1 <span style="color:red"><i>Estar formalmente demonstrado no processo que a forma de prestação dos serviços tem natureza continuada;</i></span>

2.4.2 <span style="color:red"><i>Seja juntado relatório que discorra sobre a execução contratual, com informações de que os serviços tenham sido prestados regularmente;</i></span>

2.4.3 <span style="color:red"><i>Seja juntada justificativa e motivo, por escrito, de que a Administração mantém interesse na realização do serviço;</i></span>

2.4.4 <span style="color:red"><i>Haja manifestação expressa do Contratado informando o interesse na prorrogação;</i></span>

2.4.5 <span style="color:red"><i>Seja comprovado que o Contratado mantém as condições iniciais de habilitação; e</i></span>

2.4.6 <span style="color:red"><i>Não haja registro no Cadastro Informativo de créditos não quitados do setor público federal (Cadin).</i></span>

2.5. <span style="color:red"><i>O Contratado não tem direito subjetivo à prorrogação contratual.</i></span>

2.6. <span style="color:red"><i>A prorrogação contratual deverá ser promovida mediante celebração de termo aditivo.</i></span>

2.7. <span style="color:red"><i>Nas eventuais prorrogações contratuais, os custos não renováveis já pagos ou amortizados ao longo do primeiro período de vigência da contratação deverão ser reduzidos ou eliminados como condição para a renovação.</i></span>

2.8. <span style="color:red"><i>A contratação não poderá ser prorrogada quando o Contratado tiver sido penalizado nas sanções de declaração de inidoneidade ou impedimento de licitar e contratar com poder público, observadas as abrangências de aplicação.</i></span>

<span style="color:red"><b><i><u>OU</u></i></b></span>

2.9. <span style="color:red"><i>O prazo de vigência da contratação é de ..............................(máximo de um ano) contados do(a) ............................. (data da ocorrência da emergência ou da calamidade), improrrogável, na forma do art. 75, VIII, da Lei n° 14.133/2021.</i></span>

## 3. OBRIGAÇÕES DO CONTRATANTE

3.1. São obrigações do Contratante:

3.1.1 Exigir o cumprimento de todas as obrigações assumidas pelo Contratado, de acordo com o Termo de Referência e seus anexos;

3.1.2 Receber o objeto no prazo e condições estabelecidas no Termo de Referência;

3.1.3 Notificar o Contratado, por escrito, sobre vícios, defeitos incorreções, imperfeições, falhas ou irregularidades verificadas na execução do objeto contratual, fixando prazo para que seja substituído, reparado ou corrigido, total ou parcialmente, às suas expensas, certificando-se de que as soluções por ele propostas sejam as mais adequadas;

3.1.4 Acompanhar e fiscalizar a execução contratual e o cumprimento das obrigações pelo Contratado;

3.1.5 Comunicar a empresa para emissão de Nota Fiscal em relação à parcela incontroversa da execução do objeto, para efeito de liquidação e pagamento, quando houver controvérsia sobre a execução do objeto, quanto à dimensão, qualidade e quantidade, conforme o art. 143 da Lei nº 14.133, de 2021;

3.1.6 Efetuar o pagamento ao Contratado do valor correspondente à execução do objeto, no prazo, forma e condições estabelecidos no Termo de Referência;

3.1.7 Aplicar ao Contratado as sanções previstas na lei e no Termo de Referência;

3.1.8 Cientificar o órgão de representação judicial da Advocacia-Geral da União para adoção das medidas cabíveis quando do descumprimento de obrigações pelo Contratado;

3.1.9 Explicitamente emitir decisão sobre todas as solicitações e reclamações relacionadas à execução contratual, ressalvados os requerimentos manifestamente impertinentes, meramente protelatórios ou de nenhum interesse para a boa execução do ajuste.

3.1.9.1. A Administração terá o prazo de <span style="color:red"><i>XXXXXXX</i></span>, a contar da data do protocolo do requerimento para decidir, admitida a prorrogação motivada, por igual período.

3.1.10 Responder eventuais pedidos de reestabelecimento do equilíbrio econômico-financeiro feitos pelo Contratado no prazo máximo de <span style="color:red">XXXXXX.</span>

3.1.11 <span style="color:red"><i>Notificar os emitentes das garantias quanto ao início de processo administrativo para apuração de descumprimento de cláusulas contratuais.</i></span>

3.1.12 Comunicar o Contratado na hipótese de posterior alteração do projeto pelo Contratante, no caso do art. 93, §2º, da Lei nº 14.133, de 2021.

3.1.13 Fornecer por escrito as informações necessárias para o desenvolvimento dos serviços objeto do contrato.

3.1.14 Realizar avaliações periódicas da qualidade dos serviços, após seu recebimento.

3.1.15 <span style="color:red;background:darkcyan"><i>Exigir do Contratado que providencie a seguinte documentação como condição indispensável para o recebimento definitivo de objeto, quando for o caso:</i></span>

3.1.15.1. <span style="color:red;background:darkcyan"><i>"as built", elaborado pelo responsável por sua execução;</i></span>

3.1.15.2. <span style="color:red;background:darkcyan"><i>comprovação das ligações definitivas de energia, água, telefone e gás;</i></span>

3.1.15.3. <span style="color:red;background:darkcyan"><i>laudo de vistoria do corpo de bombeiros aprovando o serviço;</i></span>

3.1.15.4. <span style="color:red;background:darkcyan"><i>carta "habite-se", emitida pela prefeitura; e</i></span>

3.1.15.5. <span style="color:red;background:darkcyan"><i>certidão negativa de débitos previdenciários específica para o registro da obra junto ao Cartório de Registro de Imóveis;</i></span>

3.1.16 <span style="color:red;background:darkcyan"><i>Arquivar, entre outros documentos, de projetos, "as built", especificações técnicas, orçamentos, termos de recebimento, contratos e aditamentos, relatórios de inspeções técnicas após o recebimento do serviço e notificações expedidas.</i></span>

3.1.17 Assegurar que o ambiente de trabalho, inclusive seus equipamentos e instalações, apresentem condições adequadas ao cumprimento, pelo Contratado, das normas de segurança e saúde no trabalho, quando o serviço for executado em suas dependências, ou em local por ela designado.

3.1.18 Previamente à expedição da ordem de serviço, verificar pendências, liberar áreas e/ou adotar providências cabíveis para a regularidade do início da sua execução.

3.2. A Administração não responderá por quaisquer compromissos assumidos pelo Contratado com terceiros, ainda que vinculados à execução do objeto contratual, bem como por qualquer dano causado a terceiros em decorrência de ato do Contratado, de seus empregados, prepostos ou subordinados.

## 4. OBRIGAÇÕES DO CONTRATADO

4.1. O Contratado deve cumprir todas as obrigações constantes do Termo de Referência e deste Anexo, assumindo como exclusivamente seus os riscos e as despesas decorrentes da boa e perfeita execução do objeto, observando, ainda, as obrigações a seguir dispostas:

4.1.1 <span style="color:red"><i>Manter preposto aceito pela Administração no local do serviço para representá-lo na execução contratual.</i></span>

4.1.2 <span style="color:red"><i>A indicação ou a manutenção do preposto da empresa poderá ser recusada pelo órgão ou entidade, desde que devidamente justificada, devendo a empresa designar outro para o exercício da atividade.</i></span>

4.1.3 Atender às determinações regulares emitidas pelo fiscal contratual ou autoridade superior e prestar todo esclarecimento ou informação por eles solicitados;

4.1.4 Alocar os empregados necessários ao perfeito cumprimento das disposições do Termo de Referência e deste Anexo, com habilitação e conhecimento adequados, fornecendo os materiais, equipamentos, ferramentas e utensílios demandados, cuja quantidade, qualidade e tecnologia deverão atender às recomendações de boa técnica e a legislação de regência;

4.1.5 Reparar, corrigir, remover, reconstruir ou substituir, às suas expensas, no total ou em parte, no prazo fixado pelo fiscal, os serviços nos quais se verificarem vícios, defeitos ou incorreções resultantes da execução ou dos materiais empregados;

4.1.6 Responsabilizar-se pelos vícios e danos decorrentes da execução do objeto, de acordo com o Código de Defesa do Consumidor (Lei nº 8.078, de 1990), bem como por todo e qualquer dano causado à Administração ou terceiros, não reduzindo essa responsabilidade a fiscalização ou o acompanhamento da execução contratual pelo Contratante, que ficará autorizado a descontar dos pagamentos devidos ou da garantia, caso exigida no edital, o valor correspondente aos danos sofridos;

4.1.7 Efetuar comunicação ao Contratante, assim que tiver ciência da impossibilidade de realização ou finalização do serviço no prazo estabelecido, para adoção de ações de contingência cabíveis.

4.1.8 Não contratar, durante a vigência da contratação, cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, de dirigente do Contratante ou do fiscal ou gestor contratuais, nos termos do artigo 48, parágrafo único, da Lei nº 14.133, de 2021;

4.1.9 Quando não for possível a verificação da regularidade no Sistema de Cadastro de Fornecedores – SICAF, o Contratado deverá entregar ao setor responsável pela fiscalização contratual, até o dia trinta do mês seguinte ao da prestação dos serviços, os seguintes documentos:

4.1.9.1. prova de regularidade relativa à Seguridade Social;

4.1.9.2. certidão conjunta relativa aos tributos federais e à Dívida Ativa da União;

4.1.9.3. certidões que comprovem a regularidade perante a Fazenda Municipal ou Distrital do domicílio ou sede do Contratado;

4.1.9.4. Certidão de Regularidade do FGTS – CRF; e

4.1.9.5. Certidão Negativa de Débitos Trabalhistas – CNDT;

4.1.10 Responsabilizar-se pelo cumprimento das obrigações previstas em Acordo, Convenção, Dissídio Coletivo de Trabalho ou equivalentes das categorias abrangidas pela contratação, por todas as obrigações trabalhistas, sociais, previdenciárias, tributárias e as demais previstas em legislação específica, cuja inadimplência não transfere a responsabilidade ao Contratante;

4.1.11 Comunicar ao Fiscal, no prazo de 24 (vinte e quatro) horas, qualquer ocorrência anormal ou acidente que se verifique no local dos serviços.

4.1.12 Prestar todo esclarecimento ou informação solicitada pelo Contratante ou por seus prepostos, garantindo-lhes o acesso, a qualquer tempo, ao local dos trabalhos, bem como aos documentos relativos à execução do empreendimento.

4.1.13 Paralisar, por determinação do Contratante, qualquer atividade que não esteja sendo executada de acordo com a boa técnica ou que ponha em risco a segurança de pessoas ou bens de terceiros.

4.1.14 Promover a guarda, manutenção e vigilância de materiais, ferramentas, e tudo o que for necessário à execução do objeto, durante a vigência contratual.

4.1.15 Conduzir os trabalhos com estrita observância às normas da legislação pertinente, cumprindo as determinações dos Poderes Públicos, mantendo sempre limpo o local dos serviços e nas melhores condições de segurança, higiene e disciplina.

4.1.16 Submeter previamente, por escrito, ao Contratante, para análise e aprovação, quaisquer mudanças nos métodos executivos que fujam às especificações do memorial descritivo ou instrumento congênere.

4.1.17 Cumprir as normas de proteção ao trabalho, inclusive aquelas relativas à segurança e à saúde no trabalho;

4.1.18 Não submeter os trabalhadores a condições degradantes de trabalho, jornadas exaustivas, servidão por dívida ou trabalhos forçados;

4.1.19 Não permitir a utilização de qualquer trabalho do menor de dezesseis anos de idade, exceto na condição de aprendiz para os maiores de quatorze anos de idade, observada a legislação;

4.1.20 Não submeter o menor de dezoito anos de idade à realização de trabalho noturno e em condições perigosas e insalubres e à realização de atividades constantes na Lista de Piores Formas de Trabalho Infantil, aprovada pelo Decreto nº 6.481, de 12 de junho de 2008;

4.1.21 Receber e dar o tratamento adequado a denúncias de discriminação, violência e assédio no ambiente de trabalho;

4.1.22 Manter, durante toda a vigência da contratação, em compatibilidade com as obrigações assumidas, todas as condições exigidas para habilitação na licitação, ou para a qualificação, na contratação direta;

4.1.23 Cumprir, durante todo o período de execução contratual, a reserva de cargos prevista em lei para pessoa com deficiência, para reabilitado da Previdência Social ou para aprendiz, bem como as reservas de cargos previstas na legislação;

4.1.24 Comprovar a reserva de cargos a que se refere a cláusula acima, no prazo fixado pela fiscalização contratual, com a indicação dos empregados que preencheram as referidas vagas;

4.1.25 Guardar sigilo sobre todas as informações obtidas em decorrência da execução do objeto;

4.1.26 Arcar com o ônus decorrente de eventual equívoco no dimensionamento dos quantitativos de sua proposta, inclusive quanto aos custos variáveis decorrentes de fatores futuros e incertos, devendo complementá-los, caso o previsto inicialmente em sua proposta não seja satisfatório para o atendimento do objeto da contratação, exceto quando ocorrer algum dos eventos arrolados no art. 124, II, d, da Lei nº 14.133, de 2021;

4.1.27 Cumprir, além dos postulados legais vigentes de âmbito federal, estadual ou municipal, as normas de segurança do Contratante;

4.1.28 <span style="color:red"><i>Realizar os serviços de manutenção e assistência técnica no(s) seguinte(s) local(is) ... (inserir endereço(s));</i></span>

4.1.28.1. <span style="color:red"><i>O técnico deverá se deslocar ao local da repartição, salvo se o Contratado tiver unidade de prestação de serviços em distância de [....] (inserir distância conforme avaliação técnica) do local demandado.</i></span>

4.1.29 <span style="color:red"><i>Realizar a transição contratual com transferência de conhecimento, tecnologia e técnicas empregadas, sem perda de informações, podendo exigir, inclusive, a capacitação dos técnicos do Contratante ou da nova empresa que continuará a execução dos serviços;</i></span>

4.1.30 <span style="color:red"><i>Ceder ao Contratante todos os direitos patrimoniais relativos ao objeto contratado, o qual poderá ser livremente utilizado e/ou alterado em outras ocasiões, sem necessidade de nova autorização do Contratado.</i></span>

4.1.30.1. <span style="color:red"><i>Considerando que o projeto contratado se refere a obra imaterial de caráter tecnológico, insuscetível de privilégio, a cessão dos direitos a que se refere o subitem acima inclui o fornecimento de todos os dados, documentos e elementos de informação pertinentes à tecnologia de concepção, desenvolvimento, fixação em suporte físico de qualquer natureza e aplicação da obra.</i></span>

4.1.31 Manter os empregados nos horários predeterminados pelo Contratante.

4.1.32 Apresentar os empregados devidamente identificados por meio de crachá.

4.1.33 Apresentar ao Contratante, quando for o caso, a relação nominal dos empregados que adentrarão no órgão para a execução do serviço.

4.1.34 Observar os preceitos da legislação sobre a jornada de trabalho, conforme a categoria profissional.

4.1.35 Atender às solicitações do Contratante quanto à substituição dos empregados alocados, no prazo fixado pela fiscalização contratual, nos casos em que ficar constatado descumprimento das obrigações relativas à execução do serviço, conforme descrito nas especificações do objeto.

4.1.36 Instruir seus empregados quanto à necessidade de acatar as Normas Internas do Contratante.

4.1.37 Instruir seus empregados a respeito das atividades a serem desempenhadas, alertando-os a não executarem atividades não abrangidas na contratação, devendo o Contratado relatar ao Contratante toda e qualquer ocorrência neste sentido, a fim de evitar desvio de função.

4.1.38 Instruir os seus empregados, quanto à prevenção de incêndios nas áreas do Contratante.

4.1.39 Adotar as providências e precauções necessárias, inclusive consulta nos respectivos órgãos, se necessário for, a fim de que não venham a ser danificadas as redes hidrossanitárias, elétricas e de comunicação.

4.1.40 <span style="color:red"><i>Estar registrado ou inscrito no Conselho Profissional competente, conforme as áreas de atuação previstas no Termo de Referência, em plena validade.</i></span>

4.1.41 <span style="color:red"><i>Obter junto aos órgãos competentes, conforme o caso, as licenças necessárias e demais documentos e autorizações exigíveis, na forma da legislação aplicável.</i></span>

4.1.42 <span style="color:red;background:darkcyan"><i>Elaborar o Diário de Obra, incluindo diariamente, pelo Engenheiro preposto responsável, as informações sobre o andamento do empreendimento, tais como, número de funcionários, de equipamentos, condições de trabalho, condições meteorológicas, serviços executados, registro de ocorrências e outros fatos relacionados, bem como os comunicados à Fiscalização e situação das atividades em relação ao cronograma previsto.</i></span>

4.1.43 Refazer, às suas expensas, os trabalhos executados em desacordo com o estabelecido nas especificações, bem como substituir aqueles realizados com materiais defeituosos ou com vício de construção, pelo prazo de 05 (cinco) anos, contado da data de emissão do Termo de Recebimento Definitivo.

4.1.44 <span style="color:red"><i>Utilizar somente matéria-prima florestal procedente, nos termos do</i></span> <span style="color:red"><i><u>artigo 11 do Decreto n° 5.975, de 2006</u></i></span><span style="color:red"><i>, de:</i></span>

4.1.44.1. <span style="color:red"><i>manejo florestal, realizado por meio de Plano de Manejo Florestal Sustentável - PMFS devidamente aprovado pelo órgão competente do Sistema Nacional do Meio Ambiente - SISNAMA;</i></span>

4.1.44.2. <span style="color:red"><i>supressão da vegetação natural, devidamente autorizada pelo órgão competente do Sistema Nacional do Meio Ambiente - SISNAMA;</i></span>

4.1.44.3. <span style="color:red"><i>florestas plantadas; e</i></span>

4.1.44.4. <span style="color:red"><i>outras fontes de biomassa florestal, definidas em normas específicas do órgão ambiental competente.</i></span>

4.1.45 <span style="color:red"><i>Comprovar a procedência legal dos produtos ou subprodutos florestais utilizados em cada etapa da execução contratual, nos termos do</i></span> <span style="color:red"><i><u>artigo 4°, inciso IX, da Instrução Normativa SLTI/MP n° 1, de 19/01/2010</u></i></span><span style="color:red"><i>, por ocasião da respectiva medição, mediante a apresentação dos seguintes documentos, conforme o caso:</i></span>

4.1.45.1. <span style="color:red"><i>Cópias autenticadas das notas fiscais de aquisição dos produtos ou subprodutos florestais;</i></span>

4.1.45.2. <span style="color:red"><i>Cópia dos Comprovantes de Registro do fornecedor e do transportador dos produtos ou subprodutos florestais junto ao Cadastro Técnico Federal de Atividades Potencialmente Poluidoras ou Utilizadoras de Recursos Ambientais - CTF, mantido pelo IBAMA, quando tal inscrição for obrigatória, acompanhados dos respectivos Certificados de Regularidade válidos, conforme</i></span> <span style="color:red"><i><u>artigo 17, inciso II, da Lei n° 6.938, de 1981</u></i></span><span style="color:red"><i>, e legislação correlata;</i></span>

4.1.45.3. <span style="color:red"><i>Documento de Origem Florestal – DOF, instituído pela Portaria n° 253, de 18/08/2006, do Ministério do Meio Ambiente, e Instrução Normativa IBAMA n° 21, de 24/12/2014, quando se tratar de produtos ou subprodutos florestais de origem nativa cujo transporte e armazenamento exijam a emissão de tal licença obrigatória; e</i></span>

4.1.45.4. <span style="color:red"><i>Caso os produtos ou subprodutos florestais utilizados na execução contratual tenham origem em Estado que possua documento de controle próprio, o Contratado deverá apresentá-lo, em complementação ao DOF, a fim de demonstrar a regularidade do transporte e armazenamento nos limites do território estadual.</i></span>

4.1.46 <span style="color:red"><i>Observar as diretrizes, critérios e procedimentos para a gestão dos resíduos da construção civil estabelecidos na Resolução nº 307, de 05/07/2002, com as alterações posteriores, do Conselho Nacional de Meio Ambiente - CONAMA, conforme artigo 4°, §§ 2° e 3°, da Instrução Normativa SLTI/MP n° 1, de 19/01/2010, nos seguintes termos:</i></span>

4.1.47 <span style="color:red"><i>O gerenciamento dos resíduos originários da contratação deverá obedecer às diretrizes técnicas e procedimentos do Programa Municipal de Gerenciamento de Resíduos da Construção Civil, ou do Projeto de Gerenciamento de Resíduos da Construção Civil apresentado ao órgão competente, conforme o caso.</i></span>

4.1.48 <span style="color:red"><i>Nos termos dos artigos 3° e 10° da Resolução CONAMA n° 307, de 05/07/2002, o Contratado deverá providenciar a destinação ambientalmente adequada dos resíduos da construção civil originários da contratação, obedecendo, no que couber, aos seguintes procedimentos:</i></span>

4.1.48.1. <span style="color:red"><i>resíduos Classe A (reutilizáveis ou recicláveis como agregados): deverão ser reutilizados ou reciclados na forma de agregados, ou encaminhados a aterros de resíduos classe A de preservação de material para usos futuros.</i></span>

4.1.48.2. <span style="color:red"><i>resíduos Classe B (recicláveis para outras destinações): deverão ser reutilizados, reciclados ou encaminhados a áreas de armazenamento temporário, sendo dispostos de modo a permitir a sua utilização ou reciclagem futura.</i></span>

4.1.48.3. <span style="color:red"><i>resíduos Classe C (para os quais não foram desenvolvidas tecnologias ou aplicações economicamente viáveis que permitam a sua reciclagem/recuperação): deverão ser armazenados, transportados e destinados em conformidade com as normas técnicas específicas.</i></span>

4.1.48.4. <span style="color:red"><i>resíduos Classe D (perigosos, contaminados ou prejudiciais à saúde): deverão ser armazenados, transportados, reutilizados e destinados em conformidade com as normas técnicas específicas.</i></span>

4.1.49 <span style="color:red"><i>Em nenhuma hipótese o Contratado poderá dispor os resíduos originários da contratação em aterros de resíduos sólidos urbanos, áreas de “bota fora”, encostas, corpos d´água, lotes vagos e áreas protegidas por Lei, bem como em áreas não licenciadas.</i></span>

4.1.50 <span style="color:red"><i>Para fins de fiscalização do fiel cumprimento do Programa Municipal de Gerenciamento de Resíduos da Construção Civil, ou do Projeto de Gerenciamento de Resíduos da Construção Civil, conforme o caso, o Contratado comprovará, sob pena de multa, que todos os resíduos removidos estão acompanhados de Controle de Transporte de Resíduos, em conformidade com as normas da Agência Brasileira de Normas Técnicas - ABNT, ABNT NBR ns. 15.112, 15.113, 15.114, 15.115 e 15.116, de 2004.</i></span>

4.1.51 <span style="color:red"><i>Observar as seguintes diretrizes de caráter ambiental:</i></span>

4.1.51.1. <span style="color:red"><i>Qualquer instalação, equipamento ou processo, situado em local fixo, que libere ou emita matéria para a atmosfera, por emissão pontual ou fugitiva, utilizado na execução contratual, deverá respeitar os limites máximos de emissão de poluentes admitidos na Resolução CONAMA n° 382, de 26/12/2006, e legislação correlata, de acordo com o poluente e o tipo de fonte.</i></span>

4.1.51.2. <span style="color:red"><i>Na execução contratual, conforme o caso, a emissão de ruídos não poderá ultrapassar os níveis considerados aceitáveis pela Norma NBR-10.151 - Avaliação do Ruído em Áreas Habitadas visando o conforto da comunidade, da Associação Brasileira de Normas Técnicas - ABNT, ou aqueles estabelecidos na NBR-10.152 - Níveis de Ruído para conforto acústico, da Associação Brasileira de Normas Técnicas - ABNT, nos termos da Resolução CONAMA n° 01, de 08/03/90, e legislação correlata.</i></span>

4.1.52 <span style="color:red"><i>Nos termos do artigo 4°, § 3°, da Instrução Normativa SLTI/MP n° 1, de 19/01/2010, deverão ser utilizados, na execução contratual, agregados reciclados, sempre que existir a oferta de tais materiais, capacidade de suprimento e custo inferior em relação aos agregados naturais, inserindo-se na planilha de formação de preços os custos correspondentes.</i></span>

4.1.53 <span style="color:red"><i>Responder por qualquer acidente de trabalho na execução dos serviços, por uso indevido de patentes registradas em nome de terceiros, por danos resultantes de defeitos ou incorreções dos serviços ou dos bens do Contratante, de seus funcionários ou de terceiros, ainda que ocorridos em via pública junto ao serviço de engenharia.</i></span>

4.1.54 <span style="color:red"><i>Realizar, conforme o caso, por meio de laboratórios previamente aprovados pela fiscalização e sob suas custas, os testes, ensaios, exames e provas que lhe caibam necessárias ao controle de qualidade dos materiais, serviços e equipamentos a serem aplicados nos trabalhos, conforme procedimento previsto nas especificações.</i></span>

4.1.55 <span style="color:red"><i>Providenciar, conforme o caso, as ligações definitivas das utilidades previstas no projeto (água, esgoto, gás, energia elétrica, telefone etc.), bem como atuar junto aos órgãos federais, estaduais e municipais e concessionárias de serviços públicos para a obtenção de licenças e regularização dos serviços e atividades concluídas (ex.: Habite-se, Licença Ambiental de Operação etc.).</i></span>

4.1.56 <span style="color:red;background:darkcyan"><i>Fornecer os projetos executivos desenvolvidos pelos Contratados, que formarão um conjunto de documentos técnicos, gráficos e descritivos referentes aos segmentos especializados de engenharia, previamente e devidamente compatibilizados, de modo a considerar todas as possíveis interferências capazes de oferecer impedimento total ou parcial, permanente ou temporário, à execução do empreendimento, de maneira a abrangê-la em seu todo, compreendendo a completa caracterização e entendimento de todas as suas especificações técnicas, para posterior execução e implantação do objeto garantindo a plena compreensão das informações prestadas, bem como sua aplicação correta nos trabalhos:</i></span>

4.1.56.1. <span style="color:red;background:darkcyan"><i>A elaboração dos projetos executivos deverá partir das soluções desenvolvidas nos anteprojetos constantes no Termo de Referência e seus anexos (Caderno de Encargos e Especificações Técnicas) e apresentar o detalhamento dos elementos construtivos e especificações técnicas, incorporando as alterações exigidas pelas mútuas interferências entre os diversos projetos.</i></span>

4.1.57 <span style="color:red"><i>Em se tratando de atividades que envolvam serviços de natureza intelectual, após o aceite do instrumento equivalente, o Contratado deverá participar de reunião inicial, devidamente registrada em Ata, para dar início à execução do serviço, com o esclarecimento das obrigações contratuais, em que estejam presentes os técnicos responsáveis pela elaboração do termo de referência, o gestor, o fiscal técnico, o fiscal administrativo, se houver, os técnicos da área requisitante, o preposto da empresa e os gerentes das áreas que executarão os serviços contratados.</i></span>

4.1.58 <span style="color:red"><i>Na contratação integrada, após a elaboração do projeto básico pelo contratado, o conjunto de desenhos, especificações, memoriais e cronograma físico-financeiro deverá ser submetido à aprovação da Administração, que avaliará sua adequação em relação aos parâmetros definidos no edital e conformidade com as normas técnicas, vedadas alterações que reduzam a qualidade ou a vida útil do empreendimento e mantida a responsabilidade integral do contratado pelos riscos associados ao projeto básico</i></span>

## 5. OBRIGAÇÕES PERTINENTES À LGPD

5.1. <span style="color:red"><i>As partes deverão cumprir a Lei nº 13.709, de 14 de agosto de 2018 (LGPD), quanto a todos os dados pessoais a que tenham acesso em razão da licitação ou da contratação, a partir da apresentação da proposta no certame, independentemente de declaração ou de aceitação expressa.</i></span>

5.2. <span style="color:red"><i>Os dados obtidos somente poderão ser utilizados para as finalidades que justificaram seu acesso e de acordo com a boa-fé e com os princípios do art. 6º da LGPD.</i></span>

5.3. <span style="color:red"><i>É vedado o compartilhamento com terceiros dos dados obtidos fora das hipóteses permitidas em Lei.</i></span>

5.4. <span style="color:red"><i>A Administração deverá ser informada no prazo de 5 (cinco) dias úteis sobre todos os contratos de suboperação firmados ou que venham a ser celebrados pelo Contratado.</i></span>

5.5. <span style="color:red"><i>Terminado o tratamento dos dados nos termos do art. 15 da LGPD, é dever do Contratado eliminá-los, com exceção das hipóteses do art. 16 da LGPD, incluindo aquelas em que houver necessidade de guarda de documentação para fins de comprovação do cumprimento de obrigações legais ou contratuais e somente enquanto não prescritas essas obrigações.</i></span>

5.6. <span style="color:red"><i>É dever do Contratado orientar e treinar seus empregados sobre os deveres, requisitos e responsabilidades decorrentes da LGPD.</i></span>

5.7. <span style="color:red"><i>O Contratado deverá exigir de suboperadores e subcontratados o cumprimento dos deveres da presente cláusula, permanecendo integralmente responsável por garantir sua observância.</i></span>

5.8. <span style="color:red"><i>O Contratante poderá realizar diligência para aferir o cumprimento dessa cláusula, devendo o Contratado atender prontamente eventuais pedidos de comprovação formulados.</i></span>

5.9. <span style="color:red"><i>O Contratado deverá prestar, no prazo fixado pelo Contratante, prorrogável justificadamente, quaisquer informações acerca dos dados pessoais para cumprimento da LGPD, inclusive quanto a eventual descarte realizado.</i></span>

5.10. <span style="color:red"><i>Bancos de dados formados a partir de contratos administrativos, notadamente aqueles que se proponham a armazenar dados pessoais, devem ser mantidos em ambiente virtual controlado, com registro individual rastreável de tratamentos realizados (LGPD, art. 37), com cada acesso, data, horário e registro da finalidade, para efeito de responsabilização, em caso de eventuais omissões, desvios ou abusos.</i></span>

5.10.1 <span style="color:red"><i>Os referidos bancos de dados devem ser desenvolvidos em formato interoperável, a fim de garantir a reutilização desses dados pela Administração nas hipóteses previstas na LGPD.</i></span>

5.11. <span style="color:red"><i>O presente instrumento está sujeito a ser alterado nos procedimentos pertinentes ao tratamento de dados pessoais, quando indicado pela autoridade competente, em especial a ANPD por meio de opiniões técnicas ou recomendações, editadas na forma da LGPD.</i></span>

5.12. <span style="color:red"><i>Os contratos e convênios de que trata o § 1º do art. 26 da LGPD deverão ser comunicados à autoridade nacional.</i></span>

## 6. DA EXTINÇÃO CONTRATUAL

6.1. <span style="color:red"><i>A contratação será extinta quando cumpridas as obrigações de ambas as partes, ainda que isso ocorra antes do prazo estipulado para tanto.</i></span>

6.2. <span style="color:red"><i>Se as obrigações não forem cumpridas no prazo estipulado, a vigência ficará prorrogada até a conclusão do objeto, caso em que deverá a Administração providenciar a readequação do cronograma fixado para a contratação.</i></span>

6.3. <span style="color:red"><i>Quando a não conclusão do objeto referida no item anterior decorrer de culpa do Contratado:</i></span>

6.3.1 <span style="color:red"><i>ficará ele constituído em mora, sendo-lhe aplicáveis as respectivas sanções administrativas; e</i></span>

6.3.2 <span style="color:red"><i>poderá a Administração optar pela extinção contratual e, nesse caso, adotará as medidas admitidas em lei para a continuidade da execução contratual</i></span>

<span style="color:red"><b><i>OU</i></b></span>

6.4. <span style="color:red"><i>A contratação será extinta quando vencido o prazo estipulado, independentemente de terem sido cumpridas ou não as obrigações de ambas as partes contraentes.</i></span>

6.5. <span style="color:red"><i>O contrato poderá ser extinto antes do prazo nele fixado, sem ônus para o CONTRATANTE, mediante justificativa formal de que não dispõe de créditos orçamentários para sua continuidade ou de que o contrato não mais lhe oferece vantagem.</i></span>

6.5.1 <span style="color:red"><i>Nesse caso, a extinção antecipada ocorrerá na próxima data de aniversário do contrato, garantido um prazo mínimo de dois meses para ciência formal do contratado, devendo ser observada a regra do art. 183 da Lei nº 14.133, de 2021 para a contagem deste prazo.</i></span>

6.6. <span style="color:red"><i>O contrato poderá ser extinto com fundamento na ausência de créditos orçamentários ou na perda de vantagem contratual antes da data de aniversário, desde que ocorra com ônus para o CONTRATANTE, conforme previsto no art. 138, §2º, da Lei nº 14.133, de 2021.</i></span>

<span style="color:red"><b><i><u>OU</u></i></b></span>

6.7. <span style="color:red"><i>O contrato será extinto quando vencido o prazo nele estipulado, observado o art. 75, inciso VIII, da Lei n.º 14.133/2021, independentemente de terem sido cumpridas ou não as obrigações de ambas as partes contraentes.</i></span>

6.8. A contratação poderá ser extinta antes de cumpridas as obrigações nela estipuladas, ou antes do prazo fixado, por algum dos motivos previstos no artigo 137 da Lei nº 14.133/21, bem como amigavelmente, assegurados o contraditório e a ampla defesa.

6.8.1 Nesta hipótese, aplicam-se também os artigos 138 e 139 da mesma Lei.

6.8.2 A alteração social ou a modificação da finalidade ou da estrutura da empresa não ensejará a extinção se não restringir sua capacidade de concluir o objeto.

6.8.3 Se a operação implicar mudança da pessoa jurídica contratada, deverá ser formalizado termo aditivo para alteração subjetiva.

6.9. O termo de extinção, sempre que possível, será precedido:

6.9.1 Balanço dos eventos contratuais já cumpridos ou parcialmente cumpridos;

6.9.2 Relação dos pagamentos já efetuados e ainda devidos;

6.9.3 Indenizações e multas.

6.10. A extinção contratual não configura óbice para o reconhecimento do desequilíbrio econômico-financeiro, hipótese em que será concedida indenização por meio de termo indenizatório.

6.11. A contratação poderá ser extinta caso se constate que o Contratado mantém vínculo de natureza técnica, comercial, econômica, financeira, trabalhista ou civil com dirigente do órgão ou entidade contratante ou com agente público que tenha desempenhado função na licitação ou na contratação direta, ou atue na fiscalização ou na gestão contratuais, ou que deles seja cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau.

## 7. DOS CASOS OMISSOS

7.1. Os casos omissos serão decididos pelo Contratante, segundo as disposições contidas na Lei nº 14.133, de 2021, e demais normas federais aplicáveis e, subsidiariamente, segundo as disposições contidas na Lei nº 8.078, de 1990 – Código de Defesa do Consumidor – e normas e princípios gerais dos contratos.

## 8. ALTERAÇÕES

8.1. Eventuais alterações contratuais reger-se-ão pela disciplina dos arts. 124 e seguintes da Lei nº 14.133, de 2021.

8.2. O Contratado é obrigado a aceitar, nas mesmas condições contratuais, os acréscimos ou supressões que se fizerem necessários, até o limite de 25% (vinte e cinco por cento) do valor inicial atualizado da contratação e, no caso de reforma de edifício ou de equipamento, o limite para os acréscimos será de 50% (cinquenta por cento).

8.3. As supressões resultantes de acordo celebrado entre as partes contratantes poderão exceder o limite de 25% (vinte e cinco por cento) do valor inicial atualizado do contrato.

8.4. As alterações contratuais deverão ser promovidas mediante celebração de termo aditivo, submetido à prévia aprovação da consultoria jurídica do Contratante, salvo nos casos de justificada necessidade de antecipação de seus efeitos, hipótese em que a formalização do aditivo deverá ocorrer no prazo máximo de 1 (um) mês.

8.5. Registros que não caracterizam alterações contratuais podem ser realizados por simples apostila, dispensada a celebração de termo aditivo, na forma do art. 136 da Lei nº 14.133, de 2021.

## 9. FORO

9.1. Fica definido o Foro da Justiça Federal em <span style="color:red">......</span>, Seção Judiciária de <span style="color:red">......</span> para dirimir os litígios que decorrerem da execução contratual que não puderem ser compostos pela conciliação, conforme art. 92, §1º, da Lei nº 14.133, de 2021.

<b>ANEXO II</b>

<b>TERMO DE CIÊNCIA E CONCORDÂNCIA</b>

Por meio deste instrumento, ..................... <span style="color:red"><i>(identificar o Contratado)</i></span> declara que está ciente e concorda com as disposições e obrigações previstas no <span style="color:red"><i>Edital</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>Aviso de Contratação Direta</i></span>, no Termo de Referência e nos demais anexos a que se refere o <span style="color:red"><i>Pregão/Concorrência/Dispensa Eletrônica</i></span> nº.........../20......., bem como que se responsabiliza, sob as penas da Lei, pela veracidade e legitimidade das informações e documentos apresentados durante o processo de contratação.

Local-UF, <span style="color:red">........</span> de <span style="color:red">...................</span> de 20<span style="color:red">....</span> .

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

(Nome <span style="color:red"><i>e Cargo do Representante Legal</i></span>)
