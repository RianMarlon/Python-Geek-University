"""
21) Escreva uma função para determinar a quantidade de números
primos abaixo de N.
"""


def primos_abaixo(numero):
    """
    Função que recebe um número e retorna a quantidade de números primos
    que existem abaixo do número informado
    :param numero: Recebe um inteiro
    :return: Retorna a quantidade de números primos abaixo de 'numero'.
    Caso o número seja float ou não seja positivo, retorna um valor do tipo None
    """

    qtd = 0

    if (numero > 0) and (numero // 1 == numero):

        for i in range(1, numero):
            cont = 0

            for j in range(1, i+1):
                if i % j == 0:
                    cont += 1

            if cont <= 2:
                qtd += 1

        return qtd


num = int(input("Digite um número: "))
print(f"\nQuantidade de números primos abaixo de {num}: {primos_abaixo(num)}")
