from siteCia.init import app
from openpyxl import Workbook
from datetime import datetime


def salvar(usuarios):
    wb = Workbook()
    sh = wb.create_sheet('Planilha1', 0)
    sh1 = wb.active
    with app.app_context():
        x = 2
        for usuario in usuarios:
            sh[f"A{x}"].value = usuario.nome
            sh[f"B{x}"].value = str(usuario.cargo).upper()
            sh[f"C{x}"].value = str(usuario.whatsapp).replace('None', 'Não cadastrado')
            sh[f"D{x}"].value = str(usuario.unidade).replace('1', 'Brasília')
            sh[f"E{x}"].value = usuario.contrato
            sh[f"F{x}"].value = datetime.strftime(usuario.admissao, '%d/%m/%Y')
            sh[f"G{x}"].value = str(usuario.email).lower()
            if usuario.salario == 0:
                sh[f"H{x}"].value = usuario.hora_aula
            else:
                sh[f"H{x}"].value = usuario.salario
            x += 1
    sh["A1"].value = 'NOME'
    sh1.column_dimensions["A"].width = 39
    sh["B1"].value = 'CARGO'
    sh1.column_dimensions["B"].width = 20
    sh["C1"].value = 'WHATSAPP'
    sh1.column_dimensions["C"].width = 15
    sh["D1"].value = 'UNIDADE'
    sh1.column_dimensions["D"].width = 9
    sh["E1"].value = 'TIPO CONTRATO'
    sh1.column_dimensions["E"].width = 15
    sh["F1"].value = 'ADMISSÃO'
    sh1.column_dimensions["F"].width = 11
    sh["G1"].value = 'E-MAIL'
    sh1.column_dimensions["G"].width = 37
    sh["H1"].value = 'REMUNERAÇÃO'
    sh1.column_dimensions["H"].width = 15

    wb.save('siteCia/Colaboradores.xlsx')
