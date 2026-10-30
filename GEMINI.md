# DIRETRIZES OFICIAIS DE ARQUITETURA E UI — DOMÍNIO CORPORAL



Este documento estabelece as regras e padrões de design, estrutura HTML, terminologia e formatação obrigatórios para **todos os aplicativos de treino** da plataforma Domínio Corporal (alunos e treinador).



---



## 1. TÍTULOS DE SEÇÕES DE TREINO (PADRÃO OURO)



Os títulos das seções de treino devem ser **estritamente sucintos, objetivos e canônicos**, eliminando qualquer redundância ou poluição visual.



### Termos Canônicos Permitidos:

- **`ATIVAÇÃO`**: Aquecimento cardiovascular suave, liberação miofascial, mobilidade articular preparatória.

- **`FORTALECIMENTO`**: Bloco principal de força, hipertrofia, musculação ou calistenia com carga.

- **`HABILIDADES`**: Bloco de skills técnicas, paradas de mão (handstands), equilíbrios, acrobacias.

- **`MOBILIDADE`**: Descompressão articular, flexibilidade, relaxamento e volta à calma pós-treino.

- **`CONDICIONAMENTO`**: Blocos aeróbicos, cardiorrespiratórios, WODs, EMOMs, AMRAPs e trabalho metabólico.



### 🚫 Proibições Estritas:

- **NÃO** usar títulos compostos ou prolixos (Exemplos proibidos: `"ATIVAÇÃO & PREPARAÇÃO ARTICULAR"`, `"FORÇA & METABOLISMO"`, `"DESCOMPRESSÃO ARTICULAR"`, `"MOBILIDADE E RECUPERAÇÃO"`, `"CONDICIONAMENTO (BOX)"`).

- **NÃO** duplicar badges dentro do cabeçalho da seção (ex: não colocar um badge `<span class="section-badge">Ativação</span>` ao lado de um título `<div class="section-title">...</div>`).



### Estrutura HTML e Visual Canônico das Seções:

- **Faixa de Cabeçalho Superior com Degradê Dark Cyber Glass (`.section-header`):** A faixa superior do card preenche de borda a borda com efeito Cyber Glass iluminado (`linear-gradient(90deg, ...)`), harmonizado com a cor sólida temática da seção (Âmbar para Ativação, Verde Esmeralda para Habilidades, Azul Ciano para Fortalecimento, Roxo Violeta para Mobilidade, Coral para Condicionamento), com divisão horizontal inferior suave e sutil brilho interno (`box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.12)`).

- **Título Clean em Branco Puro 1.15rem (`.section-title`):** Tipografia em caixa alta na cor branca pura (`#ffffff`), fonte ampliada de `1.15rem`, peso 900, **sem borda, sem badge/retângulo, sem caixas coloridas ao redor da palavra e sem bolinha**, de altíssimo contraste e legibilidade imediata ("apenas o escrito em branco sobre o degradê").

- **Relógio de Duração no Cabeçalho (`.meta-chip-time`):** Destaque suave em branco luminoso (`color: #e2e8f0; font-size: 0.82rem; font-weight: 700;`), sem molduras escuras ou caixas fechadas.

- **Borda Lateral Contínua no Card:** A borda esquerda do card de treino (4.5px) mantém a cor sólida temática da seção (Âmbar para Ativação, Azul para Fortalecimento, Esmeralda para Habilidades, Roxo para Mobilidade, Coral para Condicionamento), emoldurando o bloco com precisão esportiva.

- **Exclusividade do Verde Neon:** O verde neon (`#00ff88`) permanece 100% reservado para a ação primordial de conclusão da série (`✓`), garantindo foco e gratificação visual ao aluno.



```html

<div class="section-card sec-aquecimento"> <!-- ou sec-forca, sec-flexibilidade, sec-cardio, sec-skills -->

  <div class="section-header">

    <div class="section-title">ATIVAÇÃO</div>

    <div class="session-meta-chips">

      <span class="meta-chip meta-chip-time">⏱️ ~12 min</span>

    </div>

  </div>

  ...

</div>

```



---





### 1.1 Cabeçalho de Treino/Dia, Local e Duração Levemente Realçados:

- **Título do Treino na Barra Superior Dedicada (ao lado de `‹ Voltar`):**

  - **Eliminação Absoluta de Parênteses, Cidades, Horários e do Sufixo `-feira` (Estritamente Dia/Treino e Skill):** Os títulos dos dias de treino na barra superior (`#dedicatedBarTitle` / `dayNames`) e nos cards da rotina (`.day-name`) devem conter **estritamente o nome do dia ou treino e a skill principal**, em caixa alta pura, separados exclusivamente por **barra vertical (`|`)**:

  - **Eliminação Total da Linha de Descrição nos Cards da Rotina (`.day-focus-desc`):** Para manter o design estritamente limpo, minimalista e direto, os cards da rotina (`.training-day-card`) exibem apenas o título com o nome do dia/treino e a skill (`.day-name`) e a linha de metadados (`.day-meta-pill`). A linha de descrição secundária (`.day-focus-desc`) foi eliminada de todos os aplicativos da plataforma.

    - ❌ Proibido: `Quinta-feira (Handstand e Contemporâneo)`, `SEGUNDA • Crossfit`, `QUINTA | HANDSTAND - 13H`, `QUARTA | GINÁSIO EEFERP`

    - ✅ Canônico: `SEGUNDA | A DEFINIR`, `TERÇA | LPO`, `QUARTA | ARGOLAS`, `QUINTA | A DEFINIR`, `SEXTA | A DEFINIR`, `SEGUNDA | TREINO A`

  - **Metadados em seu Devido Lugar:** Locais (`📍`) e tempos/duração (`⏱️`) são reservados exclusivamente para as linhas de metadados (`.day-meta-pill`, `.session-overall-meta`), despoluindo completamente os títulos.

- **Realce Leve dos Escritos de Local e Duração (Página Principal e Treinos):**

  - **Página Principal (Home Hub):** Os badges de dia (`.day-meta-pill`) utilizam tipografia levemente realçada em tom slate claro (`color: #cbd5e1; font-weight: 600; font-size: 0.76rem;`), garantindo rápida identificação do local (`📍`) e tempo estimado (`⏱️`).

  - **Páginas de Treino:** O subcabeçalho geral da sessão (`.session-overall-meta`) destaca suavemente os itens (`.meta-item { color: #e2e8f0; font-weight: 600; }`), separados por barra vertical discreta (`<span class="meta-separator">|</span>`).

  ```html

  <div class="session-overall-meta">

    <button type="button" class="btn-orientacoes-popup" onclick="openOrientacoesTreino('segunda')">

      <svg viewBox="0 0 24 24" style="width:14px; height:14px; fill:currentColor;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>

      <span>ORIENTAÇÕES</span>

    </button>

    <span class="meta-separator">|</span>

    <span class="meta-item">📍 Box CrossFit</span>

    <span class="meta-separator">|</span>

    <span class="meta-item">⏳ ~55 min</span>

  </div>

  ```

- **Pop-up sem duplicidade:** O popover exibe estritamente a tag de cabeçalho `🛡️ ORIENTAÇÕES` no topo, ocultando títulos repetidos abaixo para eliminar redundância visual.

- **Cor Canônica do Botão e Pop-up:** Tom Cyan / Azul Técnico (`#38bdf8` com fundo `rgba(56, 189, 248, 0.10)` e borda `rgba(56, 189, 248, 0.35)`), transmitindo suporte clínico e instrucional sem competir visualmente com os botões verdes de ação ou conclusão de séries.



### 1.2 Padrão Dark Cyber Glass na Página Principal (Home Hub) e Demais Páginas:

- A elegância do Dark Cyber Glass é estendida à Página Principal (Home Hub) e seções estruturais do aplicativo:

  - **Card do Atleta (`.athlete-highlight-card`):** Caixa fechada com fundo dark e névoa neon suave (`rgba(0, 255, 136, 0.12)`), borda lateral esquerda de `4.5px solid var(--brand-neon)`, título com nome do atleta no topo e botões de ação internos.

  - **Card de Ferramentas (`.tools-highlight-card`):** Caixa fechada no mesmo padrão visual do card do atleta, com fundo dark e névoa ciano suave (`rgba(56, 189, 248, 0.12)`), borda lateral esquerda de `4.5px solid #38bdf8`, título `FERRAMENTAS` em caixa alta pura `1.05rem` no topo e botões internos (`Timers`, `Análises`, `Evolução`).

  - **Cabeçalho da Rotina de Treino (`#trainingHubSection .training-section-header`):** Padrão Minimalista Clean (Opção 1 Oficial), completamente transparente e sem bordas/caixas (`background: transparent; border: none;`), com o título `ROTINA DE TREINO` direto em branco puro `1.35rem`, peso 900, dando respiro visual e evidenciando os cards de treino logo abaixo.

  - **Regra Universal de Conclusão e Progresso nos Cards (`.training-day-card`):**

    - **Modo DIA (`data-workout-type="dia"` ou dias da semana):** Status binário (`›` quando pendente / `✓ Concluído` em verde neon quando finalizado). Acionado pelo envio da sessão ou com um toque direto na pílula na página principal (`onclick="event.stopPropagation(); handleWorkoutStatusClick(...)"`).

    - **Modo TREINO com Meta (`data-workout-type="treino" data-target="N"`):** Exibe a fração de progresso em ciano (`1/N`, `2/N`, `X/N`) a cada treino finalizado ou clique direto na home. Ao atingir a meta estipulada ($N/N$), a pílula se transforma automaticamente no badge verde neon **`✓ Concluído`** idêntico ao do dia. Um novo clique no card finalizado reinicia o ciclo.

  - **Cards de Rotina (`.training-day-card`):** Borda lateral contínua de `4.5px solid var(--brand-neon)`, fundo escuro com névoa neon suave e foco do dia estritamente com a skill.

  - **Perfil do Atleta (`.student-profile-header-card`):** Aplicação do padrão ciano noturno com borda `4.5px` e névoa horizontal. O container de título `.section-title-wrap` permanece sempre 100% transparente, sem bordas ou fundos, garantindo títulos limpos em branco puro.



---



## 2. CARDS DE EXERCÍCIO E MODAL DE INSTRUÇÕES (PADRÃO OURO)



### 2.1 Botão Compacto Unificado: `Instruções` (Padrão Ouro: Ícone Play + Ciano Noturno)

- Todos os cards de exercício possuem um **único botão compacto** posicionado diretamente ao lado do nome do exercício:

  ```html

  <div class="ex-title">

    <span>NOME DO EXERCÍCIO</span>

    <button type="button" class="btn-video" onclick="openVideoModal('Título', 'Descrição', 'URL_DO_VIDEO')">

      <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg> <span>Instruções</span>

    </button>

  </div>

  ```

- **Estilo Canônico:** Fundo sólido Ciano Noturno (`#0e2238`), borda técnica viva em Ciano (`#38bdf8`), texto em branco puro (`#ffffff`) em negrito 800 e ícone play em Ciano (`#38bdf8`).

- **Dimensões Compactas Otimizadas:** Padding reduzido (`2.5px 8px`), fonte enxuta (`0.68rem`) e ícone play de `9px`, ocupando ~85px de largura total (economia de ~55px em relação ao antigo `Vídeo | Instruções`), cabendo confortavelmente ao lado do título do exercício na maioria esmagadora dos dispositivos móveis.

- **Harmonia Visual:** Garante altíssimo contraste e legibilidade imediata, conversa com o Ciano das *Orientações* e **não compete visualmente com as bolinhas de série concluídas** (que preenchem em Verde Neon `✓`).

- **NUNCA** incluir linhas ou botões separados de dicas (`🛡️ Cuidados`, `🔧 Instruções`, `💡 Dicas`, `ex-cues-row`).

- **Exercícios sem vídeo:** Devem manter o mesmo botão `Instruções` passando `''` como URL (`openVideoModal(titulo, desc, '')`). A função `openVideoModal` esconde o container do vídeo automaticamente (`.video-container { display: none; }`), exibindo o texto de instruções de forma limpa.



### 2.2 Estrutura do Conteúdo no Modal (`openVideoModal`):

O modal divide dinamicamente o conteúdo em seções limpas via função `formatModalInstructions`, **sem emojis nos cabeçalhos de bloco e sem marcadores de bolinha (`•`)**:

1. **`EXECUÇÃO` (Sem Emojis):** Título em ciano (`#38bdf8`) em caixa alta pura, com **passos numerados sequenciais discretos** (`1`, `2`, `3`...) em mini círculos ciano noturno (`.modal-step-num.modal-num-exec`).

2. **`CUIDADOS` (Sem Emojis):** Título em alerta suave (`#f87171`) em caixa alta pura, com **passos numerados sequenciais discretos** (`1`, `2`, `3`...) em mini círculos coral suave (`.modal-step-num.modal-num-care` com fundo `rgba(248, 113, 113, 0.12)` e borda `rgba(248, 113, 113, 0.35)`).

3. **`DICAS` (Quando Houver - Sem Emojis):** Título em amarelo esportivo (`#fbbf24`) em caixa alta pura, com passos numerados sequenciais (`.modal-num-tip`).

4. **`BASE CIENTÍFICA` (Sem Emojis, Accordion Retrátil):**

   - Fechado por padrão (`<details class="modal-science-accordion">`), mantendo o modal ágil e despoluído.

   - **Formato Direto em Caixa Alta:** **NÃO** escrever a palavra literal "Tópico" nem a palavra literal "Explicação".

   - Cada aspecto é encabeçado pelo seu nome em **CAIXA ALTA SEGUIDO DE DOIS PONTOS** e a explicação técnica, finalizando com a citação bibliográfica: `<strong class="modal-science-heading">TÍTULO DO TÓPICO EM CAIXA ALTA:</strong> Explicação técnica... (Autor, Ano)`.

   - Havendo múltiplas informações/tópicos no mesmo exercício, cada um é separado em seu próprio bloco de parágrafo independente (`.modal-science-block`).

   - As citações bibliográficas são catalogadas e mapeadas no arquivo central `REFERENCIAS_CIENTIFICAS.md`.



### 2.3 Nomes de Exercícios:

- Em **caixa alta**, sucintos e objetivos (ex: `BOX SQUAT`, `REMADA NO BANCO`, `CAT-COW`). Detalhes de carga, cadência ou variações pertencem ao modal ou ao badge de volume.



---



## 3. SINCRONIZAÇÃO E INTEGRIDADE DE CÓPIAS



Para garantir que o aluno e o treinador vejam rigorosamente a mesma interface e dados:

- Todas as cópias de um aluno devem ter hash SHA-256 **idêntico**:

  - `ALUNOS/<nome>.html`

  - `ALUNOS/<PASTA_ALUNO>/<nome>.html`

  - `ALUNOS/<PASTA_ALUNO>/index.html`

  - `TREINO_GUI/<nome>.html`

- Idem para o aplicativo do treinador Gui:

  - `TREINO_GUI/index.html`

  - `TREINO_GUI/treino.html`

- O template padrão para novos alunos é mantido em:

  - `ALUNOS/_MODELO_NOVO_ALUNO/index.html`



---



## 4. PROIBIÇÃO ABSOLUTA DO CARACTERE '&' E TÍTULOS SUCINTOS

- **NUNCA mais usar o símbolo `&`** em nenhum título, subtítulo, botão, badge, aba, card ou texto de interface em nenhum aplicativo.

- Substituir sempre pela conjunção `"e"` por extenso ou eliminar redundâncias para manter os títulos estritamente sucintos e objetivos.

- Exemplos:

  - ❌ `"Ciência & Movimento"` ➔ ✅ `"Ciência e Movimento"`

  - ❌ `"Análise de Vídeos & Biomecânica"` ➔ ✅ `"Análise de Vídeos"` ou `"Análise de Vídeos e Biomecânica"`

  - ❌ `"Mural de Recados & Comunicados"` ➔ ✅ `"Mural de Recados"`

  - ❌ `"Salvar & Enviar"` ➔ ✅ `"Salvar e Enviar"`

  - ❌ `"Composição Corporal & Antropometria"` ➔ ✅ `"Composição Corporal e Antropometria"`

  - ❌ `"Diretrizes Clínicas & Biomecânicas"` ➔ ✅ `"ORIENTAÇÕES GERAIS"`



---



## 5. PERFIL DO ALUNO E HISTÓRICO DE AVALIAÇÕES (PADRÃO OURO)



- **Cabeçalho Limpo (`.student-profile-header-card`):**

  - O cabeçalho exibe estritamente o título da ficha (`FICHA TÉCNICA DO ATLETA / DA ALUNA`), nome, subtítulo e o grid de métricas corporais.

  - **PROIBIDO** colocar botões de formulário ou planilhas no card do cabeçalho (sem botão `Ficha de Avaliação ↗` ou `Planilha e Histórico 📊`).

- **Seção Canônica no Rodapé do Perfil (`#tab-perfil`):**

  - O acesso à ficha de avaliação fica **sempre e exclusivamente ao final da aba Perfil**, sob a seção canônica:

```html

    <!-- ==================== SEÇÃO: HISTÓRICO DE AVALIAÇÕES ==================== -->

    <div style="margin: 26px 4px 14px 4px; display: flex; align-items: baseline; justify-content: space-between; flex-wrap: wrap; gap: 8px;">

      <h3 style="font-size: 1.15rem; font-weight: 800; color: #fff; margin: 0; letter-spacing: -0.01em;">

        📋 Histórico de Avaliações

      </h3>

      <span style="font-size: 0.72rem; font-weight: 700; color: var(--brand-neon); background: rgba(0, 255, 136, 0.1); border: 1px solid rgba(0, 255, 136, 0.25); padding: 3px 8px; border-radius: 12px; text-transform: uppercase;" id="assessmentHistoryBadge">1 Ficha Arquivada</span>

    </div>



    <!-- Lista de Fichas Arquivadas -->

    <div class="assessment-history-list" id="assessmentHistoryList" style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 24px;">

      <!-- Item 1: Ficha de Avaliação Inicial -->

      <div class="assessment-history-card" onclick="openReadOnlyAssessment('inicial')" style="background: var(--card-bg, #11141a); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; padding: 16px 18px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 4px 14px rgba(0,0,0,0.4);" onmouseover="this.style.borderColor='var(--brand-neon)'" onmouseout="this.style.borderColor='rgba(255, 255, 255, 0.1)'">

        <div style="display: flex; flex-direction: column; gap: 4px;">

          <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">

            <span style="font-size: 0.95rem; font-weight: 800; color: #ffffff;" id="historyCardTitle">Ficha de Avaliação Inicial (Anamnese)</span>

            <span style="font-size: 0.68rem; font-weight: 800; color: var(--brand-neon); background: rgba(0, 255, 136, 0.12); border: 1px solid rgba(0, 255, 136, 0.3); padding: 2px 7px; border-radius: 6px;" id="historyCardStatus">✓ Arquivada</span>

          </div>

          <div style="font-size: 0.78rem; color: #94a3b8;" id="historyCardSubtitle">

            Respondida em: <strong style="color: #cbd5e1;">08/10/2026</strong> • Identificação, Saúde e Metas

          </div>

        </div>

        <div style="display: flex; align-items: center; gap: 6px; color: var(--brand-neon); font-size: 0.78rem; font-weight: 700; white-space: nowrap; margin-left: 10px;">

          <span id="historyCardAction">Ver Respostas</span>

          <span style="font-size: 0.95rem;">↗</span>

        </div>

      </div>

    </div>

```

  - Ao clicar na ficha arquivada, executa a função canônica `openReadOnlyAssessment('inicial')`, que abre a ficha em modo **somente leitura**, com todas as respostas travadas, aviso de prontuário técnico e botão de retorno `← Voltar para Perfil`.



---



## 6. ORIENTAÇÕES GERAIS NO PERFIL DO ALUNO (PADRÃO OURO)



- **Título de Seção Canônico e Unificado:**

  Em todos os aplicativos (treinador e alunos), a seção de orientações gerais na aba Perfil (`#tab-perfil`) é sempre encabeçada pelo wrapper canônico externo:

```html

    <!-- ==================== SEÇÃO: ORIENTAÇÕES GERAIS ==================== -->

    <div class="section-title-wrap" style="margin: 26px 4px 14px 4px;">

      <div class="section-title" style="font-size: 1.05rem; font-weight: 800; color: #fff; letter-spacing: 0.04em;">ORIENTAÇÕES GERAIS</div>

    </div>

```

- **Títulos dos Cards Sem Quadro Colorido (Só Emoji e Caixa Alta):**

  Cada quadro (card) de orientação possui borda lateral (`border-left: 3.5px solid <COR>;`), e o título do card dentro da orientação é **sem caixa/badge (sem quadro colorido)**, exibido diretamente em **caixa alta com emoji**, com a cor da fonte condizente com a borda do card:

  - Cyan (`#38bdf8`): `<div style="font-size: 0.92rem; font-weight: 800; color: #38bdf8; letter-spacing: 0.03em; display: flex; align-items: center; gap: 8px;"><span>🔬 TÍTULO EM CAIXA ALTA</span></div>`

  - Verde Neon (`var(--brand-neon)`): `<div style="font-size: 0.92rem; font-weight: 800; color: var(--brand-neon); letter-spacing: 0.03em; display: flex; align-items: center; gap: 8px;"><span>🛡️ TÍTULO EM CAIXA ALTA</span></div>`

  - Roxo (`#c084fc`): `<div style="font-size: 0.92rem; font-weight: 800; color: #c084fc; letter-spacing: 0.03em; display: flex; align-items: center; gap: 8px;"><span>⚡ TÍTULO EM CAIXA ALTA</span></div>`

  - Amarelo (`#fbbf24`): `<div style="font-size: 0.92rem; font-weight: 800; color: #fbbf24; letter-spacing: 0.03em; display: flex; align-items: center; gap: 8px;"><span>💊 TÍTULO EM CAIXA ALTA</span></div>`

  - Rosa / Vermelho (`#f43f5e`): `<div style="font-size: 0.92rem; font-weight: 800; color: #f43f5e; letter-spacing: 0.03em; display: flex; align-items: center; gap: 8px;"><span>🎯 TÍTULO EM CAIXA ALTA</span></div>`



---



## 7. EVOLUÇÃO E COMPOSIÇÃO CORPORAL — FÓRMULA DA MARINHA DOS EUA (PADRÃO OURO)



A Central de Evolução integra o acompanhamento antropométrico dinâmico, baseado na fórmula de circunferências da Marinha dos EUA (U.S. Navy Body Fat Method) e na Relação Cintura-Estatura (RCEst).



### 7.1 Equações Oficiais da Marinha (Hodgdon & Beckett, 1984):

- **Homens:**

  $$\%BF = \frac{495}{1.0324 - 0.19077 \cdot \log_{10}(\text{cintura} - \text{pescoço}) + 0.15456 \cdot \log_{10}(\text{estatura})} - 450$$

- **Mulheres:**

  $$\%BF = \frac{495}{1.29579 - 0.35004 \cdot \log_{10}(\text{cintura} + \text{quadril} - \text{pescoço}) + 0.22100 \cdot \log_{10}(\text{estatura})} - 450$$



### 7.2 Métricas do Painel Canônico:

1. **Peso Atual e Variação ($\Delta$ Peso):** Aferição em kg com indicador de delta luminoso desde a data inicial.

2. **Cintura Abdominal e Variação ($\Delta$ Cintura):** Medida na altura da cicatriz umbilical.

3. **Relação Cintura-Estatura (RCEst):**

   - $\text{RCEst} < 0.50$: Faixa clinicamente ideal (Verde Neon).

   - $0.50 \le \text{RCEst} \le 0.54$: Atenção preventiva (Amarelo `#fbbf24`).

   - $\text{RCEst} \ge 0.55$: Alerta visceral (Vermelho `#f43f5e`).

4. **% de Gordura Corporal (% BF):** Cálculo automático via Marinha ou percentual manual registrado pelo aluno/treinador.

5. **Impacto Articular (Regra de Messier 4:1):** Cada 1 kg de gordura inerte reduzida representa ~4 kg de alívio compressivo patelofemoral e meniscal a cada passo.



### 7.3 Componentes Interativos Obrigatórios:

- **Gráfico de Tendência Vetorial SVG (Estritamente Fisiológico):**

  - Alternância rápida entre 3 curvas temporais reais: **`Peso (kg)`**, **`Cintura (cm)`** e **`Gordura Corporal (% BF)`**.

  - **Proibição de Gráficos Artificiais no Tempo:** Carga articular e força relativa **não devem ser plotadas como curvas de tendência temporal**, pois são métricas conceituais instantâneas ("corte do momento atual").

- **Card Descritivo de Diagnóstico Biomecânico (Corte do Momento Atual):**

  - Posicionado diretamente abaixo do gráfico de evolução, detalha em dois blocos técnicos:

    1. **Carga e Alívio Articular (Messier 4:1):** Cálculo absoluto do alívio compressivo patelofemoral / meniscal por passada com base no momento atual.

    2. **Força Relativa e Alavanca (Zatsiorsky & Kraemer):** Percentual de ganho de potência relativa e menor lastro inerte passivo, com implicações práticas para movimentos ginásticos (pull-ups, HSPU, handstand, muscle-ups).

- **Modais Canônicos:**

  - `#modalAddMedicao`: Formulário direto com botão destacado de Guia de Medidas no topo, persistência automática de rascunho (`draft`), data, peso, cintura, pescoço, quadril (em grid de 2 colunas com rótulo exclusivo `(Obrigatório para mulheres)`), tópico dedicado de % de Gordura (opcional, com seleção de método: Bioimpedância, DEXA, Dobras, Ultrassom, Outro) e campo livre de observações e sensações corporais (eliminados asteriscos e dropdowns de roupas/energia).

  - `#modalInstrucoesMedidas`: Guia ilustrado passo a passo de como aferir cintura, pescoço e quadril (acionado de dentro do modal de medição).

  - `#modalInstrucoesFotos`: Guia de padronização fotográfica (iluminação, distância, postura frente/lado/costas).

  - `#modalRelatorioComposicao`: Laudo técnico completo para visualização, impressão A4 limpa (`@media print`) e compartilhamento direto para WhatsApp do treinador.



---



## 8. IMUTABILIDADE DOS TREINOS CONCLUÍDOS E DEVOLUTIVAS VIA NOTIFICAÇÕES (PADRÃO OURO)



### 8.1 Regra Estrita de Imutabilidade da Estrutura de Treinos Passados/Concluídos:

- **PROIBIÇÃO ABSOLUTA de Alterar Estrutura de Treino Concluído:** Uma vez que um treino foi executado, registrado ou concluído pelo aluno ou treinador, a sua estrutura de exercícios, séries, repetições e blocos (`tab-<dia>`) torna-se um **registro histórico estritamente imutável**.

- **NÃO** alterar nomes de exercícios, adicionar/remover exercícios, reescrever blocos ou desestruturar uma sessão já finalizada no aplicativo para tentar inserir relatórios ou observações posteriores.



### 8.2 Canal Único e Oficial para Relatórios e Devolutivas: Central de Notificações

- Todas as devolutivas técnicas, análises de vídeos de treino, diagnósticos biomecânicos e relatórios de treinamento (tanto para o treinador Gui quanto para os alunos) devem ser transmitidos **exclusivamente através da Central de Notificações (`#notificationsModal`)**:

  - Cada devolutiva ou nova análise gera uma notificação dedicada com status `unread` (ícone temático, título do treino/data, resumo sucinto).

  - A rotina de treinos permanece 100% limpa, íntegra e preservada para consultas, progressões e reexecuções futuras.



### 8.3 Padrão Canônico: Notificação de Vídeo Análise vs. Devolutiva de Treino

1. **Notificação de Análise de Vídeo (Estritamente Alerta e Link Direto):**

   - **PROIBIÇÃO de Duplicar Texto da Análise:** Quando o treinador publica uma nova análise de vídeo, **NÃO se deve transcrever nem duplicar** o diagnóstico, execução, cuidados, dicas, progressões ou exercícios sugeridos dentro da notificação ou em modais intermediários redundantes.

   - **Justificativa:** Toda essa informação técnica detalhada, acompanhada do reprodutor de vídeo, já está catalogada e estruturada na **Central de Análises (`#tab-analises` / `.analysis-card`)**.

   - **Padrão da Notificação:**

     - Ícone temático: `📹` (ou emoji esportivo da skill, ex: `🤸‍♂️`, `⚡`).

     - Título sucinto: `Nova Análise de Vídeo: [Nome da Habilidade / Exercício]`.

     - Descrição enxuta (1 frase): Informa que o vídeo foi analisado pelo treinador com diagnóstico biomecânico e progressões.

     - Ação de clique (`onclick`): Executa diretamente `openAnalysisCardFromNotif('<CARD_ID>', '<CATEGORIA>', '<NOTIF_ID>')`, levando o aluno/treinador com um toque direto ao card expandido e com foco no player de vídeo.



2. **Devolutiva Escrita no Modal de Treino (`#devolutivaTreinoModal`):**

   - **Exclusividade para Anotações da Sessão:** A devolutiva técnica textual detalhada no modal de notificações é reservada **estritamente para responder às observações, relatos de desconforto/dor articular, ajustes de carga ou dúvidas que o aluno/aluna registrar durante a execução do treino**.

   - **Conteúdo da Devolutiva:** O treinador responde pontualmente àquilo que foi anotado pelo praticante nos exercícios daquele dia específico, oferecendo ajustes clínicos, adequação de volume ou orientações para a próxima sessão.



---



## 9. CARDS DE TREINO, SÉRIES, CRONÔMETROS E DESCANSO (PADRÃO OURO)



### 9.1 Quebra Automática de Séries / Checkboxes (`flex-wrap: wrap;`):

- As pílulas de séries e minutos (`.set-pill`) dentro do container (`.sets-container`) devem **permanecer estritamente dentro da largura do card**, nunca ultrapassando a borda da tela no mobile.

- Propriedades obrigatórias:

  ```css

  .sets-container {

    display: flex;

    flex-wrap: wrap;

    gap: 6px;

    align-items: center;

    max-width: 100%;

    box-sizing: border-box;

  }

  .ex-volume-sets-row {

    max-width: 100%;

    box-sizing: border-box;

  }

  ```

- Em treinos com muitas séries (ex: EMOM de 8, 10 ou 12 minutos), os checkboxes quebram naturalmente para as linhas de baixo mantendo espaçamento uniforme e ergonomia de toque.



### 9.2 Botão de Acesso Direto ao Cronômetro para EMOM, AMRAP e TABATA:

- Sempre que houver um bloco ou exercício em formato **EMOM, E3MOM, AMRAP ou TABATA**, deve ser inserido o botão dedicado (`.btn-workout-timer-cta`).

- **Posição Obrigatória:** Imediatamente abaixo do container de séries (`.ex-volume-sets-row`), e **antes** da área de observações e envio da execução (`.ex-bottom-actions`).

- **Estilo Canônico:** Gradiente Ciano Noturno (`background: linear-gradient(90deg, rgba(56, 189, 248, 0.15) 0%, rgba(56, 189, 248, 0.05) 100%), #0e1e2e;`), borda ciano suave (`1px solid rgba(56, 189, 248, 0.45)`), texto em caixa alta e ícone de cronômetro.

- **Estrutura HTML Canônica:**

  ```html

  <div class="workout-timer-cta-wrap">

    <button type="button" class="btn-workout-timer-cta" onclick="openWorkoutTimerWithCard('emom', 8, 'EMOM 8 MIN • CONDICIONAMENTO', 'Minuto 1: 8 a 10 Candlestick Kips\nMinuto 2: 8 Ring Push-ups', this)">

      <svg viewBox="0 0 24 24"><path d="M15 1H9v2h6V1zm-4 13h2V8h-2v6zm8.03-6.61l1.42-1.42c-.43-.51-.9-.99-1.41-1.41l-1.42 1.42C16.07 4.74 14.12 4 12 4c-4.97 0-9 4.03-9 9s4.02 9 9 9 9-4.03 9-9c0-2.12-.74-4.07-1.97-5.61zM12 20c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"/></svg>

      <span>Abrir Cronômetro EMOM (8 min) ➔</span>

    </button>

  </div>

  ```

- **Espelhamento Interativo das Séries no Cronômetro:** O card de referência rápida do timer (`#timerWodQuickReference`) exibe um container espelhado das séries (`#timerWodSetsWrap` e `#timerWodSetsMirror`), permitindo que o aluno ou treinador marque cada round/minuto diretamente no cronômetro conforme o tempo avança, mantendo o card do treino 100% sincronizado.

- **Chamada Canônica:** `openWorkoutTimerWithCard(mode, minutes, title, notes, this)`



### 9.3 Tempo de Descanso Obrigatório no Badge de Volume (`REST`):

- Todo badge de volume de exercício (`.ex-volume-badge`) deve **obrigatoriamente incluir no final a especificação do tempo de descanso** entre séries ou rounds.

- **Formato Padronizado:** `• ⏱️ REST: <TEMPO>`

  - Exemplos Canônicos:

    - `3 SÉRIES • 35-45S ISOMETRIA • ⏱️ REST: 45S`

    - `3 SÉRIES • 5-6 REPS (CADÊNCIA 3010) • ⏱️ REST: 90S`

    - `3 A 4 SÉRIES • 1-2 REPS 🎥 • ⏱️ REST: 2-3 MIN`

    - `8 MINUTOS • 4 PASSAGENS • ⏱️ REST: EMOM (INTERVALO FIXO)`

    - `5 ROUNDS • WALLBALL 9 KG • ⏱️ REST: 1 MIN ENTRE ROUNDS`

    - `3 EXERCÍCIOS • DESCOMPRESSÃO COMPLETA • ⏱️ REST: LIVRE`



### 9.4 Proibição de Aspas Simples / Apóstrofos em Parâmetros de Modais (`openVideoModal`):

- **NUNCA** usar apóstrofo como representação de minutos (ex: `8'`, `12'`, `2'`) dentro dos atributos HTML `onclick="openVideoModal('...')"` para não corromper o delimitador da string JavaScript.

- Usar sempre a palavra `MIN` por extenso (ex: `EMOM 8 MIN`, `AMRAP 2 MIN`).



---



## 10. ANÁLISES DE VÍDEO E DEVOLUTIVAS TÉCNICAS (PADRÃO OURO)



Todas as análises biomecânicas de vídeo gravadas por alunos ou pelo treinador devem seguir rigorosamente a **estrutura pentapartida de blocos visuais**, com destaque temático por cores e ordem estrita:



### 10.1 Estrutura Canônica das Seções de Análise:

1. **`EXECUÇÃO` (Verde Neon `#00ff88`):**

   - Descrição cinemática limpa do movimento filmado: trajetória, posicionamento articular, pegada, ritmo e fases excêntrica/concêntrica observadas.

2. **`DIAGNÓSTICO` (Amarelo Esportivo `#fbbf24`):**

   - Análise clínica e biomecânica minuciosa: preservação articular, ativação de estabilizadores primários, vetores de força e identificação de compensações.

3. **`PROGRESSÃO` (Laranja Coral `#f97316` — Posicionado Imediatamente Antes de Exercícios Sugeridos):**

   - **Feedback 100% Sincero e Construtivo:** Aponta abertamente o que faltou na execução (perda de tensão distal, quebra sutil de alinhamento, micro-hesitação ou falta de protação/depressão).

   - **Diretriz de Aperfeiçoamento:** Explica o ajuste fino necessário e a meta técnica para alcançar a maestria no movimento (o próximo degrau).

4. **`EXERCÍCIOS SUGERIDOS` (Roxo Violeta `#a78bfa`):**

   - Prescrição prática de 2 a 3 educativos específicos com volume e intensidade para corrigir as lacunas identificadas na *Progressão*.

5. **`BASE CIENTÍFICA` (Ciano Técnico `#38bdf8`):**

   - Fundamentação fisiológica, cinesiológica e artigos acadêmicos que respaldam o diagnóstico e as progressões prescritas.



### 10.2 Estilo Visual dos Blocos:

Cada bloco utiliza fundo translúcido suave (`rgba(..., 0.04)`), borda lateral contínua de 2.5px na cor tema do bloco e títulos em negrito com a respectiva cor:

- Execução: `border-left: 2.5px solid var(--brand-neon); color: #00ff88;`

- Diagnóstico: `border-left: 2.5px solid #fbbf24; color: #fbbf24;`

- Progressão: `border-left: 2.5px solid #f97316; color: #f97316;`

- Exercícios sugeridos: `border-left: 2.5px solid #a78bfa; color: #a78bfa;`

- Base científica: `border-left: 2.5px solid #38bdf8; color: #38bdf8;`



---



## 11. PADRÃO OURO PARA TREINOS DE CROSSFIT (CARD ÚNICO DE CONDICIONAMENTO EM LISTA CONTÍNUA)



Em treinos de CrossFit, WODs e condicionamento metabólico de alta intensidade, o atleta treina com mãos calejadas/magnesadas e ritmo cardíaco elevado, **não manuseando o smartphone entre estações ou séries**.



### 11.1 Diretrizes Oficiais de Interface para CrossFit:

1. **Card Único e Nobre de `CONDICIONAMENTO`:**

   - Todo o roteiro do box (Warm Up, blocos do WOD, rounds, repetições e sprints) fica reunido em **um único card de CONDICIONAMENTO** (cor Coral `#e11d48`, classe `.sec-cardio`).

   - Evita a fragmentação em múltiplos cartões soltos, permitindo que o atleta leia a sessão inteira numa única visualização contínua.

2. **Visual de Lousa do Box (`.wod-chalkboard-container`):**

   - Diagramação clara em lista com alto contraste, divisões nítidas por blocos (`.wod-round-block`), contadores destacados de repetições (`.wod-item-rep`) e separadores visuais (`THEN...`).

   - Alertas rápidos incorporados discretamente na própria lista (ex: *step-down obrigatório no caixote*, *sem asa de frango no BMU*).

3. **Pílulas de Conclusão Enxutas (Zero Fricção Durante o WOD):**

   - Pílulas simplificadas para marcar os grandes blocos ou finalizar o WOD de uma só vez ao final do treino (`Tabata 4'`, `Bloco 1 (4R)`, `WOD Concluído 🏁`).

4. **Instruções com Cuidados e Adaptações/Escalas (`openVideoModal`):**

   - O modal `Instruções` é dividido em blocos claros:

     - **EXECUÇÃO:** Estratégia de cadência e ritmo.

     - **CUIDADOS:** Preservação articular (menisco, ombro, punhos).

     - **ADAPTAÇÕES E ESCALAS:** Opções de escala técnica (ex: C2B em vez de BMU, Single Unders em vez de Double Unders, cargas sugeridas).

     - **BASE CIENTÍFICA:** Fisiologia bioenergética e cinemática articular.

5. **Gaveta de Observações Dedicada ao Final da Sessão:**

   - Espaço imediato para o atleta anotar seu tempo oficial no Time Cap, cargas utilizadas e feedback do corpo com tranquilidade no pós-treino.

6. **Disparadores Rápidos de Cronômetro:**

   - Botões compactos de acionamento imediato dos timers da sessão (Tabata, For Time, AMRAP) embutidos diretamente no card.

---



## 12. GESTÃO ESTRATÉGICA DE CARGA E NÃO REPETIÇÃO SEMANAL (AUDITORIA ANATÔMICA)



- **Auditoria Obrigatória de Volume Acumulado:** Antes de prescrever ou estruturar qualquer nova sessão de treino (especialmente blocos de Fortalecimento e Condicionamento), é obrigatório auditar o volume e os grupos musculares já exigidos nos treinos anteriores da mesma semana e das semanas precedentes.

- **Proibição Estrita de Sobrecarga Redundante:** Se um padrão motor ou grupo muscular já recebeu alta demanda de volume ou intensidade na semana (ex: dezenas de Toes-to-Bar, V-ups e flexões de quadril; dezenas de flexões de braço e dips; agachamentos pesados), é **terminantemente proibido** prescrever novamente exercícios isolados ou desgastantes para esse mesmo padrão no bloco de fortalecimento.

- **Cobertura Global e Equilíbrio Muscular:** O bloco de fortalecimento deve ser utilizado com inteligência pedagógica para cobrir áreas anatômicas complementares, sinergistas ou deficitárias da rotina semanal — tais como:

  - **Panturrilhas (Tríceps Sural - Gastrocnêmio e Sóleo no Degrau):** Trabalho excêntrico e pausas isométricas no topo para stiffness do tendão de Aquiles, elasticidade de tornozelo, amortecimento seguro em saltos/aterrissagens gímnicas e preservação meniscal.

  - **Estabilizadores Escapulotorácicos e Manguito:** Shrugs na parede, elevação escapular estrita, trapézio inferior e rotadores externos.

  - **Cadeia Posterior e Extensão:** Eretores da espinha, isquiotibiais e glúteos em extensão (ex: Arch Rocks, pontes) para contrabalançar o excesso de flexão anterior.

  - **Tibiais e Pés:** Fortalecimento intrínseco plantar e tibial anterior.



---



## 13. BIOMETRIA E PERFORMANCE — PSE DE FOSTER + SMARTWATCH + EPOC + TRIMP (PADRÃO OURO)



### 13.1 Ordem Canônica da Central de Evolução (`#evolucaoHubMenu`):

A grade 2x2 da Central de Evolução segue rigorosamente a ordem analítica oficial:

1. **`Composição Corporal`** (Linha 1, Coluna 1 — Laranja Neon)

2. **`Biometria e Performance`** (Linha 1, Coluna 2 — Roxo Neon `#c084fc`, ao lado da Composição)

3. **`Progressão de Técnica`** (Linha 2, Coluna 1 — Azul Neon `#38bdf8`)

4. **`Central de Recordes`** (Linha 2, Coluna 2 — Vermelho Neon `#f43f5e`)



### 13.2 Fluxo de Finalização de Sessão / Checkout Biométrico (`#modalBiometriaSessao`):

Acionado automaticamente ao tocar em `Salvar e Enviar para Coach` ao final de qualquer treino (`completeWorkoutSession(dayId)`) ou na Central de Biometria e Performance:

- **Título Clean em Branco Puro:** Estritamente `Finalizar Treino`, eliminando qualquer subtítulo redundante ou prolixo (ex: proibido `"Registro de Percepção e Biometria"` ou `"PSE (Foster) e Cruzamento com Smartwatch"`).

- **Sem Banners Supérfluos de Celebração:** Eliminação de banners como `🎉 Parabéns! Sessão concluída!`, mantendo a tela focada estritamente no checkout técnico.

- **Duração Real da Sessão:**

  - Campo único destacado em linha inteira com o rótulo **`⏱️ Duração Real (min)`** (sem asterisco `*`), preservando a extração do dia de treino (`dayId`) de forma invisível via `<input type="hidden" id="bio_session_day">` e elemento técnico oculto.

- **Pergunta Clara e Direta:**

  `"De 0 a 10, quão difícil foi o treino de hoje para você?"`

- **Escala Numérica Compacta Pura (0 a 10) em Linha Única:**

  - Grid de 11 botões com números limpos (`.pse-scale-grid` com `grid-template-columns: repeat(11, 1fr)`, botões compactos `.pse-btn` de `0` a `10` com `gap: 3.5px`, altura de `28px` e padding enxuto), acomodando perfeitamente todos os 11 níveis em uma única linha horizontal sem rolagem vertical excessiva.

  - Ao tocar em um número, o badge superior exibe o nível selecionado, descrição verbal e brilho temático (ex: `Nível 7 • Muito Intenso` em laranja, `Nível 0 • Sem Esforço / Repouso` em cinza slate).

- **Anotação Manual do Smartwatch (Sem Upload de Foto/Print e Sem Textos Prolixos):**

  - Card compacto contendo diretamente os inputs numéricos opcionais: `FC Média (bpm)`, `FC Máx (bpm)` e `Calorias (kcal)`, sem textos instrucionais óbvios ou prolixos (ex: proibido `"Anote abaixo os valores que o seu smartwatch marcou na sessão:"`).

  - O aluno apenas anota os números do visor do seu relógio se desejar cruzar com a carga interna.

- **Resultado do Cruzamento / Estímulo Fisiológico:**

  - Título clean em caixa alta: **`ESTÍMULO FISIOLÓGICO`** (eliminando a palavra "Carga" do título e sem contadores redundantes de séries ao lado).

  - Exibição enxuta das métricas (`Carga Interna U.A.`, `Gasto Estimado kcal`, `Densidade / TRIMP`).

  - **Eliminação de parágrafos prolixos descritivos** na tela de checkout.

  - Link sucinto direto para a subpágina: `Relatório completo em Biometria e Performance ↗`.

  - Inclusão do botão unificado `💡 Entenda o Cálculo` (`openInstrucoesBiometriaModal()`), que abre o modal `#modalInstrucoesBiometria`:

    - Explica em termos leigos e amigáveis o que é **Carga Interna (U.A.)**, **Gasto Calórico Real (Trabalho Mecânico + EPOC)**, **Densidade / TRIMP de Banister** e **Consumo de Oxigênio (VO2 Estimado)**.

    - Inclui a **Base Científica** em formato retrátil padrão ouro (`<details class="modal-science-accordion">`), catalogando os estudos de Foster (2001), Børsheim & Bahr (2003), Banister (1991), Uth et al. (2004) e Swain et al. (1994).

- **Botão Único de Conclusão e Envio:**

  - Presença estrita do botão principal verde neon: **`SALVAR E ENVIAR PARA COACH (WHATSAPP)`**.

  - Proibido manter botões secundários redundantes (como *"Apenas Salvar no App"*).

- **Sincronização Reativa e Imediata:**

  - O envio do treino persiste os dados no `localStorage` e na nuvem, atualizando instantaneamente os gráficos e diagnósticos da subpágina de Biometria e Performance sem necessidade de recarregar a tela.



---



## 14. PERIODIZAÇÃO, ARQUIVAMENTO SEMANAL E LIMPEZA DE DIAS NÃO PROGRAMADOS (PADRÃO OURO)



### 14.1 Arquivamento Obrigatório ao Iniciar Novo Microciclo:

- Sempre que for iniciada uma nova semana de treino, a estrutura de treinos e os registros de observações da semana anterior devem ser arquivados no prontuário/histórico de dados do aluno (logs biométricos, cargas registradas e observações de execução).

- O arquivamento preserva a fidelidade da periodização, permitindo auditorias retrospectivas de volume, intensidade e adaptação neuromuscular.



### 14.2 Limpeza Estrita de Dias Não Prescritos (`A DEFINIR`):

- Os dias de treino da nova semana que **ainda não foram montados pelo treinador** devem permanecer estritamente limpos e sem nenhum exercício prescrito (com foco `A DEFINIR`).

- **PROIBIDO** deixar exercícios fantasmas, réplicas residuais da semana anterior ou conteúdos pendentes de definição nos dias ainda não montados, garantindo clareza cognitiva absoluta ao aluno sobre o que é o treino ativo do ciclo.



---



## 15. SESSÕES DE CROSSFIT NO APLICATIVO DO TREINADOR (TREINO_GUI) — PADRÃO MINIMALISTA CONDICIONAMENTO



Para as sessões de CrossFit prescritas especificamente no aplicativo do treinador Gui (`TREINO_GUI`):



### 15.1 Eliminação de Disparadores de Timers e Cronômetros:

- **PROIBIDO** inserir botões ou disparadores de cronômetros/timers (`.btn-wod-timer-trigger`, `.btn-workout-timer-cta`) dentro do card de CrossFit.

- **Justificativa Biomecânica e Prática:** No box de CrossFit, o tempo, os intervalos e o WOD são regidos e cronometrados diretamente pelo relógio/painel digital oficial do box e pelo treinador local, tornando timers no celular redundantes e poluídos durante a sessão.



### 15.2 Eliminação de Quadros e Molduras Coloridas Internas:

- **PROIBIDO** criar molduras, quadros internos coloridos, gradientes artificiais ou blocos estilo "lousa do box" (`.wod-chalkboard-container`, `.wod-chalkboard-section`, fundos vermelhos/rosa para Pay-in, badges coloridos e linhas pontilhadas internas).

- Toda a sessão deve ser apresentada em tipografia clean, com alto contraste sobre o card escuro padrão, sem caixas coloridas aninhadas que sobrecarreguem visualmente a tela.



### 15.3 Alocação Direta na Seção Canônica `CONDICIONAMENTO`:

- A sessão de CrossFit fica **alocada diretamente dentro da seção canônica `CONDICIONAMENTO`** (`.section-card.sec-cardio`), sem fragmentação artificial.

- O título do bloco já comunica com clareza o estímulo metabólico/WOD.

- O roteiro (Warm up, Skill, WOD/Pay-in) é organizado em lista com títulos em caixa alta branca (`#ffffff`) e itens em cinza slate claro (`#cbd5e1`), seguido das pílulas padrão de check-in (`.set-pill`) e da gaveta de observações/vídeo.

---

## 16. LINK DIRETO PARA CHECAGEM DO APP DO ALUNO (OBRIGATÓRIO NAS RESPOSTAS)

- Sempre que criar, atualizar ou editar o aplicativo de qualquer aluno (ou do treinador), **incluir obrigatoriamente na resposta final o link direto clicável** do aplicativo para que o treinador possa abrir e checar imediatamente no navegador (via servidor local `http://localhost:8080/ALUNOS/<PASTA>/<aluno>.html` e link de arquivo [gustavo.html](file:///c:/Users/Gui/Documents/DOMINIO_CORPORAL/ALUNOS/GUSTAVO/gustavo.html)).






