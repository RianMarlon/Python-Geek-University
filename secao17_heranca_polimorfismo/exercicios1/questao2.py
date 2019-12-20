"""
2) Baseando-se no exercício 1 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""

from secao17_heranca_polimorfismo.exercicios1.questao1 import Pessoa


class Pessoa2(Pessoa):

    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super().__init__(" ", " ", " ")


if __name__ == "__main__":
    n1 = Pessoa2()
    n1.imprimir()

    n1.nome = "Rian Marlon"
    n1.telefone = "(98) 9 9878-0875"
    n1.endereco = "Rua Batista, Bairro Saraiva Belmino"

    n1.imprimir()

