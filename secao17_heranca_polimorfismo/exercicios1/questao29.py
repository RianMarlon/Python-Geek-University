"""
29) Baseando-se no exercício 28 adicione o atributo portaFechada que
deverá ser boleano e deverá indicar se a porta do microondas está
ou não fechada. O método imprimir deve ser mdificado de forma a mostrar
na tela os valores de todos os métodos.
"""

from secao17_heranca_polimorfismo.exercicios1.questao28 import Microondas3


class Microondas4(Microondas3):

    def __init__(self, porta_fechada):
        """Construtor que recebe a informação referente a porta do microondas
        e verifica se o valor recebido é válido ou não"""

        super().__init__()
        try:
            if type(porta_fechada) == str:

                if porta_fechada.strip().title() == "False" or porta_fechada.strip() == "0":
                    self.__porta_fechada = False

                elif porta_fechada.strip().title() == "True" or porta_fechada.strip() == "1":
                    self.__porta_fechada = True

                else:
                    raise ValueError

            elif type(porta_fechada) == int:

                if porta_fechada == 0:
                    self.__porta_fechada = False

                elif porta_fechada == 1:
                    self.__porta_fechada = True

                else:
                    raise ValueError

            elif type(porta_fechada) == bool:
                self.__porta_fechada = porta_fechada

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")
            exit(1)

    @property
    def porta_fechada(self):
        """Retorna o valor contido no atributo de instância 'porta_fechada'"""
        return self.__porta_fechada

    @porta_fechada.setter
    def porta_fechada(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'porta_fechada'"""

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

            if self.__porta_fechada != novo_valor:
                self.__porta_fechada = novo_valor

            else:
                if novo_valor:
                    print("\nO microondas está com a porta fechada")

                else:
                    print("\nO microondas está com a porta aberta")

        except ValueError:
            print("\nValor inválido")

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nLigado: {'Sim' if self.ligado else 'Não'}")
        print(f"Porta fechada: {'Sim' if self.__porta_fechada else 'Não'}")


if __name__ == "__main__":
    microondas1 = Microondas4(False)
    microondas1.porta_fechada = "false"
    microondas1.ligado = "False"
    microondas1.desligar()
    microondas1.imprimir()
    microondas1.porta_fechada = "true"
    microondas1.ligar()
    microondas1.imprimir()




