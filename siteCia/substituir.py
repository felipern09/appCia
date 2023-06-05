# funcionário faz um pedido de substituição:
#   é necessário qeu apareça uma lista de professores disponíveis para substitui-lo
#   dp de escolhido o substituto é preciso sinailsar quais dias (período completo no calendario E repetição na semana)
#   é necessário um pedido para cada tipo de aula(exemplo se o porf for da musculação e ginásti tem que mandar dois pedidos

#enviar pedido:
#pedido entra em um db que guarda suas características: quem pediu, qual modalidade, período, dias na semana, quem vai substituir

#autorização:
# pedido vai para o perfil do gerente autorizar com uma informação resumida e fácil de entender
#botão autorizar e não autrizar

#autorizado:
#pedido é excluído do db de pedidos(ou muda parametro de boolean para true como 'autorizado')
# cálculos são incluidos na folha do substituto
# horas são retiradas da folha do que saiu
# pedido é adicionado em relatório de pedidos autorizados
# informação aparece para o funcionário como autorizado (puxar do db de pedidos autorizados[ ou pedidos com bool de autorização ou nao])
#informaçãoo fica relatada para o gerente como pedidos autorizados

#negado:
# pedido é excluído do db de pedidos(ou muda parametro de boolean para true como 'negado')
# pedido é adicionado em relatório de pedidos não-autorizados
# informação aparece para o funcionário como não-autorizado (puxar do db de pedidos autorizados[ ou pedidos com bool de autorização ou nao])
# informaçãoo fica relatada para o gerente como pedidos não-autorizados


