"""
8) Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = ((a ** 2) + (b ** 2)) ** 0.5. Faça uma função
que receba os valores de a e b e calcule o valor da hipotenusa através da equação
"""


def hipotenusa(cateto_a, cateto_b):
    """
    Função que recebe os valores do cateto a e cateto b e realiza o calculo da hipotenusa
    do triângulo
    :param cateto_a: recebe o valor do cateto a
    :param cateto_b: recebe o valor do cateto b
    :return: retorna a hipotenusa do triângulo
    """

    return ((cateto_a ** 2) + (cateto_b ** 2)) ** 0.5


a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

print(f"\nO valor da hipotenusa do triângulo: {hipotenusa(a, b)}")
