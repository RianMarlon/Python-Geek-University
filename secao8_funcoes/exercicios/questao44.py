"""
44) Faça uma função que receba como parâmetro um vetor X de
30 elementos inteiros e retorne, também por parâmetro, dois vetores
A e B. O vetor A deve conter os elementos pares de X eo vetor B, os
elementos impares
"""


def pares_e_impares(args):
    """
    Função que recebe um vetor 'args' de 30 elementos inteiro e retorna dois
    vetores, onde um contém os valores pares e outro os valores impares de 'args'
    :param args: Recebe um vetor de 30 elementos inteiros
    :return: Retorna dois vetores, um contendo os valores pares e outros os valores
    impares de 'args'. Caso o vetor recebido não tenha 30 elementos do tipo inteiro,
    retorna um valor do tipo None
    """

    if len(args) == 30:

        inteiros = 0
        for i in args:
            if i // 1 == i:
                inteiros += 1

        if inteiros == len(args):

            pares = []
            impares = []

            for i in args:

                if i % 2 == 0:
                    pares.append(i)

                else:
                    impares.append(i)

            return pares, impares


numeros = [30, 23, 3, 4, 65, 76, 534, 456, 46, 34, 32, 56, 345, 345, 345,
           36, 34, 34685, 34586, 3487, 3455, 34543, 345, 32, 225, 456, 566, 567, 65, 98]

print(f"\n{pares_e_impares(numeros)}")
