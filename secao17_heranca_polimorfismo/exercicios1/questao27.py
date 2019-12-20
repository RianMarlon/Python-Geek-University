"""
27) Basenado-se no exercício 26 adicione um método construtor
que permita o definição de todos os atributos no momento da
instanciação do objeto.
"""

from secao17_heranca_polimorfismo.exercicios1.questao26 import Microondas


class Microondas2(Microondas):

    def __init__(self):
        """Construtor que chama a Classe Pai"""
        super().__init__(False)


if __name__ == "__main__":
    microondas1 = Microondas2()
    microondas1.ligado = "False"
    microondas1.ligado = True
    microondas1.imprimir()

