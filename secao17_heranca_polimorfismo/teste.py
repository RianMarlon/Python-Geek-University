
from verificacao import (verificar_telefone,
                         verificar_texto,
                         verificar_endereco)


class Pessoa:

    def __init__(self, nome, endereco, telefone):
        """Construtor que recebe um nome, endereço e telefone, verificando
        se os mesmos são válidos ou não"""

        if verificar_texto(nome) and verificar_telefone(telefone) and verificar_endereco(endereco):
            self.__nome = nome.strip().title()
            self.__telefone = telefone if isinstance(telefone, int) else telefone.strip()
            self.__endereco = endereco.strip().title()

        else:
            print("Valores inválidos!")
            exit(1)

    @nome.setter
    def nome(self, valor):
        """Retorna o valor contido no atributo de instância 'nome'"""
        return self.__nome

    @telefone.getter
    def telefone(self):
        """Retorna o valor contido no atributo de instância 'telefone'"""
        return self.__telefone

    @endereco.getter
    def endereco(self):
        """Retorna o valor contido no atributo de instância 'endereço'"""
        return self.__endereco

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
        print(f"Endereço: {self.__endereco}")

