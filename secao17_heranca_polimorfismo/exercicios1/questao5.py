"""
5) bEscreva um código que apresente a classe Retangulo, com atributos
comprimento, largura, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area
e perimetro. O método imprimir deve mostrar na tela os valores de todos os
atributos. Salienta-se que a área de retângulo é obtida peça fórmula (comprimento *
largura) e o perímetro por (2 * comprimento) + (2 * largura)
"""

from secao17_heranca_polimorfismo.exercicios1.questao3 import FiguraGeometrica


class Retangulo(FiguraGeometrica):

    def __init__(self, comprimento, largura):
        """Construtor que recebe o comprimento e a largura do retângulo,
        chama a Classe Pai e verifica se os valores recebidos são válidos ou não"""
        super().__init__()

        try:

            if type(comprimento) != bool and type(comprimento) != bool:

                if float(comprimento) >= 0 and float(largura) >= 0:

                    self.__comprimento = float(comprimento)
                    self.__largura = float(largura)
                    self.__area = 0.0
                    self.__perimetro = 0.0

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def comprimento(self):
        """Retorna o valor contido no atributo de instância 'altura'"""
        return self.__comprimento

    @property
    def largura(self):
        """Retorna o valor contido no atributo de instância 'largura'"""
        return self.__largura

    @property
    def area(self):
        """Retorna o valor contido no atributo de instância 'area'"""
        return self.__area

    @property
    def perimetro(self):
        """Retorna o valor contido no atributo de instância 'perimetro'"""
        return self.__perimetro

    @comprimento.setter
    def comprimento(self, novo_comprimento):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'altura'"""

        try:

            if self.__comprimento == 0.0:

                if type(novo_comprimento) != bool:

                    if float(novo_comprimento) > 0:

                        self.__comprimento = float(novo_comprimento)
                        self.__area = 0.0
                        self.__perimetro = 0.0

                    else:
                        raise ValueError

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    @largura.setter
    def largura(self, nova_largura):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'altura'"""

        try:

            if self.__largura == 0.0:

                if type(nova_largura) != bool:

                    if float(nova_largura) > 0:

                        self.__largura = float(nova_largura)
                        self.__area = 0.0
                        self.__perimetro = 0.0

                    else:
                        raise ValueError

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    def calcular_perimetro(self):
        """Realizar o cálculo do perímetro do retângulo e atribui o
        resultado ao atributo de instância 'perimetro'"""
        self.__perimetro = (2 * self.__comprimento) + (2 * self.__largura)

    def calcular_area(self):
        """Realizar o cálculo da área do retângulo e atribui o
        resultado ao atributo de instância 'area'"""
        self.__area = self.__comprimento * self.__largura

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nComprimento: {self.__comprimento}")
        print(f"Largura: {self.__largura}")
        print(f"Perímetro: {self.__perimetro}")
        print(f"Área: {self.__area}")


if __name__ == "__main__":
    r1 = Retangulo(19, 12)
    r1.imprimir()
    r1.calcular_area()
    r1.imprimir()
    r1.calcular_perimetro()
    r1.imprimir()

