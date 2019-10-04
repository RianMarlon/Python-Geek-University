"""
5) Faça uma função e um programa de teste para o cálculo do volume
de uma esfera. Sendo que o raio é passado por parâmetro.
V = 4/3 * r * R³
"""

from math import pi


def volume_esfera(raio):
    """
    Função que recebe um raio da esfera como parametro e retorna o volume do da esfera
    :param raio: recebe o raio da esfera
    :return: retorna o volume da esfera
    """

    return (4/3) * pi * (raio ** 3)


raio_parametro = float(input("Digite o raio da esfera: "))

print(f"\nVolume da esfera: {volume_esfera(raio_parametro)}")
