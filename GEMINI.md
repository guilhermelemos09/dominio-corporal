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
  - **Eliminação Absoluta de Parênteses e do Sufixo `-feira`:** Os títulos dos dias de treino na barra superior (`#dedicatedBarTitle` / `dayNames`) devem ser **estritamente em caixa alta**, com o nome do dia isolado (sem `-feira`), separados do foco da sessão exclusivamente por **barra vertical (`|`)**:
    - ❌ Proibido: `Quinta-feira (Handstand e Contemporâneo)` ou `SEGUNDA • Crossfit` ou `TREINO VIAGEM — SESSÃO A`
    - ✅ Canônico: `QUINTA | HANDSTAND E CONTEMPORÂNEO`, `SEGUNDA | BOX CROSSFIT`, `SEGUNDA | SESSÃO A`
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
    <span class="meta-item">📍 Academia do Prédio | SP</span>
    <span class="meta-separator">|</span>
    <span class="meta-item">⏳ ~50 a 60 min</span>
  </div>
  ```
- **Pop-up sem duplicidade:** O popover exibe estritamente a tag de cabeçalho `🛡️ ORIENTAÇÕES` no topo, ocultando títulos repetidos abaixo para eliminar redundância visual.
- **Cor Canônica do Botão e Pop-up:** Tom Cyan / Azul Técnico (`#38bdf8` com fundo `rgba(56, 189, 248, 0.10)` e borda `rgba(56, 189, 248, 0.35)`), transmitindo suporte clínico e instrucional sem competir visualmente com os botões verdes de ação ou conclusão de séries.

### 1.2 Padrão Dark Cyber Glass na Página Principal (Home Hub) e Demais Páginas:
- A elegância do Dark Cyber Glass é estendida à Página Principal (Home Hub) e seções estruturais do aplicativo:
  - **Card do Atleta (`.athlete-highlight-card`):** Caixa fechada com fundo dark e névoa neon suave (`rgba(0, 255, 136, 0.12)`), borda lateral esquerda de `4.5px solid var(--brand-neon)`, título com nome do atleta no topo e botões de ação internos.
  - **Card de Ferramentas (`.tools-highlight-card`):** Caixa fechada no mesmo padrão visual do card do atleta, com fundo dark e névoa ciano suave (`rgba(56, 189, 248, 0.12)`), borda lateral esquerda de `4.5px solid #38bdf8`, título `FERRAMENTAS` em caixa alta pura `1.05rem` no topo e botões internos (`Timers`, `Análises`, `Evolução`).
  - **Cabeçalho da Rotina de Treino (`#trainingHubSection .training-section-header`):** Padrão Minimalista Clean, completamente transparente e sem bordas/caixas (`background: transparent; border: none;`), com o título `ROTINA DE TREINO` direto em branco puro `1.05rem`, peso 900, dando respiro visual e evidenciando os cards de treino logo abaixo.
  - **Cards de Rotina (`.training-day-card`):** Borda lateral contínua de `4.5px solid var(--brand-neon)`, fundo escuro com névoa neon suave e interação em hover translúcido.
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
- **Gráfico de Tendência Vetorial SVG:** Curva temporal com alternância ágil entre `Peso (kg)` e `Cintura (cm) e RCEst`.
- **Modais Canônicos:**
  - `#modalAddMedicao`: Formulário completo com data, peso, cintura, pescoço, quadril (mulheres), % BF manual opcional, vestimenta, energia e fotos.
  - `#modalInstrucoesMedidas`: Guia ilustrado passo a passo de como aferir cintura, pescoço e quadril.
  - `#modalInstrucoesFotos`: Guia de padronização fotográfica (iluminação, distância, postura frente/lado/costas).
  - `#modalRelatorioComposicao`: Laudo técnico completo para visualização, impressão A4 limpa (`@media print`) e compartilhamento direto para WhatsApp do treinador.



