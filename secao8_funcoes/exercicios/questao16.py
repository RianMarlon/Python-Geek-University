"""
16) Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha
na tela usando vários símbolos de igual (Ex: ========). A função recebe
por parâmetro quantos sinais de igual serão mostrados
"""


def desenha_linha(quantidade):
    """
    Função que recebe uma quantidade, o valor da variavel 'quantidade'
    informará a quantidade de vezes que irá se repetir o sinal
    :param quantidade: Recebe a quantidade de vezes que se deseja colocar o sinal
    """

    if quantidade // 1 == quantidade:

        print()
        for i in range(quantidade):
            print("=", end='')

        print()

    else:
        print("\nValor inválido")


qtd = float(input("Digite a quantidade de sinais '=' que serão mostrados na tela: "))

desenha_linha(qtd)
