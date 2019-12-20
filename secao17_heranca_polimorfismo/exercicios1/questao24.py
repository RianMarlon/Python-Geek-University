"""
24) Baseando-se no exercicio 23 adicione os métodos canalAcima e
canalAbaixo, sendo que o método canalAcima deve sintonizar sempre
o próximo canal em relaão ao canal atual, onde ao chegar ao maior
canal possível deverá voltar ao canal 1. O método canalAbaixo deve
sintonizar sempre o canal anterior em relação ao canal atual, onde
ao chegar ao canal 1 deverá voltar ao maior canal possível, simulando
desta forma o funcionamento de um televisor.
"""

from secao17_heranca_polimorfismo.exercicios1.questao23 import Televisor4


class Televisor5(Televisor4):

    def __init__(self, numero_canais, volume_maximo):
        """Construtor que recebe as informações referente ao número de canais,
        volume máximo, chama a Classe Pai e manda os valores para a mesma"""

        super().__init__(numero_canais, volume_maximo)

    def canal_acima(self):
        """Irá para o próximo canal em relação ao atual"""

        if self.ligado:

            if self.canal < self.numero_canais:
                self.canal += 1

            elif self.canal == self.numero_canais:
                self.canal = 1

        else:
            print("\nO televisor está desligado")

    def canal_abaixo(self):
        """Irá para o canal anterior em relação ao atual"""

        if self.ligado:

            if self.canal > 1:
                self.canal -= 1

            elif self.canal == 1:
                self.canal = self.numero_canais

        else:
            print("\nO televisor está desligado")


if __name__ == "__main__":

    tv1 = Televisor5(800, 200)
    tv1.imprimir()
    tv1.ligar()
    tv1.canal = 800
    tv1.imprimir()
    tv1.canal_acima()
    tv1.imprimir()
    tv1.canal_abaixo()
    tv1.imprimir()
    tv1.ligar()
    tv1.volume = 41
    [tv1.canal_acima() for _ in range(15)]
    tv1.volume = 100
    tv1.desligar()
    tv1.imprimir()

