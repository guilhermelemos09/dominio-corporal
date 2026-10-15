-- ============================================================================
-- DOMÍNIO CORPORAL — SCHEMA OFICIAL DE BANCO DE DADOS (SUPABASE / POSTGRESQL)
-- ============================================================================
-- Como executar no Supabase:
-- 1. Acesse o seu projeto em https://supabase.com/dashboard
-- 2. No menu lateral esquerdo, clique em "SQL Editor"
-- 3. Clique em "+ New query", cole todo este código e clique em "Run" (botão verde)
-- ============================================================================

-- Extensão para geração de UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. TABELA DE ALUNOS E TREINADOR
CREATE TABLE IF NOT EXISTS public.alunos (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    papel TEXT NOT NULL DEFAULT 'aluno', -- 'treinador' ou 'aluno'
    genero TEXT DEFAULT 'M',             -- 'M' ou 'F' (para fórmulas de composição)
    estatura_cm NUMERIC(5,2),
    data_inicio DATE DEFAULT CURRENT_DATE,
    ativo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- 2. TABELA DE LOGS DE TREINOS CONCLUÍDOS
CREATE TABLE IF NOT EXISTS public.treinos_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    aluno_slug TEXT NOT NULL REFERENCES public.alunos(slug) ON DELETE CASCADE,
    dia_id TEXT NOT NULL,                -- 'segunda', 'terca', 'quarta', 'treino_a', etc.
    data_treino TEXT NOT NULL,           -- '15/10/2026'
    series_concluidas INTEGER NOT NULL DEFAULT 0,
    total_series INTEGER NOT NULL DEFAULT 0,
    aderencia_pct INTEGER NOT NULL DEFAULT 100,
    notas_gerais TEXT,
    notas_exercicios JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- 3. TABELA DE OBSERVAÇÕES E CARGAS POR EXERCÍCIO
CREATE TABLE IF NOT EXISTS public.exercicios_notas (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    aluno_slug TEXT NOT NULL REFERENCES public.alunos(slug) ON DELETE CASCADE,
    exercicio_id TEXT NOT NULL,
    exercicio_nome TEXT,
    nota TEXT NOT NULL,
    data_registro TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- 4. TABELA DE MEDIÇÕES E COMPOSIÇÃO CORPORAL (FÓRMULA DA MARINHA)
CREATE TABLE IF NOT EXISTS public.medicoes_corporais (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    aluno_slug TEXT NOT NULL REFERENCES public.alunos(slug) ON DELETE CASCADE,
    data_medicao TEXT NOT NULL,
    peso NUMERIC(5,2) NOT NULL,
    cintura NUMERIC(5,2) NOT NULL,
    pescoco NUMERIC(5,2),
    quadril NUMERIC(5,2),
    bf_pct NUMERIC(4,1),
    rcest NUMERIC(4,3),
    vestimenta TEXT,
    energia TEXT,
    notas TEXT,
    fotos_json JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- 5. TABELA DE AVALIAÇÕES E ANAMNESE TÉCNICA
CREATE TABLE IF NOT EXISTS public.avaliacoes_anamnese (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    aluno_slug TEXT NOT NULL REFERENCES public.alunos(slug) ON DELETE CASCADE,
    tipo TEXT NOT NULL DEFAULT 'inicial', -- 'inicial', 'reavaliacao'
    respostas JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- 6. TABELA DA CENTRAL DE NOTIFICAÇÕES E DEVOLUTIVAS
CREATE TABLE IF NOT EXISTS public.notificacoes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    destinatario_slug TEXT NOT NULL REFERENCES public.alunos(slug) ON DELETE CASCADE,
    remetente_slug TEXT NOT NULL DEFAULT 'gui',
    tipo TEXT NOT NULL DEFAULT 'feedback', -- 'feedback', 'analise', 'comunicado'
    titulo TEXT NOT NULL,
    resumo TEXT NOT NULL,
    conteudo_modal JSONB DEFAULT '{}'::jsonb,
    lida BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc', NOW())
);

-- ============================================================================
-- ÍNDICES DE PERFORMANCE
-- ============================================================================
CREATE INDEX IF NOT EXISTS idx_treinos_logs_aluno ON public.treinos_logs(aluno_slug);
CREATE INDEX IF NOT EXISTS idx_treinos_logs_data ON public.treinos_logs(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_exercicios_notas_aluno ON public.exercicios_notas(aluno_slug, exercicio_id);
CREATE INDEX IF NOT EXISTS idx_medicoes_aluno ON public.medicoes_corporais(aluno_slug, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_notificacoes_destinatario ON public.notificacoes(destinatario_slug, lida);

-- ============================================================================
-- PERMISSÕES E POLÍTICAS DE ACESSO (ROW LEVEL SECURITY - RLS)
-- Permite leitura e escrita pelo anon_key do cliente web dos apps
-- ============================================================================
ALTER TABLE public.alunos ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.treinos_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.exercicios_notas ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.medicoes_corporais ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.avaliacoes_anamnese ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.notificacoes ENABLE ROW LEVEL SECURITY;

-- Políticas públicas para o aplicativo (anon key)
DROP POLICY IF EXISTS "Anon Select Alunos" ON public.alunos;
CREATE POLICY "Anon Select Alunos" ON public.alunos FOR SELECT TO anon USING (true);

DROP POLICY IF EXISTS "Anon All Treinos" ON public.treinos_logs;
CREATE POLICY "Anon All Treinos" ON public.treinos_logs FOR ALL TO anon USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "Anon All Notas" ON public.exercicios_notas;
CREATE POLICY "Anon All Notas" ON public.exercicios_notas FOR ALL TO anon USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "Anon All Medicoes" ON public.medicoes_corporais;
CREATE POLICY "Anon All Medicoes" ON public.medicoes_corporais FOR ALL TO anon USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "Anon All Avaliacoes" ON public.avaliacoes_anamnese;
CREATE POLICY "Anon All Avaliacoes" ON public.avaliacoes_anamnese FOR ALL TO anon USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "Anon All Notificacoes" ON public.notificacoes;
CREATE POLICY "Anon All Notificacoes" ON public.notificacoes FOR ALL TO anon USING (true) WITH CHECK (true);

-- Permissões de concessão para a role anon e authenticated
GRANT USAGE ON SCHEMA public TO anon, authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA public TO anon, authenticated;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO anon, authenticated;

-- ============================================================================
-- DADOS INICIAIS (SEED)
-- ============================================================================
INSERT INTO public.alunos (slug, nome, papel, genero, estatura_cm)
VALUES
    ('gui', 'Guilherme Lemos', 'treinador', 'M', 180.0),
    ('helenice', 'Helenice Rosa', 'aluna', 'F', 160.0),
    ('jean', 'Jean Hilário', 'aluno', 'M', 178.0)
ON CONFLICT (slug) DO UPDATE
SET nome = EXCLUDED.nome, papel = EXCLUDED.papel;
