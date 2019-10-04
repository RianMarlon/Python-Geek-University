"""
12) Escreva uma função que receba um número inteiro maior que zero
e retorne a soma de todos os seus algarismos. Por exemplo,
ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido
não for maior do que zero, o programa terminará com a mensagem "Número inválido"
"""


def soma_algarismos(numero):
    """
    Função que recebe um número inteiro positivo e retorna o resultado da soma dos algarismos
    :param numero: Recebe um inteiro positivo
    :return: Retorna o resultado da soma dos algarismos do número. Caso o número seja float
    ou não seja positivo, retorna um valor do tipo None
    """

    if (numero > 0) and (numero // 1 == numero):

        algarismos = str(numero)
        soma = 0

        for i in algarismos:
            soma += int(i)

        return soma


num = int(input("Digite um número: "))

print(f"\nA soma dos algarismos: {soma_algarismos(num)}")
