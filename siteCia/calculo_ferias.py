from datetime import datetime
from datetime import timedelta
# solicitardata de hoje+60dsó liberar calendario a partir dessa data
inicio_min1 = datetime.date(datetime.today() + timedelta(days=60))
fim_max = inicio_min1 + timedelta(days=30)
inicio_format = inicio_min1.strftime('%d/%m/%Y')


# # dividir fériasaparecer novo calendario para segundo período
#
# # primeiro período+ segundo período=30
# primeiro_periodo = timedelta(fim1)-timedelta(inicio1)
# restantes = timedelta(days=30)-timedelta(days=primeiro_periodo)
# #só liberar calandário para os dias restantes
# datetime.today() + restantes
#
# # Caso não tire férias até XX XX XXXX entrará de férias obrigatórias
#

