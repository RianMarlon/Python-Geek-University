"""
28) Baseando-se no exercício 27 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso.
"""

from secao17_heranca_polimorfismo.exercicios1.questao27 import Microondas2


class Microondas3(Microondas2):

    def __init__(self):
        """Construtor que chama a Classe Pai"""
        super().__init__()

    @Microondas2.ligado.setter
    def ligado(self, novo_valor):
        """Impedindo a mudança de valor do atributo de instância 'ligado'"""
        print("\nNão pode ligar ou desligar o microondas desse modo")

    def ligar(self):
        """Liga o microondas"""
        if self.ligado:
            print("\nO microondas já está ligado")

        else:
            self._Eletrodomestico__ligado = True

    def desligar(self):
        """Desliga o microondas"""
        if self.ligado:
            self._Eletrodomestico__ligado = False

        else:
            print("\nO microondas já está desligado")


if __name__ == "__main__":
    microondas1 = Microondas3()
    microondas1.ligado = "False"
    microondas1.desligar()
    microondas1.imprimir()
    microondas1.ligar()
    microondas1.imprimir()
