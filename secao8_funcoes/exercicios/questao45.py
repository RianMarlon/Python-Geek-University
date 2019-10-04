"""
45) Faça uma função que calcule o desvio padrão de um vetor  contendo n números

Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)

onde m é a media do vetor.
"""


def desvio_padrao(args):
    """
    Função que recebe um vetor de números e retorna o resultado do desvio padrão do vetor
    :param args: Recebe um vetor de números
    :return: Retorna o resultado do desvio padrão do vetor. Caso não seja um número,
    retorna um erro do tipo TypeError
    """

    n = len(args)
    m = sum(args) / len(args)

    distancia = 0
    for i in args:
        distancia += (i - m) ** 2

    return (distancia / n) ** 0.5


print(f"\nDesvio padrão: {desvio_padrao([22, 324, 34, 23, 2432, 3443, 323.43, 345.45, 43.54, 34.8])}")
