"""
22) Baseando-se no exercicio 21 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso
"""

from secao17_heranca_polimorfismo.exercicios1.questao21 import Televisor2


class Televisor3(Televisor2):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__()

    @Televisor2.ligado.setter
    def ligado(self, novo_valor):
        """Impedindo a mudança de valor do atributo de instância 'ligado'"""
        print("\nNão pode ligar ou desligar o televisor desse modo")

    def ligar(self):

        if self.ligado:
            print("\nO televisor já está ligado")

        else:
            self._Eletrodomestico__ligado = True

    def desligar(self):

        if self.ligado:
            self._Eletrodomestico__ligado = False

        else:
            print("\nO televisor já está desligado")


if __name__ == "__main__":
    tv1 = Televisor3()
    tv1.imprimir()
    tv1.ligar()
    tv1.canal = 0
    tv1.imprimir()
    tv1.ligar()
    tv1.volume = 39
    tv1.desligar()
    tv1.imprimir()

