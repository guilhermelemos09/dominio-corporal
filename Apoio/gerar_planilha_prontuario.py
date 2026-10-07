import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_prontuario_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active) # Remove default sheet

    # Color Palette inspired by USP / LACIDH research project & Dominio Corporal
    NAVY_FILL = PatternFill(start_color='0F172A', end_color='0F172A', fill_type='solid') # Slate 900
    HEADER_FILL = PatternFill(start_color='1E293B', end_color='1E293B', fill_type='solid') # Slate 800
    NEON_HEADER = PatternFill(start_color='064E3B', end_color='064E3B', fill_type='solid') # Deep Emerald
    BLUE_HEADER = PatternFill(start_color='0C4A6E', end_color='0C4A6E', fill_type='solid') # Deep Sky Blue
    AMBER_HEADER = PatternFill(start_color='78350F', end_color='78350F', fill_type='solid') # Deep Amber
    ZEBRA_FILL = PatternFill(start_color='F8FAFC', end_color='F8FAFC', fill_type='solid') # Slate 50
    SUCCESS_FILL = PatternFill(start_color='ECFDF5', end_color='ECFDF5', fill_type='solid') # Light Mint
    ALERT_FILL = PatternFill(start_color='FEF2F2', end_color='FEF2F2', fill_type='solid') # Light Rose

    FONT_TITLE = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
    FONT_SECTION = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
    FONT_HEADER = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
    FONT_BOLD = Font(name='Calibri', size=10, bold=True, color='0F172A')
    FONT_REGULAR = Font(name='Calibri', size=10, color='1E293B')
    FONT_MUTED = Font(name='Calibri', size=9, color='64748B')
    FONT_SUCCESS = Font(name='Calibri', size=10, bold=True, color='065F46')
    FONT_LINK = Font(name='Calibri', size=10, color='0284C7', underline='single')

    THIN_BORDER = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )
    BOTTOM_DOUBLE = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='double', color='0F172A')
    )

    # ====================================================
    # ABA 1: 01_Prontuario_Geral
    # ====================================================
    ws1 = wb.create_sheet('01_Prontuario_Geral')
    ws1.views.sheetView[0].showGridLines = True

    # Title Banner
    ws1.merge_cells('A1:G1')
    ws1['A1'] = 'DOMÍNIO CORPORAL | PRONTUÁRIO TÉCNICO & DIRETRIZES DO ALUNO'
    ws1['A1'].font = FONT_TITLE
    ws1['A1'].fill = NAVY_FILL
    ws1['A1'].alignment = Alignment(horizontal='center', vertical='center')
    ws1.row_dimensions[1].height = 34

    # Section 1: Dados Cadastrais
    ws1.merge_cells('A3:G3')
    ws1['A3'] = '1. DADOS CADASTRAIS & PERFIL GERAL'
    ws1['A3'].font = FONT_SECTION
    ws1['A3'].fill = HEADER_FILL
    ws1['A3'].alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws1.row_dimensions[3].height = 24

    cadastrais = [
        ('Nome Completo:', 'Guilherme de Paula Lemos', 'ID Matrícula:', 'ALUNO-001 (Nível Avançado / Atleta)'),
        ('Idade / Nascimento:', '34 anos (1992)', 'Data Início:', '29/09/2026'),
        ('Coach Responsável:', 'Domínio Corporal (@guilemos_dominiocorporal)', 'WhatsApp Oficial:', '(16) 98122-2356'),
        ('Drive de Mídia:', 'https://drive.google.com/drive/folders/dominio_corporal', 'Status do Ciclo:', 'Ativo • Microciclo 05/10 a 11/10/2026')
    ]

    cur_row = 4
    for label1, val1, label2, val2 in cadastrais:
        ws1[f'A{cur_row}'] = label1
        ws1[f'A{cur_row}'].font = FONT_BOLD
        ws1.merge_cells(f'B{cur_row}:C{cur_row}')
        ws1[f'B{cur_row}'] = val1
        ws1[f'B{cur_row}'].font = FONT_REGULAR
        
        ws1[f'D{cur_row}'] = label2
        ws1[f'D{cur_row}'].font = FONT_BOLD
        ws1.merge_cells(f'E{cur_row}:G{cur_row}')
        ws1[f'E{cur_row}'] = val2
        ws1[f'E{cur_row}'].font = FONT_LINK if 'http' in val2 else FONT_REGULAR
        
        for col in range(1, 8):
            ws1.cell(row=cur_row, column=col).border = THIN_BORDER
        ws1.row_dimensions[cur_row].height = 20
        cur_row += 1

    # Section 2: Biometria & Composição Corporal
    cur_row += 1
    ws1.merge_cells(f'A{cur_row}:G{cur_row}')
    ws1[f'A{cur_row}'] = '2. COMPOSIÇÃO CORPORAL & ANTROPOMETRIA'
    ws1[f'A{cur_row}'].font = FONT_SECTION
    ws1[f'A{cur_row}'].fill = NEON_HEADER
    ws1[f'A{cur_row}'].alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws1.row_dimensions[cur_row].height = 24
    cur_row += 1

    biometria = [
        ('Peso Inicial (02/07/2026):', '97.0 kg', 'Peso Atual (05/10/2026):', '84.0 kg'),
        ('Delta Ponderal Acumulado:', '-13.0 kg (Ritmo médio ~1.0 kg/sem)', 'Meta de Gordura:', '20% -> 14%'),
        ('Estatura Corporal:', '1.78 m', 'Farmacoterapia:', 'Tirzepatida (Mounjaro)'),
        ('Aporte Proteico Diário:', '2.0 a 2.4 g/kg (Preservação de sarcômeros)', 'Relação Potência/Peso:', 'Elevada (+W/kg para calistenia e ginástica)')
    ]

    for label1, val1, label2, val2 in biometria:
        ws1[f'A{cur_row}'] = label1
        ws1[f'A{cur_row}'].font = FONT_BOLD
        ws1.merge_cells(f'B{cur_row}:C{cur_row}')
        ws1[f'B{cur_row}'] = val1
        ws1[f'B{cur_row}'].font = FONT_SUCCESS if '-13.0' in val1 or '84.0' in val1 else FONT_REGULAR
        
        ws1[f'D{cur_row}'] = label2
        ws1[f'D{cur_row}'].font = FONT_BOLD
        ws1.merge_cells(f'E{cur_row}:G{cur_row}')
        ws1[f'E{cur_row}'] = val2
        ws1[f'E{cur_row}'].font = FONT_REGULAR
        
        for col in range(1, 8):
            ws1.cell(row=cur_row, column=col).border = THIN_BORDER
        ws1.row_dimensions[cur_row].height = 20
        cur_row += 1

    # Section 3: Parâmetros Articulares & Prescrições Clínicas
    cur_row += 1
    ws1.merge_cells(f'A{cur_row}:G{cur_row}')
    ws1[f'A{cur_row}'] = '3. PARÂMETROS CLÍNICOS, CIRÚRGICOS & GESTÃO ARTICULAR'
    ws1[f'A{cur_row}'].font = FONT_SECTION
    ws1[f'A{cur_row}'].fill = BLUE_HEADER
    ws1[f'A{cur_row}'].alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws1.row_dimensions[cur_row].height = 24
    cur_row += 1

    articular = [
        ('Joelho Esquerdo (Menisco Lateral):', 'FOCO CLÍNICO ATIVO: Rompimento parcial com atrito em flexão >110°. Conduta: dominância de quadril/posterior, tíbias estritamente verticais, step-down nas caixas e solo complacente.'),
        ('Ombro Direito (Pós-Cirúrgico):', '100% ZERADO E CONSOLIDADO: Acromioplastia e reparo de supraespinhal consolidados há anos. Apto para puxadas e empurres pesados com elevação escapular ativa.'),
        ('Tendões de Aquiles Bilaterais:', 'Sutura cirúrgica há 8 anos. Alongamento tendíneo pós-sutura. Conduta: sarcomerogênese em série, flexão plantar em degrau (3-4s pausa), sóleo pesado e isometrias.'),
        ('Cotovelo / Tríceps Esquerdo:', 'Pós-viscossuplementação, praticamente zerado. Excelente tolerância mecânica em argolas e barras; atenção leve para evitar hiperextensão sob choque.')
    ]

    for label, desc in articular:
        ws1[f'A{cur_row}'] = label
        ws1[f'A{cur_row}'].font = FONT_BOLD
        ws1.merge_cells(f'B{cur_row}:G{cur_row}')
        ws1[f'B{cur_row}'] = desc
        ws1[f'B{cur_row}'].font = FONT_REGULAR
        ws1[f'B{cur_row}'].alignment = Alignment(wrap_text=True, vertical='center')
        
        for col in range(1, 8):
            ws1.cell(row=cur_row, column=col).border = THIN_BORDER
        ws1.row_dimensions[cur_row].height = 36
        cur_row += 1

    # Section 4: Metas do Ciclo
    cur_row += 1
    ws1.merge_cells(f'A{cur_row}:G{cur_row}')
    ws1[f'A{cur_row}'] = '4. METAS DO CICLO & DIRETRIZES DE RENDIMENTO'
    ws1[f'A{cur_row}'].font = FONT_SECTION
    ws1[f'A{cur_row}'].fill = AMBER_HEADER
    ws1[f'A{cur_row}'].alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws1.row_dimensions[cur_row].height = 24
    cur_row += 1

    metas = [
        ('Meta 1 - Definição Muscular:', 'Manter taxa de perda de 0.8 a 1.0 kg/semana via balanço energético e estímulo tensional, preservando o tecido muscular magro.'),
        ('Meta 2 - Habilidades Gímnicas:', 'Aperfeiçoar parada de mãos livre na manjota (bone stacking), Press to Handstand sem salto, One-Arm Crocodile e giros de oitava na barra fixa.'),
        ('Meta 3 - Mobilidade para Dança:', 'Recuperar amplitude funcional de flexão profunda sem pinçamento meniscal, permitindo transições ágeis no solo (floorwork).')
    ]

    for label, desc in metas:
        ws1[f'A{cur_row}'] = label
        ws1[f'A{cur_row}'].font = FONT_BOLD
        ws1.merge_cells(f'B{cur_row}:G{cur_row}')
        ws1[f'B{cur_row}'] = desc
        ws1[f'B{cur_row}'].font = FONT_REGULAR
        ws1[f'B{cur_row}'].alignment = Alignment(wrap_text=True, vertical='center')
        for col in range(1, 8):
            ws1.cell(row=cur_row, column=col).border = THIN_BORDER
        ws1.row_dimensions[cur_row].height = 26
        cur_row += 1

    ws1.column_dimensions['A'].width = 24
    ws1.column_dimensions['B'].width = 26
    ws1.column_dimensions['C'].width = 18
    ws1.column_dimensions['D'].width = 20
    ws1.column_dimensions['E'].width = 24
    ws1.column_dimensions['F'].width = 20
    ws1.column_dimensions['G'].width = 20

    # ====================================================
    # ABA 2: 02_Historico_Treinos
    # ====================================================
    ws2 = wb.create_sheet('02_Historico_Treinos')
    ws2.views.sheetView[0].showGridLines = True
    ws2.freeze_panes = 'C3'

    ws2.merge_cells('A1:M1')
    ws2['A1'] = 'DOMÍNIO CORPORAL | HISTÓRICO CONSOLIDADO DE TREINOS & DIÁRIO DE SESSÕES'
    ws2['A1'].font = FONT_TITLE
    ws2['A1'].fill = NAVY_FILL
    ws2['A1'].alignment = Alignment(horizontal='center', vertical='center')
    ws2.row_dimensions[1].height = 32

    headers_s2 = [
        'Data', 'Dia', 'Sessão', 'Treino Prescrito', 'Local', 'Status',
        'Séries Feitas', 'Total Séries', 'Aderência', 'Cargas Utilizadas',
        'Sensações & Anotações do Aluno', 'Avaliação do Coach', 'Gestão Articular'
    ]

    for col_idx, h in enumerate(headers_s2, start=1):
        c = ws2.cell(row=2, column=col_idx, value=h)
        c.font = FONT_HEADER
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        c.border = BOTTOM_DOUBLE
    ws2.row_dimensions[2].height = 28

    sessions = [
        (
            '05/10/2026', 'Segunda', 'Sessão 1', 'Box CrossFit • Puxada & Metcon (EMOM 12\' + Triplo AMRAP)',
            'Box CrossFit', 'Concluído ✅', 10, 10, 1.0,
            'Wall Ball 9kg, DB Snatch 22.5kg, Thrusters 30kg',
            'Strict Pull-up com hollow firme; agachamento do Wall Ball travado a 90° poupou 100% o joelho esquerdo. Sem dor no ombro.',
            'Excelente ritmo escapuloumeral e contração de dorsal. Preservação meniscal estrita cumprida.',
            'Joelho 100% protegido (sem flexão >90° sob carga)'
        ),
        (
            '06/10/2026', 'Terça', 'Sessão 2', 'Box CrossFit (120 reps empurrar) + Autoregulação Noturna',
            'Box CrossFit', 'Concluído ✅', 14, 14, 1.0,
            'Supino 60kg, Z-Press 15kg, Barra WOD 30kg, 80 Box Jump Overs',
            'Supino e Z-Press sólidos; WOD com 30kg e step-down nas caixas. Decisão de descansar à noite e transferir ginástica pesada para quarta.',
            'Autoregulação clínica perfeita. Preveniu sobrecarga neural nos motoneurônios do tríceps e deltoide.',
            'Step-down protegeu platô tibial; ombro direito estável'
        ),
        (
            '07/10/2026', 'Quarta', 'Sessão 3', 'Ginásio EEFERP • Ginástica Artística, Habilidades na Manjota & EMOM 12\'',
            'Ginásio EEFERP', 'Concluído ✅', 14, 14, 1.0,
            'HSPU peso corporal, KB Swing 20-24kg, Argolas, Barras',
            'Handstand na manjota com elevação escapular limpa; HSPU com descida a 45° sem compressão cervical; EMOM 12\' com KB Swings dominantes de quadril.',
            'Sessão nobre cumprida em frescor neuromuscular. Alinhamento corporal perfeito e zero impacto articular.',
            'Tatame complacente dissipou forças de reação do solo'
        ),
        (
            '08/10/2026', 'Quinta', 'Sessão 4 (Planejada)', 'Dança Contemporânea & Aperfeiçoamento de Floorwork',
            'EEFERP Solo', 'Planejado 📅', 0, 8, 0.0,
            'Peso Corporal (Tatame e solo macio)',
            'Foco em transições fluidas no solo, giros sem sobrecarga em rotação tibial externa forçada.',
            'Prescrição orientada à descompressão e amplitude gradual de joelho.',
            'Atenção ao corno posterior do menisco em giros'
        ),
        (
            '09/10/2026', 'Sexta', 'Sessão 5 (Planejada)', 'Portagem de Força com Amigo + Argolas Altas (Zero Pernas)',
            'Box / Ginásio', 'Planejado 📅', 0, 10, 0.0,
            'Peso Corporal + Parceiro volante (~63 kg)',
            'Treino de bases e portagem em alinhamento de bone stacking; argolas altas (Strict RMU e Candle Kips). Repouso absoluto de membros inferiores.',
            'Blindagem biomecânica de pernas visando a viagem e festival no fim de semana.',
            'Membros inferiores descansados para o festival'
        )
    ]

    for r_idx, sess in enumerate(sessions, start=3):
        ws2.row_dimensions[r_idx].height = 42
        is_zebra = (r_idx % 2 == 0)
        row_fill = ZEBRA_FILL if is_zebra else None
        
        for c_idx, val in enumerate(sess, start=1):
            cell = ws2.cell(row=r_idx, column=c_idx, value=val)
            cell.font = FONT_REGULAR
            cell.border = THIN_BORDER
            if row_fill:
                cell.fill = row_fill
                
            if c_idx in [1, 2, 3, 5]:
                cell.alignment = Alignment(horizontal='center', vertical='center')
            elif c_idx == 6:
                cell.alignment = Alignment(horizontal='center', vertical='center')
                cell.font = FONT_SUCCESS if 'Concluído' in str(val) else FONT_MUTED
                cell.fill = SUCCESS_FILL if 'Concluído' in str(val) else (row_fill or PatternFill(fill_type=None))
            elif c_idx in [7, 8]:
                cell.alignment = Alignment(horizontal='center', vertical='center')
            elif c_idx == 9:
                cell.alignment = Alignment(horizontal='center', vertical='center')
                cell.number_format = '0%'
            elif c_idx in [10, 11, 12, 13]:
                cell.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)

    col_widths_s2 = [12, 10, 12, 36, 16, 14, 8, 8, 11, 30, 42, 38, 30]
    for idx, w in enumerate(col_widths_s2, start=1):
        ws2.column_dimensions[get_column_letter(idx)].width = w

    # ====================================================
    # ABA 3: 03_Registro_Videos_Drive
    # ====================================================
    ws3 = wb.create_sheet('03_Registro_Videos_Drive')
    ws3.views.sheetView[0].showGridLines = True
    ws3.freeze_panes = 'C3'

    ws3.merge_cells('A1:K1')
    ws3['A1'] = 'DOMÍNIO CORPORAL | REGISTRO DE VÍDEOS, LINKS DO DRIVE & ANÁLISES CINEMÁTICAS'
    ws3['A1'].font = FONT_TITLE
    ws3['A1'].fill = NAVY_FILL
    ws3['A1'].alignment = Alignment(horizontal='center', vertical='center')
    ws3.row_dimensions[1].height = 32

    headers_s3 = [
        'Data', 'Movimento / Gesto', 'Categoria', 'Duração',
        'Aparelho / Local', 'Link do Arquivo (Drive / Mídia)',
        'Na Prática (O que acontece)', 'Diagnóstico (O que ajustar)',
        'Exercícios Sugeridos', 'Base Científica & Origem', 'Status'
    ]

    for col_idx, h in enumerate(headers_s3, start=1):
        c = ws3.cell(row=2, column=col_idx, value=h)
        c.font = FONT_HEADER
        c.fill = BLUE_HEADER
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        c.border = BOTTOM_DOUBLE
    ws3.row_dimensions[2].height = 28

    videos_data = [
        (
            '02/10/2026', 'Press Handstand no Ombro do Parceiro', 'Portagem & Handstand', '15s',
            'Box CrossFit', 'Midia/WhatsApp Video 2026-10-02 at 14.44.21.mp4',
            'O parceiro de baixo mantém joelhos semifletidos para estabilidade. O Gui apoia nos ombros dele, projeta o tronco à frente e sobe o quadril sem salto. No topo, abre em straddle mantendo o alinhamento sobre a coluna da base e desce suavemente.',
            'A subida foi muito suave e estável. No topo, ao abrir as pernas, o quadril empina um pouco para trás e a lombar curva de leve. Basta travar bem a barriga e o bumbum para a coluna subir reta.',
            '• Press na paralela baixa com costas na parede (3x3 com pausa de 3s no topo).\n• Subida no ombro com pernas unidas (pike press) para ganhar mais força de compressão.',
            'Empilhamento ósseo com absorção da carga axial (~84 kg) pela base; translação escapular que projeta o centro de gravidade sobre as clavículas; desaceleração excêntrica conduzida por peitoral menor e trapézio inferior.',
            'Validado ✅'
        ),
        (
            '02/10/2026', '1x Strict RMU Livre + 2x Candle Kips', 'Argolas Altas', '25s',
            'Box CrossFit', 'Midia/WhatsApp Video 2026-10-02 at 14.44.18.mp4',
            'Retorno às argolas com subida estrita. Pegada falsa com punho flexionado, puxada até o peito na altura das mãos e cotovelos colados sem impulso de pernas. Em seguida, descida em vela e balanço com braços esticados para retornar ao apoio.',
            'Subida de força muito segura para o ombro operado. Na passagem para empurrar o apoio, os joelhos deram uma leve dobrada. As pernas devem ficar 100% esticadas e pontas dos pés ativas.',
            '• Transições lentas na argola baixa com pés no chão (3x5 reps com cotovelos colados).\n• Séries de 2 a 3 repetições estritas consecutivas mantendo a pegada falsa firme.',
            'Flexão ulnocarpal profunda elimina defasagem mecânica do punho, poupando a articulação glenoumeral no ombro operado e inserção do tríceps; candle kip converte energia potencial em momento angular por tração estendida.',
            'Validado ✅'
        ),
        (
            '01/10/2026', 'Sequência Acrobática Completa (L-Sit -> Press -> Croc)', 'Manjota / Canes', '42s',
            'Ginásio EEFERP', 'https://drive.google.com/file/d/1tNgCqQQXc_sA3WCwqryKIRbHE7mK8zZX/view?usp=sharing',
            'Entrada em L-sit estático suspenso, subida contínua sem embalo até a parada de mãos aberta, trava estável por 8s, descida controlada e encaixe do cotovelo na bacia para One-Arm Crocodile por 7s com o outro braço estendido.',
            'L-sit e subida na parada de mãos impecáveis. No apoio de um braço só (Crocodile), o quadril deu uma leve caída para o lado. O corpo precisa ficar reto como uma prancha paralela ao chão.',
            '• Isometria na manjota com apoio de apenas 2 dedos da mão livre (3x 8-10s por lado).\n• Retorno do Crocodile para as duas mãos sem encostar os pés no chão.',
            'Força concêntrica de flexores de quadril e deltóide anterior com elevação escapular mantida; apoio do olécrano na espinha ilíaca ântero-superior e torque anti-rotacional neutralizado por oblíquos contralaterais.',
            'Validado ✅'
        ),
        (
            '01/10/2026', '4x Giros de Oitava Consecutivos (Glide Kips)', 'Barra Fixa', '4 reps',
            'Ginásio EEFERP', 'https://drive.google.com/file/d/1o5mW2GK-qtiffr74zTQOUaQ4PBfOzfxI/view?usp=sharing',
            'Balanço amplo perto do chão, flexão de quadril aproximando as canelas da barra no retorno do pêndulo e puxada com cotovelos estendidos até o apoio sobre a barra, encadeando 4 repetições contínuas com ritmo constante.',
            'Excelente ritmo nas 4 repetições. Na subida em cima da barra, o peito ainda sobe um pouco recolhido. Abra o peito e projete os ombros à frente da barra para embalar fácil na repetição seguinte.',
            '• Balanço de oitava segurando bola medicinal leve entre os tornozelos (3x6 reps).\n• Saída da oitava ligada direto no giro de apoio para trás na barra.',
            'Timing na reversão do pêndulo angular encurtando o raio de rotação para ascensão vertical; extensão de ombro com grande dorsal e tríceps cabeça longa com rápida troca de punhos por cima do eixo.',
            'Validado ✅'
        ),
        (
            '05/10/2026', 'Evolução Antropométrica e Comparativo 97kg -> 84kg', 'Composição Corporal', 'Fotos',
            'Clínica / Box', 'Midia/comparacao_frontal_relaxado.jpg | gui_foto.jpg',
            'Comparativo fotográfico evidenciando redução da adiposidade abdominal e definição do contorno muscular em 95 dias de acompanhamento, com preservação da estrutura muscular em tronco e braços.',
            'Perda de peso consistente e com ótima retenção de massa muscular. Manter a disciplina para não acelerar demais e garantir a preservação da força nas habilidades gímnicas.',
            '• Manter ingestão proteica alta (2.0-2.4 g/kg) e hidratação rigorosa.\n• Refeed limpo sincronizado com dias de treinos mais pesados na EEFERP.',
            'Estímulo tensional frequente e aporte proteico de 2.0 a 2.4 g/kg preservando massa magra; descompressão de 40 a 50 kg no platô tibial por ciclo de passo/agachamento (-13 kg acumulados).',
            'Validado ✅'
        )
    ]

    for r_idx, v in enumerate(videos_data, start=3):
        ws3.row_dimensions[r_idx].height = 46
        is_zebra = (r_idx % 2 == 0)
        row_fill = ZEBRA_FILL if is_zebra else None
        
        for c_idx, val in enumerate(v, start=1):
            cell = ws3.cell(row=r_idx, column=c_idx, value=val)
            cell.font = FONT_REGULAR
            cell.border = THIN_BORDER
            if row_fill: cell.fill = row_fill
            
            if c_idx in [1, 3, 4, 5, 11]:
                cell.alignment = Alignment(horizontal='center', vertical='center')
                if c_idx == 11:
                    cell.font = FONT_SUCCESS
                    cell.fill = SUCCESS_FILL
            elif c_idx == 6:
                cell.alignment = Alignment(horizontal='left', vertical='center')
                cell.font = FONT_LINK if 'http' in str(val) else FONT_REGULAR
            else:
                cell.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)

    col_widths_s3 = [12, 30, 20, 10, 16, 34, 40, 42, 40, 40, 14]
    for idx, w in enumerate(col_widths_s3, start=1):
        ws3.column_dimensions[get_column_letter(idx)].width = w

    # ====================================================
    # ABA 4: 04_Metricas_Evolucao
    # ====================================================
    ws4 = wb.create_sheet('04_Metricas_Evolucao')
    ws4.views.sheetView[0].showGridLines = True

    ws4.merge_cells('A1:F1')
    ws4['A1'] = 'DOMÍNIO CORPORAL | EVOLUÇÃO PONDERAL & MARCOS DE DESEMPENHO'
    ws4['A1'].font = FONT_TITLE
    ws4['A1'].fill = NAVY_FILL
    ws4['A1'].alignment = Alignment(horizontal='center', vertical='center')
    ws4.row_dimensions[1].height = 32

    # Subseção 1: Pesagem
    ws4.merge_cells('A2:F2')
    ws4['A2'] = 'TABELA 1: LINHA DO TEMPO PONDERAL (JULHO A OUTUBRO DE 2026)'
    ws4['A2'].font = FONT_SECTION
    ws4['A2'].fill = HEADER_FILL
    ws4['A2'].alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws4.row_dimensions[2].height = 24

    headers_s4_1 = ['Data Registro', 'Massa Corporal (kg)', 'Delta Semanal (kg)', 'Delta Acumulado (kg)', '% Gordura Est.', 'Notas Clínicas']
    for col_idx, h in enumerate(headers_s4_1, start=1):
        c = ws4.cell(row=3, column=col_idx, value=h)
        c.font = FONT_HEADER
        c.fill = NEON_HEADER
        c.alignment = Alignment(horizontal='center', vertical='center')
        c.border = BOTTOM_DOUBLE
    ws4.row_dimensions[3].height = 24

    pesagens = [
        ('02/07/2026', 97.0, 0.0, 0.0, '22.5%', 'Início do protocolo de recomposição corporal'),
        ('01/08/2026', 93.2, -3.8, -3.8, '21.0%', 'Adaptação excelente e queda expressiva de retenção hídrica'),
        ('01/09/2026', 88.5, -4.7, -8.5, '19.5%', 'Descompressão articular já sentida nos joelhos e corrida'),
        ('14/09/2026', 87.2, -1.3, -9.8, '19.4%', 'Bioimpedância clínica LaCiDH validada'),
        ('05/10/2026', 84.0, -3.2, -13.0, '18.0%', 'Registro oficial em fotos comparativas (-13kg acumulados!)')
    ]

    for r_idx, row in enumerate(pesagens, start=4):
        ws4.row_dimensions[r_idx].height = 22
        for c_idx, val in enumerate(row, start=1):
            cell = ws4.cell(row=r_idx, column=c_idx, value=val)
            cell.font = FONT_REGULAR
            cell.border = THIN_BORDER
            if c_idx in [1, 5]:
                cell.alignment = Alignment(horizontal='center', vertical='center')
            elif c_idx in [2, 3, 4]:
                cell.alignment = Alignment(horizontal='right', vertical='center')
                if c_idx in [3, 4] and isinstance(val, (int, float)) and val < 0:
                    cell.font = FONT_SUCCESS
            else:
                cell.alignment = Alignment(horizontal='left', vertical='center')

    # Subseção 2: Marcos de Força
    cur_row_s4 = 10
    ws4.merge_cells(f'A{cur_row_s4}:F{cur_row_s4}')
    ws4[f'A{cur_row_s4}'] = 'TABELA 2: MARCOS DE FORÇA & HABILIDADES ESPECÍFICAS'
    ws4[f'A{cur_row_s4}'].font = FONT_SECTION
    ws4[f'A{cur_row_s4}'].fill = HEADER_FILL
    ws4[f'A{cur_row_s4}'].alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws4.row_dimensions[cur_row_s4].height = 24
    cur_row_s4 += 1

    headers_s4_2 = ['Habilidade / Exercício', 'Melhor Marca Recente', 'Data Validação', 'Aparelho / Carga', 'Sensação / Articulação', 'Status Técnico']
    for col_idx, h in enumerate(headers_s4_2, start=1):
        c = ws4.cell(row=cur_row_s4, column=col_idx, value=h)
        c.font = FONT_HEADER
        c.fill = AMBER_HEADER
        c.alignment = Alignment(horizontal='center', vertical='center')
        c.border = BOTTOM_DOUBLE
    ws4.row_dimensions[cur_row_s4].height = 24
    cur_row_s4 += 1

    marcos_forca = [
        ('Supino Reto (Bench Press)', '60 kg (4x10 reps)', '06/10/2026', 'Barra Olímpica', 'Ombro direito 100% confortável, sem pinçamento', 'Sólido ✅'),
        ('Z-Press Sentado no Solo', '15 kg cada halter (4x10)', '06/10/2026', 'Halteres', 'Estabilidade de core e postura ereta impecáveis', 'Sólido ✅'),
        ('Handstand Livre na Manjota', '25 a 30 segundos cravados', '01/10/2026', 'Manjota de Madeira', 'Empilhamento ósseo perfeito, controle fino na ponta dos dedos', 'Dominado 🤸'),
        ('One-Arm Crocodile na Manjota', '7 segundos unilaterais', '01/10/2026', 'Manjota', 'Torque anti-rotacional unilateral de oblíquos e fulcro pélvico', 'Avançado ⚡'),
        ('Strict Ring Muscle-Up (RMU)', '1 repetição livre estrita', '02/10/2026', 'Argolas Altas', 'Retorno de 2 anos com false grip perfeito e zero dor no ombro', 'Desbloqueado 🏆'),
        ('Giros de Oitava (Glide Kips)', '4 repetições contínuas', '01/10/2026', 'Barra Fixa Gímnica', 'Reversão de pêndulo angular fluída e subida estendida', 'Dominado 🔄'),
        ('Agachamento com Wall Ball', '40 reps @ 9 kg', '05/10/2026', 'Bola de 9 kg', 'Limitado estritamente a 90° para proteção total do menisco', 'Controlado 🛡️')
    ]

    for row in marcos_forca:
        ws4.row_dimensions[cur_row_s4].height = 24
        for c_idx, val in enumerate(row, start=1):
            cell = ws4.cell(row=cur_row_s4, column=c_idx, value=val)
            cell.font = FONT_REGULAR
            cell.border = THIN_BORDER
            if c_idx in [3, 6]:
                cell.alignment = Alignment(horizontal='center', vertical='center')
                if c_idx == 6:
                    cell.font = FONT_SUCCESS
                    cell.fill = SUCCESS_FILL
            elif c_idx == 2:
                cell.alignment = Alignment(horizontal='center', vertical='center')
                cell.font = FONT_BOLD
            else:
                cell.alignment = Alignment(horizontal='left', vertical='center')
        cur_row_s4 += 1

    col_widths_s4 = [28, 22, 16, 22, 40, 18]
    for idx, w in enumerate(col_widths_s4, start=1):
        ws4.column_dimensions[get_column_letter(idx)].width = w

    # Destination: project root for direct 1-click consultation
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dest_path = os.path.join(root_dir, 'PRONTUARIO_E_HISTORICO_GUILHERME_LEMOS.xlsx')
    wb.save(dest_path)
    print(f'Sucesso! Planilha gerada na raiz de consultas em:\n  - {dest_path}')

if __name__ == '__main__':
    build_prontuario_workbook()
