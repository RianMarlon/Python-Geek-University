"""
25) Baseando-se no exercício 24 adicione os métodos volumeAcima
e volumeAbaixo, sendo que o método volumeAcima deve modificar
o volume para o próximo nível de volume possível, onde ao chegar
ao volumeMaximo não poderá possibilitar que o volume seja alterado.
O método volumeAbaixo deve modificar o volume para o nível imediatamente
inferior de volume me relação ao volume atual, não podendo ser menor do
que 0, simulando desta forma o funcionamento de um televisor.
"""

from secao17_heranca_polimorfismo.exercicios1.questao24 import Televisor5


class Televisor6(Televisor5):

    def __init__(self, numero_canais, volume_maximo):
        """Construtor que recebe as informações referente ao número de canais,
        volume máximo, chama a Classe Pai e manda os valores para a mesma"""
        super().__init__(numero_canais, volume_maximo)

    @Televisor5.volume.setter
    def volume(self, novo_valor):
        """Impedindo a mudança de valor do atributo de instância 'volume'"""
        print('\nNão pode alterar o volume desse modo')

    def volume_acima(self):
        """Irá para o próximo nível de volume possível em relação ao atual"""
        if self.ligado:

            if self.volume < self.volume_maximo:
                self._Televisor__volume += 1

            else:
                print("\nNão pode aumentar o volume")

        else:
            print("\nO televisor está desligado")

    def volume_abaixo(self):
        """Irá para o nível inferior de volume em relação ao atual"""
        if self.ligado:

            if self.volume > 0:
                self._Televisor__volume -= 1

            else:
                print("\nNão pode diminuir o volume")

        else:
            print("\nO televisor está desligado")


if __name__ == "__main__":
    tv1 = Televisor6(800, 200)
    tv1.imprimir()
    tv1.ligar()
    tv1.canal = 800
    tv1.volume_abaixo()
    tv1.imprimir()
    tv1.canal_acima()
    tv1.imprimir()
    tv1.canal_abaixo()
    tv1.imprimir()
    tv1.ligar()
    tv1.volume = 41
    [tv1.canal_acima() for _ in range(15)]
    tv1.volume = 100
    [tv1.volume_acima() for _ in range(90)]
    tv1.desligar()
    tv1.imprimir()
