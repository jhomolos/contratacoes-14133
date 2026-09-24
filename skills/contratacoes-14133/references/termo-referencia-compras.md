# Modelo de Termo de Referência — Aquisições (Compras), Exceto TIC

Fonte: modelo oficial da Advocacia-Geral da União (AGU) para a Lei nº 14.133/2021, versão de dezembro/2025, fornecido pelo usuário. Confirmado (por comparação de hash dos arquivos) que a AGU disponibiliza o mesmo arquivo tanto na seção de licitação quanto na de contratação direta do site — este único modelo cobre **licitação (pregão/concorrência) e contratação direta (dispensa/inexigibilidade)**, com a escolha feita através das alternativas "OU" presentes no próprio texto.

## Quando usar este arquivo

Use este modelo quando o objeto da contratação for **aquisição de bens (compras)** e **não** for Tecnologia da Informação e Comunicação (TIC) — o próprio modelo declara "AQUISIÇÕES, EXCETO TIC" no cabeçalho. Se a contratação for de bens de TIC, este modelo não se aplica; pergunte ao usuário se ele possui o modelo AGU específico para TIC.

## Como preencher

- O texto contém alternativas separadas por "OU". Escolha a alternativa compatível com o caso (licitação vs. contratação direta, com ou sem cota reservada para ME/EPP, com ou sem garantia contratual, características do objeto) e **risque as não escolhidas com `<s>…</s>`, sem apagá-las** (Regra de ouro do `SKILL.md`). O "OU" que separa a alternativa descartada também é riscado. Trechos de realce (turquesa, rosa, azul-petróleo etc.) que não se aplicam ao objeto seguem a mesma regra: riscados, não removidos.
- Substitua todos os campos entre colchetes (ex.: `[INSERIR OBJETO]`, `XX%`, `R$....`) pelo conteúdo do caso, marcado com o código de cores do `SKILL.md` (vermelho; azul só para prazo numérico por extenso), com as informações obtidas do ETP e do DFD já elaborados ou perguntadas diretamente ao usuário.
- Não invente fundamentação legal, percentuais de multa, prazos ou índices de reajuste que o modelo deixa em aberto — pergunte ao usuário ou extraia do ETP.

## Como ler este arquivo: numeração, cores e formatação do modelo

O corpo abaixo da linha horizontal reproduz o `.docx` oficial (`modelos-tr-pregao-conc/modelo-de-termo-de-referencia-compras-lei-no-14-133-dez-25.docx`) com a **numeração automática**, a **hierarquia dos parágrafos**, as **cores de fonte**, os **realces** e o **negrito/itálico/sublinhado** originais, em HTML embutido no Markdown (`<span style="color:red">`, `<span style="background:cyan">`, `<b>`, `<i>`, `<u>`). A conversão foi feita por `scripts/modelo_docx_para_md.py` e conferida contra o Microsoft Word: a numeração de todos os parágrafos é idêntica à exibida no Word. Quando a AGU publicar versão nova, gere este corpo de novo com o mesmo script em vez de editar à mão.

Legenda da própria AGU ("Orientações para uso do modelo – leitura obrigatória"):

| No modelo | Significado |
|---|---|
| Texto preto (sem itálico) | Redação que se espera invariável. **Qualquer alteração exige justificativa nos autos.** |
| <span style="color:red"><i>Vermelho itálico</i></span> | Texto a preencher ou adotar conforme oportunidade e conveniência, de acordo com o objeto. São as previsões "feitas para variar"; inclui as alternativas "OU" e os campos entre colchetes. |
| Realce <span style="background:yellow">amarelo</span> | Alterado em relação à versão anterior do modelo (informativo; não muda a aplicabilidade). |
| Realce <span style="background:cyan">turquesa</span> | Aplicável **exclusivamente ao Sistema de Registro de Preços (SRP)**. Fora de SRP, riscar. |
| Realce <span style="background:lime">verde brilhante</span> | Cláusulas de **margem de preferência** (Decreto nº 11.890/2024). |

As **notas explicativas** do modelo (comentários do Word) estão em `termo-referencia-compras-notas.md`, organizadas pelo número do item. Consulte a nota do item antes de escolher entre alternativas "OU", riscar uma cláusula ou alterar texto preto. Segundo a AGU, notas explicativas e realces são removidos só na **versão final**: na minuta que vai à análise jurídica, mantenha-os.

**Ao produzir o TR**, siga a seção "Regra de ouro" do `SKILL.md`: mantenha a numeração, a hierarquia, as cores, os realces e a formatação do modelo, e aplique por cima o código de alterações do IPP (vermelho = inclusão, verde = ajuste de redação, azul = só prazo numérico escrito por extenso, `<s>` = supressão).

## Orientações do IPP da AGU para o TR

Detalhamento completo em `references/ipp-agu-orientacoes.md`, seção "Termo de Referência". Pontos decisivos:

- **Prazo de vigência não é número arbitrário**: deve decorrer da **soma** dos prazos de execução, de substituição ou reparo (quando necessários), recebimento provisório, recebimento definitivo e pagamento.
- **Garantia do produto ≠ garantia de execução do contrato**: a primeira (CDC ou convencional) relaciona-se à higidez e qualidade do bem fornecido; a segunda (arts. 96 a 102) assegura a regular execução do contrato. São campos distintos, e dispensar uma não afeta a outra.
- **Especificações vedadas**: as excessivas, irrelevantes ou desnecessárias que limitem a competitividade ou direcionem a contratação; as que não representem a real demanda de desempenho do órgão; e as defasadas tecnológica ou metodologicamente. Toda especificação restritiva exige justificativa de pertinência.
- **Catálogo Eletrônico de Padronização**: especificar preferencialmente conforme o catálogo disponível no PNCP; não o utilizando, justifique.
- **Habilitação**: os critérios devem ser justificados nos autos, analisando qualificação econômico-financeira e técnica **à luz dos riscos da contratação** — não por praxe. Fixar **preços máximos aceitáveis globais e unitários**.
- **Contratação direta**: identificar a forma (dispensa ou inexigibilidade) com os **fundamentos de fato e de direito**, e observar o regime de pesquisa de preços do art. 7º da IN SEGES/ME nº 65/2021.
- **Mapa de Riscos**: deve ser atualizado e juntado **ao final da elaboração do TR**.
- **Divulgação**: o TR vai ao **PNCP na mesma data** da divulgação do edital ou do aviso de contratação direta (art. 12 da IN SEGES/ME nº 81/2022); o Compras.gov.br faz isso automaticamente.
- **Registre a data de extração deste modelo**: ela é exigida na **Declaração de utilização de modelos AGU/MGI** que instrui o processo.

---

<b>MODELO DE TERMO DE REFERÊNCIA<br>Lei nº 14.133, de 1º de abril de 2021<br>AQUISIÇÕES, EXCETO TIC</b>

<b>LICITAÇÃO E CONTRATAÇÃO DIRETA</b>

<span style="color:red"><b><i>ÓRGÃO OU ENTIDADE PÚBLICA</i></b></span>

(Processo Administrativo n° <span style="color:red"><i>xxxxx</i></span>.<span style="color:red"><i>xxxxxx</i></span>/<span style="color:red"><i>xxxx</i></span>-<span style="color:red"><i>xx</i></span>)

<b>TERMO DE REFERÊNCIA</b>

## 1. CONDIÇÕES GERAIS DA CONTRATAÇÃO

1.1. Aquisição de <span style="color:red"><i>[</i></span><span style="color:red"><b><i>INSERIR OBJETO</i></b></span><span style="color:red"><i>]</i></span><span style="color:red">,</span> <span style="color:red"><i>[incluindo instalação, montagem INCLUIR ATIVIDADES],</i></span> nos termos da tabela abaixo, conforme condições e exigências estabelecidas neste instrumento.

| <b>ITEM</b> | <b>ESPECIFICAÇÃO</b> | <b>CATMAT</b> | <b>UNIDADE DE MEDIDA</b> | <b>QUANTIDADE</b> | <b>VALOR UNITÁRIO</b> | <b>VALOR TOTAL</b> |
|---|---|---|---|---|---|---|
| <b>1</b> |  |  |  |  | <span style="color:red">R$ .... OU SIGILOSO</span> | <span style="color:red">R$ .... OU SIGILOSO</span> |
| <b>2</b> | <span style="color:red"><i>Idem ao Item 1 – Cota reservada para ME/EPP em XX,XX% (ver nota explicativa)</i></span> |  |  |  |  |  |
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

1.2. <span style="color:red"><i>Os bens objeto desta contratação são caracterizados como comuns, conforme justificativa constante do Estudo Técnico Preliminar.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.3. <span style="color:red"><i>Os bens objeto desta contratação são caracterizados como</i></span> <span style="color:red"><b><i>especiais</i></b></span><span style="color:red"><i>, conforme justificativa constante do Estudo Técnico Preliminar.</i></span>

1.4. <span style="color:red"><i>O objeto desta contratação não se enquadra como bem de luxo, conforme Decreto nº 10.818, de 27 de setembro de 2021.</i></span>

1.5. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, na forma do artigo 105 da Lei n° 14.133, de 2021.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.6. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo, limitado a 5 anos]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, prorrogável por até 10 anos, na forma dos artigos 106 e 107 da Lei n° 14.133, de 2021.</i></span>

1.7. <span style="color:red"><i>1.6.1 O fornecimento de bens é enquadrado como continuado tendo em vista que [...], sendo a vigência plurianual mais vantajosa considerando [...]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[o Estudo Técnico Preliminar]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[os termos da Nota Técnica .../...];</i></span>

<span style="color:red"><b><i>OU</i></b></span>

1.8. <span style="color:red"><i>O prazo de vigência da contratação é de</i></span> <span style="color:red"><b><i>[indicar o prazo, limitado a um ano da ocorrência da emergência ou calamidade]</i></b></span> <span style="color:red"><i>contados do(a)</i></span> <span style="color:red"><b><i>[indicar o termo inicial da vigência]</i></b></span><span style="color:red"><i>, improrrogável, na forma do art. 75, inciso VIII, da Lei n° 14.133/2021.</i></span>

1.9. O contrato ou outro instrumento hábil que o substitua oferece maior detalhamento das regras que serão aplicadas em relação à vigência da contratação.

## 2. FUNDAMENTAÇÃO E DESCRIÇÃO DA NECESSIDADE DA CONTRATAÇÃO

2.1. A Fundamentação da Contratação e de seus quantitativos encontra-se pormenorizada em tópico específico dos Estudos Técnicos Preliminares, apêndice deste Termo de Referência.

2.2. <span style="color:red"><i>O objeto da contratação está previsto no Plano de Contratações Anual [</i></span><span style="color:red"><b><i>ANO</i></b></span><span style="color:red"><i>], conforme detalhamento a seguir:</i></span>

I) <span style="color:red"><i>ID PCA no PNCP: [...];</i></span>

II) <span style="color:red"><i>Data de publicação no PNCP: [...];</i></span>

III) <span style="color:red"><i>Id do item no PCA: [...];</i></span>

IV) <span style="color:red"><i>Classe/Grupo: [...];</i></span>

V) <span style="color:red"><i>Identificador da Futura Contratação: [...];</i></span>

<span style="color:red"><b><i>OU</i></b></span>

2.3. <span style="color:red"><i>O objeto da contratação está previsto no Plano de Contratações Anual [</i></span><span style="color:red"><b><i>ANO</i></b></span><span style="color:red"><i>], conforme consta das informações básicas desse Termo de Referência.</i></span>

## 3. DESCRIÇÃO DA SOLUÇÃO COMO UM TODO CONSIDERADO O CICLO DE VIDA DO OBJETO E ESPECIFICAÇÃO DO PRODUTO

3.1. A descrição da solução como um todo encontra-se pormenorizada em tópico específico dos Estudos Técnicos Preliminares, apêndice deste Termo de Referência.

## 4. REQUISITOS DA CONTRATAÇÃO

### <span style="color:red"><b><i>Sustentabilidade</i></b></span>

4.1. <span style="color:red"><i>Além dos critérios de sustentabilidade eventualmente inseridos na descrição do objeto, devem ser atendidos os seguintes requisitos, que se baseiam no Guia Nacional de Contratações Sustentáveis:</i></span>

4.1.1 <span style="color:red"><i>[...];</i></span>

4.1.2 <span style="color:red"><i>[...]; e</i></span>

4.1.3 <span style="color:red"><i>[...].</i></span>

### <span style="color:red"><b><i>Indicação de marcas ou modelos</i></b></span>

4.2. <span style="color:red"><i>Na presente contratação será admitida a indicação da(s) seguinte(s) marca(s), característica(s) ou modelo(s), de acordo com as justificativas contidas nos Estudos Técnicos Preliminares: (...).</i></span>

### <span style="color:red"><b><i>Da vedação de contratação de marca ou produto</i></b></span>

4.3. <span style="color:red"><i>Diante das conclusões extraídas do processo administrativo nº</i></span> <span style="color:red"><b><i>xxxxx.xxxxxx/xxxx-xx</i></b></span><span style="color:red"><i>, a Administração não aceitará o fornecimento dos seguintes produtos/marcas:</i></span>

4.3.1.1. <span style="color:red"><i>[...]</i></span>

4.3.1.2. <span style="color:red"><i>[...]</i></span>

### <span style="color:red"><b><i>Da exigência de amostra</i></b></span>

4.4. <span style="color:red"><i>Havendo o aceite da proposta quanto ao valor, o interessado classificado provisoriamente em primeiro lugar deverá apresentar amostra, que terá data, local e horário de sua realização divulgados por mensagem no sistema, cuja presença será facultada a todos os interessados, incluindo os demais fornecedores interessados.</i></span>

4.5. <span style="color:red"><i>Serão exigidas amostras dos seguintes itens:</i></span>

4.5.1 <span style="color:red"><i>[...];</i></span>

4.5.2 <span style="color:red"><i>[...]; e</i></span>

4.5.3 <span style="color:red"><i>[...].</i></span>

4.6. <span style="color:red"><i>As amostras poderão ser entregues no endereço [</i></span><span style="color:red"><b><i>indicar o endereço</i></b></span><span style="color:red"><i>]</i></span><span style="color:red;background:lime"><i>,</i></span> <span style="color:red"><i>no prazo limite de [</i></span><span style="color:red"><b><i>indicar o prazo</i></b></span><span style="color:red"><i>], sendo que a empresa assume total responsabilidade pelo envio e por eventual atraso na entrega.</i></span>

4.7. <span style="color:red"><i>É facultada prorrogação o prazo estabelecido, a partir de solicitação fundamentada no chat pelo interessado, antes de findo o prazo.</i></span>

4.8. <span style="color:red"><i>No caso de não haver entrega da amostra ou ocorrer atraso na entrega, sem justificativa aceita, ou havendo entrega de amostra fora das especificações previstas, a proposta será recusada.</i></span>

4.9. <span style="color:red"><i>Serão avaliados os seguintes aspectos e padrões mínimos de aceitabilidade:</i></span>

4.9.1 <span style="color:red"><i>Itens (....): ...........;</i></span>

4.9.2 <span style="color:red"><i>Itens (....): ............</i></span>

4.10. <span style="color:red"><i>Os resultados das avaliações serão divulgados por meio de mensagem no sistema.</i></span>

4.11. <span style="color:red"><i>Se a(s) amostra(s) apresentada(s) pelo primeiro classificado não for(em) aceita(s), será analisada a aceitabilidade da proposta ou lance ofertado pelo segundo classificado. Seguir-se-á com a verificação da(s) amostra(s) e, assim, sucessivamente, até a verificação de uma que atenda às especificações constantes neste Termo de Referência.</i></span>

4.12. <span style="color:red"><i>Os exemplares colocados à disposição da Administração serão tratados como protótipos, podendo ser manuseados e desmontados pela equipe técnica responsável pela análise, não gerando direito a ressarcimento.</i></span>

4.13. <span style="color:red"><i>Após a divulgação do resultado final do certame, as amostras entregues deverão ser recolhidas pelos fornecedores no prazo de</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) dias, após o qual poderão ser descartadas pela Administração, sem direito a ressarcimento.</i></span>

4.14. <span style="color:red"><i>Os interessados deverão colocar à disposição da Administração todas as condições indispensáveis à realização de testes e fornecer, sem ônus, os manuais impressos em língua portuguesa, necessários ao seu perfeito manuseio, quando for o caso.</i></span>

### <span style="color:red"><b><i>Da exigência de carta de solidariedade</i></b></span>

4.15. <span style="color:red"><i>Em caso de fornecedor, revendedor ou distribuidor, será exigida</i></span> <span style="color:red;background:yellow"><i>do licitante/interessado provisoriamente classificado em primeiro lugar, nos termos do edital ou do aviso de contratação direta,</i></span> <span style="color:red"><i>carta de solidariedade emitida pelo fabricante, que assegure a execução do contrato.</i></span>

### <b>Subcontratação</b>

4.16. <span style="color:red"><i>Não será admitida a subcontratação do objeto contratual.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.17. <span style="color:red"><i>É permitida a subcontratação parcial do objeto, até o limite de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor total do contrato, nas seguintes condições:</i></span>

4.18. <span style="color:red"><i>É vedada a subcontratação completa ou da parcela principal da obrigação, abaixo discriminada:</i></span>

4.18.1 <span style="color:red"><i>[...];</i></span>

4.18.2 <span style="color:red"><i>[...]; e</i></span>

4.18.3 <span style="color:red"><i>[...].</i></span>

4.19. <span style="color:red"><i>Poderão ser subcontratadas as seguintes parcelas do objeto:</i></span>

4.19.1 <span style="color:red"><i>[...];</i></span>

4.19.2 <span style="color:red"><i>[...]; e</i></span>

4.19.3 <span style="color:red"><i>[...].</i></span>

4.20. <span style="color:red"><i>Em qualquer hipótese de subcontratação, permanece a responsabilidade integral do Contratado pela perfeita execução contratual, cabendo-lhe realizar a supervisão e coordenação das atividades do subcontratado, bem como responder perante o Contratante pelo rigoroso cumprimento das obrigações contratuais correspondentes ao objeto da subcontratação.</i></span>

4.21. <span style="color:red"><i>A subcontratação depende de autorização prévia do Contratante, a quem incumbe avaliar se o subcontratado cumpre os requisitos de qualificação técnica necessários para a execução do objeto.</i></span>

4.22. <span style="color:red"><i>O Contratado apresentará à Administração documentação que comprove a capacidade técnica do subcontratado, que será avaliada e juntada aos autos do processo correspondente.</i></span>

4.23. <span style="color:red"><i>É vedada a subcontratação de pessoa física ou jurídica, se aquela ou os dirigentes desta mantiverem vínculo de natureza técnica, comercial, econômica, financeira, trabalhista ou civil com dirigente do órgão ou entidade contratante ou com agente público que desempenhe função na contratação ou atue na fiscalização ou na gestão do contrato, ou se deles forem cônjuge, companheiro ou parente em linha reta, colateral, ou por afinidade, até o terceiro grau.</i></span>

### <b>Garantia da contratação</b>

4.24. <span style="color:red"><i>Não haverá exigência da garantia da contratação dos art. 96 e seguintes da Lei nº 14.133, de 2021, pelas razões constantes do Estudo Técnico Preliminar.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

4.25. <span style="color:red"><i>Será exigida a garantia da contratação de que tratam os arts. 96 e seguintes da Lei nº 14.133, de 2021, com validade durante a execução do contrato e 90 (noventa) dias após término da vigência contratual, podendo o Contratado optar pela caução em dinheiro ou em títulos da dívida pública, seguro-garantia, fiança bancária ou título de capitalização, em valor correspondente a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor</i></span> <span style="color:red"><b><i>[total]</i></b></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><b><i>[anual]</i></b></span> <span style="color:red"><i>da contratação.</i></span>

4.26. <span style="color:red"><i>Em caso de opção pelo seguro-garantia, a parte adjudicatária deverá apresentá-la, no máximo, até a data de assinatura do contrato.</i></span>

4.26.1 <span style="color:red"><i>A apólice de seguro-garantia permanecerá em vigor mesmo que o Contratado não pague o prêmio nas datas convencionadas.</i></span>

4.26.2 <span style="color:red"><i>Caso o adjudicatário não apresente a apólice de seguro de garantia antes da assinatura do contrato, ocorrerá a preclusão do direito de escolha dessa modalidade de garantia.</i></span>

4.26.3 <span style="color:red"><i>A apólice de seguro-garantia deverá acompanhar as modificações referentes à vigência do contrato principal mediante a emissão do respectivo endosso pela seguradora.</i></span>

4.26.4 <span style="color:red"><i>Será permitida a substituição da apólice de seguro-garantia na data de renovação ou de aniversário, desde que mantidas as condições e coberturas da apólice vigente e nenhum período fique descoberto, ressalvados os períodos de suspensão contratual.</i></span>

4.26.5 <span style="color:red"><i>Caso o adjudicatário não opte pelo seguro-garantia ou não apresente a apólice de seguro de garantia antes da assinatura do contrato, deverá apresentar, no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, a critério do Contratante, contado da assinatura do contrato, comprovante de prestação de garantia nas modalidades de caução em dinheiro ou títulos da dívida pública, fiança bancária ou títulos de capitalização.</i></span>

4.27. <span style="color:red"><i>Caso seja a garantia em dinheiro a modalidade de garantia escolhida pelo Contratado, deverá ser efetuada em favor do Contratante, em conta específica na Caixa Econômica Federal, com correção monetária.</i></span>

4.28. <span style="color:red"><i>Caso a opção seja por utilizar títulos da dívida pública, estes devem ter sido emitidos sob a forma escritural, mediante registro em sistema centralizado de liquidação e de custódia autorizado pelo Banco Central do Brasil, e avaliados pelos seus valores econômicos, conforme definido pelo Ministério competente.</i></span>

4.29. <span style="color:red"><i>No caso de garantia na modalidade de fiança bancária, deverá ser emitida por banco ou instituição financeira devidamente autorizada a operar no País pelo Banco Central do Brasil, e deverá constar expressa renúncia do fiador aos benefícios do artigo 827 do Código Civil.</i></span>

4.30. <span style="color:red"><i>Na hipótese de opção pelo título de capitalização, a garantia deverá ser custeada por pagamento único, com resgate pelo valor total, sob a modalidade de instrumento de garantia, emitido por sociedades de capitalização regulamente constituídas e autorizadas pelo Governo Federal.</i></span>

4.30.1 <span style="color:red"><i>O título de capitalização deverá ser apresentado ao Contratante juntamente com as condições gerais e o número do processo administrativo sob o qual o plano de capitalização foi aprovado pela Susep (art. 8º, III, da Circular SUSEP nº 656, de 11 de março de 2022).</i></span>

4.31. <span style="color:red"><i>A garantia assegurará, qualquer que seja a modalidade escolhida, sob pena de não aceitação, o pagamento de:</i></span>

4.31.1 <span style="color:red"><i>prejuízos advindos do não cumprimento do objeto do contrato e do não adimplemento das demais obrigações nele previstas; e</i></span>

4.31.2 <span style="color:red"><i>multas moratórias e punitivas aplicadas pela Administração ao Contratado.</i></span>

4.32. <span style="color:red"><i>No caso de alteração do valor do contrato, ou prorrogação de sua vigência, a garantia deverá ser ajustada ou renovada, no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, contado da data de assinatura do termo aditivo ou da emissão do apostilamento, seguindo os mesmos parâmetros utilizados quando da contratação.</i></span>

4.33. <span style="color:red"><i>Na hipótese de suspensão do contrato por ordem ou inadimplemento da Administração, o Contratado ficará desobrigado de renovar a garantia ou de endossar a apólice de seguro até a ordem de reinício da execução ou o adimplemento pela Administração.</i></span>

4.34. <span style="color:red"><i>Se o valor da garantia for utilizado total ou parcialmente em pagamento de qualquer obrigação, o Contratado obriga-se a fazer a respectiva reposição no prazo máximo de 10 (dez) dias úteis, prorrogáveis por igual período, a critério do Contratante, contados da data em que for notificada.</i></span>

4.35. <span style="color:red"><i>O Contratante executará a garantia na forma prevista na legislação que rege a matéria.</i></span>

4.35.1 <span style="color:red"><i>O emitente da garantia ofertada pelo Contratado deverá ser notificado pelo Contratante quanto ao início de processo administrativo para apuração de descumprimento de cláusulas contratuais.</i></span>

4.35.2 <span style="color:red"><i>Caso se trate da modalidade seguro-garantia, ocorrido o sinistro durante a vigência da apólice, sua caracterização e comunicação poderão ocorrer fora desta vigência, não caracterizando fato que justifique a negativa do sinistro, desde que respeitados os prazos prescricionais aplicados ao contrato de seguro, nos termos do art. 20 da Circular Susep n° 662, de 11 de abril de 2022.</i></span>

4.36. <span style="color:red"><i>Extinguir-se-á a garantia com a restituição da carta fiança, autorização para a liberação de importâncias depositadas em dinheiro a título de garantia ou anuência ao resgate do título de capitalização, acompanhada de declaração do Contratante, mediante termo circunstanciado, de que o Contratado cumpriu todas as cláusulas do contrato.</i></span>

4.36.1 <span style="color:red"><i>A extinção da garantia na modalidade seguro-garantia observará a regulamentação da Susep.</i></span>

4.36.2 <span style="color:red"><i>A Administração deverá apurar se há alguma pendência contratual antes do término da vigência da apólice.</i></span>

4.37. <span style="color:red"><i>A garantia somente será liberada ou restituída após a fiel execução do contrato ou após a sua extinção por culpa exclusiva da Administração e, quando em dinheiro, será atualizada monetariamente.</i></span>

4.38. <span style="color:red"><i>O Contratado autoriza o Contratante a reter, a qualquer tempo, a garantia, na forma prevista neste Termo de Referência.</i></span>

4.39. <span style="color:red"><i>O garantidor não é parte para figurar em processo administrativo instaurado pelo Contratante com o objetivo de apurar prejuízos e/ou aplicar sanções ao Contratado.</i></span>

4.40. <span style="color:red"><i>A garantia de execução é independente de eventual garantia do produto ou serviço prevista neste Termo de Referência.</i></span>

<b>Reserva de cotas para microempresas e empresas de pequeno porte:</b>

4.41. <span style="color:red"><i>Na presente licitação, será realizada a reserva de cota de até vinte e cinco por cento do objeto para a contratação de microempresas e empresas de pequeno porte.</i></span>

4.41.1 <span style="color:red"><i>Na hipótese de não haver vencedor para a cota reservada, esta poderá ser adjudicada ao vencedor da cota principal ou, diante de sua recusa, aos fornecedores remanescentes, desde que pratiquem o preço do primeiro colocado da cota principal.</i></span>

4.41.2 <span style="color:red"><i>Se a mesma empresa vencer a cota reservada e a cota principal, a contratação das cotas deverá ocorrer pelo menor preço.</i></span>

4.41.3 <span style="color:red"><i>Será dada a prioridade de aquisição aos produtos das cotas reservadas quando forem adjudicados aos licitantes qualificados como microempresas ou empresas de pequeno porte, ressalvados os casos em que a cota reservada for inadequada para atender as quantidades ou as condições do pedido, conforme vier a ser decidido pela Administração, nos termos do art. 8º, §4º, do Decreto n. 8.538, de 2015.</i></span>

### <b>Margem de Preferência:</b>

4.42. <span style="color:red"><i>O objeto da contratação enquadra-se na margem de preferência .............</i></span> <span style="color:red"><b><i>[normal]</i></b></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><b><i>[adicional]</i></b></span> <span style="color:red"><i>de ........ %, prevista no Decreto n.º....................., conforme disposto na Resolução n.º ......................... da Comissão Interministerial de Contratações Públicas para o Desenvolvimento Sustentável – CICS, por se tratar de ................</i></span> <span style="color:red"><b><i>[bens manufaturados nacionais que atendam a normas técnicas brasileiras]</i></b></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><b><i>[bens reciclados, recicláveis ou biodegradáveis].</i></b></span>

## 5. MODELO DE EXECUÇÃO DO OBJETO

### <b>Condições de Entrega</b>

5.1. <span style="color:red"><i>O prazo de entrega dos bens é de ......... dias, contados do(a) ................................, em remessa única.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

5.2. <span style="color:red"><i>As parcelas serão entregues nos seguintes prazos e condições:</i></span>

| <span style="color:red">Parcela</span> | <span style="color:red">Composição da parcela</span> | <span style="color:red">Prazo de entrega</span> |
|---|---|---|
| <span style="color:red">1ª</span> | <span style="color:red">... unidades do item ..., ... unidades do item ...</span> | <i>... dias da Assinatura/da Ordem de Fornecimento/[...]</i> |
| <span style="color:red">2ª</span> | <span style="color:red">... unidades do item ..., ... unidades do item ...</span> | <i>... dias da Assinatura/da Ordem de Fornecimento/[...]</i> |
| <span style="color:red">3ª</span> | <span style="color:red">... unidades do item ..., ... unidades do item ...</span> | <i>... dias da Assinatura/da Ordem de Fornecimento/[...]</i> |
| <span style="color:red">[...]</span> | <span style="color:red">... unidades do item ..., ... unidades do item ...</span> | <i>... dias da Assinatura/da Ordem de Fornecimento/[...]</i> |

5.3. <span style="color:red"><i>Caso não seja possível a entrega na data assinalada, a empresa deverá comunicar as razões respectivas com pelo menos (...) dias de antecedência para que qualquer pleito de prorrogação de prazo seja analisado, ressalvadas situações de caso fortuito e força maior.</i></span>

5.4. <span style="color:red"><i>Os bens deverão ser entregues no seguinte endereço [...]</i></span>

5.4.1 <span style="color:red"><i>No caso de produtos perecíveis, o prazo de validade na data da entrega não poderá ser inferior a ...... (......) (dias ou meses ou anos), ou a (metade, um terço, dois terços etc.) do prazo total recomendado pelo fabricante.</i></span>

### <b>Garantia, manutenção e assistência técnica</b>

5.5. <span style="color:red"><i>O prazo de garantia é aquele estabelecido na Lei nº 8.078, de 11 de setembro de 1990 (Código de Defesa do Consumidor)</i></span>

<span style="color:red"><b><i>OU</i></b></span>

5.6. <span style="color:red"><i>O prazo de garantia contratual dos bens, complementar à garantia legal, será de, no mínimo, \_\_\_ (\_\_\_\_) meses, ou pelo prazo fornecido pelo fabricante, se superior, contado a partir do primeiro dia útil subsequente à data do recebimento definitivo do objeto.</i></span>

5.7. <span style="color:red"><i>Caso o prazo da garantia oferecida pelo fabricante seja inferior ao estabelecido nesta cláusula, o fornecedor deverá complementar a garantia do bem ofertado pelo período restante.</i></span>

5.8. <span style="color:red"><i>A garantia será prestada com vistas a manter os equipamentos fornecidos em perfeitas condições de uso, sem qualquer ônus ou custo adicional para o Contratante.</i></span>

5.9. <span style="color:red"><i>A garantia abrange a realização da manutenção corretiva dos bens pelo próprio Contratado, ou, se for o caso, por meio de assistência técnica autorizada, de acordo com as normas técnicas específicas.</i></span>

5.10. <span style="color:red"><i>Entende-se por manutenção corretiva aquela destinada a corrigir os defeitos apresentados pelos bens, compreendendo a substituição de peças, a realização de ajustes, reparos e correções necessárias.</i></span>

5.11. <span style="color:red"><i>As peças que apresentarem vício ou defeito no período de vigência da garantia deverão ser substituídas por outras novas, de primeiro uso, e originais, que apresentem padrões de qualidade e desempenho iguais ou superiores aos das peças utilizadas na fabricação do equipamento.</i></span>

5.12. <span style="color:red;background:yellow"><i>Uma vez notificado, o Contratado realizará a reparação ou substituição dos bens que apresentarem vício ou defeito no prazo de até</i></span> <span style="color:red;background:yellow"><b><i>XX</i></b></span> <span style="color:red;background:yellow"><i>(</i></span><span style="color:red;background:yellow"><b><i>xxxxx</i></b></span><span style="color:red;background:yellow"><i>) dias úteis, já incluído nesse prazo o tempo necessário para eventual retirada e devolução do bem, a cargo do Contratado.</i></span>

5.13. <span style="color:red"><i>O prazo indicado no subitem anterior, durante seu transcurso, poderá ser prorrogado uma única vez, por igual período, mediante solicitação escrita e justificada do Contratado, aceita pelo Contratante.</i></span>

5.14. <span style="color:red"><i>Na hipótese do subitem acima, o Contratado deverá disponibilizar equipamento equivalente, de especificação igual ou superior ao anteriormente fornecido, para utilização em caráter provisório pelo Contratante, de modo a garantir a continuidade dos trabalhos administrativos durante a execução dos reparos.</i></span>

5.15. <span style="color:red"><i>Decorrido o prazo para reparos e substituições sem o atendimento da solicitação do Contratante ou a apresentação de justificativas pelo Contratado, fica o Contratante autorizado a contratar empresa diversa para executar os reparos, ajustes ou a substituição do bem ou de seus componentes, bem como a exigir do Contratado o reembolso pelos custos respectivos, sem que tal fato acarrete a perda da garantia dos equipamentos.</i></span>

5.16. <span style="color:red"><i>O custo referente ao transporte dos equipamentos cobertos pela garantia será de responsabilidade do Contratado.</i></span>

5.17. <span style="color:red"><i>A garantia legal ou contratual do objeto tem prazo de vigência próprio e desvinculado daquele fixado no contrato, permitindo eventual aplicação de penalidades em caso de descumprimento de alguma de suas condições, mesmo depois de expirada a vigência contratual.</i></span>

## 6. MODELO DE GESTÃO DO CONTRATO

6.1. O contrato deverá ser executado fielmente pelas partes, de acordo com as cláusulas avençadas e as normas da Lei nº 14.133, de 2021, e cada parte responderá pelas consequências de sua inexecução total ou parcial.

6.2. Em caso de impedimento, ordem de paralisação ou suspensão do contrato, o cronograma de execução será prorrogado automaticamente pelo tempo correspondente, anotadas tais circunstâncias mediante simples apostila.

6.3. As comunicações entre o órgão ou entidade e a contratada devem ser realizadas por escrito sempre que o ato exigir tal formalidade, admitindo-se o uso de mensagem eletrônica para esse fim.

6.4. O órgão ou entidade poderá convocar representante da empresa para adoção de providências que devam ser cumpridas de imediato.

6.5. <span style="color:red"><i>Após a assinatura do contrato ou instrumento equivalente, o órgão ou entidade poderá convocar o representante da empresa contratada para reunião inicial para apresentação do plano de fiscalização, que conterá informações acerca das obrigações contratuais, dos mecanismos de fiscalização, das estratégias para execução do objeto, do plano complementar de execução da contratada, quando houver, do método de aferição dos resultados e das sanções aplicáveis, dentre outros.</i></span>

### <b>Fiscalização</b>

6.6. A execução do contrato deverá ser acompanhada e fiscalizada pelo(s) fiscal(is) do contrato, ou pelos respectivos substitutos.

### <b>Fiscalização Técnica</b>

6.7. O fiscal técnico do contrato acompanhará a execução do contrato, para que sejam cumpridas todas as condições estabelecidas no contrato, de modo a assegurar os melhores resultados para a Administração.

6.8. O fiscal técnico do contrato anotará no histórico de gerenciamento do contrato todas as ocorrências relacionadas à execução do contrato, com a descrição do que for necessário para a regularização das faltas ou dos defeitos observados.

6.9. Identificada qualquer inexatidão ou irregularidade, o fiscal técnico do contrato emitirá notificações para a correção da execução do contrato, determinando prazo para a correção.

6.10. O fiscal técnico do contrato informará ao gestor do contato, em tempo hábil, a situação que demandar decisão ou adoção de medidas que ultrapassem sua competência, para que adote as medidas necessárias e saneadoras, se for o caso.

6.11. No caso de ocorrências que possam inviabilizar a execução do contrato nas datas aprazadas, o fiscal técnico do contrato comunicará o fato imediatamente ao gestor do contrato.

6.12. O fiscal técnico do contrato comunicará ao gestor do contrato, em tempo hábil, o término do contrato sob sua responsabilidade, com vistas à renovação tempestiva ou à prorrogação contratual.

### <b>Fiscalização Administrativa</b>

6.13. O fiscal administrativo do contrato verificará a manutenção das condições de habilitação da contratada, acompanhará o empenho, o pagamento, as garantias, as glosas e a formalização de apostilamento e termos aditivos, solicitando quaisquer documentos comprobatórios pertinentes, caso necessário.

6.14. Caso ocorra descumprimento das obrigações contratuais, o fiscal administrativo do contrato atuará tempestivamente na solução do problema, reportando ao gestor do contrato para que tome as providências cabíveis, quando ultrapassar a sua competência.

6.15. <span style="color:red"><i>Além do disposto acima, a fiscalização contratual obedecerá às seguintes rotinas:</i></span>

6.15.1 <span style="color:red"><i>[...];</i></span>

6.15.2 <span style="color:red"><i>[...]; e</i></span>

6.15.3 <span style="color:red"><i>[...].</i></span>

6.16. A fiscalização de que trata esta cláusula não exclui nem reduz a responsabilidade do Contratado, inclusive perante terceiros, por qualquer irregularidade, ainda que resultante de imperfeições técnicas, vícios redibitórios, ou emprego de material inadequado ou de qualidade inferior e, na ocorrência desta, não implica corresponsabilidade da Contratante ou de seus agentes, gestores e fiscais, de conformidade.

### <b>Gestor do Contrato</b>

6.17. Cabe ao gestor do contrato:

6.17.1 coordenar a atualização do processo de acompanhamento e fiscalização do contrato contendo todos os registros formais da execução no histórico de gerenciamento do contrato, a exemplo da ordem de serviço, do registro de ocorrências, das alterações e das prorrogações contratuais, elaborando relatório com vistas à verificação da necessidade de adequações do contrato para fins de atendimento da finalidade da administração.

6.17.2 acompanhar os registros realizados pelos fiscais do contrato, de todas as ocorrências relacionadas à execução do contrato e as medidas adotadas, informando, se for o caso, à autoridade superior àquelas que ultrapassarem a sua competência.

6.17.3 acompanhar a manutenção das condições de habilitação da contratada, para fins de empenho de despesa e pagamento, e anotará os problemas que obstem o fluxo normal da liquidação e do pagamento da despesa no relatório de riscos eventuais.

6.17.4 emitir documento comprobatório da avaliação realizada pelos fiscais técnico, administrativo e setorial quanto ao cumprimento de obrigações assumidas pelo Contratado, com menção ao seu desempenho na execução contratual, baseado nos indicadores objetivamente definidos e aferidos, e a eventuais penalidades aplicadas, devendo constar do cadastro de atesto de cumprimento de obrigações.

6.17.5 tomar providências para a formalização de processo administrativo de responsabilização para fins de aplicação de sanções, a ser conduzido pela comissão de que trata o art. 158 da Lei nº 14.133, de 2021, ou pelo agente ou pelo setor com competência para tal, conforme o caso.

6.17.6 elaborar relatório final com informações sobre a consecução dos objetivos que tenham justificado a contratação e eventuais condutas a serem adotadas para o aprimoramento das atividades da Administração.

6.17.7 enviar a documentação pertinente ao setor de contratos para a formalização dos procedimentos de liquidação e pagamento, no valor dimensionado pela fiscalização e gestão nos termos do contrato.

## 7. INFRAÇÕES E SANÇÕES ADMINISTRATIVAS

7.1. Comete infração administrativa, nos termos da Lei nº 14.133, de 2021, o Contratado que:

a) der causa à inexecução parcial do contrato;

b) der causa à inexecução parcial do contrato que cause grave dano à Administração ou ao funcionamento dos serviços públicos ou ao interesse coletivo;

c) der causa à inexecução total do contrato;

d) ensejar o retardamento da execução ou da entrega do objeto da contratação sem motivo justificado;

e) apresentar documentação falsa ou prestar declaração falsa durante a execução do contrato;

f) praticar ato fraudulento na execução do contrato;

g) comportar-se de modo inidôneo ou cometer fraude de qualquer natureza;

h) praticar ato lesivo previsto no art. 5º da Lei nº 12.846, de 1º de agosto de 2013.

7.2. Serão aplicadas ao Contratado que incorrer nas infrações acima descritas as seguintes sanções:

7.2.1 Advertência, quando o Contratado der causa à inexecução parcial do contrato, sempre que não se justificar a imposição de penalidade mais grave;

7.2.2 Impedimento de licitar e contratar, quando praticadas as condutas descritas nas alíneas “b”, “c” e “d” do subitem acima, sempre que não se justificar a imposição de penalidade mais grave;

7.2.3 Declaração de inidoneidade para licitar e contratar, quando praticadas as condutas descritas nas alíneas “e”, “f”, “g” e “h” do subitem acima, bem como nas alíneas “b”, “c” e “d”, que justifiquem a imposição de penalidade mais grave.

7.2.4 Multa:

7.2.4.1. <span style="color:red"><i>Moratória, para as infrações descritas no item “d”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) por dia de atraso injustificado sobre o valor da parcela inadimplida, até o limite de</i></span> <span style="color:red"><b><i>XX</i></b></span> <span style="color:red"><i>(</i></span><span style="color:red"><b><i>xxxxx</i></b></span><span style="color:red"><i>) dias</i></span>

7.2.4.2. <span style="color:red"><i>Moratória de 0,07% (sete centésimos por cento) por dia de atraso injustificado sobre o valor total do contrato, até o máximo de 2% (dois por cento), pela inobservância do prazo fixado para apresentação, suplementação ou reposição da garantia;</i></span>

7.2.4.2.1 <span style="color:red"><i>O atraso superior a 25 (vinte e cinco) dias para apresentação, suplementação ou reposição da garantia autoriza a Administração a promover a extinção do contrato por descumprimento ou cumprimento irregular de suas cláusulas, conforme dispõe o inciso I do art. 137 da Lei n. 14.133, de 2021.</i></span>

7.2.4.3. <span style="color:red"><i>Compensatória, para as infrações descritas acima alíneas “</i></span><span style="color:red"><b><i>e</i></b></span><span style="color:red"><i>” a “</i></span><span style="color:red"><b><i>h</i></b></span><span style="color:red"><i>” de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

7.2.4.4. <span style="color:red"><i>Compensatória, para a inexecução total do contrato prevista acima na alínea “</i></span><span style="color:red"><b><i>c</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

7.2.4.5. <span style="color:red"><i>Compensatória, para a infração descrita acima na alínea “</i></span><span style="color:red"><b><i>b</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

7.2.4.6. <span style="color:red"><i>Compensatória, em substituição à multa moratória para a infração descrita acima na alínea “d”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação.</i></span>

7.2.4.7. <span style="color:red"><i>Compensatória, para a infração descrita acima na alínea “</i></span><span style="color:red"><b><i>a</i></b></span><span style="color:red"><i>”, de</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) a</i></span> <span style="color:red"><b><i>XX</i></b></span><span style="color:red"><i>% (</i></span><span style="color:red"><b><i>xxxxx</i></b></span> <span style="color:red"><i>por cento) do valor da contratação [, ressalvadas as seguintes infrações também enquadráveis nessa alínea:]</i></span>

7.2.4.7.1. <span style="color:red"><i>[INDICAR ITENS ESPECÍFICOS DE INEXECUÇÃO PARCIAL QUE JUSTIFIQUEM PENALIDADE DIVERSA</i></span><span style="color:red">];</span>

7.3. A aplicação das sanções previstas neste Termo de Referência não exclui, em hipótese alguma, a obrigação de reparação integral do dano causado ao Contratante.

7.4. Todas as sanções previstas neste Termo de Referência poderão ser aplicadas cumulativamente com a multa.

7.5. Antes da aplicação da multa será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis, contado da data de sua intimação.

7.6. Se a multa aplicada e as indenizações cabíveis forem superiores ao valor do pagamento eventualmente devido pelo Contratante ao Contratado, além da perda desse valor, a diferença será descontada da garantia prestada ou será cobrada judicialmente.

7.7. A multa poderá ser recolhida administrativamente no prazo máximo de <span style="color:red"><i>XX</i></span> (<span style="color:red"><i>xxxxx</i></span>) dias, a contar da data do recebimento da comunicação enviada pela autoridade competente.

7.8. A aplicação das sanções realizar-se-á em processo administrativo que assegure o contraditório e a ampla defesa ao Contratado, observando-se o procedimento previsto no caput e parágrafos do art. 158 da Lei nº 14.133, de 2021, para as penalidades de impedimento de licitar e contratar e de declaração de inidoneidade para licitar ou contratar.

7.8.1 Para a garantia da ampla defesa e contraditório, as notificações serão enviadas eletronicamente para os endereços de e-mail informados na proposta comercial, bem como os cadastrados pela empresa no SICAF.

7.8.2 Os endereços de e-mail informados na proposta comercial e/ou cadastrados no SICAF serão considerados de uso contínuo da empresa, não cabendo alegação de desconhecimento das comunicações a eles comprovadamente enviadas.

7.9. Na aplicação das sanções serão considerados:

7.9.1 a natureza e a gravidade da infração cometida;

7.9.2 as peculiaridades do caso concreto;

7.9.3 as circunstâncias agravantes ou atenuantes;

7.9.4 os danos que dela provierem para o Contratante; e

7.9.5 a implantação ou o aperfeiçoamento de programa de integridade, conforme normas e orientações dos órgãos de controle.

7.10. Os atos previstos como infrações administrativas na Lei nº 14.133, de 2021, ou em outras leis de licitações e contratos da Administração Pública que também sejam tipificados como atos lesivos na Lei nº 12.846, de 2013, serão apurados e julgados conjuntamente, nos mesmos autos, observados o rito procedimental e autoridade competente definidos na referida Lei.

7.11. A personalidade jurídica do Contratado poderá ser desconsiderada sempre que utilizada com abuso do direito para facilitar, encobrir ou dissimular a prática dos atos ilícitos previstos neste Termo de Referência ou para provocar confusão patrimonial, e, nesse caso, todos os efeitos das sanções aplicadas à pessoa jurídica serão estendidos aos seus administradores e sócios com poderes de administração, à pessoa jurídica sucessora ou à empresa do mesmo ramo com relação de coligação ou controle, de fato ou de direito, com o Contratado, observados, em todos os casos, o contraditório, a ampla defesa e a obrigatoriedade de análise jurídica prévia.

7.12. O Contratante deverá, no prazo máximo de 15 (quinze) dias úteis, contado da data de aplicação da sanção, informar e manter atualizados os dados relativos às sanções por ela aplicadas, para fins de publicidade no Cadastro Nacional de Empresas Inidôneas e Suspensas (CEIS) e no Cadastro Nacional de Empresas Punidas (CNEP), instituídos no âmbito do Poder Executivo Federal.

7.12.1 As penalidades serão obrigatoriamente registradas no SICAF.

7.13. As sanções de impedimento de licitar e contratar e declaração de inidoneidade para licitar ou contratar são passíveis de reabilitação na forma do art. 163 da Lei nº 14.133, de 2021.

7.14. Os débitos do Contratado para com a Administração Contratante, resultantes de multa administrativa e/ou indenizações, não inscritos em dívida ativa, poderão ser compensados, total ou parcialmente, com os créditos devidos pelo referido órgão decorrentes deste mesmo contrato ou de outros contratos administrativos que o Contratado possua com o mesmo órgão ora Contratante, na forma da Instrução Normativa SEGES/ME nº 26, de 13 de abril de 2022.

## 8. CRITÉRIOS DE MEDIÇÃO E DE PAGAMENTO

### <b>Recebimento</b>

8.1. Os bens serão recebidos provisoriamente, de forma sumária, no ato da entrega, juntamente com a nota fiscal ou instrumento de cobrança equivalente, pelo(a) responsável pelo acompanhamento e fiscalização do contrato, para efeito de posterior verificação de sua conformidade com as especificações constantes no Termo de Referência e na proposta.

8.2. Os bens poderão ser rejeitados, no todo ou em parte, inclusive antes do recebimento provisório, quando em desacordo com as especificações constantes no Termo de Referência e na proposta, devendo ser substituídos no prazo de <span style="color:red">.... (...)</span> dias, a contar da notificação da contratada, às suas custas, sem prejuízo da aplicação das penalidades.

8.3. O recebimento definitivo ocorrerá no prazo de <span style="color:red">XXXX(XXXX)</span> dias úteis, a contar do recebimento da nota fiscal ou instrumento de cobrança equivalente pela Administração, após a verificação da qualidade e quantidade do material e consequente aceitação mediante termo detalhado.

8.4. Para as contratações decorrentes de despesas cujos valores não ultrapassem o limite de que trata o inciso II do art. 75 da Lei nº 14.133, de 2021, o prazo máximo para o recebimento definitivo será de até <span style="color:red">XXXXX (XXX)</span> dias úteis.

8.5. O prazo para recebimento definitivo poderá ser excepcionalmente prorrogado, de forma justificada, por igual período, quando houver necessidade de diligências para a aferição do atendimento das exigências contratuais.

8.6. No caso de controvérsia sobre a execução do objeto, quanto à dimensão, qualidade e quantidade, deverá ser observado o teor do art. 143 da Lei nº 14.133, de 2021, comunicando-se à empresa para emissão de Nota Fiscal quanto à parcela incontroversa da execução do objeto, para efeito de liquidação e pagamento.

8.7. O prazo para a solução, pelo Contratado, de inconsistências na execução do objeto ou de saneamento da nota fiscal ou de instrumento de cobrança equivalente, verificadas pela Administração durante a análise prévia à liquidação de despesa, não será computado para os fins do recebimento definitivo.

8.8. O recebimento provisório ou definitivo não excluirá a responsabilidade civil pela solidez e pela segurança dos bens nem a responsabilidade ético-profissional pela perfeita execução do contrato.

8.9. As atividades de montagem, instalação e quaisquer outras necessárias para o funcionamento ou uso do bem correrão por conta do Contratado e são condição para o recebimento do objeto.

### <b>Liquidação</b>

8.10. Recebida a Nota Fiscal ou documento de cobrança equivalente, correrá o prazo de dez dias úteis para fins de liquidação, na forma desta seção, prorrogáveis por igual período, nos termos do art. 7º, §3º da Instrução Normativa SEGES/ME nº 77/2022.

8.11. O prazo de que trata o item anterior será reduzido à metade, mantendo-se a possibilidade de prorrogação, no caso de contratações decorrentes de despesas cujos valores não ultrapassem o limite de que trata o inciso II do art. 75 da Lei nº 14.133, de 2021.

8.12. Para fins de liquidação, o setor competente deverá verificar se a nota fiscal ou instrumento de cobrança equivalente apresentado expressa os elementos necessários e essenciais do documento, tais como:

8.12.1 o prazo de validade;

8.12.2 a data da emissão;

8.12.3 os dados do contrato e do órgão contratante;

8.12.4 o período respectivo de execução do contrato;

8.12.5 o valor a pagar; e

8.12.6 eventual destaque do valor de retenções tributárias cabíveis.

8.13. Havendo erro na apresentação da nota fiscal ou instrumento de cobrança equivalente, ou circunstância que impeça a liquidação da despesa, esta ficará sobrestada até que o Contratado providencie as medidas saneadoras, reiniciando-se o prazo após a comprovação da regularização da situação, sem ônus ao Contratante;

8.14. A nota fiscal ou instrumento de cobrança equivalente deverá ser obrigatoriamente acompanhado da comprovação da regularidade fiscal, constatada por meio de consulta on-line ao SICAF ou, na impossibilidade de acesso ao referido Sistema, mediante consulta aos sítios eletrônicos oficiais ou à documentação mencionada no art. 68 da Lei nº 14.133, de 2021.

8.15. A Administração deverá realizar consulta ao SICAF para:

8.15.1 verificar a manutenção das condições de habilitação exigidas;

8.15.2 identificar possível razão que impeça a participação em licitação/contratação no âmbito do órgão ou entidade, tais como a proibição de contratar com a Administração ou com o Poder Público, bem como ocorrências impeditivas indiretas.

8.16. Constatando-se, junto ao SICAF, a situação de irregularidade do Contratado, será providenciada sua notificação, por escrito, para que, no prazo de 5 (cinco) dias úteis, regularize sua situação ou, no mesmo prazo, apresente sua defesa. O prazo poderá ser prorrogado uma vez, por igual período, a critério do Contratante.

8.17. Não havendo regularização ou sendo a defesa considerada improcedente, o Contratante deverá comunicar aos órgãos responsáveis pela fiscalização da regularidade fiscal quanto à inadimplência do Contratado, bem como quanto à existência de pagamento a ser efetuado, para que sejam acionados os meios pertinentes e necessários para garantir o recebimento de seus créditos.

8.18. Persistindo a irregularidade, o Contratante deverá adotar as medidas necessárias à rescisão contratual nos autos do processo administrativo correspondente, assegurada ao Contratado a ampla defesa.

8.19. Havendo a efetiva execução do objeto, os pagamentos serão realizados normalmente, até que se decida pela rescisão do contrato, caso o Contratado não regularize sua situação junto ao SICAF.

### <b>Prazo de pagamento</b>

8.20. O pagamento será efetuado no prazo de até 10 (dez) dias úteis contados da finalização da liquidação da despesa, conforme seção anterior, nos termos da Instrução Normativa SEGES/ME nº 77, de 2022.

8.21. No caso de atraso pelo Contratante, os valores devidos ao Contratado serão atualizados monetariamente entre o termo final do prazo de pagamento até a data de sua efetiva realização, mediante aplicação do índice <span style="color:red"><i>XXXX</i></span> de correção monetária.

### <b>Forma de pagamento</b>

8.22. O pagamento será realizado por meio de ordem bancária, para crédito em banco, agência e conta corrente indicados pelo Contratado.

8.23. Será considerada data do pagamento o dia em que constar como emitida a ordem bancária para pagamento.

8.24. Quando do pagamento, será efetuada a retenção tributária prevista na legislação aplicável.

8.25. Independentemente do percentual de tributo inserido na planilha, quando houver, serão retidos na fonte, quando da realização do pagamento, os percentuais estabelecidos na legislação vigente.

8.26. O Contratado regularmente optante pelo Simples Nacional, nos termos da Lei Complementar nº 123, de 2006, não sofrerá a retenção tributária quanto aos impostos e contribuições abrangidos por aquele regime. No entanto, o pagamento ficará condicionado à apresentação de comprovação, por meio de documento oficial, de que faz jus ao tratamento tributário favorecido previsto na referida Lei Complementar.

### <span style="color:red"><b><i>Antecipação de pagamento</i></b></span>

8.27. <span style="color:red"><i>A presente contratação permite a antecipação de pagamento ......... (parcial/total), conforme as regras previstas no presente tópico.</i></span>

8.28. <span style="color:red"><i>O Contratado emitirá recibo/nota fiscal/fatura/documento idôneo/... correspondente ao valor da antecipação de pagamento de R$ ...... (valor por extenso), tão logo ... (incluir condicionante – ex: seja assinado o termo de contrato, ou seja, prestada a garantia etc.), para que o Contratante efetue o pagamento antecipado.</i></span>

8.29. <span style="color:red"><i>Para as etapas seguintes do contrato, a antecipação do pagamento ocorrerá da seguinte forma:</i></span>

8.29.1 <span style="color:red"><i>R$..... (valor em extenso) quando do início da segunda etapa.</i></span>

8.29.2 <span style="color:red"><i>(...)</i></span>

8.30. <span style="color:red"><i>Quando admitida a antecipação de pagamento, fica o Contratado obrigado a devolver, com correção monetária, a integralidade do valor antecipado, na hipótese de inexecução do objeto.</i></span>

8.31. <span style="color:red"><i>No caso de inexecução parcial, deverá haver a devolução do valor relativo à parcela não executada do contrato.</i></span>

8.32. <span style="color:red"><i>O valor relativo à parcela antecipada e não executada do contrato será atualizado monetariamente pela variação acumulada do ........ (especificar o índice de correção monetária a ser adotado), ou outro índice que venha a substituí-lo, desde a data do pagamento da antecipação até a data da devolução.</i></span>

8.33. <span style="color:red"><i>A liquidação ocorrerá de acordo com as regras do tópico respectivo deste instrumento.</i></span>

8.34. <span style="color:red"><i>O pagamento antecipado será efetuado no prazo máximo de até ..... (....) dias, contados do recebimento do ...... (recibo OU nota fiscal OU fatura OU documento idôneo).</i></span>

8.35. <span style="color:red"><i>A antecipação de pagamento dispensa o ateste ou recebimento prévios do objeto, os quais deverão ocorrer após a regular execução da parcela contratual a que se refere o valor antecipado.</i></span>

8.36. <span style="color:red"><i>O pagamento de que trata este item está condicionado à tomada das seguintes providências pelo Contratado:</i></span>

8.36.1 <span style="color:red"><i>comprovação da execução da etapa imediatamente anterior do objeto pelo Contratado, para a antecipação do valor remanescente;</i></span>

8.36.2 <span style="color:red"><i>prestação da garantia adicional nas modalidades de que trata o art. 96 da Lei nº 14.133, de 2021, no percentual de ...%.</i></span>

8.37. <span style="color:red"><i>O pagamento do valor a ser antecipado ocorrerá respeitando eventuais retenções tributárias incidentes.</i></span>

### <b>Cessão de Crédito</b>

8.38. As cessões de crédito dependerão de prévia aprovação do Contratante.

8.38.1 A eficácia da cessão de crédito, em relação à Administração, está condicionada à celebração de termo aditivo ao contrato administrativo.

8.38.2 Sem prejuízo do regular atendimento da obrigação contratual de cumprimento de todas as condições de habilitação por parte do Contratado (cedente), a celebração do aditamento de cessão de crédito e a realização dos pagamentos respectivos também se condicionam à regularidade fiscal e trabalhista do cessionário, bem como à certificação de que o cessionário não se encontra impedido de licitar e contratar com o Poder Público, conforme a legislação em vigor, ou de receber benefícios ou incentivos fiscais ou creditícios, direta ou indiretamente, conforme o art. 12 da Lei nº 8.429, de 1992, nos termos do Parecer JL-01, de 18 de maio de 2020.

8.38.3 O crédito a ser pago à cessionária é exatamente aquele que seria destinado à cedente (Contratado) pela execução do objeto contratual, restando absolutamente incólumes todas as defesas e exceções ao pagamento e todas as demais cláusulas exorbitantes ao direito comum aplicáveis no regime jurídico de direito público incidente sobre os contratos administrativos, incluindo a possibilidade de pagamento em conta vinculada ou de pagamento pela efetiva comprovação do fato gerador, quando for o caso, e o desconto de multas, glosas e prejuízos causados à Administração.

8.38.4 A cessão de crédito não afetará a execução do objeto contratado, que continuará sob a integral responsabilidade do Contratado.

8.39. O disposto nesta seção não afeta as operações de crédito de que trata a Instrução Normativa SEGES/MGI nº 82, de 21 de fevereiro de 2025, as quais ficam por esta regidas.

### <b>Reajuste</b>

8.40. Os preços inicialmente contratados são fixos e irreajustáveis no prazo de um ano contado da data do orçamento estimado, em <span style="color:red"><i>\_\_/\_\_/\_\_ (DD/MM/AAAA)</i></span>.

8.41. Após o interregno de um ano, e independentemente de pedido do Contratado, os preços iniciais serão reajustados, mediante a aplicação, pelo Contratante, do índice <span style="color:red">\_\_\_\_\_\_\_\_\_\_\_</span> <span style="color:red"><i>(indicar o índice a ser adotado</i></span><i>),</i> exclusivamente para as obrigações iniciadas e concluídas após a ocorrência da anualidade.

8.42. Nos reajustes subsequentes ao primeiro, o interregno mínimo de um ano será contado a partir dos efeitos financeiros do último reajuste.

8.43. No caso de atraso ou não divulgação do(s) índice (s) de reajustamento, o Contratante pagará ao Contratado a importância calculada pela última variação conhecida, liquidando a diferença correspondente tão logo seja(m) divulgado(s) o(s) índice(s) definitivo(s).

8.44. Nas aferições finais, o(s) índice(s) utilizado(s) para reajuste será(ão), obrigatoriamente, o(s) definitivo(s).

8.45. Caso o(s) índice(s) estabelecido(s) para reajustamento venha(m) a ser extinto(s) ou de qualquer forma não possa(m) mais ser utilizado(s), será(ão) adotado(s), em substituição, o(s) que vier(em) a ser determinado(s) pela legislação então em vigor.

8.46. Na ausência de previsão legal quanto ao índice substituto, as partes elegerão novo índice oficial, para reajustamento do preço do valor remanescente, por meio de termo aditivo.

8.47. O reajuste será realizado por apostilamento.

## 9. FORMA E CRITÉRIOS DE SELEÇÃO DO FORNECEDOR E FORMA DE FORNECIMENTO

### <b>Forma de seleção e critério de julgamento da proposta</b>

9.1. O fornecedor será selecionado por meio da realização de procedimento de LICITAÇÃO, na modalidade <span style="color:red">[</span><span style="color:red"><i>PREGÃO</i></span><span style="color:red">]</span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red">[</span><span style="color:red"><i>CONCORRÊNCIA</i></span><span style="color:red">]</span>, sob a forma ELETRÔNICA, com adoção do critério de julgamento pelo <span style="color:red">[</span><span style="color:red"><i>MENOR PREÇO</i></span><span style="color:red">]</span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red">[</span><span style="color:red"><i>MAIOR DESCONTO</i></span><span style="color:red">]</span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red">[</span><span style="color:red"><i>TÉCNICA E PREÇO</i></span><span style="color:red">].</span>

<span style="color:red"><b><i>OU</i></b></span>

9.2. <span style="color:red"><i>O fornecedor será selecionado por meio de contratação direta com fundamento no art. [</i></span><span style="color:red"><b><i>74 OU 75</i></b></span><span style="color:red"><i>], inciso [</i></span><span style="color:red"><b><i>indicar o inciso</i></b></span><span style="color:red"><i>], da Lei nº 14.133, de 1º de abril de 2021, com base no seguinte fundamento: [</i></span><span style="color:red"><b><i>descrever a fundamentação da contratação para enquadramento no dispositivo legal indicado</i></b></span><span style="color:red"><i>].</i></span>

### <b>Forma de fornecimento</b>

9.3. O fornecimento do objeto será ............ <span style="color:red">[integral/parcelado/continuado]</span>.

### <span style="background:cyan"><b>Critérios de aceitabilidade de preços</b></span>

9.4. <span style="color:red;background:cyan"><i>Em se tratando de contratação para registro de preços, caso adotado o critério de julgamento de menor preço ou de maior desconto por grupo de itens, o critério de aceitabilidade de preços unitários máximos será:</i></span>

9.4.1 <span style="color:red;background:cyan"><i>Valores unitários: conforme planilha de composição de preços anexa ao edital</i></span> <span style="color:red;background:cyan"><b><i><u>OU</u></i></b></span> <span style="color:red;background:cyan"><i>tabela constante no item XXXXXX deste Termo de Referência.</i></span>

### <b>Exigências de habilitação</b>

9.5. Para fins de habilitação, deverá o interessado comprovar os seguintes requisitos:

### <b>Habilitação jurídica</b>

9.6. pessoa física: cédula de identidade (RG) ou documento equivalente que, por força de lei, tenha validade para fins de identificação em todo o território nacional;

9.7. empresário individual: inscrição no Registro Público de Empresas Mercantis, a cargo da Junta Comercial da respectiva sede;

9.8. Microempreendedor Individual - MEI: Certificado da Condição de Microempreendedor Individual - CCMEI, cuja aceitação ficará condicionada à verificação da autenticidade no sítio https://www.gov.br/empresas-e-negocios/pt-br/empreendedor;

9.9. sociedade empresária, sociedade limitada unipessoal – SLU ou sociedade identificada como empresa individual de responsabilidade limitada - EIRELI: inscrição do ato constitutivo, estatuto ou contrato social no Registro Público de Empresas Mercantis, a cargo da Junta Comercial da respectiva sede, acompanhada de documento comprobatório de seus administradores;

9.10. sociedade empresária estrangeira: portaria de autorização de funcionamento no Brasil, publicada no Diário Oficial da União e arquivada na Junta Comercial da unidade federativa onde se localizar a filial, agência, sucursal ou estabelecimento, a qual será considerada como sua sede, conforme Instrução Normativa DREI/ME n.º 77, de 18 de março de 2020;

9.11. sociedade simples: inscrição do ato constitutivo no Registro Civil de Pessoas Jurídicas do local de sua sede, acompanhada de documento comprobatório de seus administradores;

9.12. filial, sucursal ou agência de sociedade simples ou empresária: inscrição do ato constitutivo da filial, sucursal ou agência da sociedade simples ou empresária, respectivamente, no Registro Civil das Pessoas Jurídicas ou no Registro Público de Empresas Mercantis onde opera, com averbação no Registro onde tem sede a matriz;

9.13. sociedade cooperativa: ata de fundação e estatuto social, com a ata da assembleia que o aprovou, devidamente arquivado na Junta Comercial ou inscrito no Registro Civil das Pessoas Jurídicas da respectiva sede, além do registro de que trata o art. 107 da Lei nº 5.764, de 16 de dezembro 1971.

9.14. <span style="color:red"><i>Ato de autorização para o exercício da atividade de ............ (especificar a atividade contratada sujeita à autorização), expedido por ....... (especificar o órgão competente) nos termos do art. ..... da (Lei/Decreto) n° ........</i></span>

9.15. Os documentos apresentados deverão estar acompanhados de todas as alterações ou da consolidação respectiva.

### <b>Habilitação fiscal, social e trabalhista</b>

9.16. Prova de inscrição no Cadastro Nacional de Pessoas Jurídicas ou no Cadastro de Pessoas Físicas, conforme o caso;

9.17. Prova de regularidade fiscal perante a Fazenda Nacional, mediante apresentação de certidão expedida conjuntamente pela Secretaria da Receita Federal do Brasil (RFB) e pela Procuradoria-Geral da Fazenda Nacional (PGFN), referente a todos os créditos tributários federais e à Dívida Ativa da União (DAU) por elas administrados, inclusive aqueles relativos à Seguridade Social, nos termos da Portaria Conjunta nº 1.751, de 02 de outubro de 2014, do Secretário da Receita Federal do Brasil e da Procuradora-Geral da Fazenda Nacional;

9.18. Prova de regularidade com o Fundo de Garantia do Tempo de Serviço (FGTS);

9.19. Prova de inexistência de débitos inadimplidos perante a Justiça do Trabalho, mediante a apresentação de certidão negativa ou positiva com efeito de negativa, nos termos do Título VII-A da Consolidação das Leis do Trabalho, aprovada pelo Decreto-Lei nº 5.452, de 1º de maio de 1943;

9.20. Prova de inscrição no cadastro de contribuintes Estadual ou Distrital relativo ao domicílio ou sede do fornecedor, pertinente ao seu ramo de atividade e compatível com o objeto contratual;

9.21. Prova de regularidade com a Fazenda Estadual ou Distrital do domicílio ou sede do fornecedor, relativa à atividade em cujo exercício contrata ou concorre;

9.22. Caso o fornecedor seja considerado isento dos tributos relacionados ao objeto contratual, deverá comprovar tal condição mediante a apresentação de declaração da Fazenda respectiva do seu domicílio ou sede, ou outra equivalente, na forma da lei.

9.23. O fornecedor enquadrado como microempreendedor individual que pretenda auferir os benefícios do tratamento diferenciado previstos na Lei Complementar n. 123, de 2006, estará dispensado da prova de inscrição nos cadastros de contribuintes estadual e municipal.

### <b>Qualificação Econômico-Financeira</b>

9.24. certidão negativa de insolvência civil expedida pelo distribuidor do domicílio ou sede do interessado, caso se trate de pessoa física, desde que admitida a sua participação na licitação/contratação, ou de sociedade simples;

9.25. certidão negativa de falência expedida pelo distribuidor da sede do fornecedor;

9.26. balanço patrimonial, demonstração de resultado de exercício e demais demonstrações contábeis <span style="color:red"><i>................... [do último exercício social]</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>[dos dois últimos exercícios sociais]</i></span><i>,</i> já exigíveis e apresentados na forma da lei, comprovando, índices de Liquidez Geral (LG), Liquidez Corrente (LC), e Solvência Geral (SG) superiores a 1 (um), obtidos por meio da aplicação das seguintes fórmulas:

| LG = | Ativo Circulante + Realizável a Longo Prazo |
|---|---|
|  | Passivo Circulante + Passivo Não Circulante |

| SG = | Ativo Total |
|---|---|
|  | Passivo Circulante + Passivo Não Circulante |

| LC = | Ativo Circulante |
|---|---|
|  | Passivo Circulante |

9.27. Caso a empresa interessada apresente resultado inferior ou igual a 1 (um) em qualquer dos índices de Liquidez Geral (LG), Solvência Geral (SG) e Liquidez Corrente (LC), será exigido para fins de habilitação <span style="color:red"><i>[capital mínimo]</i></span> <span style="color:red"><i><u>OU</u></i></span> <span style="color:red"><i>[patrimônio líquido mínimo]</i></span> de <span style="color:red">......</span>% <span style="color:red">[até 10%]</span> do <span style="color:red"><i>[valor total estimado da contratação]</i></span> <span style="color:red"><i><u>OU</u></i></span> <span style="color:red"><i>[valor total estimado da parcela pertinente].</i></span>

9.28. <span style="color:red"><i>Os indicadores fixados acima deverão ser atingidos em cada um dos dois últimos exercícios sociais, sob pena de inabilitação;</i></span>

9.29. Os documentos referidos acima limitar-se-ão ao último exercício no caso de a pessoa jurídica ter sido constituída há menos de 2 (dois) anos;

9.30. Os documentos referidos acima deverão ser exigidos com base no limite definido pela Receita Federal do Brasil para transmissão da Escrituração Contábil Digital - ECD ao Sped.

9.31. As empresas criadas no exercício financeiro da licitação/contratação deverão atender a todas as exigências da habilitação e poderão substituir os demonstrativos contábeis pelo balanço de abertura.

9.32. <span style="color:red"><i>O atendimento dos índices econômicos previstos neste item deverá ser atestado mediante declaração assinada por profissional habilitado da área contábil, apresentada pelo fornecedor.</i></span>

### <b>Qualificação Técnica</b>

9.33. <span style="color:red"><i>Registro ou inscrição da empresa na entidade profissional competente</i></span> <span style="color:red"><b><i>.........(escrever por extenso, se for o caso</i></b></span><span style="color:red"><i>), em plena validade;</i></span>

9.33.1 <span style="color:red"><i>Sociedades empresárias estrangeiras atenderão à exigência por meio da apresentação, no momento da assinatura do contrato ou do aceite de instrumento equivalente, da solicitação de registro perante a entidade profissional competente no Brasil.</i></span>

9.34. <span style="color:red"><i>Comprovação de aptidão para o fornecimento de bens similares, de complexidade tecnológica e operacional equivalente ou superior à do objeto desta contratação, ou do item pertinente, por meio da apresentação de certidões ou atestados emitidos por pessoas jurídicas de direito público ou privado, ou pelo conselho profissional competente, quando for o caso.</i></span>

9.34.1 <span style="color:red"><i>Para fins da comprovação de que trata este subitem, os atestados deverão dizer respeito a contratos executados com as seguintes características mínimas:</i></span>

9.34.1.1. <span style="color:red"><i>[...];</i></span>

9.34.1.2. <span style="color:red"><i>[...]; e</i></span>

9.34.1.3. <span style="color:red"><i>[...].</i></span>

9.34.2 <span style="color:red"><i>Serão admitidos, para fins de comprovação de quantitativo mínimo exigido, a apresentação e o somatório de diferentes atestados relativos a contratos executados de forma concomitante.</i></span>

9.34.3 <span style="color:red"><i>Os atestados de capacidade técnica poderão ser apresentados em nome da matriz ou da filial do fornecedor.</i></span>

9.34.4 <span style="color:red"><i>O fornecedor disponibilizará todas as informações necessárias à comprovação da legitimidade dos atestados, apresentando, quando solicitado pela Administração, cópia do contrato que deu suporte à contratação, endereço atual do Contratante e local em que foi executado o objeto contratado, dentre outros documentos.</i></span>

9.35. <span style="color:red"><i>Prova de atendimento aos requisitos ........, previstos na lei ............: .</i></span>

### <b>Disposições gerais sobre habilitação</b>

9.36. Quando permitida a participação de empresas estrangeiras que não funcionem no País, as exigências de habilitação serão atendidas mediante documentos equivalentes, inicialmente apresentados em tradução livre.

9.37. Na hipótese de o fornecedor ser empresa estrangeira que não funcione no País, para assinatura do contrato ou da ata de registro de preços ou do aceite do instrumento equivalente, os documentos exigidos para a habilitação serão traduzidos por tradutor juramentado no País e apostilados nos termos do disposto no Decreto nº 8.660, de 29 de janeiro de 2016, ou de outro que venha a substituí-lo, ou consularizados pelos respectivos consulados ou embaixadas.

9.38. Não serão aceitos documentos de habilitação com indicação de CNPJ/CPF diferentes, salvo aqueles legalmente permitidos.

9.39. Se o fornecedor for a matriz, todos os documentos deverão estar em nome da matriz, e se o fornecedor for a filial, todos os documentos deverão estar em nome da filial, exceto para atestados de capacidade técnica, e no caso daqueles documentos que, pela própria natureza, comprovadamente, forem emitidos somente em nome da matriz.

9.40. Serão aceitos registros de CNPJ de fornecedor matriz e filial com diferenças de números de documentos pertinentes ao CND e ao CRF/FGTS, quando for comprovada a centralização do recolhimento dessas contribuições.

## 10. ESTIMATIVAS DO VALOR DA CONTRATAÇÃO

10.1. <span style="color:red"><i>O custo estimado total da contratação, que corresponde ao valor máximo aceitável, é de R$... (por extenso), conforme custos unitários apostos na [</i></span><span style="color:red"><b><i>tabela contida no item 1.1 acima</i></b></span><span style="color:red"><i>]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[</i></span><span style="color:red"><b><i>em anexo</i></b></span><span style="color:red"><i>].</i></span>

10.2. <span style="color:red"><i>O valor de referência para aplicação do maior desconto corresponde a R$.....</i></span>

<span style="color:red"><b><i>OU</i></b></span>

10.3. <span style="color:red"><i>O custo estimado da contratação possui caráter sigiloso e será tornado público apenas e imediatamente após o julgamento das propostas.</i></span>

10.3.1 <span style="color:red"><i>Quando as propostas permanecerem com preços acima do orçamento estimado, o custo estimado da contratação será tornado público após a fase de lances.</i></span>

10.4. <span style="color:red"><i>A estimativa de custo levou em consideração o risco envolvido na contratação e sua alocação entre Contratante e Contratado, conforme especificado na matriz de risco constante do Contrato.</i></span>

10.5. <span style="color:red;background:cyan"><i>Em caso de Registro de Preços, os preços registrados poderão ser alterados ou atualizados em decorrência de eventual redução dos preços praticados no mercado ou de fato que eleve o custo dos bens, das obras ou dos serviços registrados, nas seguintes situações:</i></span>

10.5.1 <span style="color:red;background:cyan"><i>em caso de força maior, caso fortuito ou fato do príncipe ou em decorrência de fatos imprevisíveis ou previsíveis de consequências incalculáveis, que inviabilizem a execução da ata tal como pactuada, nos termos do disposto na alínea “d” do inciso II do capu</i></span><span style="color:red;background:cyan"><b><i>t</i></b></span> <span style="color:red;background:cyan"><i>do art. 124 da Lei nº 14.133, de 2021;</i></span>

10.5.2 <span style="color:red;background:cyan"><i>em caso de criação, alteração ou extinção de quaisquer tributos ou encargos legais ou superveniência de disposições legais, com comprovada repercussão sobre os preços registrados;</i></span>

10.5.3 <span style="color:red;background:cyan"><i>serão reajustados os preços registrados, respeitada a contagem da anualidade e o índice previsto para a contratação; ou</i></span>

10.5.4 <span style="color:red;background:cyan"><i>poderão ser repactuados, a pedido do interessado, conforme critérios definidos para a contratação.</i></span>

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

12.1. As informações contidas neste Termo de Referência não são classificadas como <span style="background:lime">sigilosas</span> <span style="color:red;background:lime"><i>[exceto</i></span> <span style="color:red"><i>o custo estimado da contratação, que possui caráter sigiloso até o julgamento das propostas].</i></span>

<span style="color:red"><i>[Local]</i></span><i>,</i> <span style="color:red"><i>[dia]</i></span> <i>de</i> <span style="color:red"><i>[mês]</i></span> <i>de</i> <span style="color:red"><i>[ano].</i></span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Identificação e assinatura do servidor (ou equipe) responsável

<b>ANEXO I</b>

<b>Regras aplicáveis ao instrumento substitutivo ao contrato</b>

<span style="color:red"><b><i>(Contratações de pequeno valor - art. 95, inciso I, da Lei n. 14.133/2021, Orientação Normativa nº 84, de 17 de maio de 2024)</i></b></span>

<span style="color:red"><b><i>OU</i></b></span>

<span style="color:red"><b><i>(Compra com entrega imediata e integral de bens adquiridos, sem previsão de obrigações futuras, inclusive quanto à assistência técnica, independentemente do valor - art. 95, inciso II, da Lei n. 14.133/2021)</i></b></span>

## 1. FORMALIZAÇÃO DA CONTRATAÇÃO

1.1. O adjudicatário terá o <span style="color:red"><i>prazo de ...............,</i></span> contado a partir da data de sua convocação, para aceitar o instrumento equivalente ao contrato ............ <span style="color:red"><i>[Nota de Empenho/Carta Contrato/Autorização]</i></span> <span style="color:red"><b><i>OU</i></b></span> <span style="color:red"><i>[constante deste Anexo]</i></span>, sob pena de decair do direito à contratação, sem prejuízo das sanções previstas.

1.2. O prazo poderá ser prorrogado, por igual período, por solicitação justificada do adjudicatário e aceita pela Administração.

1.3. O aceite do instrumento equivalente pelo adjudicatário implica no reconhecimento de que:

1.3.1 referido instrumento substitui o termo de contrato, sendo-lhe aplicáveis as disposições da Lei nº 14.133/2021;

1.3.2 o Contratado se vincula à sua proposta e às previsões contidas no <span style="color:red"><i>Edital</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>na Autorização de Contratação Direta e/ou no Aviso de Dispensa Eletrônica,</i></span> no Termo de Referência e em seus anexos, conforme Termo de Ciência e Concordância (Anexo II).

## 2. VIGÊNCIA E PRORROGAÇÃO

2.1. <span style="color:red"><i>O prazo de vigência da contratação é aquele estabelecido no Termo de Referência, na forma do artigo 105 da Lei n° 14.133, de 2021.</i></span>

2.2. <span style="color:red"><i>O prazo de vigência será automaticamente prorrogado, independentemente de termo aditivo, quando o objeto não for concluído no período firmado acima, ressalvadas as providências cabíveis no caso de culpa do Contratado, previstas neste instrumento.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

2.3. <span style="color:red"><i>O prazo de vigência da contratação é aquele estabelecido no Termo de Referência, prorrogável por até 10 anos, na forma dos artigos 106 e 107 da Lei n° 14.133, de 2021.</i></span>

2.4. <span style="color:red"><i>A prorrogação de que trata este item é condicionada ao ateste, pela autoridade competente, de que as condições e os preços permanecem vantajosos para a Administração, permitida a negociação com o Contratado, bem como à inexistência de registros no Cadastro Informativo de créditos não quitados do setor público federal (Cadin).</i></span>

2.5. <span style="color:red"><i>O Contratado não tem direito subjetivo à prorrogação contratual.</i></span>

2.6. <span style="color:red"><i>A prorrogação contratual deverá ser promovida mediante celebração de termo aditivo.</i></span>

2.7. <span style="color:red"><i>A contratação não poderá ser prorrogada quando o Contratado tiver sido penalizado nas sanções de declaração de inidoneidade ou impedimento de licitar e contratar com poder público, observadas as abrangências de aplicação.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

2.8. <span style="color:red"><i>O prazo de vigência da contratação é de ..............................(máximo de um ano) contados do(a) ............................. (data da ocorrência da emergência ou da calamidade), improrrogável, na forma do art. 75, VIII, da Lei n° 14.133/2021.</i></span>

## 3. OBRIGAÇÕES DO CONTRATANTE

3.1. São obrigações do Contratante:

3.1.1 Exigir o cumprimento de todas as obrigações assumidas pelo Contratado, de acordo com o Termo de Referência e seus anexos;

3.1.2 Receber o objeto no prazo e condições estabelecidas no Termo de Referência;

3.1.3 Notificar o Contratado, por escrito, sobre vícios, defeitos incorreções, imperfeições, falhas ou irregularidades verificadas na execução do objeto contratual, fixando prazo para que seja substituído, reparado ou corrigido, total ou parcialmente, às suas expensas, certificando-se de que as soluções por ele propostas sejam as mais adequadas;

3.1.4 Acompanhar e fiscalizar a execução contratual e o cumprimento das obrigações pelo Contratado;

3.1.5 Efetuar o pagamento ao Contratado do valor correspondente ao fornecimento do objeto, no prazo, forma e condições estabelecidos no Termo de Referência e neste Anexo;

3.1.6 Aplicar ao Contratado as sanções previstas na lei e no Termo de Referência;

3.1.7 Cientificar o órgão de representação judicial da Advocacia-Geral da União para adoção das medidas cabíveis quando do descumprimento de obrigações pelo Contratado;

3.1.8 Explicitamente emitir decisão sobre todas as solicitações e reclamações relacionadas à execução contratual, ressalvados os requerimentos manifestamente impertinentes, meramente protelatórios ou de nenhum interesse para a boa execução do ajuste.

3.1.8.1. A Administração terá o prazo de <span style="color:red"><i>XXXXXXX</i></span>, a contar da data do protocolo do requerimento para decidir, admitida a prorrogação motivada, por igual período.

3.1.9 Responder eventuais pedidos de reestabelecimento do equilíbrio econômico-financeiro feitos pelo Contratado no prazo máximo de <span style="color:red">XXXXXX.</span>

3.1.10 <span style="color:red"><i>Notificar os emitentes das garantias quanto ao início de processo administrativo para apuração de descumprimento de cláusulas contratuais.</i></span>

3.2. A Administração não responderá por quaisquer compromissos assumidos pelo Contratado com terceiros, ainda que vinculados à execução do objeto contratual, bem como por qualquer dano causado a terceiros em decorrência de ato do Contratado, de seus empregados, prepostos ou subordinados.

## 4. OBRIGAÇÕES DO CONTRATADO

4.1. O Contratado deve cumprir todas as obrigações constantes do Termo de Referência e deste Anexo, assumindo como exclusivamente seus os riscos e as despesas decorrentes da boa e perfeita execução do objeto, observando, ainda, as obrigações a seguir dispostas:

4.1.1 Entregar o objeto acompanhado do manual do usuário, com uma versão em português, <span style="color:red"><i>e da relação da rede de assistência técnica autorizada</i></span>;

4.1.2 Responsabilizar-se pelos vícios e danos decorrentes do objeto, de acordo com o Código de Defesa do Consumidor;

4.1.3 Comunicar ao Contratante, no prazo máximo de 24 (vinte e quatro) horas que antecede a data da entrega, os motivos que impossibilitem o cumprimento do prazo previsto, com a devida comprovação;

4.1.4 Atender às determinações regulares emitidas pelo fiscal ou gestor contratuais ou autoridade superior e prestar todo esclarecimento ou informação por eles solicitados;

4.1.5 Reparar, corrigir, remover, reconstruir ou substituir, às suas expensas, no total ou em parte, no prazo fixado pelo fiscal contratual, os bens nos quais se verificarem vícios, defeitos ou incorreções resultantes da execução ou dos materiais empregados;

4.1.6 Responsabilizar-se pelos vícios e danos decorrentes da execução do objeto, bem como por todo e qualquer dano causado à Administração ou terceiros, não reduzindo essa responsabilidade a fiscalização ou o acompanhamento da execução contratual pelo Contratante, que ficará autorizado a descontar dos pagamentos devidos ou da garantia, caso exigida, o valor correspondente aos danos sofridos;

4.1.7 Quando não for possível a verificação da regularidade no Sistema de Cadastro de Fornecedores – SICAF, o Contratado deverá entregar ao setor responsável pela fiscalização contratual, junto com a Nota Fiscal para fins de pagamento, os seguintes documentos:

4.1.7.1. prova de regularidade relativa à Seguridade Social;

4.1.7.2. certidão conjunta relativa aos tributos federais e à Dívida Ativa da União;

4.1.7.3. certidões que comprovem a regularidade perante a Fazenda Estadual ou Distrital do domicílio ou sede do Contratado;

4.1.7.4. Certidão de Regularidade do FGTS – CRF; e

4.1.7.5. Certidão Negativa de Débitos Trabalhistas – CNDT;

4.1.8 Responsabilizar-se pelo cumprimento de todas as obrigações trabalhistas, previdenciárias, fiscais, comerciais e as demais previstas em legislação específica, cuja inadimplência não transfere a responsabilidade ao Contratante e não poderá onerar o objeto da contratação;

4.1.9 Comunicar ao Fiscal, no prazo de 24 (vinte e quatro) horas, qualquer ocorrência anormal ou acidente que se verifique no local da execução do objeto contratual.

4.1.10 Paralisar, por determinação do Contratante, qualquer atividade que não esteja sendo executada de acordo com a boa técnica ou que ponha em risco a segurança de pessoas ou bens de terceiros.

4.1.11 Manter, durante toda a vigência da contratação, em compatibilidade com as obrigações assumidas, todas as condições exigidas para habilitação na licitação ou para qualificação na contratação direta;

4.1.12 Cumprir, durante todo o período de execução contratual, a reserva de cargos prevista em lei para pessoa com deficiência, para reabilitado da Previdência Social ou para aprendiz, bem como as reservas de cargos previstas na legislação;

4.1.13 Comprovar a reserva de cargos a que se refere a cláusula acima, no prazo fixado pela fiscalização contratual, com a indicação dos empregados que preencheram as referidas vagas;

4.1.14 Guardar sigilo sobre todas as informações obtidas em decorrência da execução do objeto;

4.1.15 Arcar com o ônus decorrente de eventual equívoco no dimensionamento dos quantitativos de sua proposta, inclusive quanto aos custos variáveis decorrentes de fatores futuros e incertos, devendo complementá-los, caso o previsto inicialmente em sua proposta não seja satisfatório para o atendimento do objeto da contratação, exceto quando ocorrer algum dos eventos arrolados no art. 124, II, d, da Lei nº 14.133, de 2021;

4.1.16 Cumprir, além dos postulados legais vigentes de âmbito federal, estadual ou municipal, as normas de segurança do Contratante;

4.1.17 <span style="color:red"><i>Alocar os empregados necessários, com habilitação e conhecimento adequados, ao perfeito cumprimento das obrigações assumidas, fornecendo os materiais, equipamentos, ferramentas e utensílios demandados, cuja quantidade, qualidade e tecnologia deverão atender às recomendações de boa técnica e a legislação de regência;</i></span>

4.1.18 <span style="color:red"><i>Orientar e treinar seus empregados sobre os deveres previstos na Lei nº 13.709, de 14 de agosto de 2018, adotando medidas eficazes para proteção de dados pessoais a que tenha acesso por força da execução contratual;</i></span>

4.1.19 <span style="color:red"><i>Conduzir os trabalhos com estrita observância às normas da legislação pertinente, cumprindo as determinações dos Poderes Públicos, mantendo sempre limpo o local de execução do objeto e nas melhores condições de segurança, higiene e disciplina.</i></span>

4.1.20 <span style="color:red"><i>Submeter previamente, por escrito, ao Contratante, para análise e aprovação, quaisquer mudanças nos métodos executivos que fujam às especificações do memorial descritivo ou instrumento congênere.</i></span>

4.1.21 <span style="color:red"><i>Não permitir a utilização de qualquer trabalho do menor de dezesseis anos, exceto na condição de aprendiz para os maiores de quatorze anos, nem permitir a utilização do trabalho do menor de dezoito anos em trabalho noturno, perigoso ou insalubre.</i></span>

4.1.22 <span style="color:red"><i>Cumprir as normas de proteção ao trabalho, inclusive aquelas relativas à segurança e à saúde no trabalho;</i></span>

4.1.23 <span style="color:red"><i>Não submeter os trabalhadores a condições degradantes de trabalho, jornadas exaustivas, servidão por dívida ou trabalhos forçados;</i></span>

4.1.24 <span style="color:red"><i>Não permitir a utilização de qualquer trabalho do menor de dezesseis anos de idade, exceto na condição de aprendiz para os maiores de quatorze anos de idade, observada a legislação pertinente;</i></span>

4.1.25 <span style="color:red"><i>Não submeter o menor de dezoito anos de idade à realização de trabalho noturno e em condições perigosas e insalubres e à realização de atividades constantes na Lista de Piores Formas de Trabalho Infantil, aprovada pelo Decreto nº 6.481, de 12 de junho de 2008;</i></span>

4.1.26 <span style="color:red"><i>Receber e dar o tratamento adequado a denúncias de discriminação, violência e assédio no ambiente de trabalho.</i></span>

## 5. DA EXTINÇÃO CONTRATUAL

5.1. <span style="color:red"><i>A contratação será extinta quando cumpridas as obrigações de ambas as partes, ainda que isso ocorra antes do prazo estipulado para tanto.</i></span>

5.2. <span style="color:red"><i>Se as obrigações não forem cumpridas no prazo estipulado, a vigência ficará prorrogada até a conclusão do objeto, caso em que deverá a Administração providenciar a readequação do cronograma fixado para a contratação.</i></span>

5.3. <span style="color:red"><i>Quando a não conclusão do objeto referida no item anterior decorrer de culpa do Contratado:</i></span>

5.3.1 <span style="color:red"><i>ficará ele constituído em mora, sendo-lhe aplicáveis as respectivas sanções administrativas; e</i></span>

5.3.2 <span style="color:red"><i>poderá a Administração optar pela extinção contratual e, nesse caso, adotará as medidas admitidas em lei para a continuidade da execução contratual.</i></span>

<span style="color:red"><b><i>OU</i></b></span>

5.4. <span style="color:red"><i>A contratação será extinta quando vencido o prazo estipulado, independentemente de terem sido cumpridas ou não as obrigações de ambas as partes contraentes.</i></span>

5.5. <span style="color:red"><i>O contrato poderá ser extinto antes do prazo nele fixado, sem ônus para o CONTRATANTE,</i></span> <span style="color:red;background:yellow"><i>mediante justificativa formal de que não dispõe</i></span> <span style="color:red"><i>de créditos orçamentários para sua continuidade ou de que o contrato não mais lhe oferece vantagem.</i></span>

5.5.1 <span style="color:red"><i>Nesse caso, a extinção</i></span> <span style="color:red;background:yellow"><i>antecipada</i></span> <span style="color:red"><i>ocorrerá na próxima data de aniversário do contrato,</i></span> <span style="color:red;background:yellow"><i>garantido um prazo mínimo de dois meses para ciência formal do contratado, devendo ser observada a regra do art. 183 da Lei nº 14.133, de 2021 para a contagem deste prazo</i></span><span style="color:red"><i>.</i></span>

5.6. <span style="color:red;background:yellow"><i>O contrato poderá ser extinto com fundamento na ausência de créditos orçamentários ou na perda de vantagem contratual antes da data de aniversário, desde que ocorra com ônus para o CONTRATANTE, conforme previsto no art. 138, §2º, da Lei nº 14.133, de 2021</i></span><span style="color:red"><i>.</i></span>

<span style="color:red"><b><i><u>OU</u></i></b></span>

5.7. <span style="color:red"><i>O contrato será extinto quando vencido o prazo nele estipulado, observado o art. 75, inciso VIII, da Lei n.º 14.133/2021, independentemente de terem sido cumpridas ou não as obrigações de ambas as partes contraentes.</i></span>

5.8. A contratação poderá ser extinta antes de cumpridas as obrigações nela estipuladas, ou antes do prazo fixado, por algum dos motivos previstos no artigo 137 da Lei nº 14.133/21, bem como amigavelmente, assegurados o contraditório e a ampla defesa.

5.8.1 Nesta hipótese, aplicam-se também os artigos 138 e 139 da mesma Lei.

5.8.2 A alteração social ou a modificação da finalidade ou da estrutura da empresa não ensejará a extinção se não restringir sua capacidade de concluir o objeto.

5.8.2.1. Se a operação implicar mudança da pessoa jurídica contratada, deverá ser formalizado termo aditivo para alteração subjetiva.

5.9. O termo de extinção, sempre que possível, será precedido:

5.9.1 Balanço dos eventos contratuais já cumpridos ou parcialmente cumpridos;

5.9.2 Relação dos pagamentos já efetuados e ainda devidos;

5.9.3 Indenizações e multas.

5.10. A extinção contratual não configura óbice para o reconhecimento do desequilíbrio econômico-financeiro, hipótese em que será concedida indenização por meio de termo indenizatório.

5.11. A contratação poderá ser extinta caso se constate que o Contratado mantém vínculo de natureza técnica, comercial, econômica, financeira, trabalhista ou civil com dirigente do órgão ou entidade contratante ou com agente público que tenha desempenhado função na licitação ou na contratação direta, ou atue na fiscalização ou na gestão contratuais, ou que deles seja cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau.

## 6. DOS CASOS OMISSOS

6.1. Os casos omissos serão decididos pelo Contratante, segundo as disposições contidas na Lei nº 14.133, de 2021, e demais normas federais aplicáveis e, subsidiariamente, segundo as disposições contidas na Lei nº 8.078, de 1990 – Código de Defesa do Consumidor – e normas e princípios gerais dos contratos.

## 7. ALTERAÇÕES

7.1. Eventuais alterações contratuais reger-se-ão pela disciplina dos arts. 124 e seguintes da Lei nº 14.133, de 2021.

7.2. O Contratado é obrigado a aceitar, nas mesmas condições contratuais, os acréscimos ou supressões que se fizerem necessários, até o limite de 25% (vinte e cinco por cento) do valor inicial atualizado da contratação.

7.3. As supressões resultantes de acordo celebrado entre as partes contratantes poderão exceder o limite de 25% (vinte e cinco por cento) do valor inicial atualizado do contrato.

7.4. As alterações contratuais deverão ser promovidas mediante celebração de termo aditivo, submetido à prévia aprovação da consultoria jurídica do Contratante, salvo nos casos de justificada necessidade de antecipação de seus efeitos, hipótese em que a formalização do aditivo deverá ocorrer no prazo máximo de 1 (um) mês.

7.5. Registros que não caracterizam alterações contratuais podem ser realizados por simples apostila, dispensada a celebração de termo aditivo, na forma do art. 136 da Lei nº 14.133, de 2021.

## 8. FORO

8.1. Fica definido o Foro da Justiça Federal em <span style="color:red">......</span>, Seção Judiciária de <span style="color:red">......</span> para dirimir os litígios que decorrerem da execução contratual que não puderem ser compostos pela conciliação, conforme art. 92, §1º, da Lei nº 14.133, de 2021.

<b>ANEXO II</b>

<b>TERMO DE CIÊNCIA E CONCORDÂNCIA</b>

Por meio deste instrumento, ..................... <span style="color:red"><i>(identificar o Contratado)</i></span> declara que está ciente e concorda com as disposições e obrigações previstas no <span style="color:red"><i>Edital</i></span> <span style="color:red"><b><i><u>OU</u></i></b></span> <span style="color:red"><i>Aviso de Contratação Direta</i></span>, no Termo de Referência e nos demais anexos a que se refere o <span style="color:red"><i>Pregão/Concorrência/Dispensa Eletrônica</i></span> nº.........../20......., bem como que se responsabiliza, sob as penas da Lei, pela veracidade e legitimidade das informações e documentos apresentados durante o processo de contratação.

Local-UF, <span style="color:red">........</span> de <span style="color:red">...................</span> de 20<span style="color:red">....</span> .

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

(Nome <span style="color:red"><i>e Cargo do Representante Legal</i></span>)
