"""
33) Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
Ex: se N = 4, N! = 24. logo, a soma de seus algarismos é 2 + 4 = 6.
"""


def soma_fatorial(numero):
    """
    Função que recebe um número positivo e retorna a soma dos algarismo de N!
    :param numero: Recebe um número inteiro positivo
    :return: Retorna a soma dos algarismo de 'numero'!
    """

    if (numero >= 0) and (numero // 1 == numero):

        fatorial = 1

        for i in range(1, int(numero+1)):
            fatorial *= i

        string = str(fatorial)

        soma = 0
        for i in range(len(string)):
            soma += int(string[i])

        return soma

    return 0


num = int(input("Digite um número: "))
print(f"\nA soma dos algarismos de {num}!: {soma_fatorial(num)}")
