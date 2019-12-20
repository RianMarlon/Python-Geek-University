"""
POO - Herança Múltipla

Herança múltipla nada mais é do que a possibilidade de uma classe herdar de
múltiplas classe, fazendo com que a classe filha herde todos os atributos e
métodos de todas as classes herdadas.

# OBS: A herança múltipla pode ser feita de duas maneira:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;


# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MutiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


# OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a
herança, herdará todos os atributos e métodos das super classes.

"""


class Animal:

    def __init__(self, nome):

        self.__nome = nome

    @property
    def nome(self):
        return f"{self.__nome}"

    def comprimentar(self):
        return f"Eu sou {self.__nome}"


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self.nome}"

    def cumprimentar(self):
        return f"Eu sou {self.nome} do mar!"


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self.nome} está andando."

    def cumprimentar(self):
        return f"Eu sou {self.nome} da terra!"


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xim")
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim("Tux")
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # ???? Method Resolution Order - MRO


# Objeto é instância de...

print(f"Tux é instância de Pinguim? {isinstance(tux, Pinguim)}")  # True
print(f"Tux é instância de Aquatico? {isinstance(tux, Aquatico)}")  # True
print(f"Tux é instância de Terrestre? {isinstance(tux, Terrestre)}")  # True
print(f"Tux é instância de Animal? {isinstance(tux, Animal)}")  # True
print(f"Tux é instância de object? {isinstance(tux, object)}")  # True