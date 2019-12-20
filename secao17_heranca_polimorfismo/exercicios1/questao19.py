"""
19) Baseando-se no exercicio 18 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso.
"""

from secao17_heranca_polimorfismo.exercicios1.questao18 import Eletrodomestico2


class Eletrodomestico3(Eletrodomestico2):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__()

    @Eletrodomestico2.ligado.setter
    def ligado(self, novo_valor):
        """Impedindo a mudança de valor do atributo de instância 'ligado'"""
        print("\nNão pode desligar ou ligar o eletrodoméstico desse modo")

    def ligar(self):
        """Liga o eletrodoméstico, caso o mesmo esteja desligado"""

        if self.ligado:
            print("\nO Eletrodoméstico já está ligado")

        else:
            self._Eletrodomestico__ligado = True

    def desligar(self):
        """Desliga o eletrodoméstico, caso o mesmo esteja ligada"""

        if self.ligado:
            self._Eletrodomestico__ligado = False

        else:
            print("\nO Eletrodoméstico já está desligado")


if __name__ == "__main__":
    geladeira = Eletrodomestico3()
    geladeira.imprimir()
    geladeira.ligar()
    geladeira.imprimir()
    geladeira.ligar()
    geladeira.desligar()
    geladeira.imprimir()

