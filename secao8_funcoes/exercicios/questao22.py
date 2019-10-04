"""
22) Crie uma função que receba parâmetro um valor inteiro e gere como
saída n linhas com pontos de exclamação, conforme o exemplo abaixo (para n = 5):

    !
    !!
    !!!
    !!!!
    !!!!!
"""


def pontos_exclamao(numero):
    """
    Função que recebe um número positivo inteiro e gera como saída a quantidade de linhas,
    de acordo com o número recebido, com pontos de exclamação. Caso seja float ou não seja positivo,
    ele mostra uma mensagem informando que o número é inválido
    :param numero: Recebe um inteiro
    """

    print()
    if (numero > 0) and (numero // 1 == numero):
        for i in range(1, numero+1, 1):
            print("!" * i)

    else:
        print("Número inválido")


num = int(input("Digite um número: "))
pontos_exclamao(num)
