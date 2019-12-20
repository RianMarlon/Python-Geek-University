"""
8) Baseando-se no exercício 7 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""

from secao17_heranca_polimorfismo.exercicios1.questao7 import Circulo


class Circulo2(Circulo):

    def __init__(self):
        """Construtor Padrão que chama a classe Pai"""
        super().__init__(0)


if __name__ == "__main__":

    c1 = Circulo2()
    c1.imprimir()
    c1.raio = 6.7
    c1.imprimir()
    c1.calcular_perimetro()
    c1.imprimir()
    c1.calcular_area()
    c1.imprimir()

