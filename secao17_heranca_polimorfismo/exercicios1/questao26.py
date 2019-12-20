"""
26) Escreva um código que apresente a classe Microondas, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os
valores de todos os atributos. O atributo ligado será boleano e verá indicar
o estado atual do microondas, se ligado ou desligado.
"""

from secao17_heranca_polimorfismo.exercicios1.questao17 import Eletrodomestico


class Microondas(Eletrodomestico):

    def __init__(self, ligado):
        """Construtor que recebe as informações referente ao microondas(se está ligada ou não)
        e chama a Classe Pai"""
        super().__init__(ligado)

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

            if self._Eletrodomestico__ligado != novo_valor:
                self._Eletrodomestico__ligado = novo_valor

            else:
                if novo_valor:
                    print("\nO microondas já está ligado")

                else:
                    print("\nO microondas já está desligado")

        except ValueError:
            print("\nValor inválido")


if __name__ == "__main__":
    microondas1 = Microondas(False)
    microondas1.ligado = "False"
    microondas1.ligado = True
    microondas1.imprimir()

