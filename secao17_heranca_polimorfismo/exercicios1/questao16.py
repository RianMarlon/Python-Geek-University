"""
16) Basenado-se no exercício 15 adicione os métodos ligar e deligar que
deverão mudar o conteúdo do atibuto ligada conforme o caso.
"""

from secao17_heranca_polimorfismo.exercicios1.questao15 import Moto7


class Moto8(Moto7):

    def __init__(self):
        """Construtor padrão que chama a Classe Pai"""
        super().__init__()

    @Moto7.ligada.setter
    def ligada(self, novo_valor):
        """Impedindo a mudança de valor do atributo de instância 'ligada'"""
        print("\nNão pode ligar ou desligar a moto desse modo")

    def ligar(self):
        """Liga a moto, caso a mesma esteja desligada"""

        if not self.ligada:
            if self.marcha == self.menor_marcha:
                self._Moto6__ligada = True

            else:
                print("\nAVISO: A marcha não está no neutro(menor marcha)")
                self._Moto6__ligada = True

        else:
            print("\nA moto já está ligada")

    def desligar(self):
        """Desliga a moto, caso a mesma esteja ligada"""

        if self.ligada:

            if self.marcha == self.menor_marcha:
                self._Moto6__ligada = False

            else:
                print("\nAVISO: A marcha não está no neutro(menor marcha)")
                self._Moto6__ligada = False

        else:
            print("\nA moto já está desligada")


if __name__ == "__main__":

    moto1 = Moto8()
    moto1.marca = "yamaha"
    moto1.modelo = "xj6"
    moto1.cor = "branco"
    moto1.imprimir()
    moto1.maior_marcha = 6
    moto1.menor_marcha = 1
    moto1.imprimir()

    moto1.marcha_acima()

    moto1.ligar()

    moto1.marcha_acima()

    moto1.imprimir()

    moto1.marcha_acima()
    moto1.marcha_acima()
    moto1.marcha_abaixo()
    moto1.marcha_acima()

    moto1.imprimir()

    moto1.desligar()

    moto1.imprimir()

    moto1.desligar()




