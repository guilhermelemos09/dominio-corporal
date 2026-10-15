/* ==========================================================================
   DOMÍNIO CORPORAL — CLIENTE DE BANCO DE DADOS NA NUVEM (OFFLINE-FIRST)
   Suporte a: Supabase (REST), Google Sheets (Apps Script Webhook) e LocalStorage
   ========================================================================== */

window.DominioDB = (function() {
  const STORAGE_CONFIG_KEY = 'dominio_db_custom_config';
  const SYNC_QUEUE_KEY = 'dominio_db_sync_queue';

  // Configurações Padrão
  const defaultConfig = {
    provider: 'auto', // 'auto' | 'supabase' | 'sheets' | 'local' | 'hybrid'
    supabaseUrl: '',
    supabaseAnonKey: '',
    sheetsUrl: '',
    athleteSlug: 'gui',
    athleteName: 'Guilherme Lemos'
  };

  function getConfig() {
    try {
      const saved = localStorage.getItem(STORAGE_CONFIG_KEY);
      const appDefault = window.DOMINIO_APP_CONFIG || {};
      return { ...defaultConfig, ...appDefault, ...(saved ? JSON.parse(saved) : {}) };
    } catch (e) {
      return { ...defaultConfig, ...(window.DOMINIO_APP_CONFIG || {}) };
    }
  }

  function saveConfig(cfg) {
    try {
      localStorage.setItem(STORAGE_CONFIG_KEY, JSON.stringify(cfg));
      updateCloudStatusUI();
      return true;
    } catch (e) {
      console.error('[DominioDB] Erro ao salvar configuração:', e);
      return false;
    }
  }

  function getQueue() {
    try {
      return JSON.parse(localStorage.getItem(SYNC_QUEUE_KEY) || '[]');
    } catch (e) {
      return [];
    }
  }

  function saveQueue(q) {
    try {
      localStorage.setItem(SYNC_QUEUE_KEY, JSON.stringify(q));
    } catch (e) {}
    updateCloudStatusUI();
  }

  function enqueue(action, payload) {
    const q = getQueue();
    q.push({
      id: 'sync_' + Date.now() + '_' + Math.random().toString(36).substr(2, 5),
      action: action,
      payload: payload,
      timestamp: new Date().toISOString()
    });
    saveQueue(q);
  }

  async function sendToSupabase(table, data) {
    const cfg = getConfig();
    if (!cfg.supabaseUrl || !cfg.supabaseAnonKey) {
      throw new Error('Supabase não configurado');
    }
    const cleanUrl = cfg.supabaseUrl.replace(/\/+$/, '');
    const url = `${cleanUrl}/rest/v1/${table}`;
    const resp = await fetch(url, {
      method: 'POST',
      headers: {
        'apikey': cfg.supabaseAnonKey,
        'Authorization': `Bearer ${cfg.supabaseAnonKey}`,
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify(data)
    });
    if (!resp.ok) {
      const errTxt = await resp.text().catch(() => '');
      throw new Error(`Erro Supabase (${resp.status}): ${errTxt}`);
    }
    return true;
  }

  async function sendToSheets(action, data) {
    const cfg = getConfig();
    if (!cfg.sheetsUrl) {
      throw new Error('Google Sheets não configurado');
    }
    // Google Apps Script Web App (doPost) com no-cors para evitar bloqueios de redirecionamento 302
    await fetch(cfg.sheetsUrl, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain' },
      body: JSON.stringify({ action: action, data: data })
    });
    return true;
  }

  async function dispatchCloud(action, data) {
    const cfg = getConfig();
    let sentSupabase = false;
    let sentSheets = false;

    const useSupabase = cfg.supabaseUrl && cfg.supabaseAnonKey && (cfg.provider === 'auto' || cfg.provider === 'supabase' || cfg.provider === 'hybrid');
    const useSheets = cfg.sheetsUrl && (cfg.provider === 'sheets' || cfg.provider === 'hybrid' || (cfg.provider === 'auto' && !cfg.supabaseUrl));

    if (!useSupabase && !useSheets) {
      return true; // Modo local puro
    }

    // 1. Supabase
    if (useSupabase) {
      try {
        if (action === 'salvarTreino') {
          await sendToSupabase('treinos_logs', {
            aluno_slug: data.aluno_slug || cfg.athleteSlug,
            dia_id: data.dia_id,
            data_treino: data.data_treino,
            series_concluidas: data.series_concluidas || 0,
            total_series: data.total_series || 0,
            aderencia_pct: data.aderencia_pct || 100,
            notas_gerais: data.notas_gerais || '',
            notas_exercicios: data.notas_exercicios || {}
          });
          sentSupabase = true;
        } else if (action === 'salvarMedicao') {
          await sendToSupabase('medicoes_corporais', {
            aluno_slug: data.aluno_slug || cfg.athleteSlug,
            data_medicao: data.data_medicao,
            peso: data.peso,
            cintura: data.cintura,
            pescoco: data.pescoco || null,
            quadril: data.quadril || null,
            bf_pct: data.bf_pct || null,
            rcest: data.rcest || null,
            vestimenta: data.vestimenta || null,
            energia: data.energia || null,
            notas: data.notas || null
          });
          sentSupabase = true;
        } else if (action === 'salvarNotaExercicio') {
          await sendToSupabase('exercicios_notas', {
            aluno_slug: data.aluno_slug || cfg.athleteSlug,
            exercicio_id: data.exercicio_id,
            exercicio_nome: data.exercicio_nome || '',
            nota: data.nota,
            data_registro: data.data_registro || new Date().toLocaleDateString('pt-BR')
          });
          sentSupabase = true;
        } else if (action === 'salvarAvaliacao') {
          await sendToSupabase('avaliacoes_anamnese', {
            aluno_slug: data.aluno_slug || cfg.athleteSlug,
            tipo: data.tipo || 'inicial',
            respostas: data.respostas || {}
          });
          sentSupabase = true;
        }
      } catch (err) {
        console.warn('[DominioDB] Erro de envio para o Supabase:', err);
      }
    }

    // 2. Google Sheets
    if (useSheets) {
      try {
        await sendToSheets(action, data);
        sentSheets = true;
      } catch (err) {
        console.warn('[DominioDB] Erro de envio para o Sheets:', err);
      }
    }

    const ok = (useSupabase && sentSupabase) || (useSheets && sentSheets);
    if (!ok) {
      enqueue(action, data);
      return false;
    }
    return true;
  }

  // Descarregar fila quando online
  async function flushSyncQueue() {
    const q = getQueue();
    if (q.length === 0) return 0;
    const remaining = [];
    let synced = 0;

    for (const item of q) {
      try {
        const ok = await dispatchCloud(item.action, item.payload);
        if (ok) synced++;
        else remaining.push(item);
      } catch (e) {
        remaining.push(item);
      }
    }

    saveQueue(remaining);
    return synced;
  }

  // Métodos de Fachada
  async function salvarTreinoConcluido(dadosTreino) {
    const cfg = getConfig();
    const payload = {
      aluno_slug: cfg.athleteSlug,
      aluno_nome: cfg.athleteName,
      ...dadosTreino
    };
    return dispatchCloud('salvarTreino', payload);
  }

  async function salvarMedicao(medicao) {
    const cfg = getConfig();
    const payload = {
      aluno_slug: cfg.athleteSlug,
      ...medicao
    };
    return dispatchCloud('salvarMedicao', payload);
  }

  async function salvarNotaExercicio(exId, exName, nota) {
    const cfg = getConfig();
    const payload = {
      aluno_slug: cfg.athleteSlug,
      exercicio_id: exId,
      exercicio_nome: exName,
      nota: nota,
      data_registro: new Date().toLocaleDateString('pt-BR')
    };
    return dispatchCloud('salvarNotaExercicio', payload);
  }

  async function salvarAvaliacao(tipo, respostas) {
    const cfg = getConfig();
    const payload = {
      aluno_slug: cfg.athleteSlug,
      tipo: tipo || 'inicial',
      respostas: respostas
    };
    return dispatchCloud('salvarAvaliacao', payload);
  }

  async function testConnection(testCfg) {
    const cfg = testCfg || getConfig();
    const results = { supabase: null, sheets: null };

    if (cfg.supabaseUrl && cfg.supabaseAnonKey) {
      try {
        const cleanUrl = cfg.supabaseUrl.replace(/\/+$/, '');
        const resp = await fetch(`${cleanUrl}/rest/v1/alunos?select=count`, {
          headers: {
            'apikey': cfg.supabaseAnonKey,
            'Authorization': `Bearer ${cfg.supabaseAnonKey}`
          }
        });
        results.supabase = resp.ok;
      } catch (e) {
        results.supabase = false;
      }
    }

    if (cfg.sheetsUrl) {
      try {
        // Teste de conectividade simples
        await fetch(cfg.sheetsUrl, { method: 'GET', mode: 'no-cors' });
        results.sheets = true;
      } catch (e) {
        results.sheets = false;
      }
    }

    return results;
  }

  function getStatus() {
    const cfg = getConfig();
    const q = getQueue();
    const hasSupabase = Boolean(cfg.supabaseUrl && cfg.supabaseAnonKey);
    const hasSheets = Boolean(cfg.sheetsUrl);

    let provider = 'local';
    let providerLabel = 'Local (Offline)';

    if (hasSupabase && hasSheets) {
      provider = 'hybrid';
      providerLabel = 'Híbrido (Supabase + Sheets)';
    } else if (hasSupabase) {
      provider = 'supabase';
      providerLabel = 'Supabase';
    } else if (hasSheets) {
      provider = 'sheets';
      providerLabel = 'Google Sheets';
    }

    return {
      isConfigured: hasSupabase || hasSheets,
      provider: provider,
      providerLabel: providerLabel,
      queueCount: q.length,
      online: navigator.onLine
    };
  }

  function updateCloudStatusUI() {
    const status = getStatus();
    const dot = document.getElementById('cloudStatusDot');
    const label = document.getElementById('cloudStatusLabel');
    const badge = document.getElementById('btnCloudStatusIndicator');
    if (!dot || !label) return;

    if (!status.isConfigured) {
      dot.style.background = '#94a3b8'; // Cinza
      dot.style.boxShadow = 'none';
      label.textContent = 'Local';
      if (badge) badge.title = 'Modo Local (Clique para configurar banco de dados na nuvem)';
    } else if (status.queueCount > 0) {
      dot.style.background = '#fbbf24'; // Amarelo
      dot.style.boxShadow = '0 0 8px rgba(251, 191, 36, 0.6)';
      label.textContent = `${status.queueCount} pendente${status.queueCount > 1 ? 's' : ''}`;
      if (badge) badge.title = `${status.queueCount} registros aguardando envio para ${status.providerLabel}`;
    } else {
      dot.style.background = '#00ff88'; // Verde Neon
      dot.style.boxShadow = '0 0 8px rgba(0, 255, 136, 0.6)';
      label.textContent = status.providerLabel.split(' ')[0];
      if (badge) badge.title = `Conectado a ${status.providerLabel}`;
    }
  }

  // Listener para retorno de conexão
  window.addEventListener('online', () => {
    updateCloudStatusUI();
    flushSyncQueue();
  });
  window.addEventListener('offline', () => {
    updateCloudStatusUI();
  });

  return {
    getConfig: getConfig,
    saveConfig: saveConfig,
    salvarTreinoConcluido: salvarTreinoConcluido,
    salvarMedicao: salvarMedicao,
    salvarNotaExercicio: salvarNotaExercicio,
    salvarAvaliacao: salvarAvaliacao,
    flushSyncQueue: flushSyncQueue,
    testConnection: testConnection,
    getStatus: getStatus,
    updateCloudStatusUI: updateCloudStatusUI
  };
})();
