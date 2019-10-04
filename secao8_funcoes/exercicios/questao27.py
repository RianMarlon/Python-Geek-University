"""
27) Faça uma função que receba como parâmetro o valor de um ângulo em
graus e calcule o valor do seno desse ângulo usando sua respectiva serie de Taylor:

sin x = E (n = 0) = (-1) ^ n  / (2n + 1)! * x ^ 2n + 1 = x - (x ^ 3 / 3!) + (x ^ 5 / 5!) - ...
para todo x, onde x é o valor do ângulo em radianos. Considerar r = 3.141593 e n variando
de 0 até 5
"""

from math import factorial


def seno(angulo):
    """
    Função que recebe um valor de um ângulo em graus, transforma o ângulo em graus para radianos e
    calcula o valor do seno do ângulo em radianos usando a série de Taylor. Retorna o resultado do calculo
    :param angulo: Recebe o valor do ângulo em graus
    :return: Retorna uma mensagem informando o valor do ângulo em radianos e o resultado do cálculo.
    Se o ângulo não for negativo, retorna uma mensagem informando que o ângulo é inválido.
    """

    if angulo > 0:

        pi = 3.141593

        x = angulo * pi / 180

        sen = 0.0

        for n in range(6):

            numerador = x ** (2 * n + 1)
            denominador = factorial(2 * n + 1)

            sen += (-1) ** n / denominador * numerador

        return f"{angulo}° em radianos: {x}" \
               f"\nSeno de {x}: {sen}"

    return "Valor inválido"


angulo_em_graus = int(input("Digite o valor do ângulo em graus: "))
print(f"\n{seno(angulo_em_graus)}")
