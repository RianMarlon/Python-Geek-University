"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (nós, desenvolvedores).


import json

ret = json.dumps(['produto', {"PlayStation 4": ("2TB", "Novo", "220V", 2340)}])

print(type(ret))

print(ret)

import json


class Gato:

    def __init__(self, raca, nome):
        self.__raca = raca
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":

    felix = Gato("Felix", "Vira-Lata")

    print(felix.__dict__)

    ret = json.dumps(felix.__dict__)
    print(ret)

Integrando o JSON com o Pickle

pip install jsonpickle


import jsonpickle


class Gato:

    def __init__(self, raca, nome):
        self.__raca = raca
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":

    felix = Gato("Felix", "Vira-Lata")

    ret = jsonpickle.encode(felix)
    print(ret)

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, raca, nome):
        self.__raca = raca
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":

    felix = Gato("Felix", "Vira-Lata")

    with open("felix.json", "w", encoding="utf-8") as arquivo:

        ret = jsonpickle.encode(felix)
        arquivo.write(ret)

"""

# Lendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, raca, nome):
        self.__raca = raca
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":

    felix = Gato("Felix", "Vira-Lata")

    with open("felix.json", "r", encoding="utf-8") as arquivo:

        conteudo = arquivo.read()
        ret = jsonpickle.decode(conteudo)
        print(ret)
        print(type(ret))
        print(ret.nome)
        print(ret.raca)

