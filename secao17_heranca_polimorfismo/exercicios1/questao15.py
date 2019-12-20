"""
15) Basenado-se no exercício 14 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do objeto.
"""


from secao17_heranca_polimorfismo.exercicios1.questao14 import Moto6


class Moto7(Moto6):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__(False)


if __name__ == "__main__":
    moto1 = Moto7()
    moto1.marca = "yamaha"
    moto1.imprimir()
    moto1.modelo = "xj6"
    moto1.imprimir()
    moto1.cor = "branco"
    moto1.imprimir()
    moto1.maior_marcha = 6
    moto1.menor_marcha = 1
    moto1.imprimir()

    moto1.marcha_acima()
    moto1.marcha_acima()

    moto1.ligada = "True"

    moto1.imprimir()

    moto1.marcha_acima()
    moto1.marcha_acima()
    moto1.marcha_abaixo()
    moto1.marcha_acima()

    moto1.imprimir()

    moto1.ligada = False

    moto1.imprimir()

    moto1.ligada = True

    moto1.imprimir()




