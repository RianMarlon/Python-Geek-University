"""
32) Faça uma funçao chamada 'simplifica' que recebe como parâmetro o numerador
e o denominador de uma fração. Esta função deve simplificar a fração
recebebida dividindo o numero e o denominador pelo maior fator possível.
Por exemplo, a fração 36/60 simplifica para 3/5 dividindo o numerador e o denominador
por 12. A funcão deve modificar as variáveis passadas como parâmetro.
"""


def simplifica(numerador, denominador):
    """
    Função que recebe como parâmetro o numerador e o denominador de uma fração e retorna os
    dois valores recebidos, modificados
    :param numerador: Recebe o valor do numerador da fração
    :param denominador: Recebe o valor do denominador da fração
    :return: Retorna o valor do numerador e do denominador, modificados
    """

    if denominador > 0:

        for i in range(denominador, 1, -1):

            if numerador % i == 0 and denominador % i == 0:
                numerador = int(numerador / i)
                denominador = int(denominador / i)

                break

    else:

        for i in range(denominador*(-1), 1, -1):

            if numerador % i == 0 and denominador % i == 0:
                numerador = int(numerador / i)
                denominador = int(denominador / i)

                break

    return numerador, denominador


numerador1 = int(input("Digite o numerador da fração: "))
denominador1 = int(input("Digite o denominador da fração: "))

novo_numerador, novo_denominador = simplifica(numerador1, denominador1)

print(f"\nFração simplificada: {novo_numerador} / {novo_denominador}")
