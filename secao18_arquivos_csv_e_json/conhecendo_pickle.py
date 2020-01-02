"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O módulo Pickle não é seguro contra dados maliciosos, e desta
forma não é recomendado trabalhar com arquivo Pickle vindo de outras
pessoas que você não conheça ou de fontes desconhecidas.


import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"{self.__nome} está comendo...")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self.nome} está miando...")


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self.nome} está latindo...")


if __name__ == "__main__":

    felix = Gato("Felix")
    pluto = Cachorro("Pluto")

    # Fazendo a escrita em arquivo pickle

    with open("animais.pickle", "wb") as arquivo:

        pickle.dump((felix, pluto), arquivo)

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"{self.__nome} está comendo...")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self.nome} está miando...")


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self.nome} está latindo...")


if __name__ == "__main__":

    felix = Gato("Felix")
    pluto = Cachorro("Pluto")

    # Fazer a leitura em arquivos de dados em arquivos pickle

    with open("animais.pickle", "rb") as arquivo:

        gato, cachorro = pickle.load(arquivo)
        print(f"O gato chama-se {gato.nome}")
        gato.mia()
        print(f"O tipo do gato é {type(gato)}")

        print(f"O cachorro chama-se {cachorro.nome}")
        cachorro.late()
        print(f"O tipo do cachorro é {type(cachorro)}")


