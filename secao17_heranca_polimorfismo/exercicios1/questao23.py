"""
23) Basenado-se no exercício 22 adicione os atributos numeroCanais
e, volumeMaximo, onde numeroCanais indica o número máximo de canais
que o televisor pode sintonizar e volumeMaximo indica qual o maior nível
de volume possível. O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os atributos.
"""

from secao17_heranca_polimorfismo.exercicios1.questao22 import Televisor3


class Televisor4(Televisor3):

    def __init__(self, numero_canais, volume_maximo):
        """Construtor que recebe as informações referente ao número de canais,
        volume máximo, chama a Classe Pai e verifica se o valor recebido é válido ou não"""

        super().__init__()

        try:

            if type(numero_canais) != bool and type(volume_maximo) != bool:
                self.__numero_canais = int(numero_canais)
                self.__volume_maximo = int(volume_maximo)

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def numero_canais(self):
        """Retorna o valor contido no atributo de instância 'numero_canais'"""
        return self.__numero_canais

    @property
    def volume_maximo(self):
        """Retorna o valor contido no atributo de instância 'volume_maximo'"""
        return self.__volume_maximo

    @numero_canais.setter
    def numero_canais(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'numero_canais'"""

        try:

            if type(novo_valor) != bool:

                if int(novo_valor) >= self.canal:
                    self.numero_canais = int(novo_valor)

                else:
                    print("\nO número de canais não pode ser menor que o canal atual")

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    @volume_maximo.setter
    def volume_maximo(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'volume_maximo'"""

        try:

            if type(novo_valor) != bool:

                if int(novo_valor) >= self.canal:
                    self.volume_maximo = int(novo_valor)

                else:
                    print("\nO volume máximo não pode ser menor que o volume atual")

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    @Televisor3.canal.setter
    def canal(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'canal' que não
        pode ser maior que o número de canais ou menor que 1"""

        try:

            if self.ligado:

                if type(novo_valor) != bool:

                    if (int(novo_valor) > 0) and (int(novo_valor) <= self.numero_canais):

                        self._Televisor__canal = int(novo_valor)

                    else:
                        print("\nCanal inválido")

                else:
                    raise ValueError

            else:
                print("\nO televisor está desligado")

        except ValueError:
            print("\nValor inválido")

    @Televisor3.volume.setter
    def volume(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'volume_maximo'
        que não pode ser maior que o volume máximo ou menor que 0"""

        try:

            if self.ligado:

                if type(novo_valor) != bool:

                    if (int(novo_valor) >= 0) and (int(novo_valor) <= self.volume_maximo):

                        self._Televisor__volume = int(novo_valor)

                    else:
                        print("\nVolume inválido")

                else:
                    raise ValueError

            else:
                print("\nO televisor está desligado")

        except ValueError:
            print("\nValor inválido")


if __name__ == "__main__":
    tv1 = Televisor4(800, 200)
    tv1.imprimir()
    tv1.ligar()
    tv1.canal = 800
    tv1.imprimir()
    tv1.ligar()
    tv1.volume = 39
    tv1.desligar()
    tv1.imprimir()

