"""
25) Faça uma funçao que receba um inteiro N como parâmetro, calcucle e retorne
o resultado da seguinte série:

    S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3)
"""


def calculo(numero):
    """
    Função que recebe um inteiro e realiza o calculo da série: S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3),
    retornando o resultado do calculo
    :param numero: Recebe um inteiro
    :return: Retorna o resultado do cálculo da série
    """

    if (numero > 0) and (numero // 1 == numero):
        resultado = 0
        for i in range(1, numero+1):
            resultado += (i ** 2 + 1) / (i + 3)

        return resultado

    elif (numero < 0) and (numero // 1 == numero):

        resultado = 0
        for i in range(numero, 1, 1):
            resultado += (i ** 2 + 1) / (i + 3)

        return resultado

    return 0


num = int(input("Digite um número: "))
print(f"\nResultado do cálculo: {calculo(num)}")
