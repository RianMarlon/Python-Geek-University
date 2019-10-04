"""
31) Faça uma função para calcular o número neperiano usando uma série.
A função deve ter como parâmetro o número de termos que serão somados
(note que, quannto maior o número, mais próxima a resposta estará do valor e).

l = E(n=0) = 1 / n! = 1 / !0 + 1 / 1! + 1 / 2! + 1 / 3!
"""

from math import factorial


def numero_neperiano(numero):
    """
    Função que recebe um número de termos que serão somados para realizar
    o cálculo do número neperiano. Retorna o resultado do cálculo
    :param numero: Recebe um número inteiro(quantidade de termos)
    :return: Retorna o resultado do cálculo. Caso o 'numero' seja float ou não seja positivo,
    retorna um valor do tipo None
    """

    if (numero >= 0) and (numero // 1 == numero):

        calculo = 0
        numerador = 1

        for i in range(numero):

            denominador = factorial(i)

            calculo += numerador / denominador

        return calculo


num = int(input("Digite a quantidade de termos: "))
print(f"\nNúmero neperiano: {numero_neperiano(num)}")
