"""
30) Baseando-se no exercício 29 qadicione os métodos fecharPorta e abrirPorta que
deverá mudar o contéudo do atributo portaFechada conforme o caso.
"""

from secao17_heranca_polimorfismo.exercicios1.questao29 import Microondas4


class Microondas5(Microondas4):

    def __init__(self):
        """Construtor que chama a Classe Pai"""
        super().__init__(True)

    @Microondas4.porta_fechada.setter
    def porta_fechada(self, novo_valor):
        """Impedindo a mudança de valor do atributo de instância 'ligado'"""
        print("\nNão pode abrir ou fechar a porta do microondas desse modo")

    def fechar_porta(self):
        """Fecha a porta do microondas"""
        if self.porta_fechada:
            print("\nA porta do microondas já está fechada")

        else:
            self._Microondas4__porta_fechada = True

    def abrir_porta(self):
        """Abre a porta do microondas"""
        if self.porta_fechada:
            self._Microondas4__porta_fechada = False

        else:
            print("\nA porta do microondas já está aberta")


if __name__ == "__main__":
    microondas1 = Microondas5()
    microondas1.porta_fechada = "false"
    microondas1.ligado = "False"
    microondas1.desligar()
    microondas1.imprimir()
    microondas1.porta_fechada = "true"
    microondas1.ligar()
    microondas1.imprimir()
    microondas1.abrir_porta()


