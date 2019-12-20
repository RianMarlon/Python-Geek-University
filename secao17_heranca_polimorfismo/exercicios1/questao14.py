"""
14)Baseando-se no exercício 13 adicione o atributo ligada que terá a função
de indicar se a moto está ligada ou não. Este atributo deverá ser do tipo
boleano. O método imprimir deve ser modificado de forma a mostrar na tela
os vaores de todos os atributos.
"""

from secao17_heranca_polimorfismo.exercicios1.questao13 import Moto5


class Moto6(Moto5):

    def __init__(self, ligada):
        """Construtor que recebe a informação referente a moto(se está ligada ou não),
        chama a Classe Pai e verifica se o valor recebido é válido ou não"""
        super().__init__()

        try:

            if type(ligada) == str:

                if ligada.strip().title() == "False" or ligada.strip() == "0":
                    self.__ligada = False

                elif ligada.strip().title() == "True" or ligada.strip() == "1":
                    self.__ligada = True

                else:
                    raise ValueError

            elif type(ligada) == int:

                if ligada == 0:
                    self.__ligada = False

                elif ligada == 1:
                    self.ligada = True

                else:
                    raise ValueError

            elif type(ligada) == bool:

                self.__ligada = ligada

        except ValueError:
            print("\nValor inválido")
            exit(1)

    @property
    def ligada(self):
        """Retorna o valor contido no atributo de instância 'ligada'"""
        return self.__ligada

    @ligada.setter
    def ligada(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'ligada'"""
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

            if self.__ligada != novo_valor:

                if self.marcha == self.menor_marcha:
                    self.__ligada = bool(novo_valor)

                else:
                    print("\nAVISO: A marcha não está no neutro(menor marcha)")
                    self.__ligada = bool(novo_valor)

            else:

                if bool(novo_valor):
                    print("\nA moto já está ligada")

                else:
                    print("\nA moto já está desligada")

        except ValueError:
            print("\nValor inválido")

    def marcha_abaixo(self):
        """Desce uma marcha, caso a moto esteja ligada e ainda tenha uma marcha abaixo da atual"""

        if self.__ligada:

            if self.marcha > self.menor_marcha:
                self._Moto__marcha -= 1

            else:
                print("\nJá se encontra na menor marcha")

        else:
            print("\nMoto está desligada")

    def marcha_acima(self):
        """Sobe uma marcha, caso a moto esteja ligada e ainda tenha uma marcha acima da atual"""

        if self.__ligada:
            if self.marcha < self.maior_marcha:
                self._Moto__marcha += 1

            else:
                print("\nJá se encontra na maior marcha")

        else:
            print("\nMoto está desligada")

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Marcha atual: {self.marcha}")
        print(f"Menor marcha: {self.menor_marcha}")
        print(f"Maior marcha: {self.maior_marcha}")
        print(f"Ligada? {'Sim' if self.__ligada else 'Não'}")


if __name__ == "__main__":
    moto1 = Moto6("False")
    moto1.marca = "yamaha"
    moto1.imprimir()
    moto1.modelo = "xj6"
    moto1.imprimir()
    moto1.cor = "branco"
    moto1.imprimir()
    moto1.maior_marcha = 6
    moto1.menor_marcha = 1
    moto1.imprimir()

    moto1.marcha_acima()
    moto1.marcha_acima()

    moto1.ligada = "True"

    moto1.imprimir()

    moto1.marcha_acima()
    moto1.marcha_acima()
    moto1.marcha_abaixo()
    moto1.marcha_acima()

    moto1.imprimir()

    moto1.ligada = False

    moto1.imprimir()

    moto1.ligada = True

    moto1.imprimir()

    moto1.ligada = True


