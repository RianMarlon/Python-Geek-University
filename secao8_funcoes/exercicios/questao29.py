"""
29) Faça uma função que receba como parâmetro o valor de um ângulo em graus e
calcule o valor do seno hiperbólico desse ângulo usando sua respectiva série de Taylor:

sinh x = E (n=0) = (x ** (2 * n + 1)) / (2 * n + 1)! = x + x**3 / 3! + x**5 / 5! ...
para todo x, onde x é o valor do ângulo em radianos. Considerar pi = 3.141593
e n variando de 0 até 5.
"""

from math import factorial


def seno_hiperbolico(angulo):
    """
    Função que recebe o valor do ângulo em graus, transforma de graus para radianos e calcula
    o seno hiperbólico. Retorna uma mensagem informando o valor do angulo em radianos e o resultado
    do cálculo
    :param angulo: Recebe o valor do ângulo em graus
    :return: Retorna uma mensagem informando o valor do ângulo em radianos e o resultado do cálculo.
    Se o ângulo for negativo, retorna uma mensagem informando que o ângulo é inválido
    """

    if angulo > 0:

        pi = 3.141593
        x = angulo * pi / 180

        senh = 0
        for n in range(6):

            numerador = x ** (2 * n + 1)
            denominador = factorial(2 * n + 1)

            senh += numerador / denominador

        return f"{angulo}° em radianos: {x}" \
               f"\nSeno hiperbólico de {x}: {senh}"

    return "Valor inválido"


angulo1 = int(input("Digite o valor do ângulo em graus: "))
print(f"\n{seno_hiperbolico(angulo1)}")
