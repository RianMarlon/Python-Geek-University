"""
35) Faça uma função não-recursiva que receba um número inteiro positivo n
e retorne o fatorial quádruplo desse número. O fatorial quádruplo de um número n é dado
por: (2 * n)! / n!
"""

from math import factorial


def fatorial_quadruplo(numero):
    """
    Função que recebe um número inteiro e positivo. Retorna o resultado do fatorial quádruplo desse número.
    :param numero: Recebe um número inteiro e positivo
    :return: Retorna o resultado do fatorial quádruplo do número quando esse número é
    positivo e inteiro. Caso seja float ou não seja positivo, retorna um valor do tipo None
    """

    if (numero > 0) and (numero // 1 == numero):

        numerador = factorial(numero*2)
        denominador = factorial(numero)

        return int(numerador / denominador)


num = int(input("Digite um número: "))
print(f"\nFatorial quádruplo de {num}: {fatorial_quadruplo(num)}")
