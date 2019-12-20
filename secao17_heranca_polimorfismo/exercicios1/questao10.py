"""
10) Baseando-se no exercício 9 adicione um método construtor que permita
a definição de todos os atributos no momento da instânciação do objeto
"""
from secao17_heranca_polimorfismo.exercicios1.questao9 import Moto


class Moto2(Moto):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__("", "", "", 0)


if __name__ == "__main__":
    moto1 = Moto2()
    moto1.marca = "yamaha"
    moto1.imprimir()
    moto1.modelo = "xj6"
    moto1.imprimir()
    moto1.cor = "branco"
    moto1.imprimir()
    moto1.marcha = 6
    moto1.imprimir()

