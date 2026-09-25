# Exemplos resolvidos

## 1. Instrumento por PN e opcionais – variante A
**Entrada:** PN N5171B, opcionais 506, UNT, UNW, AMG, AXT (parte deles só no campo Nome).
**Raciocínio:** 506 → 6 GHz; UNT → AM/FM/ΦM; UNW → pulso estreito; AMG → calibração não acreditada (substituir pela CG-4); AXT → maleta. Converter os valores do datasheet em limites com pequena folga para admitir R&S, Anritsu e AnaPico; perguntar ao usuário se os limites atendem.
**Saída (resumida):**
> Gerador de sinais analógicos de RF com faixa de frequência contínua de, no mínimo, 9 kHz a 6 GHz, resolução de frequência igual ou melhor que 0,01 Hz, [...] modulações AM, FM e ΦM com fonte interna e entrada externa, modulação em pulso com tempos de subida e descida iguais ou inferiores a 10 ns e largura mínima de pulso igual ou inferior a 20 ns, [...] interfaces GPIB, LAN e USB com SCPI. Acompanhado de maleta rígida de transporte. Calibração acreditada com declaração de conformidade (CG-4). Referência: Keysight N5171B com opcionais 506, UNT, UNW, AMG e AXT, similar ou superior.

## 2. Acessório dedicado – variante A com compatibilidade
> Bateria recarregável de íons de lítio, 70 Wh, para uso nos analisadores portáteis da série FieldFox. Deve ser compatível, elétrica, mecânica e funcionalmente, com os analisadores Keysight FieldFox. Referência: Keysight N9910X-876, similar ou superior.

## 3. Marca exigida – variante B
**Contexto:** o PN militar 13677432 corresponde a uma interface NI GPIB-USB-HS; o MET/CAL não reconhece conversores de outras marcas (informação do usuário, a documentar no ETP).
> Interface controladora GPIB (IEEE 488.2) para USB 2.0 Hi-Speed, com cabo USB integrado e conector GPIB de 24 pinos para ligação direta ao instrumento, acompanhada de licença do driver NI-488.2. O produto deverá ser novo, original e de procedência comprovada (aquisição junto ao fabricante ou a distribuidor autorizado, com número de série verificável). Referência: National Instruments GPIB-USB-HS (778927-01).
**Para o ETP:** justificativa pela alínea b, com evidência (lista de hardware suportado ou testes que falharam).

## 4. Peça de reposição – forma, ajuste e função
**Contexto:** cabo do radar, banda L, 50 cm, conectores N.
> Conjunto de cabo coaxial de RF montado, 50 Ω, semiflexível ou flexível de baixa perda, para operação em banda L (1 GHz a 2 GHz), com comprimento de 50 cm (tolerância de ±1 cm) e conectores tipo N nas duas extremidades, com o mesmo gênero dos conectores do cabo original, perda de inserção do conjunto igual ou inferior a 0,3 dB em 2 GHz, SWR igual ou inferior a 1,25 de 1 GHz a 2 GHz e eficiência de blindagem igual ou superior a 90 dB. Referência: Raytheon Canada G444399-1, similar ou superior.

## 5. Item comum – variante C
> Cabo HDMI 2.1, macho-macho, comprimento de 2 m (tolerância de ±5%), com suporte a 4K a 120 Hz e 8K a 60 Hz, largura de banda de 48 Gbit/s, certificação Ultra High Speed HDMI, conectores com contatos banhados a ouro.

## 6. Diálogo de parceria (trecho)
**Usuário:** "Quero que só marcas boas participem, nada de chinês."
**Resposta adequada:** explicar que o art. 9º, I, impede excluir pela origem, e que várias marcas de referência fabricam na Ásia; em seguida, oferecer os filtros legítimos (especificação garantida, tabela ponto a ponto, calibração acreditada, linha corrente, procedência, amostra e marca reprovada em processo) e perguntar quais aplicar a este item.

**Usuário:** "Esse sensor tem que ser compatível com o FieldFox."
**Resposta adequada:** avisar que a exigência restringe a oferta à Keysight; perguntar se o uso principal é com o FieldFox (então variante A ou B, justificada pela alínea b) ou com PC (então retirar a exigência e ampliar a competição).
