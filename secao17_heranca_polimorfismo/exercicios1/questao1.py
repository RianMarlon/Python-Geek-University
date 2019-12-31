"""
1) Escreva um código que apresente a classe Pessoa, com atributos nome,
endereço e telefone e, o método imprimir. O método imprimir deve mostra todos
os valores de todos os atributos.
"""

from verificacao import (verificar_telefone,
                         verificar_texto,
                         verificar_endereco)


class Pessoa:

    def __init__(self, nome, endereco, telefone):
        """Construtor que recebe um nome, endereço e telefone da pessoa,
        verificando se os mesmos são válidos ou não"""

        if verificar_texto(nome) and verificar_endereco(endereco) and verificar_telefone(telefone):
            self.__nome = nome.strip().title()
            self.__telefone = telefone if isinstance(telefone, int) else telefone.strip()
            self.__endereco = endereco.strip().title()

        else:
            print("\nValores inválidos!")
            exit(1)

    @property
    def nome(self):
        """Retorna o valor contido no atributo de instância 'nome'"""
        return self.__nome

    @property
    def telefone(self):
        """Retorna o valor contido no atributo de instância 'telefone'"""
        return self.__telefone

    @property
    def endereco(self):
        """Retorna o valor contido no atributo de instância 'endereço'"""
        return self.__endereco

    @nome.setter
    def nome(self, novo_nome):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'nome'"""

        if verificar_texto(novo_nome):

            self.__nome = novo_nome

        else:
            print("\nNome inválido")

    @telefone.setter
    def telefone(self, novo_telefone):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'telefone'"""

        if verificar_telefone(novo_telefone):
            self.__telefone = novo_telefone

        else:
            print("\nTelefone inválido")

    @endereco.setter
    def endereco(self, novo_endereco):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'endereco'"""

        if verificar_endereco(novo_endereco):
            self.__endereco = novo_endereco

        else:
            print("\nEndereço inválido")

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nNome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
        print(f"Endereço: {self.__endereco}")


if __name__ == "__main__":
    pessoa1 = Pessoa("Rian Marlon", "Rua: Marleno Guimarães, Bairro: 2 de Agosto", "(99) 9 8999-9988")
    pessoa1.imprimir()





