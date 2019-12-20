"""
7) Escreva um código que apresente a classe Circulo,
com atributos raio, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calculaPerimetro
devem efetual seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um círculo é obtida pela fórmula
(pi * raio * raio) e o perímetro por (2 * pi * raio), onde pi = 3,141516
"""


from secao17_heranca_polimorfismo.exercicios1.questao3 import FiguraGeometrica


class Circulo(FiguraGeometrica):

    def __init__(self, raio):
        """Construtor que recebe o raio do círculo, chama a Classe Pai
        e verifica se o valor recebido é válido ou não"""
        super().__init__()

        try:

            if type(raio) != bool:

                if float(raio) >= 0:

                    self.__raio = float(raio)
                    self.__area = 0
                    self.__perimetro = 0

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")
            exit(1)

    @property
    def raio(self):
        """Retorna o valor contido no atributo de instância 'raio'"""
        return self.__raio

    @property
    def perimetro(self):
        """Retorna o valor contido no atributo de instância 'perimetro'"""
        return self.__perimetro

    @property
    def area(self):
        """Retorna o valor contido no atributo de instância 'area'"""
        return self.__area

    @raio.setter
    def raio(self, novo_raio):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'raio'"""

        try:

            if self.__raio == 0:

                if float(novo_raio) > 0:

                    self.__raio = novo_raio

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    def calcular_perimetro(self):
        """Realizar o cálculo do perímetro do círculo e atribui o resultado ao
        atributo de instância 'perimetro'"""
        pi = 3.141516
        self.__area = 2 * pi * self.__raio

    def calcular_area(self):
        """Realizar o cálculo da área do círculo e atribui o resultado ao
         atributo de instância 'area'"""
        pi = 3.141516
        self.__perimetro = pi * (self.__raio ** 2)

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nRaio: {self.__raio}")
        print(f"Perímetro: {self.__perimetro}")
        print(f"Área: {self.__area}")


if __name__ == "__main__":
    c1 = Circulo("7.6")
    c1.imprimir()
    c1.calcular_area()
    c1.imprimir()
    c1.calcular_perimetro()
    c1.imprimir()




