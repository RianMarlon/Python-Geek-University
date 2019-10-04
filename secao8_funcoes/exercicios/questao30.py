"""
30) Faça uma função que receba como parâmetor o valor de um ângulo em graus e calcule
o valor do cosseno hiperbólico desse ângulo usando sua respectiva série de Taylor:

cosh x = E (n=0) = (x**(2*n)) / (2n)! = 1 + (x**2) / 2! + (x*4) / (4)! + ...
para todo x, onde x é o valor do ângulo em radianos. Considerar pi = 3.141593 e
n variando de 0 até 5.
"""

from math import factorial


def cosseno_hiperbolico(angulo):
    """
    Função que recebe o valor do ângulo em graus, transforma de graus para radianos e calcula
    o cosseno hiperbólico. Retorna uma mensagem informando o valor do angulo em radianos e o resultado
    do cálculo
    :param angulo: Recebe o valor do ângulo em graus
    :return: Retorna uma mensagem informando o valor do ângulo em radianos e o resultado do cálculo.
    Se o ângulo for negativo, retorna uma mensagem informando que o ângulo é inválido

    """

    if angulo > 0:

        pi = 3.141593
        x = angulo * pi / 180

        cosh = 0

        for n in range(6):

            numerador = x ** (2 * n)
            denominador = factorial(2 * n)

            cosh += numerador / denominador

        return f"{angulo}° em radianos: {x}" \
               f"\nCosseno hiperbólico de {x}: {cosh}"

    return "Valor inválido"


angulo1 = int(input("Digite o valor do ângulo em graus: "))
print(f"\n{cosseno_hiperbolico(angulo1)}")
