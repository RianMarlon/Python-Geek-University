"""
20) Escreva um código que apresente a classe Televisor, com atributos
ligado, canal e volume e, o método imprimir. O método imprimir deve
mostrar na tela os valores de todos os atributos. O atributo ligado
será boleano e deverá indicar o estado atual do televisor, se ligado
ou desligado. O atributo canal deverá indicar o canal atual em que
o televisor está sintonizado. O atributo volume deverá indicar o volume
atual do televisor.
"""

from secao17_heranca_polimorfismo.exercicios1.questao17 import Eletrodomestico


class Televisor(Eletrodomestico):

    def __init__(self, ligado, canal, volume):
        """Construtor que recebe as informações referente ao televisor(se está ligada ou não),
        o canal, o volume, chama a Classe Pai e verifica se o valor recebido é válido ou não"""
        super().__init__(ligado)

        try:

            if type(canal) != bool and type(volume) != bool:

                if int(canal) > 0:
                    self.__canal = int(canal)

                    if (int(volume) >= 0) and (int(volume) <= 100):
                        self.__volume = int(volume)

                    else:
                        raise ValueError

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def canal(self):
        """Retorna o valor contido no atributo de instância 'canal'"""
        return self.__canal

    @property
    def volume(self):
        """Retorna o valor contido no atributo de instância 'volume'"""
        return self.__volume

    @Eletrodomestico.ligado.setter
    def ligado(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'ligado'"""
        try:

            if type(novo_valor) == str:

                if novo_valor.strip().title() == "False" or novo_valor.strip() == "0":
                    novo_valor = False

                elif novo_valor.strip().title() == "True" or novo_valor.strip() == "1":
                    novo_valor = True

                else:
                    raise ValueError

            elif type(novo_valor) == int:

                if novo_valor == 0:
                    novo_valor = False

                elif novo_valor == 1:
                    novo_valor = True

                else:
                    raise ValueError

            elif type(novo_valor) == bool:
                novo_valor = novo_valor

            else:
                raise ValueError

            if self.ligado != novo_valor:
                self._Eletrodomestico__ligado = novo_valor

            else:
                if novo_valor:
                    print("\nO Televisor já está ligado")

                else:
                    print("\nO Televisor já está desligado")

        except ValueError:
            print("\nValor inválido")

    @canal.setter
    def canal(self, novo_canal):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'canal'"""
        try:

            if self.ligado:

                if int(novo_canal) != bool:

                    if int(novo_canal) > 0:
                        self.__canal = int(novo_canal)

                    else:
                        print("\nCanal inválido")

                else:
                    raise ValueError

            else:
                print("\nO televisor está desligado")

        except ValueError:
            print("\nValor inválido")
            exit(1)

    @volume.setter
    def volume(self, novo_volume):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'volume'"""
        try:

            if self.ligado:

                if int(novo_volume) != bool:

                    if (int(novo_volume) >= 0) and (int(novo_volume) <= 100):
                        self.__volume = int(novo_volume)

                    else:
                        print("\nVolume inválido")

                else:
                    raise ValueError

            else:
                print("\nO televisor está desligado")

        except ValueError:
            print("\nValor inválido")
            exit(1)

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nLigado: {'Sim' if self.ligado else 'Não'}")
        print(f"Canal: {self.__canal}")
        print(f"Volume: {self.__volume}")


if __name__ == "__main__":
    tv1 = Televisor("False", 1, 68)
    tv1.ligado = False
    tv1.imprimir()
    tv1.canal = 1
    tv1.imprimir()
    tv1.volume = 39
    tv1.imprimir()

