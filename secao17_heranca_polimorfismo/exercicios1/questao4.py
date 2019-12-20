"""
4) Baseando-se no exercício 3 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""

from secao17_heranca_polimorfismo.exercicios1.questao3 import Quadrado


class Quadrado2(Quadrado):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__(0)


if __name__ == "__main__":
    q1 = Quadrado2()
    q1.lado = 87.9
    q1.imprimir()
    q1.calcular_area()
    q1.imprimir()
    q1.calcular_perimetro()
    q1.imprimir()

