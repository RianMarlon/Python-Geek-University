"""
12) Basenado-se no exercicio 11 adicione os atributos menorMarcha
e maiorMarcha, onde o atributo menorMarcha indica qual será a menor
marcha possível para a moto e o atributo maiorMarcha indica qual será
a maior marcha possível. Desta forma os métodos marchaAcima e marchaAbaixo
deve ser reescritos de forma a não permitirem a troca de marchar para valores
abaixo da menorMarcha e acima da maiorMarcha. O método imprimir deve ser
modificado de forma a mostrar na tela os valores de todos os atributos.
"""

from secao17_heranca_polimorfismo.exercicios1.questao11 import Moto3


class Moto4(Moto3):

    def __init__(self, menor_marcha, maior_marcha):
        """Construtor que recebe a menor marcha e a maior marcha, e chama a Classe Pai
        e verifica se os valores recebidos são válidos ou não"""
        super().__init__()

        try:
            if type(menor_marcha) != bool and type(maior_marcha) != bool:

                if int(menor_marcha) >= 0 and int(maior_marcha >= 0):
                    self.__menor_marcha = int(menor_marcha)
                    self.__maior_marcha = int(maior_marcha)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def menor_marcha(self):
        """Retorna o valor contido no atributo de instância 'menor_marcha'"""
        return self.__menor_marcha

    @property
    def maior_marcha(self):
        """Retorna o valor contido no atributo de instância 'maior_marcha'"""
        return self.__maior_marcha

    @menor_marcha.setter
    def menor_marcha(self, nova_menor_marcha):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'menor_marcha'"""

        try:

            if self.__menor_marcha == 0 and self.marcha == 0:

                if type(nova_menor_marcha) != bool:

                    if int(nova_menor_marcha) >= 0:

                        if int(nova_menor_marcha) <= int(self.maior_marcha):
                            self.__menor_marcha = int(nova_menor_marcha)
                            self._Moto__marcha = int(nova_menor_marcha)

                        else:
                            print("\nA menor marcha não pode ser maior que a maior marcha")

                    else:
                        raise ValueError

                else:
                    raise ValueError

            else:
                print("\nNão pode alterar a menor marcha, pois a marcha atual já foi modificada")

        except ValueError:
            print("\nValor inválido")

    @maior_marcha.setter
    def maior_marcha(self, nova_maior_marcha):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'menor_marcha'"""

        try:

            if self.__maior_marcha == 0:

                if type(nova_maior_marcha) != bool:

                    if int(nova_maior_marcha) > 0 and int(nova_maior_marcha) >= self.marcha:
                        self.__maior_marcha = int(nova_maior_marcha)

                    else:
                        raise ValueError

                else:
                    raise ValueError

            else:
                print("\nMaior marcha já definida")

        except ValueError:
            print("\nValor inválido")

    def marcha_abaixo(self):
        """Desce uma marcha, caso ainda tenha uma marcha abaixo da atual"""

        if self.marcha > self.__menor_marcha:
            self._Moto__marcha -= 1

        else:
            print("\nJá se encontra na menor marcha")

    def marcha_acima(self):
        """Sobe uma marcha, caso ainda tenha uma marcha acima da atual"""

        if self.marcha < self.__maior_marcha:
            self._Moto__marcha += 1

        else:
            print("\nJá se encontra na maior marcha")

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Marcha atual: {self.marcha}")
        print(f"Menor marcha: {self.__menor_marcha}")
        print(f"Maior marcha: {self.__maior_marcha}")


if __name__ == "__main__":
    moto1 = Moto4(0, 8)
    moto1.marca = "yamaha"
    moto1.imprimir()
    moto1.modelo = "xj6"
    moto1.imprimir()
    moto1.cor = "branco"
    moto1.imprimir()

    moto1.menor_marcha = 10
    moto1.marcha = 4

    moto1.imprimir()

    moto1.marcha_acima()
    moto1.marcha_acima()
    moto1.marcha_abaixo()
    moto1.marcha_acima()
    moto1.marcha_acima()

    moto1.imprimir()

