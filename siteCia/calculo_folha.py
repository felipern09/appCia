# adicionar hrs de subtituição
# criar pg de substituição para  funcionário preencher
# escolher o nome do profissional
# marcar quantas hrs ele isra fazer a mais em cada dia da semana
# colocar data final da substituição
# calculo folha
# 	adicionar multiplicaçao por DSR
# 	montar logica de soma da hr de escala
# 	montar logica de soma da hr de substituiçao
# 	montaro logica de pedido -> autorização -> soma hrs

from datetime import datetime, timedelta
from flask_login import current_user
from dateutil.relativedelta import relativedelta


class Calcular:
    nomedias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    dsr = 1.17
    data = datetime.today()
    if data.day >= 21:
        inicio = datetime(day=21, month=data.month, year=data.year)
        fechamento = datetime(day=20, month=(data + relativedelta(months=1)).month, year=(data + relativedelta(months=1)).year)
    if data.day < 21:
        inicio = datetime(day=21, month=(data - relativedelta(months=1)).month, year=(data - relativedelta(months=1)).year)
        fechamento = datetime(day=20, month=data.month, year=data.year)

    dias_st = [(inicio).strftime('%d/%m'), (inicio + timedelta(days=1)).strftime('%d/%m'),
               (inicio + timedelta(days=2)).strftime('%d/%m'), (inicio + timedelta(days=3)).strftime('%d/%m'),
               (inicio + timedelta(days=4)).strftime('%d/%m'), (inicio + timedelta(days=5)).strftime('%d/%m'),
               (inicio + timedelta(days=6)).strftime('%d/%m'),
               (inicio + timedelta(days=7)).strftime('%d/%m'), (inicio + timedelta(days=8)).strftime('%d/%m'),
               (inicio + timedelta(days=9)).strftime('%d/%m'), (inicio + timedelta(days=10)).strftime('%d/%m'),
               (inicio + timedelta(days=11)).strftime('%d/%m'), (inicio + timedelta(days=12)).strftime('%d/%m'),
               (inicio + timedelta(days=13)).strftime('%d/%m'),
               (inicio + timedelta(days=14)).strftime('%d/%m'), (inicio + timedelta(days=15)).strftime('%d/%m'),
               (inicio + timedelta(days=16)).strftime('%d/%m'), (inicio + timedelta(days=17)).strftime('%d/%m'),
               (inicio + timedelta(days=18)).strftime('%d/%m'), (inicio + timedelta(days=19)).strftime('%d/%m'),
               (inicio + timedelta(days=20)).strftime('%d/%m'),
               (inicio + timedelta(days=21)).strftime('%d/%m'), (inicio + timedelta(days=22)).strftime('%d/%m'),
               (inicio + timedelta(days=23)).strftime('%d/%m'), (inicio + timedelta(days=24)).strftime('%d/%m'),
               (inicio + timedelta(days=25)).strftime('%d/%m'), (inicio + timedelta(days=26)).strftime('%d/%m'),
               (inicio + timedelta(days=27)).strftime('%d/%m'),
               (inicio + timedelta(days=28)).strftime('%d/%m'), (inicio + timedelta(days=29)).strftime('%d/%m'),
               (inicio + timedelta(days=30)).strftime('%d/%m')]
    dias = [inicio, inicio + timedelta(days=1), inicio + timedelta(days=2), inicio + timedelta(days=3),
            inicio + timedelta(days=4), inicio + timedelta(days=5), inicio + timedelta(days=6),
            inicio + timedelta(days=7), inicio + timedelta(days=8), inicio + timedelta(days=9),
            inicio + timedelta(days=10), inicio + timedelta(days=11), inicio + timedelta(days=12),
            inicio + timedelta(days=13),
            inicio + timedelta(days=14), inicio + timedelta(days=15), inicio + timedelta(days=16),
            inicio + timedelta(days=17), inicio + timedelta(days=18), inicio + timedelta(days=19),
            inicio + timedelta(days=20),
            inicio + timedelta(days=21), inicio + timedelta(days=22), inicio + timedelta(days=23),
            inicio + timedelta(days=24), inicio + timedelta(days=25), inicio + timedelta(days=26),
            inicio + timedelta(days=27),
            inicio + timedelta(days=28), inicio + timedelta(days=29), inicio + timedelta(days=30)]
    semana = [nomedias[inicio.weekday()], nomedias[(inicio + timedelta(days=1)).weekday()],
              nomedias[(inicio + timedelta(days=2)).weekday()],
              nomedias[(inicio + timedelta(days=3)).weekday()], nomedias[(inicio + timedelta(days=4)).weekday()],
              nomedias[(inicio + timedelta(days=5)).weekday()],
              nomedias[(inicio + timedelta(days=6)).weekday()], nomedias[(inicio + timedelta(days=7)).weekday()],
              nomedias[(inicio + timedelta(days=8)).weekday()],
              nomedias[(inicio + timedelta(days=9)).weekday()], nomedias[(inicio + timedelta(days=10)).weekday()],
              nomedias[(inicio + timedelta(days=11)).weekday()],
              nomedias[(inicio + timedelta(days=12)).weekday()], nomedias[(inicio + timedelta(days=13)).weekday()],
              nomedias[(inicio + timedelta(days=14)).weekday()],
              nomedias[(inicio + timedelta(days=15)).weekday()], nomedias[(inicio + timedelta(days=16)).weekday()],
              nomedias[(inicio + timedelta(days=17)).weekday()],
              nomedias[(inicio + timedelta(days=18)).weekday()], nomedias[(inicio + timedelta(days=19)).weekday()],
              nomedias[(inicio + timedelta(days=20)).weekday()],
              nomedias[(inicio + timedelta(days=21)).weekday()], nomedias[(inicio + timedelta(days=22)).weekday()],
              nomedias[(inicio + timedelta(days=23)).weekday()],
              nomedias[(inicio + timedelta(days=24)).weekday()], nomedias[(inicio + timedelta(days=25)).weekday()],
              nomedias[(inicio + timedelta(days=26)).weekday()],
              nomedias[(inicio + timedelta(days=27)).weekday()], nomedias[(inicio + timedelta(days=28)).weekday()],
              nomedias[(inicio + timedelta(days=29)).weekday()],
              nomedias[(inicio + timedelta(days=30)).weekday()]]

    def __init__(self, user):
        self.user = user
        self.horas = []
        self.soma_carga = 0
        self.salario = 0

    def hosrista(self):
        hr_aula = current_user.hora_aula
        hr_seg, hr_ter, hr_qua, hr_qui, hr_sex = current_user.hr_seg, current_user.hr_ter, current_user.hr_qua, \
                                                 current_user.hr_qui, current_user.hr_sex
        hr_esc = 0
        hr_aula2 = current_user.hora_aula2
        hr_seg2, hr_ter2, hr_qua2, hr_qui2, hr_sex2 = current_user.hr_seg2, current_user.hr_ter2, current_user.hr_qua2, \
                                                      current_user.hr_qui2, current_user.hr_sex2
        hr_esc2 = 0
        hr_aula3 = current_user.hora_aula3
        hr_seg3, hr_ter3, hr_qua3, hr_qui3, hr_sex3 = current_user.hr_seg3, current_user.hr_ter3, current_user.hr_qua3, \
                                                      current_user.hr_qui3, current_user.hr_sex3
        hr_esc3 = 0
        seg = 0
        ter = 0
        qua = 0
        qui = 0
        sex = 0
        sab = 0
        data = datetime.today()
        if data.day >= 21:
            inicio = datetime(day=21, month=data.month, year=data.year)
            fechamento = datetime(day=20, month=(data + relativedelta(months=1)).month, year=(data + relativedelta(months=1)).year)
        if data.day < 21:
            inicio = datetime(day=21, month=(data - relativedelta(months=1)).month, year=(data - relativedelta(months=1)).year)
            fechamento = datetime(day=20, month=data.month, year=data.year)

        def intervalo(inicio, fechamento):
            if data.day >= 21:
                inicio = datetime(day=21, month=data.month, year=data.year)
                fechamento = datetime(day=20, month=(data + relativedelta(months=1)).month,
                                      year=(data + relativedelta(months=1)).year)
            if data.day < 21:
                inicio = datetime(day=21, month=(data - relativedelta(months=1)).month,
                                  year=(data - relativedelta(months=1)).year)
                fechamento = datetime(day=20, month=data.month, year=data.year)

            for n in range(int((fechamento - inicio).days) + 1):
                yield inicio + timedelta(n)

        for dia in intervalo(inicio, fechamento):
            if dia.weekday() == 0:
                seg += 1
            if dia.weekday() == 1:
                ter += 1
            if dia.weekday() == 2:
                qua += 1
            if dia.weekday() == 3:
                qui += 1
            if dia.weekday() == 4:
                sex += 1

        carga1 = hr_seg * seg + hr_ter * ter + hr_qua * qua + hr_qui * qui + hr_sex * sex
        carga2 = hr_seg2 * seg + hr_ter2 * ter + hr_qua2 * qua + hr_qui2 * qui + hr_sex2 * sex
        carga3 = hr_seg3 * seg + hr_ter3 * ter + hr_qua3 * qua + hr_qui3 * qui + hr_sex3 * sex
        self.soma_carga = carga1 + carga2 + carga3
        self.salario = (carga1 * self.dsr * hr_aula) + (carga2 * self.dsr * hr_aula2) + (carga3 * self.dsr * hr_aula3)
        dia = self.data
        def hr(dia):
            if datetime.weekday(dia) == 0:
                hr = hr_seg + hr_seg2 + hr_seg3
            if datetime.weekday(dia) == 1:
                hr = hr_ter + hr_ter2 + hr_ter3
            if datetime.weekday(dia) == 2:
                hr = hr_qua + hr_qua2 + hr_qua3
            if datetime.weekday(dia) == 3:
                hr = hr_qui + hr_qui2 + hr_qui3
            if datetime.weekday(dia) == 4:
                hr = hr_sex + hr_sex2 + hr_sex3
            if datetime.weekday(dia) == 5:
                hr = hr_esc + hr_esc2 + hr_esc3
            if datetime.weekday(dia) == 6:
                hr = 0
            return hr

        self.horas = [hr(self.inicio), hr(self.inicio + timedelta(days=1)), hr(self.inicio + timedelta(days=2)),
                      hr(self.inicio + timedelta(days=3)), hr(self.inicio + timedelta(days=4)),
                      hr(self.inicio + timedelta(days=5)), hr(self.inicio + timedelta(days=6)),
                      hr(self.inicio + timedelta(days=7)), hr(self.inicio + timedelta(days=8)),
                      hr(self.inicio + timedelta(days=9)), hr(self.inicio + timedelta(days=10)),
                      hr(self.inicio + timedelta(days=11)), hr(self.inicio + timedelta(days=12)),
                      hr(self.inicio + timedelta(days=13)),
                      hr(self.inicio + timedelta(days=14)), hr(self.inicio + timedelta(days=15)),
                      hr(self.inicio + timedelta(days=16)), hr(self.inicio + timedelta(days=17)),
                      hr(self.inicio + timedelta(days=18)), hr(self.inicio + timedelta(days=19)),
                      hr(self.inicio + timedelta(days=20)),
                      hr(self.inicio + timedelta(days=21)), hr(self.inicio + timedelta(days=22)),
                      hr(self.inicio + timedelta(days=23)), hr(self.inicio + timedelta(days=24)),
                      hr(self.inicio + timedelta(days=25)), hr(self.inicio + timedelta(days=26)),
                      hr(self.inicio + timedelta(days=27)),
                      hr(self.inicio + timedelta(days=28)), hr(self.inicio + timedelta(days=29)),
                      hr(self.inicio + timedelta(days=30))]

    def mensalista(self):
        self.salario = self.user.salario
        uteis = 22
        dia = self.data

        def hrs(dia):
            if datetime.weekday(dia) == 0:
                hr = 220 / uteis
            if datetime.weekday(dia) == 1:
                hr = 220 / uteis
            if datetime.weekday(dia) == 2:
                hr = 220 / uteis
            if datetime.weekday(dia) == 3:
                hr = 220 / uteis
            if datetime.weekday(dia) == 4:
                hr = 220 / uteis
            if datetime.weekday(dia) == 5:
                hr = 0
            if datetime.weekday(dia) == 6:
                hr = 0
            return hr

        self.horas = [hrs(self.inicio), hrs(self.inicio + timedelta(days=1)), hrs(self.inicio + timedelta(days=2)),
                      hrs(self.inicio + timedelta(days=3)), hrs(self.inicio + timedelta(days=4)),
                      hrs(self.inicio + timedelta(days=5)), hrs(self.inicio + timedelta(days=6)),
                      hrs(self.inicio + timedelta(days=7)), hrs(self.inicio + timedelta(days=8)),
                      hrs(self.inicio + timedelta(days=9)), hrs(self.inicio + timedelta(days=10)),
                      hrs(self.inicio + timedelta(days=11)), hrs(self.inicio + timedelta(days=12)),
                      hrs(self.inicio + timedelta(days=13)),
                      hrs(self.inicio + timedelta(days=14)), hrs(self.inicio + timedelta(days=15)),
                      hrs(self.inicio + timedelta(days=16)), hrs(self.inicio + timedelta(days=17)),
                      hrs(self.inicio + timedelta(days=18)), hrs(self.inicio + timedelta(days=19)),
                      hrs(self.inicio + timedelta(days=20)),
                      hrs(self.inicio + timedelta(days=21)), hrs(self.inicio + timedelta(days=22)),
                      hrs(self.inicio + timedelta(days=23)), hrs(self.inicio + timedelta(days=24)),
                      hrs(self.inicio + timedelta(days=25)), hrs(self.inicio + timedelta(days=26)),
                      hrs(self.inicio + timedelta(days=27)),
                      hrs(self.inicio + timedelta(days=28)), hrs(self.inicio + timedelta(days=29)),
                      hrs(self.inicio + timedelta(days=30))]
