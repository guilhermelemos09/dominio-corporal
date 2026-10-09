# DIRETRIZES OFICIAIS DE ARQUITETURA & UI — DOMÍNIO CORPORAL

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

### Estrutura HTML Canônica:
```html
<div class="section-card sec-aquecimento"> <!-- ou sec-forca, sec-flexibilidade, sec-cardio, sec-skills -->
  <div class="section-header" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
    <div class="section-title-wrap">
      <div class="section-title">ATIVAÇÃO</div>
    </div>
    <div class="session-meta-chips">
      <span class="meta-chip meta-chip-time">⏱️ ~12 min</span>
    </div>
  </div>
  ...
</div>
```

---

## 2. CARDS DE EXERCÍCIO (PADRÃO OURO)

### 2.1 Botão Único Unificado: `Vídeo | Instruções`
- Todos os cards de exercício possuem um **único botão primário** posicionado ao lado do título:
  ```html
  <div class="ex-title">
    <span>NOME DO EXERCÍCIO</span>
    <button type="button" class="btn-video" onclick="openVideoModal('Título', 'Descrição', 'URL_DO_VIDEO')">
      <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg> <span>Vídeo | Instruções</span>
    </button>
  </div>
  ```
- **NUNCA** incluir linhas ou botões separados de dicas (`🛡️ Cuidados`, `🔧 Instruções`, `💡 Dicas`, `ex-cues-row`).
- **Exercícios sem vídeo:** Devem manter o mesmo botão `Vídeo | Instruções` passando `''` como URL (`openVideoModal(titulo, desc, '')`). A função `openVideoModal` esconde o container do vídeo automaticamente (`.video-container { display: none; }`), exibindo o texto de instruções de forma limpa.

### 2.2 Estrutura do Texto no Modal (`openVideoModal`):
A descrição do modal deve seguir rigorosamente a ordem:
1. `<b>Execução:</b> ...` *(PROIBIDO usar "Na prática")*
2. `<b>Cuidados:</b> ...`
3. `<b>Dicas:</b> ...` *(quando houver)*
4. `<b>Base científica:</b> ...` *(SEMPRE ao final de tudo)*

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
