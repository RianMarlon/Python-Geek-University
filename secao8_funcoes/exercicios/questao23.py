"""
23) Escreva uma função que gere um triângulo lateral de altura 2*n-1 e n largura.
Por exemplo, a saída para n = 4 seria:

    *
    **
    ***
    ****
    ***
    **
    *
"""


def triangulo_lateral(numero):
    """
    Função que recebe um número inteiro positivo e imprimi na tela um triângulo lateral de altura 2*'numero'-1
    e largura 'numero'. Caso o número seja float ou não seja positivo, imprimi na tela que o valor é inválido
    :param numero: Recebe um inteiro
    """

    print()
    if (numero > 0) and (numero // 1 == numero):

        for i in range(1, numero+1, 1):
            print("*" * i)

        for i in range(numero-1, 0, -1):
            print("*" * i)

    else:
        print("Número inválido")


num = int(input("Digite um número: "))
triangulo_lateral(num)
