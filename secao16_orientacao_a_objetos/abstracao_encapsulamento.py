"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de uma grupo lógico e
hierárquico utilizando classes.

Encasular -> cápsula

            classe
--------------------------------
|                               |
|      atributos e métodos      |
|_______________________________|

# Relembrando Atirbuts/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado
__nome e um método privado chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas
Python não bloqueia este acesso fora da classe. Com Python acontece um fenômeno
chamado Name Mangling, que faz uma alteração na forma de acessar os elementos privados,
conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo
atributos e métodos privados do usuário.

print(conta1.__dict__)

print(conta1.extrato())

print(conta1._Conta__titular)  # Name Mangling

conta1._Conta__titular = "Angelina"

print(conta1.__dict__)

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)

"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor

            else:
                print("Saldo insuficiente")

        else:
            print("O valor deve ser positivo")

    def transferir(self, valor, conta_destino):

        if valor > 0:

            if self.__saldo >= valor:

                # 1 - Remover o valor da conta de origem

                self.__saldo -= valor
                self.__saldo -= 10  # Taxa de transferência paga por quem realizou a transferência

                # 2 - Adicionar o valor na conta de destino
                conta_destino.__saldo += valor

            else:
                print("Saldo insuficiente")

        else:
            print("O valor deve ser positivo")


# Testando
conta1 = Conta("Angelina", 150.00, 1500)
print(conta1.extrato())

conta2 = Conta("Felocity", 300, 2000)
print(conta2.extrato())

conta2.transferir(100, conta1)

print(conta1.extrato())
print(conta2.extrato())




