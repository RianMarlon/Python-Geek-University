"""
28) Faça uma função que receba como parâmetro o valor de um ângulo em grau
e calcule o valor do cosseno desse ângulo usando sua respectiva série de Taylor:

cos x = E(n=0) = (-1) ^ n / (2 * n)! * (x ^ 2 * n) = 1 - (x^2 / 2!) + (x^4 / 4!) - ...
para todo x, onde x é o valor do ângulo em radianos. Considerar pi = 3.141593 e n variando
de 0 até 5.
"""

from math import factorial


def cosseno(angulo):
    """
    Função que recebe o valor de um ângulo em graus, trasnforma o ângulo de graus para
    radianos e calcula o valor do seno do ângulo em radianos usando a série de Taylor.
    Retorna uma mensagem informando o resultado do calculo
    :param angulo: Recebe o valor do ângulo em graus
    :return: Retorna uma mensagem informando o valor do ângulo em radianos e o resultado do cálculo.
    Se o ângulo for negativo, retorna uma mensagem informando que o ângulo é inválido
    """

    if angulo > 0:

        pi = 3.141593

        x = angulo * pi / 180
        cos = 0

        for n in range(6):

            numerador = x ** (2 * n)
            denominador = factorial(2 * n)

            cos += (-1) ** n / denominador * numerador

        return f"{angulo}° em radianos: {x}" \
               f"\nCosseno de {x}: {cos}"

    return "Valor inválido"


angulo_em_graus = int(input("Digite o valor do ângulo em graus: "))
print(f"\n{cosseno(angulo_em_graus)}")

