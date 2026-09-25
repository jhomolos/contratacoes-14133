# Regras de redação

## Sumário
1. Estrutura do texto
2. Sentido dos limites (tabela)
3. Terminologia metrológica (VIM)
4. O que retirar ou generalizar
5. Opcionais → funções
6. Acessórios, peças de reposição e compatibilidade
7. Itens comuns de mercado
8. Serviços
9. Erros reais encontrados em revisões (aprenda com eles)

## 1. Estrutura do texto
Ordem recomendada, sempre em um único parágrafo:
1. **O que é** (nome genérico, sem marca): "Gerador de sinais analógicos de RF ..."
2. **Faixas e desempenho** (grandeza, faixa, exatidão/incerteza, resolução), com limites orientados.
3. **Funções** (uma por opcional relevante).
4. **Interfaces, alimentação, ambiente**, só o que importa para o uso.
5. **Composição do fornecimento** ("Acompanhado de: ...").
6. **Compatibilidade** com o acervo, quando houver: "Deve ser compatível, elétrica, mecânica e funcionalmente, com ..."
7. **Remissões** às condições gerais, quando o órgão adotar essa prática ("Calibração conforme CG-4").
8. **Final**, conforme a variante: `Referência: X, similar ou superior.` (A) · `Referência: X.` (B) · nada (C).

Frases no presente ou no futuro ("deve", "deverá"), sem adjetivos vagos ("de alta qualidade", "robusto", "de primeira linha"), que não são verificáveis.

## 2. Sentido dos limites
| Parâmetro | Melhor quando | Redação |
|---|---|---|
| Exatidão, incerteza, erro, SWR/VSWR, ruído, ondulação, jitter, DANL, THD, tempo de subida/descida, perda de inserção, zona morta, tempo de controle | **menor** | "igual ou inferior a", "igual ou melhor que", "máximo de" |
| Perda de retorno, isolação, diretividade, faixa dinâmica, razão liga/desliga, sensibilidade (em mV/µW), potência máxima, memória, autonomia, resolução em dígitos | **maior** | "igual ou superior a", "no mínimo" |
| Faixas (frequência, tensão, temperatura) | **mais larga** | "de, no mínimo, X a Y" (quem cobre mais atende) |
| Resolução (em unidade, ex.: 0,01 Hz) | **menor valor** | "igual ou melhor que 0,01 Hz" |

Atenção a DANL e ruído em dBm: "–152 dBm ou inferior" significa mais negativo. Escreva "igual ou inferior a –152 dBm/Hz", o que é inequívoco.

## 3. Terminologia metrológica (VIM)
- **Exatidão, erro, incerteza e resolução**, em vez de "precisão" (que no VIM tem outro sentido).
- Especificação **garantida** (specified/warranted), e não "típica". Se só existir valor típico, diga que é típico e decida com o usuário se ele serve.
- Explicite a condição da especificação quando for relevante: período (1 ano), temperatura (23 °C ± 5 °C), largura de banda de resolução, pré-amplificador ligado ou desligado.
- **Calibração**: "certificado acreditado RBC/ILAC-MRA com resultados e incertezas" (ver CG-4). Códigos de fabricante para calibração não acreditada (ex.: Keysight AMG, UK6) viram "calibração acreditada com declaração de conformidade e regra de decisão (ILAC-G8)", quando for o caso.

## 4. O que retirar ou generalizar
| Encontrado no rascunho | Problema | Faça |
|---|---|---|
| "display OLED", "tela touch de 5 polegadas" | Construtivo, de uma marca só | "display com leitura simultânea de ..." ou retire |
| "36 medidas automáticas", "16 GB de memória" | Número exato do datasheet | "no mínimo 30 ...", "armazenamento interno", ou pergunte a real necessidade |
| Protocolos de nicho (CAN XL, SENT, 10BASE-T1S) | Restringe a oferta | Mantenha só os que o usuário usa de fato |
| Lista exaustiva de unidades de medida | Copiada do datasheet | Liste as usuais |
| Pilha AAA, cor, material do gabinete | Irrelevante | Retire, salvo motivo real |
| Protocolos/proprietários de conectividade (Fluke Connect, LTE) | Marca | "comunicação sem fio com aplicativo/software" |
| "típico" em requisito metrológico | Não é verificável | Valor garantido |
| Faixas extremas além do uso (ex.: 1000 V CC para medir elementos de 2 V) | Afasta concorrentes | Pergunte o uso e ajuste |

## 5. Opcionais → funções
Para cada opcional (do PN **e** do nome/descrição): identifique a função no guia de configuração e escreva a função no texto. Exemplos já confirmados:
- Keysight FieldFox: 210 VNA transmissão/reflexão · 211 parâmetros S completos em 2 portas · 233 analisador de espectro · 235 pré-amplificador · 302 suporte a sensor USB · 308 voltímetro vetorial · 310 medidor de potência integrado · 330 medição de pulso com sensor de pico USB · 112 QuickCal (confirmado na série A; confirme na série C) · 358 EMF (requer 307 GPS e 233).
- Keysight EXG/MXG: 506 até 6 GHz · 520 até 20 GHz · 1E1 atenuador (nível mínimo baixo) · UNT AM/FM/ΦM · UNW pulso estreito · AMG calibração com incertezas e banda de guarda (não acreditada) · AXT maleta rígida.
- R&S EVSG1000 (analisador portátil de nível de sinal e modulação): K1 ILS CRS/CLR 2F · K2 VOR · K3 marker beacon · K6 COM ATC · K7 LF/NDB · K10 espectro RF/FI 70–410 MHz · K11 espectro AF · K12 AF no tempo · K21 gravação · K22 alta taxa · K24 sensores de potência · Z2 maleta · EVS-Z3 antena dipolo · EVS-Z4 bolsa · EVS-Z6 capa rígida · B2/B3 bateria.
Se não achar o significado de um código, **não invente**: escreva `[DEFINIR função do opcional X]` e avise o usuário.

## 6. Acessórios, peças de reposição e compatibilidade
- **Acessório dedicado** (bateria, maleta, fonte, cabo de interface): descreva a função, inclua a frase de compatibilidade e use a variante A (terceiros podem comprovar compatibilidade) ou B (com justificativa pela alínea b).
- **Peça de reposição de sistema** (PN de desenho, fabricante do sistema): escreva uma especificação de forma, ajuste e função (faixa de frequência, conectores e gênero, comprimento, potência, perda, SWR, dimensões e fixação, sentido de circulação etc.). Sem desenho ou datasheet, deixe `[DEFINIR]` e peça os dados; não finja que sabe.
- **Item de projeto militar/NSN**: verifique se é, na verdade, um item comercial com número militar (ex.: NSN de uma interface NI GPIB-USB-HS). Se for, especifique o item comercial. Se o provedor for FMS, lembre que a aquisição pode não ser por pregão.
- **Itens sujeitos a falsificação** (interfaces, componentes eletrônicos, cabos de marca): exija produto novo, original, com procedência comprovada (fabricante ou distribuidor autorizado) e número de série verificável (CG-10).

## 7. Itens comuns de mercado
Para itens comprados na internet ou em qualquer loja (informática, consumo, ferramentas):
- Pesquise 3 ou mais produtos de marcas diferentes e escreva o **mínimo comum** que atende à necessidade. A variante C (sem referência) costuma bastar.
- Cite normas quando existirem (ABNT, IEC, Inmetro compulsório) e requisitos objetivos (capacidade, dimensões, potência, compatibilidade, garantia).
- Use a variante A só se a marca ajudar a identificar o item (ex.: "Referência: Raspberry Pi 500 Kit, similar ou superior."), lembrando que "similar" precisa ser definível. Se o item depende de um ecossistema (ex.: HATs Raspberry Pi), descreva a compatibilidade exigida.
- Verifique o CATMAT pelo item genérico.

## 8. Serviços
Estrutura sugerida: objeto · escopo (itens, quantidades, modelos) · requisitos do prestador (ex.: acreditação ISO/IEC 17025 com escopo que abranja as grandezas e faixas) · requisitos de execução (local, prazos, pontos de calibração, norma ou procedimento de referência, peças incluídas ou não) · entregáveis (certificado com incertezas, declaração de conformidade, relatório) · critérios de aceitação · garantia do serviço. Marca não se aplica, exceto quando a peça ou o software de um fabricante estiver incluído; nesse caso, siga a lógica das variantes.

Exemplo:
> Serviço de calibração acreditada de 12 multímetros digitais de 6½ dígitos, em laboratório acreditado pela Cgcre/Inmetro (RBC) ou por organismo signatário do ILAC-MRA, com escopo que abranja tensão e corrente CC/CA, resistência e frequência nas faixas dos instrumentos, contemplando no mínimo [n] pontos por função conforme a lista anexa, com emissão de certificado de calibração contendo resultados, incertezas expandidas (k ≈ 2) e declaração de conformidade com as especificações do fabricante, com regra de decisão informada, e prazo de execução de até 30 dias corridos a contar do recebimento dos instrumentos.

## 9. Erros reais encontrados em revisões
- **Incerteza "mínima"** e **perda de retorno "máxima"**: sentidos invertidos (ver seção 2).
- **Tempo de subida "de no mínimo 2,9 ns"**: deveria ser "igual ou inferior a".
- **Especificação de um modelo com o PN de outro**: "12 dígitos/s e 20 ps" atribuídos ao 53210A, características do 53230A. Confira sempre o datasheet do PN citado.
- **Base de tempo contraditória** no mesmo texto (100 s/div e 1000 s/div). Releia o texto inteiro.
- **Descrição do plano diferente do PN** (EVSG1000 descrito como "analyzer" e tratado erradamente como gerador). Confirme no site do fabricante antes de contradizer o usuário.
- **Obsolescência presumida** sem checar o site do fabricante.
- **Lista de fabricantes desalinhada** com os itens de uma planilha, ou com modelos inventados. Confira linha a linha e cite só modelos confirmados.
- **Equivalente indicado que não atende**: circulador de 0,95–1,225 GHz indicado para banda L de 1–2 GHz; carga "sem líquido" que excluía o equivalente refrigerado a óleo. Confronte cada equivalente com cada requisito.
