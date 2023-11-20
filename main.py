from model.conta import Conta
from model.CategoriasLancamento.receita import Receita
from model.CategoriasLancamento.despesa import Despesa

# Criar duas contas para o usuário
conta_nu = Conta('Nubank', 2000)
conta_bra = Conta('Bradesco', 15.50)
conta_ticket = Conta('Ticket', 185.60)

# Criar lançamentos
receita1 = Receita(1600, '2023-11-01', '2023-11-01', conta_nu, 'Salário', 'Salário')
despesa1 = Despesa(100, '2023-11-01', '2023-11-01', conta_ticket, 'Rodizio Japa', 'Alimentação Fora')

# Realizar os lançamentos nas contas

print(receita1.valor)

