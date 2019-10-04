"""
20) Faça um algoritmo que receba um número inteiro positivo n
e calcule o seu fatorial, n!
"""


def fatorial(numero):
    """
    Função que recebe um número e retorna o resultado do fatorial do número
    :param numero: Recebe um inteiro
    :return: Retorna o resultado do calculo do fatorial do número.
    Caso o número seja float ou não seja positivo, retorna uma valor do tipo None
    """

    if (numero > 0) and (numero // 1 == numero):

        resultado = 1

        for i in range(1, numero+1):

            resultado *= i

        return resultado


num = int(input("Digite um número: "))

print(f"\nResultado do fatorial de {num}: {fatorial(num)}")
