"""
13) Baseando-se no exercício 12 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""


from secao17_heranca_polimorfismo.exercicios1.questao12 import Moto4


class Moto5(Moto4):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__(0, 0)


if __name__ == "__main__":

    moto1 = Moto5()
    moto1.marca = "yamaha"
    moto1.imprimir()
    moto1.modelo = "xj6"
    moto1.imprimir()
    moto1.cor = "bra99co"
    moto1.imprimir()

    moto1.maior_marcha = "8"
    moto1.menor_marcha = 1

    moto1.imprimir()

    moto1.marcha_acima()
    moto1.marcha_acima()
    moto1.marcha_abaixo()
    moto1.marcha_acima()
    moto1.marcha_acima()

    moto1.menor_marcha = 5

    moto1.imprimir()







