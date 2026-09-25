# contratacoes-14133

Skill para [Claude Code](https://claude.com/claude-code) que elabora e revisa a documentação técnica de contratações públicas federais sob a **Lei nº 14.133/2021** (Nova Lei de Licitações e Contratos), a partir do Documento de Formalização de Demanda (DFD) do usuário.

O objetivo central é reduzir a dependência de conhecimento jurídico prévio: o usuário raramente sabe, de antemão, se sua contratação é pregão, concorrência, dispensa ou inexigibilidade — e menos ainda qual dos 5 incisos do art. 74 ou dos 18 incisos do art. 75 se aplica. A skill descobre isso por perguntas de fato (o que é o objeto, quanto vale, quantos fornecedores existem, há urgência), não perguntando diretamente "qual é o enquadramento legal?".

## O que a skill produz

Documentação ao longo da cadeia:

```
DFD → Estudo Técnico Preliminar (ETP) + Mapa de Riscos → Termo de Referência (TR) → Parecer Técnico (quando exigido)
```

- **Estudo Técnico Preliminar (ETP)** — genérico ou de TIC, com entrevista inicial adaptada à natureza do objeto (bem, serviço, curso, obra, TI etc.) em vez de um checklist fixo.
- **Mapa de Gerenciamento de Riscos** — documento independente, não um anexo do ETP; é elaborado em paralelo a ele e atualizado a cada etapa seguinte da contratação.
- **Termo de Referência (TR)** — usando os modelos vigentes da AGU, um por tipo de objeto (compras, serviços/obras, TIC), cobrindo tanto licitação quanto contratação direta na mesma peça.
- **Parecer Técnico** — cobre tanto a contratação direta (dispensa/inexigibilidade, com o inciso exato do art. 74/75, a prova documental exigida e a seção específica de cada hipótese) quanto os quatro cenários em que a lei também exige manifestação técnica dentro da licitação (banca de técnica e preço, bens/serviços especiais, amostra/prova de conceito, subsídio a recurso técnico).

- **Especificação técnica de itens** (arts. 41 e 42) — descrição de bens e serviços por desempenho, a partir de PN, CFF/CAGE e opcionais de fabricante, com decisão guiada sobre indicar a marca como referência ("similar ou superior"), exigi-la com justificativa ou omiti-la, e levantamento de equivalentes para a pesquisa de mercado. Funciona dentro do ETP/TR ou de forma avulsa (um item, uma lista, uma planilha de plano de aquisição). Incorporada da skill `especificacao-tecnica-lei14133`.

A skill também **revisa documentação já pronta** — própria, de terceiros, ou um checklist processual completo — apontando ausências e inconsistências em vez de reescrever do zero.

## O que torna o fluxo diferente de preencher um modelo

- **Triagem de enquadramento antes de qualquer redação** (`enquadramento-legal-triagem.md`): percorre os arts. 28 a 32 (modalidades) e 72 a 75 (contratação direta) da lei como uma árvore de perguntas de fato, concluindo o dispositivo aplicável para o usuário confirmar — nunca o contrário.
- **Regra de ouro do modelo AGU**: nada do texto-modelo é apagado. Alternativas "OU" não escolhidas ficam riscadas e visíveis, com a motivação da escolha na própria minuta — acelera a análise jurídica e evidencia que cada opção foi ponderada.
- **Regra da assertividade no Parecer Técnico**: ao contrário do ETP (art. 18, §2º, exige justificar todo tópico ausente), o parecer **omite sem justificar** as seções condicionais que não se aplicam ao caso concreto — cada parecer só contém o que precisa demonstrar.
- **Portão de entrevista antes da redação do Parecer Técnico**: reúne, num único momento, tudo que falta perguntar (inciso exato, prova documental, alíneas, vedações do art. 14, idoneidade do fornecedor, instrumento contratual) em vez de intercalar perguntas com trechos já escritos.
- **Orientação de publicação no SIASG**: depois de elaborados o ETP, o Mapa de Riscos e o TR, a skill lembra o usuário de publicá-los no módulo correspondente do SIASG, sob a UASG (Unidade de Compra) adequada — regra informada pelo usuário, não deduzida da lei.

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
    termo-referencia-*.md               # modelos de TR da AGU (compras / serviços-obras × TIC / não-TIC), com numeração, cores e realces
    termo-referencia-*-notas.md         # notas explicativas da AGU de cada modelo, indexadas pelo número do item
    parecer-tecnico-topicos.md          # Parecer Técnico: contratação direta (art. 74/75) e licitação (arts. 36-38, 41-42, 165)
    ipp-agu-orientacoes.md              # digest do IPP da AGU/MGI (como preencher cada campo, e por quê)
    guia-contratacoes-sustentaveis.md   # enquadramento no Guia Nacional de Contratações Sustentáveis (AGU, 8ª ed.)
    checklist-completude.md             # roteiro de conferência processual
    especificacao/                      # especificação técnica de itens (arts. 41-42)
      fluxo-especificacao.md            #   fluxo de trabalho e onde cada saída entra no ETP/TR
      regras_redacao.md                 #   redação por desempenho, sentido dos limites, VIM, serviços, erros comuns
      fundamentacao_legal.md            #   hipóteses de indicação de marca e modelos de justificativa
      condicoes_gerais.md               #   CG-1 a CG-12 e em que seção do modelo AGU cada uma entra
      exemplos.md                       #   casos resolvidos
  scripts/
    modelo_docx_para_md.py              # converte modelo AGU .docx em Markdown (e extrai as notas com --notas)
    verificar_especificacao.py          # confere formato e erros comuns das especificações (texto, .txt ou .xlsx)

lei-14133-2021.md          # Lei nº 14.133/2021 convertida para Markdown (fonte: planalto.gov.br)
IPP-AGU-fev-2024.md        # Instrumento de Padronização dos Procedimentos de Contratação, na íntegra
guia-nacional-contratacoes-sustentaveis-2025.txt  # Guia Nacional de Contratações Sustentáveis (AGU, 8ª ed.), texto integral
modelos-tr-pregao-conc/      # modelos .docx de TR da AGU (compras; serviços e obras), que cobrem licitação e contratação direta
modelos-tr-tic/              # modelos .docx de TR da AGU para TIC (compras; serviços)
modelos-outros/              # outros modelos de referência (Mapa de Risco, formatação visual)
listas-verificacao/          # listas de verificação oficiais

.agents/skills/skill-creator/  # ferramenta de autoria/avaliação de skills (anthropics/skills), usada só para
                                # desenvolver este repositório — não faz parte do plugin publicado
```

Arquivos com dados pessoais reais (CPF, nomes, processos em andamento) ficam fora do controle de versão — ver `.gitignore`. Os arquivos de `references/` foram construídos a partir de exemplos reais do órgão do usuário, mas com esses dados removidos e generalizados na extração da estrutura.

## Como usar

### Claude Code (recomendado)

**Via plugin marketplace (mais prático):**

```bash
/plugin marketplace add jhomolos/contratacoes-14133
/plugin install contratacoes-14133@contratacoes-14133-marketplace
```

**Instalação manual:**

Copie a pasta `skills/contratacoes-14133/` para:
- `.claude/skills/` (escopo do projeto — sincroniza com time)
- `~/.claude/skills/` (escopo pessoal — só na sua máquina)

**Como invocar:**

Mencione em uma conversa: "DFD", "ETP", "Termo de Referência", "Parecer Técnico", "Mapa de Riscos", "licitação", "dispensa", "inexigibilidade", ou peça para "montar/revisar documentação de contratação". A skill dispara automaticamente pela descrição em `SKILL.md`.

Depois forneça o DFD (ou peça para a skill elaborá-lo) e a Portaria de designação da Equipe de Planejamento; a partir daí a skill conduz a entrevista de cada etapa.

### Codex CLI (Anthropic)

```bash
codex skills add jhomolos/contratacoes-14133
```

Invocação: use os mesmos gatilhos de palavras-chave que no Claude Code (DFD, ETP, TR, etc.).

### Outros agentes (Abacus, ChatGPT, etc.)

A skill é um **conjunto de documentos de referência em Markdown** — não requer integração específica.

**Opção 1: Como material de consulta**

1. Clone ou baixe este repositório: `git clone https://github.com/jhomolos/contratacoes-14133.git`
2. Carregue os arquivos de referência (`skills/contratacoes-14133/references/*.md`) no seu agente como documentos de contexto
3. Peça ao agente para seguir o fluxo:
   ```
   DFD → Estudo Técnico Preliminar (ETP) 
        + Mapa de Riscos (documento independente)
        → Termo de Referência (TR) 
        → Parecer Técnico (quando necessário)
   ```

**Opção 2: Passos manuais (sem integração)**

Você pode usar a skill como um **guia estruturado**:

1. Forneça o DFD ao seu agente
2. Peça que siga os tópicos em `skills/contratacoes-14133/references/etp-topicos.md`
3. Peça que consulte `skills/contratacoes-14133/references/enquadramento-legal-triagem.md` para triagem de enquadramento legal
4. Continue com `termo-referencia-*.md` conforme o tipo de objeto (compras, serviços, TIC)
5. Se necessário parecer técnico, consulte `parecer-tecnico-topicos.md`

### Sem instalação (acesso direto ao repositório)

Visite o repositório no GitHub: `https://github.com/jhomolos/contratacoes-14133`

- Leia o `README.md` para contexto
- Navegue até `skills/contratacoes-14133/references/` e abra os arquivos `.md` que precisa
- Use-os como referência para estruturar sua documentação de contratação — o fluxo e os tópicos valem independentemente do agente usado

## Manutenção

Os modelos de TR da AGU são atualizados periodicamente. Quando o usuário indicar uma versão mais nova, o arquivo de referência correspondente deve ser **substituído**, não mesclado com a versão anterior — ver a nota em `SKILL.md`, seção "Nota sobre os arquivos de referência".

`skills-lock.json` e `.agents/skills/skill-creator/` registram a skill `skill-creator` (anthropics/skills), usada como ferramenta de autoria/avaliação deste repositório — não faz parte do plugin publicado em `.claude-plugin/`.

Ao alterar `name` em `skills/contratacoes-14133/SKILL.md`, `.claude-plugin/plugin.json` e `.claude-plugin/marketplace.json`, mantenha os três sincronizados — o marketplace referencia o plugin pelo campo `name`, e o comando de instalação (`/plugin install <plugin>@<marketplace>`) depende dessa correspondência exata.
