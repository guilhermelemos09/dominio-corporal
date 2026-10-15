# 🏛️ ARQUITETURA DE BANCO DE DADOS — DOMÍNIO CORPORAL

Este diretório contém os scripts e esquemas oficiais para integração do banco de dados na nuvem da plataforma **Domínio Corporal**.

---

## ⚡ OPÇÃO 1 (RECOMENDADA): SUPABASE (PostgreSQL Serverless)

O **Supabase** é a escolha ideal para o Domínio Corporal porque fornece latência instantânea (< 100ms), suporte a notificações em tempo real, consultas relacionais e integração nativa com PWAs hospedados no GitHub Pages sem requerer servidor próprio.

### Como Ativar em 2 Minutos:
1. Acesse [supabase.com](https://supabase.com) e crie uma conta gratuita (ou faça login com GitHub).
2. Clique em **"New project"** (escolha um nome, ex: `dominio-corporal-db`, e região `São Paulo (sa-east-1)`).
3. No menu lateral do projeto, clique no ícone **SQL Editor** (`>_`).
4. Clique em **"+ New query"**, abra o arquivo [`schema.sql`](./schema.sql), copie todo o seu conteúdo, cole no editor e clique no botão verde **"Run"**.
   - As 6 tabelas (`alunos`, `treinos_logs`, `exercicios_notas`, `medicoes_corporais`, `avaliacoes_anamnese`, `notificacoes`), índices e políticas de segurança serão criados instantaneamente.
5. No menu lateral, clique em **Project Settings** (engrenagem) -> **API**.
6. Copie os dois valores:
   - **Project URL:** `https://xxxxxxxxxxxx.supabase.co`
   - **Project API Keys -> `anon` `public`:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`
7. No aplicativo (menu Perfil -> *Nuvem & Banco de Dados* ou diretamente no código), cole a URL e a Chave Anon.
8. Pronto! Todos os treinos, observações, pesagens e notificações passam a ser sincronizados em tempo real na nuvem!

---

## 📊 OPÇÃO 2: GOOGLE SHEETS (via Google Apps Script)

Se você preferir visualizar todos os dados consolidados em uma planilha tradicional do Google Sheets no seu Google Drive:

### Como Ativar:
1. Abra o [Google Sheets](https://sheets.google.com) e crie uma nova planilha (ex: `Domínio Corporal - Banco de Dados`).
2. No menu superior da planilha, clique em **Extensões** -> **Apps Script**.
3. Apague o código padrão e cole todo o conteúdo do arquivo [`google_apps_script.js`](./google_apps_script.js).
4. Clique em **Implantar** (botão azul) -> **Nova implantação**.
5. Selecione o tipo **App da Web** (ícone de engrenagem) e configure:
   - **Executar como:** *Eu (seu e-mail)*
   - **Quem pode acessar:** *Qualquer pessoa* (imprescindível para o app do aluno conseguir enviar sem pedir login do Google).
6. Clique em **Implantar**, autorize o acesso da sua conta Google e copie a **URL do app da Web** gerada (termina com `/exec`).
7. Cole a URL no aplicativo. O script criará automaticamente as abas formatadas na planilha:
   - `Treinos Logs`
   - `Medições Corporais`
   - `Exercícios Notas`
   - `Avaliações Anamnese`

---

## 🔄 RESILIÊNCIA OFFLINE-FIRST (GARANTIA DE FUNCIONAMENTO)

O módulo cliente `DominioDB` implementa a arquitetura **Offline-First com Fallback Elegante**:
- **0ms de Bloqueio:** O aluno e o treinador nunca ficam travados esperando resposta de rede. Qualquer ação salva no `localStorage` no mesmo milissegundo.
- **Fila de Sincronização (`Sync Queue`):** Se a academia estiver sem sinal de internet ou a requisição falhar, os dados são enfileirados localmente (`dominio_db_sync_queue`) e enviados automaticamente assim que o dispositivo recuperar a conexão.
- **Modo Local:** Enquanto nenhuma chave de nuvem for inserida, o app opera normalmente no modo local sem nenhum erro no console.
