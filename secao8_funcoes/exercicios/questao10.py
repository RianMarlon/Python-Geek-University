"""
10) Faça uma função que receba dois números e retorne qual deles é o maior.
"""


def maior_numero(numero1, numero2):
    """
    Função que recebe dois números e retorna o maior número
    :param numero1: recebe um valor
    :param numero2: recebe um valor
    :return: retorna o maior número ('numero1' ou 'numero2')
    """

    return max([numero1, numero2])


num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

print(f"\nO maior número: {maior_numero(num1, num2)}")
