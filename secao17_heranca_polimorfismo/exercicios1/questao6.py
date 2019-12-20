"""
6) Baseando-se no exercício 5 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação
do objeto.
"""

from secao17_heranca_polimorfismo.exercicios1.questao5 import Retangulo


class Retangulo2(Retangulo):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__(0, 0)


if __name__ == "__main__":
    r1 = Retangulo2()
    r1.largura = 12
    r1.imprimir()
    r1.comprimento = 23
    r1.imprimir()
    r1.calcular_perimetro()
    r1.imprimir()
    r1.calcular_area()
    r1.imprimir()

