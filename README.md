# skill-14133

Skill para [Claude Code](https://claude.com/claude-code) que elabora e revisa a documentação técnica de contratações públicas federais sob a **Lei nº 14.133/2021** (Nova Lei de Licitações e Contratos), a partir do Documento de Formalização de Demanda (DFD) do usuário.

O objetivo central é reduzir a dependência de conhecimento jurídico prévio: o usuário raramente sabe, de antemão, se sua contratação é pregão, concorrência, dispensa ou inexigibilidade — e menos ainda qual dos 5 incisos do art. 74 ou dos 18 incisos do art. 75 se aplica. A skill descobre isso por perguntas de fato (o que é o objeto, quanto vale, quantos fornecedores existem, há urgência), não perguntando diretamente "qual é o enquadramento legal?".

## O que a skill produz

Documentação ao longo da cadeia:

```
DFD → Estudo Técnico Preliminar (ETP) + Mapa de Riscos → Termo de Referência (TR) → Parecer Técnico (quando exigido)
```

- **Estudo Técnico Preliminar (ETP)** — genérico ou de TIC, com entrevista inicial adaptada à natureza do objeto (bem, serviço, curso, obra, TI etc.) em vez de um checklist fixo.
- **Mapa de Gerenciamento de Riscos** — anexo obrigatório do ETP, atualizado a cada etapa seguinte da contratação.
- **Termo de Referência (TR)** — usando os modelos vigentes da AGU, um por tipo de objeto (compras, serviços/obras, TIC), cobrindo tanto licitação quanto contratação direta na mesma peça.
- **Parecer Técnico** — cobre tanto a contratação direta (dispensa/inexigibilidade, com o inciso exato do art. 74/75, a prova documental exigida e a seção específica de cada hipótese) quanto os quatro cenários em que a lei também exige manifestação técnica dentro da licitação (banca de técnica e preço, bens/serviços especiais, amostra/prova de conceito, subsídio a recurso técnico).

A skill também **revisa documentação já pronta** — própria, de terceiros, ou um checklist processual completo — apontando ausências e inconsistências em vez de reescrever do zero.

## O que torna o fluxo diferente de preencher um modelo

- **Triagem de enquadramento antes de qualquer redação** (`enquadramento-legal-triagem.md`): percorre os arts. 28 a 32 (modalidades) e 72 a 75 (contratação direta) da lei como uma árvore de perguntas de fato, concluindo o dispositivo aplicável para o usuário confirmar — nunca o contrário.
- **Regra de ouro do modelo AGU**: nada do texto-modelo é apagado. Alternativas "OU" não escolhidas ficam riscadas e visíveis, com a motivação da escolha na própria minuta — acelera a análise jurídica e evidencia que cada opção foi ponderada.
- **Regra da assertividade no Parecer Técnico**: ao contrário do ETP (art. 18, §2º, exige justificar todo tópico ausente), o parecer **omite sem justificar** as seções condicionais que não se aplicam ao caso concreto — cada parecer só contém o que precisa demonstrar.
- **Portão de entrevista antes da redação do Parecer Técnico**: reúne, num único momento, tudo que falta perguntar (inciso exato, prova documental, alíneas, vedações do art. 14, idoneidade do fornecedor, instrumento contratual) em vez de intercalar perguntas com trechos já escritos.

## Estrutura do repositório

```
.claude-plugin/
  plugin.json                           # manifesto do plugin (nome, versão, autor, keywords)
  marketplace.json                      # catálogo que aponta para este mesmo repositório

skills/contratacoes-14133/
  SKILL.md                              # comportamento e fluxo de trabalho da skill
  references/
    dfd-topicos.md                      # estrutura do DFD (Decreto nº 10.947/2022, IN SGD/ME nº 94/2022)
    enquadramento-legal-triagem.md      # árvore de perguntas: modalidade e dispositivo aplicável (arts. 28-32, 72-75)
    etp-topicos.md                      # ETP genérico + entrevista inicial condicional
    etp-tic-topicos.md                  # ETP de TIC (IN SGD/ME nº 94/2022)
    mapa-riscos-modelo.md               # Mapa de Gerenciamento de Riscos
    termo-referencia-*.md               # modelos de TR da AGU (compras / serviços-obras × TIC / não-TIC)
    parecer-tecnico-topicos.md          # Parecer Técnico: contratação direta (art. 74/75) e licitação (arts. 36-38, 41-42, 165)
    ipp-agu-orientacoes.md              # digest do IPP da AGU/MGI (como preencher cada campo, e por quê)
    checklist-completude.md             # roteiro de conferência processual

lei-14133-2021.md          # Lei nº 14.133/2021 convertida para Markdown (fonte: planalto.gov.br)
IPP-AGU-fev-2024.md        # Instrumento de Padronização dos Procedimentos de Contratação, na íntegra
modelos-tr-*/               # modelos .docx de TR publicados pela AGU (contratação direta / pregão-concorrência / TIC)
modelos-outros/              # outros modelos de referência (Mapa de Risco, formatação visual)
listas-verificacao/          # listas de verificação oficiais

.agents/skills/skill-creator/  # ferramenta de autoria/avaliação de skills (anthropics/skills), usada só para
                                # desenvolver este repositório — não faz parte do plugin publicado
```

Arquivos com dados pessoais reais (CPF, nomes, processos em andamento) ficam fora do controle de versão — ver `.gitignore`. Os arquivos de `references/` foram construídos a partir de exemplos reais do órgão do usuário, mas com esses dados removidos e generalizados na extração da estrutura.

## Como usar

**Via plugin marketplace (recomendado)**, dentro do Claude Code:

```
/plugin marketplace add jhomolos/skill-14133
/plugin install contratacoes-14133@contratacoes-14133-marketplace
```

**Manualmente**: copie `skills/contratacoes-14133/` para `.claude/skills/` (escopo do projeto) ou `~/.claude/skills/` (escopo pessoal) no seu ambiente Claude Code.

Depois de instalada:

1. Inicie uma conversa mencionando DFD, ETP, TR, Parecer Técnico, Mapa de Riscos, licitação, dispensa, inexigibilidade, ou peça para montar/revisar a documentação de uma contratação — a skill dispara pela descrição em `SKILL.md`.
2. Forneça o DFD (ou peça para a skill elaborá-lo) e a Portaria de designação da Equipe de Planejamento; a partir daí a skill conduz a entrevista de cada etapa.

## Manutenção

Os modelos de TR da AGU são atualizados periodicamente. Quando o usuário indicar uma versão mais nova, o arquivo de referência correspondente deve ser **substituído**, não mesclado com a versão anterior — ver a nota em `SKILL.md`, seção "Nota sobre os arquivos de referência".

`skills-lock.json` e `.agents/skills/skill-creator/` registram a skill `skill-creator` (anthropics/skills), usada como ferramenta de autoria/avaliação deste repositório — não faz parte do plugin publicado em `.claude-plugin/`.

Ao alterar `name` em `skills/contratacoes-14133/SKILL.md`, `.claude-plugin/plugin.json` e `.claude-plugin/marketplace.json`, mantenha os três sincronizados — o marketplace referencia o plugin pelo campo `name`, e o comando de instalação (`/plugin install <plugin>@<marketplace>`) depende dessa correspondência exata.
