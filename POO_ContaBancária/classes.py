from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def inserir_conta(self, conta):
        self.conta = conta
        

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def Depositar(self, valor):
        self.saldo += valor
        print('O valor foi depositado em conta.')

    def Consultar(self, conta):
        self.conta = conta
        print(f'O saldo é {self.conta.saldo}.')
    
    @abstractmethod
    def Sacar(self, valor): pass

class Poupanca(Conta):
    def Sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente.')
            return
        self.saldo -= valor
        print('O valor foi sacado da conta.')

class Corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=500):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def Sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente.')
            return
        self.saldo -= valor
        print('O valor foi sacado da conta.')


class Banco:
    def __init__(self):
        self.agencias = [100, 200, 300]
        self.clientes = []
        self.contas = []

    def add_cliente(self, cliente):
        self.clientes.append(cliente) 

    def add_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        
        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True