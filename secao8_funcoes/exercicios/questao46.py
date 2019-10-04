"""
46) Crie um programa contendo as seguintes funcões que recebem um vetor V
números reais como parâmetros:

. Impressão normal do vetor.
. Impressão inversa.
. Função que retorna a média aritmética dos elementos do vetor.

"""


def imprimir_normal(args):
    """
    Função que recebe um vetor de números reais e imprimi na tela o vetor normalmente. Caso possua
    algum elemento que não seja um número, imprimi na tela que é aceito apenas números
    :param args: Recebe um vetor de números
    """

    numeros = True
    for i in args:
        if not(type(i) == int or type(i) == float):
            numeros = False

    if numeros:
        print(f"Vetor normal: {args}")

    else:
        print("Apenas números!")


def imprimir_inverso(args):
    """
    Função que recebe um vetor de números reais e imprimi o vetor de forma inversa. Caso possua
    algum elemento que não seja um número, imprimi jna tela que é aceito apenas números
    :param args: Recebe um vetor de números
    """

    numeros = True
    for i in args:
        if not(type(i) == int or type(i) == float):
            numeros = False

    if numeros:
        print(f"Vetor inverso: {args[::-1]}")

    else:
        print("Apenas números!")


def media_vetor(args):
    """
    Função que recebe um vetor de números reais e retorna a média aritmética do vetor
    :param args: Recebe um vetor de números
    :return: Retorna a média do vetor. Caso exista algum valor que não seja um número,
    retorna um valor do tipo None
    """

    numeros = True
    for i in args:
        if not (type(i) == int or type(i) == float):
            numeros = False

    if numeros:
        return sum(args) / len(args)


imprimir_normal([12, 324, 435.345, 53.65, 34.543, 23.56, 234, 564, 45, 321])
imprimir_inverso([12, 324, 435.345, 53.65, 34.543, 23.56, 234, 564, 45, 321])
print(f"Média aritmética do vetor: {media_vetor([12, 324, 435.345, 53.65, 34.543, 23.56, 234, 564, 45, 321])}")
