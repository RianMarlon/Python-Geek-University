"""
11) Baseando-se no exercício 10 adicione os métodos marchaAcima e
marchaAbaixo que deverão efetuar a troca de marchas, onde o método
marchaAcima deverá subir uma marcha, ou seja, se a moto estiver em
primeira marcha, deverá ser trocada para segunda marcha e assim por diante.
O método marchaAbaixo deverá realiar o oposto, ou seja, descer a marcha.
O método imprimir deve ser modificado de forma a mostrar na tela os valores
de todos os atributos.
"""

from secao17_heranca_polimorfismo.exercicios1.questao10 import Moto2


class Moto3(Moto2):

    def __init__(self):
        """Construtor Padrão que chama a Clsse Pai"""
        super().__init__()

    @Moto2.marcha.setter
    def marcha(self, nova_marcha):
        """Impedindo a mudança de valor do atributo de instância 'marcha'"""
        print("\nNão pode alterar a marcha desse modo")

    def marcha_abaixo(self):
        """Sobe uma marcha"""

        if self.marcha > 0:
            self._Moto__marcha += 1

        else:
            print("\nMarcha inválida")

    def marcha_acima(self):
        """Desce uma marcha"""

        self._Moto__marcha += 1


if __name__ == "__main__":
    moto1 = Moto3()
    moto1.marca = "yamaha"
    moto1.imprimir()
    moto1.modelo = "xj6"
    moto1.imprimir()
    moto1.cor = "branco"
    moto1.imprimir()
    moto1.marcha = 3

    moto1.marcha_acima()
    moto1.marcha_acima()
    moto1.marcha_acima()
    moto1.marcha_abaixo()

    moto1.imprimir()

