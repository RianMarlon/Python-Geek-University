"""
31) Basenado-se no exerício 30 modifique o método ligar para que só ligue
o equipamento quando a porta do mesmo estiver fechada, simulando assim
o funcionamento de um microondas.
"""

from secao17_heranca_polimorfismo.exercicios1.questao30 import Microondas5


class Microondas6(Microondas5):

    def __init__(self):
        """Construtor padrão que chama a Classe Pai"""
        super().__init__()

    def ligar(self):
        """Liga o microondas caso a porta do mesmo esteja fechada"""

        if self.porta_fechada:

            if self.ligado:
                print("\nO microondas já está ligado")

            else:
                self._Eletrodomestico__ligado = True

        else:
            print("\nA porta do microondas está aberta")


if __name__ == "__main__":
    microondas1 = Microondas6()
    microondas1.porta_fechada = "false"
    microondas1.ligado = "False"
    microondas1.desligar()
    microondas1.imprimir()
    microondas1.porta_fechada = "true"
    microondas1.ligar()
    microondas1.imprimir()
    microondas1.abrir_porta()
    microondas1.desligar()
    microondas1.ligar()
    microondas1.imprimir()
    microondas1.fechar_porta()
    microondas1.ligar()
    microondas1.imprimir()


