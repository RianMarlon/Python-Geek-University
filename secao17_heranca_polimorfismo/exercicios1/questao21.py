"""
21) Basenado-se no exercício 20 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do
objeto.
"""

from secao17_heranca_polimorfismo.exercicios1.questao20 import Televisor


class Televisor2(Televisor):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__(False, 1, 0)


if __name__ == "__main__":
    tv1 = Televisor2()
    tv1.imprimir()
    tv1.canal = 198
    tv1.imprimir()
    tv1.volume = 39
    tv1.imprimir()



