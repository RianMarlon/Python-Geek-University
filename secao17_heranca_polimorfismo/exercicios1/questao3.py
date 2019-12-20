"""
3) Escreva um código que apresente a classe Quadrado, com atributos
lado, área e perímetro e, os métodos calcularArea, calcularPerimetro
e imprimir. Os métodos calcularArea e calcularPerimetro devem efetuar
seus respectivos cálculos e colocar os valores nos atributos area e
perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um quadrado é obtida pela
fórmula (lado * lado) e o perímetro por (4 * lado).
"""


class FiguraGeometrica:

    def __init__(self):
        pass

    def calcular_perimetro(self):
        """Método Abstrato"""
        raise NotImplementedError

    def calcular_area(self):
        """Método Abstrato"""
        raise NotImplementedError

    def imprimir(self):
        """Método abstrato"""
        raise NotImplementedError


class Quadrado(FiguraGeometrica):

    def __init__(self, lado):
        """Construtor que recebe o lado do quadrado, chama a Classe Pai e
        verifica se o valor recebido é válido ou não"""

        super().__init__()

        try:

            if type(lado) != bool:

                if float(lado) >= 0:

                    self.__lado = float(lado)
                    self.__area = 0.0
                    self.__perimetro = 0.0

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    @property
    def lado(self):
        """Retorna o valor contido no atributo de instância 'lado'"""
        return self.__lado

    @property
    def perimetro(self):
        """Retorna o valor contido no atributo de instância 'perimetro'"""
        return self.__perimetro

    @property
    def area(self):
        """Retorna o valor contido no atributo de instância 'area'"""
        return self.__area

    @lado.setter
    def lado(self, novo_lado):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'lado'"""

        try:

            if self.__lado == 0.0:

                if type(novo_lado) != bool:

                    if float(novo_lado) > 0:

                        self.__lado = float(novo_lado)
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
            exit(1)

    def calcular_perimetro(self):
        """Realizar o cálculo do perímetro do quadrado e atribui o
        resultado ao atributo de instância perimetro'"""
        self.__perimetro = 4 * self.__lado

    def calcular_area(self):
        """Realizar o cálculo da área do quadrado e atribui o resultado
        ao atributo de instância 'area'"""
        self.__area = self.__lado * self.__lado

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nLado: {self.__lado}")
        print(f"Perímetro: {self.__perimetro}")
        print(f"Área: {self.__area}")


if __name__ == "__main__":
    q1 = Quadrado("92.899")
    q1.imprimir()
    q1.calcular_area()
    q1.imprimir()
    q1.calcular_perimetro()
    q1.imprimir()


