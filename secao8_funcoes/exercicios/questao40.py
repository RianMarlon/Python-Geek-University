"""
40) Faça uma função que receba um vetor de inteiros e retorne
quantos valores pares ele possui.
"""


def qtd_pares(args):
    """
    Função que recebe um vetor de inteiros e retorna a quantidade de valores pares do vetor
    :param args: Recebe um vetor de números inteiros
    :return: Retorna a quantidade de valores pares que o vetor possui.
    Caso exista algum número float, retorna um valor do tipo None
    """

    inteiros = 0
    for i in args:
        if i // 1 == i:
            inteiros += 1

    if inteiros == len(args):
        cont = 0
        for i in args:

            if i % 2 == 0:
                cont += 1

        return cont


lista = [10, 12, 14, 22, 45, 46, 5, 7, 3, 1, 11, 15, 17]
print(f"\n{qtd_pares(lista)}")
