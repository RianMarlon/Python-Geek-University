"""
42) Faça uma função que receba um vetor de reais e retorne a média
dele.
"""


def media(args):
    """
    Função que recebe um vetor de números reais e retorna a média do vetor
    :param args: Recebe um vetor de números reais
    :return: Retorna a média do vetor
    """

    return sum(args) / len(args)


print(f"\n{media([32.8, 23.7, 43, 2])}")
