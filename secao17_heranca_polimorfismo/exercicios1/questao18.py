"""
18) Baseando-se no exercício 17 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""

from secao17_heranca_polimorfismo.exercicios1.questao17 import Eletrodomestico


class Eletrodomestico2(Eletrodomestico):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__(False)


if __name__ == "__main__":
    geladeira = Eletrodomestico2()
    geladeira.imprimir()
    geladeira.ligado = False
    geladeira.imprimir()
    geladeira.ligado = True
    geladeira.imprimir()

