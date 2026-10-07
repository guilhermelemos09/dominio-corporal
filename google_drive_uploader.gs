/**
 * =========================================================================
 * DOMÍNIO CORPORAL — SCRIPT DE UPLOAD DE VÍDEOS PARA GOOGLE DRIVE
 * =========================================================================
 * 
 * Este script recebe os vídeos gravados diretamente do aplicativo Web,
 * organiza em pastas no seu Google Drive e envia um e-mail de notificação
 * instantânea para o Prof. Gui Lemos.
 * 
 * COMO INSTALAR (LEVA MENOS DE 2 MINUTOS):
 * 1. Acesse: https://script.google.com/
 * 2. Clique no botão "+ Novo projeto" (canto superior esquerdo)
 * 3. Apague o código padrão que estiver lá e cole todo este arquivo
 * 4. Dê um nome ao projeto (ex: "Upload Videos Dominio Corporal")
 * 5. Clique no botão azul "Implantar" (canto superior direito) -> "Nova implantação"
 * 6. Na engrenagem ao lado de "Selecione o tipo", escolha "App da Web"
 * 7. Preencha os campos:
 *    - Descrição: "API Upload Videos"
 *    - Executar como: "Eu (seu e-mail)"
 *    - Quem pode acessar: "Qualquer pessoa" (OBRIGATÓRIO para o app do aluno conseguir enviar sem pedir login)
 * 8. Clique em "Implantar" e autorize as permissões da sua conta Google
 * 9. Copie a "URL do app da Web" gerada (termina em "/exec")
 * 10. Cole essa URL no modal do seu app!
 * =========================================================================
 */

function doPost(e) {
  try {
    // 1. Decodificar os dados recebidos do aplicativo
    var payload;
    if (e.postData && e.postData.contents) {
      payload = JSON.parse(e.postData.contents);
    } else {
      throw new Error("Nenhum dado recebido no corpo da requisição.");
    }

    var studentName = payload.studentName || "Aluno";
    var exerciseName = payload.exerciseName || "Geral";
    var notes = payload.notes || "Nenhuma observação informada.";
    var mimeType = payload.mimeType || "video/mp4";
    var base64Data = payload.base64;

    if (!base64Data) {
      throw new Error("Arquivo de vídeo não enviado ou corrompido.");
    }

    // 2. Limpar prefixo base64 se existir (ex: data:video/mp4;base64,...)
    var cleanBase64 = base64Data.replace(/^data:video\/[a-zA-Z0-9.-]+;base64,/, '')
                                .replace(/^data:application\/octet-stream;base64,/, '');

    // 3. Organizar pastas no Google Drive
    // Pasta Raiz
    var rootFolderName = "Domínio Corporal - Vídeos de Alunos";
    var rootFolders = DriveApp.getFoldersByName(rootFolderName);
    var rootFolder = rootFolders.hasNext() ? rootFolders.next() : DriveApp.createFolder(rootFolderName);

    // Subpasta por Aluno (ex: "Jean", "Gui")
    var studentFolders = rootFolder.getFoldersByName(studentName);
    var studentFolder = studentFolders.hasNext() ? studentFolders.next() : rootFolder.createFolder(studentName);

    // 4. Gerar nome padronizado do arquivo com data e hora
    var now = new Date();
    var timeZone = "America/Sao_Paulo";
    var timestamp = Utilities.formatDate(now, timeZone, "yyyy-MM-dd_HH-mm");
    var safeExercise = exerciseName.replace(/[^a-zA-Z0-9À-ÿ\s-]/g, '').trim().replace(/\s+/g, '_');
    var fileName = timestamp + "_" + safeExercise + "_" + studentName + ".mp4";

    // 5. Criar arquivo no Google Drive
    var decodedBytes = Utilities.base64Decode(cleanBase64);
    var blob = Utilities.newBlob(decodedBytes, mimeType, fileName);
    var driveFile = studentFolder.createFile(blob);

    // Tornar o arquivo visível para quem tiver o link (para você abrir direto)
    try {
      driveFile.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
    } catch(shareErr) {
      // Ignora erro se restrito pela organização
    }

    var fileUrl = driveFile.getUrl();

    // 6. Notificação Instantânea por E-mail para o Prof. Gui Lemos
    try {
      var recipient = Session.getActiveUser().getEmail();
      if (recipient) {
        var subject = "🔔 Novo Vídeo para Análise: " + studentName + " — " + exerciseName;
        var emailHtml = '<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background: #0f172a; color: #f8fafc; padding: 24px; border-radius: 12px; border: 1px solid #334155;">' +
          '<h2 style="color: #38bdf8; margin-top: 0;">📹 Novo Vídeo Recebido no Domínio Corporal</h2>' +
          '<p style="font-size: 15px; line-height: 1.5;">Um aluno acabou de subir um vídeo de execução para análise biomecânica diretamente pelo aplicativo:</p>' +
          '<table style="width: 100%; border-collapse: collapse; margin: 16px 0; background: #1e293b; border-radius: 8px; overflow: hidden;">' +
            '<tr><td style="padding: 10px 14px; color: #94a3b8; font-weight: bold; width: 35%;">Aluno:</td><td style="padding: 10px 14px; color: #fff;">' + studentName + '</td></tr>' +
            '<tr><td style="padding: 10px 14px; color: #94a3b8; font-weight: bold;">Exercício:</td><td style="padding: 10px 14px; color: #38bdf8; font-weight: bold;">' + exerciseName + '</td></tr>' +
            '<tr><td style="padding: 10px 14px; color: #94a3b8; font-weight: bold;">Data / Hora:</td><td style="padding: 10px 14px; color: #fff;">' + Utilities.formatDate(now, timeZone, "dd/MM/yyyy HH:mm") + '</td></tr>' +
            '<tr><td style="padding: 10px 14px; color: #94a3b8; font-weight: bold;">Observações:</td><td style="padding: 10px 14px; color: #cbd5e1;">' + notes + '</td></tr>' +
            '<tr><td style="padding: 10px 14px; color: #94a3b8; font-weight: bold;">Nome do Arquivo:</td><td style="padding: 10px 14px; color: #94a3b8; font-size: 13px;">' + fileName + '</td></tr>' +
          '</table>' +
          '<div style="text-align: center; margin: 24px 0;">' +
            '<a href="' + fileUrl + '" target="_blank" style="background: #38bdf8; color: #020617; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 15px; display: inline-block;">▶️ Assistir Vídeo no Google Drive</a>' +
          '</div>' +
          '<hr style="border: none; border-top: 1px solid #334155; margin: 20px 0;">' +
          '<p style="font-size: 12px; color: #64748b; margin: 0; text-align: center;">Domínio Corporal • Treinamento Físico & Biomecânica de Alta Performance</p>' +
        '</div>';

        MailApp.sendEmail({
          to: recipient,
          subject: subject,
          htmlBody: emailHtml
        });
      }
    } catch(mailErr) {
      Logger.log("Erro ao enviar email de notificacao: " + mailErr.toString());
    }

    // 7. Retorno de sucesso para o aplicativo
    var responseObj = {
      status: "success",
      message: "Vídeo enviado com sucesso!",
      fileName: fileName,
      fileUrl: fileUrl,
      fileId: driveFile.getId(),
      folderName: studentName
    };

    return ContentService.createTextOutput(JSON.stringify(responseObj))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    Logger.log("Erro no doPost: " + error.toString());
    var errorObj = {
      status: "error",
      message: error.toString()
    };
    return ContentService.createTextOutput(JSON.stringify(errorObj))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "online",
    service: "Domínio Corporal - Upload API",
    time: new Date().toISOString()
  })).setMimeType(ContentService.MimeType.JSON);
}
