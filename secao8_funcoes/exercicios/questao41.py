"""
41) Faça uma função que receba um vetor de inteiro e retorne o maior valor
"""


def maior_numero(args):
    """
    Função que recebe um vetor de inteiro e retorna o maior valor
    :param args: Recebe um vetor de números inteiros
    :return: Retorna o maior valor. Caso exista algum número float, retorna um valor do tipo None
    """

    inteiros = 0
    for i in args:
        if i // 1 == i:
            inteiros += 1

    if inteiros == len(args):
        return max(args)


print(f"\nMaior valor: {maior_numero([32, 45, 32, 43, 545, 453, 3244, 4345, 4543, 2343])}")
