"""
17) Escreva um código que apresente a classe Eletrdoméstico, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os valores de
todos os atributos. O atributo ligado será booleano e deverá indica o estado
atual do eletrodoméstico, se ligado ou desligado.
"""


class Eletrodomestico:

    def __init__(self, ligado):
        """Construtor que recebe a informação referente ao eletrodoméstico(se está ligado ou não)
        e verifica se o valor recebido é válido ou não"""
        try:
            if type(ligado) == str:

                if ligado.strip().title() == "False" or ligado.strip() == "0":
                    self.__ligado = False

                elif ligado.strip().title() == "True" or ligado.strip() == "1":
                    self.__ligado = True

                else:
                    raise ValueError

            elif type(ligado) == int:

                if ligado == 0:
                    self.__ligado = False

                elif ligado == 1:
                    self.__ligado = True

                else:
                    raise ValueError

            elif type(ligado) == bool:
                self.__ligado = ligado

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")
            exit(1)

    @property
    def ligado(self):
        """Retorna o valor contido no atributo de instância 'ligado'"""
        return self.__ligado

    @ligado.setter
    def ligado(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'ligado'"""
        try:

            if type(novo_valor) == str:

                if novo_valor.strip().title() == "False" or novo_valor.strip() == "0":
                    novo_valor = False

                elif novo_valor.strip().title() == "True" or novo_valor.strip() == "1":
                    novo_valor = True

                else:
                    raise ValueError

            elif type(novo_valor) == int:

                if novo_valor == 0:
                    novo_valor = False

                elif novo_valor == 1:
                    novo_valor = True

                else:
                    raise ValueError

            elif type(novo_valor) == bool:
                novo_valor = novo_valor

            else:
                raise ValueError

            if self.__ligado != novo_valor:
                self.__ligado = novo_valor

            else:
                if novo_valor:
                    print("\nO Eletrodoméstico já está ligado")

                else:
                    print("\nO Eletrodoméstico já está desligado")

        except ValueError:
            print("\nValor inválido")

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nLigado: {'Sim' if self.__ligado else 'Não'}")


if __name__ == "__main__":

    geladeira = Eletrodomestico("false")
    geladeira.imprimir()
    geladeira.ligado = False
    geladeira.imprimir()
    geladeira.ligado = True
    geladeira.imprimir()

