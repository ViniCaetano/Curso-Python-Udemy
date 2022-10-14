from classes import Cliente
from classes import Conta
from classes import Poupanca
from classes import Corrente
from classes import Banco

banco = Banco()

cl1 = Cliente('Vinícius', 25)
co1 = Corrente(100, 12345, 2000)
cl1.inserir_conta(co1)

banco.add_conta(co1)
banco.add_cliente(cl1)

if banco.autenticar(cl1):
    cl1.conta.Depositar(500)
else:
    print('Cliente não autenticado.')

print('')

co1.Consultar(co1)

print('')

if banco.autenticar(cl1):
    cl1.conta.Sacar(3000)
else:
    print('Cliente não autenticado.')

print('')

co1.Consultar(co1)

print('#########################################################################')


cl2 = Cliente('Guilherme', 18)
co2 = Poupanca(200, 67890, 2000)
cl2.inserir_conta(co2)

banco.add_conta(co2)
banco.add_cliente(cl2)

if banco.autenticar(cl2):
    cl2.conta.Depositar(500)
else:
    print('Cliente não autenticado.')

print('')

co2.Consultar(co2)

print('')

if banco.autenticar(cl2):
    cl2.conta.Sacar(3000)
else:
    print('Cliente não autenticado.')

print('')

co2.Consultar(co2)
