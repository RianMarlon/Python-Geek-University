"""
1) Crie uma classe para representar uma pessoa, como os atirbutos privados de
nome, idade e altura. Crie os métodos públicos necessários para sets e gets e
também um método para imprimir os dados de uma pessoa.
"""

from secao13_leitura_escrita_de_arquivos.exercicio.verificacao import verificar_nome


class Pessoa:

    def __init__(self, nome, idade, altura):
        """Construtor que recebe por parâmetro um nome(string), uma idade(int) e uma
         altura(float) da pessoa"""

        try:

            if verificar_nome(nome):
                self.__nome = str(nome).strip().title()

                if not (type(idade) == bool) and not(type(altura) == bool):

                    if not (type(idade) == float):

                        if int(idade) >= 0 and float(altura) > 0:

                            self.__idade = int(idade)
                            self.__altura = float("{:.2f}".format(float(altura)))

                        else:
                            raise ValueError

                    else:
                        raise ValueError

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    def get_nome(self):
        """Retorna o atributo de instância 'nome'"""
        return self.__nome

    def get_idade(self):
        """Retorna o atributo de instância 'idade'"""
        return self.__idade

    def get_altura(self):
        """Retorna o atributo de instância 'altura'"""
        return self.__altura

    def set_nome(self, nome_novo):
        """Recebe um valor do tipo string que irá ser o novo valor do atributo de instância 'nome'"""

        if verificar_nome(nome_novo):
            self.__nome = str(nome_novo).strip().title()

        else:
            print("Nome inválido")

    def set_idade(self, idade_nova):
        """Recebe um valor do tipo int que irá ser o novo valor do atributo de instância 'idade'"""
        try:
            if not type(idade_nova) == bool and not type(idade_nova) == float:

                if int(idade_nova) >= 0:
                    self.__idade = int(idade_nova)

            else:
                raise ValueError

        except ValueError:
            print("Idade inválida")

    def set_altura(self, altura_nova):
        """Recebe um valor do tipo float que irá ser o novo valor do atributo de instância 'idade'"""
        try:

            if not type(altura_nova) == bool:

                if float(altura_nova) > 0:
                    self.__altura = "{:.2f}".format(float(altura_nova))

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("Altura inválida")

    def dados_pessoa(self):
        """Imprimi na tela os dados referentes a determinada instância"""
        print(f"Nome: {self.__nome}; Idade: {self.__idade}; Altura: {self.__altura}")


if __name__ == "__main__":

    p1 = Pessoa("Rian Marlon", "28", 1.82)
    p1.dados_pessoa()

    # p1.set_altura(True)  # Erro
    # p1.set_altura("Kksjjsjs")  # Erro
    # p1.set_idade(True)  # Erro
    # p1.set_idade("sksksdjd")  # Erro
    # p1.set_nome(435)  # Erro
    # p1.set_nome(432.345)  # Erro
    # p1.set_nome("4324345")  # Erro
    # p1.set_nome("432.45")  # Erro
    # p1.set_nome("True")  # Erro
    # p1.set_nome(True)  # Erro
    # p1.set_nome("Kksksks^`[}")  # Erro

    p1.set_nome("Augusto Monteiro")
    p1.set_idade(23)
    p1.set_altura("1.80")

    p1.dados_pessoa()
