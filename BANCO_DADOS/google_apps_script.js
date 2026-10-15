/**
 * ============================================================================
 * DOMÍNIO CORPORAL — SCRIPT DE BANCO DE DADOS GOOGLE SHEETS (APPS SCRIPT)
 * ============================================================================
 * 
 * Este script transforma uma planilha do Google Sheets em uma API REST
 * para receber e salvar treinos, notas, anamneses e métricas corporais.
 * 
 * COMO INSTALAR NO SEU GOOGLE DRIVE (PASSO A PASSO):
 * 1. Crie uma nova planilha no seu Google Sheets (nomeie como: "Domínio Corporal - Banco de Dados")
 * 2. Na planilha, clique no menu superior: "Extensões" -> "Apps Script"
 * 3. Apague o código padrão que estiver lá e cole todo este arquivo
 * 4. Dê um nome ao projeto no topo (ex: "API Banco Dominio Corporal")
 * 5. Clique no botão azul "Implantar" (canto superior direito) -> "Nova implantação"
 * 6. Na engrenagem ao lado de "Selecione o tipo", escolha "App da Web"
 * 7. Configure:
 *    - Descrição: "API Banco de Dados v1"
 *    - Executar como: "Eu (seu e-mail)"
 *    - Quem pode acessar: "Qualquer pessoa" (OBRIGATÓRIO para o app do aluno conseguir enviar sem login Google)
 * 8. Clique em "Implantar" e conceda as permissões de acesso
 * 9. Copie a "URL do app da Web" gerada (termina em "/exec")
 * 10. Cole essa URL nas configurações do seu app!
 * ============================================================================
 */

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000); // Aguarda até 10s para evitar conflito de gravação simultânea

  try {
    var rawData = e.postData && e.postData.contents ? e.postData.contents : "{}";
    var payload = JSON.parse(rawData);
    var action = payload.action || "salvarTreino";
    var data = payload.data || {};
    var ss = SpreadsheetApp.getActiveSpreadsheet();

    if (action === "salvarTreino") {
      var sheet = getOrCreateSheet(ss, "Treinos Logs", [
        "Data/Hora Registro", "Data do Treino", "Aluno Slug", "Aluno Nome", "Dia/Foco", 
        "Séries Feitas", "Total Séries", "Aderência %", "Notas Gerais", "Notas Exercícios (JSON)"
      ]);
      sheet.appendRow([
        new Date().toISOString(),
        data.data_treino || new Date().toLocaleDateString("pt-BR"),
        data.aluno_slug || "gui",
        data.aluno_nome || "Guilherme Lemos",
        data.dia_id || "geral",
        data.series_concluidas || 0,
        data.total_series || 0,
        (data.aderencia_pct || 100) + "%",
        data.notas_gerais || "",
        JSON.stringify(data.notas_exercicios || {})
      ]);
      return jsonResponse({ status: "success", message: "Treino registrado com sucesso no Sheets" });
    }

    if (action === "salvarMedicao") {
      var sheetMed = getOrCreateSheet(ss, "Medições Corporais", [
        "Data/Hora Registro", "Data Medição", "Aluno Slug", "Peso (kg)", "Cintura (cm)", 
        "Pescoço (cm)", "Quadril (cm)", "% BF", "RCEst", "Vestimenta", "Energia", "Notas"
      ]);
      sheetMed.appendRow([
        new Date().toISOString(),
        data.data_medicao || new Date().toLocaleDateString("pt-BR"),
        data.aluno_slug || "gui",
        data.peso || "",
        data.cintura || "",
        data.pescoco || "",
        data.quadril || "",
        data.bf_pct || "",
        data.rcest || "",
        data.vestimenta || "",
        data.energia || "",
        data.notas || ""
      ]);
      return jsonResponse({ status: "success", message: "Medição registrada com sucesso no Sheets" });
    }

    if (action === "salvarNotaExercicio") {
      var sheetNotas = getOrCreateSheet(ss, "Exercícios Notas", [
        "Data/Hora Registro", "Aluno Slug", "Exercício ID", "Exercício Nome", "Nota Técnica"
      ]);
      sheetNotas.appendRow([
        new Date().toISOString(),
        data.aluno_slug || "gui",
        data.exercicio_id || "",
        data.exercicio_nome || "",
        data.nota || ""
      ]);
      return jsonResponse({ status: "success", message: "Nota registrada com sucesso no Sheets" });
    }

    if (action === "salvarAvaliacao") {
      var sheetAv = getOrCreateSheet(ss, "Avaliações Anamnese", [
        "Data/Hora Registro", "Aluno Slug", "Tipo", "Respostas (JSON)"
      ]);
      sheetAv.appendRow([
        new Date().toISOString(),
        data.aluno_slug || "aluno",
        data.tipo || "inicial",
        JSON.stringify(data.respostas || {})
      ]);
      return jsonResponse({ status: "success", message: "Avaliação registrada com sucesso no Sheets" });
    }

    return jsonResponse({ status: "error", message: "Ação desconhecida: " + action });

  } catch (err) {
    return jsonResponse({ status: "error", message: err.toString() });
  } finally {
    lock.releaseLock();
  }
}

function doGet(e) {
  // Retorna status e dados básicos para verificação de saúde da API
  return jsonResponse({
    status: "online",
    name: "API Domínio Corporal Google Sheets",
    version: "1.0",
    timestamp: new Date().toISOString()
  });
}

function getOrCreateSheet(ss, name, headers) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    sheet.appendRow(headers);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight("bold").setBackground("#0f172a").setFontColor("#38bdf8");
  }
  return sheet;
}

function jsonResponse(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
