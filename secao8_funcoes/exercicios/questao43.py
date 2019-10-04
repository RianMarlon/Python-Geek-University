"""
43) Faça uma função que receba um vetor de inteiros e o preencha
com números aleatórios sem repetição.
"""

from random import randint


def preencher_vetor(args):
    """
    Função que recebe um vetor de inteiros e o preenche com números aleatórios
    sem repetição
    :param args: Recebe um vetor de inteiros
    :return: Retorna o vetor recebido com a adição de números aleatórios. Caso exista um
    número float, retorna um valor do tipo None
    """

    inteiros = 0
    for i in args:
        if i // 1 == i:
            inteiros += 1

    if inteiros == len(args):

        for i in range(len(args)):

            num = randint(1, 9999)

            if num not in args:
                args.append(num)

        return args


print(f"\n{preencher_vetor([1, 56, 43, 35, 3454, 3453, 3424, 4345])}")
