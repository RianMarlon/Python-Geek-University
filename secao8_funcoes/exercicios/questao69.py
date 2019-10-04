"""
69) Faça um programa que faça operações simples de frações:
    . Crie e leia duas frações p e q, compostas por numerador e denominador.
    . Encontre o máximo divisor comum entre o numerador e o denominador, e simplifique
    as frações.
    . Apresente a soma, a subtração, o produto e o quociente entre as frações lidas.

Obs.: Cria uma função para cada item.
"""


def cria_fracao():
    """
    Função que ler o numerador e denominador de cada fração e retorna
    os valores lidos, formando duas frações
    :return: Retorna duas funções 'p' e 'q', compostas por numerador e denominador
    """

    numerador1 = int(input("Digite o numerador da primeira fração: "))
    denominador1 = int(input("Digite o denominador da primeira fração: "))

    numerador2 = int(input("\nDigite o numerador da segunda fração: "))
    denominador2 = int(input("Digite o denominador da segunda fração: "))
    print()

    return numerador1, denominador1, numerador2, denominador2


def simplifica_fracao(numerador1, denominador1):
    """
    Função que simplifica a fração de acordo com os números recebidos e
    imprimi na tela a fração simplificada
    :param numerador1: Recebe o numerador da fração
    :param denominador1: Recebe o denominador da fração
    """

    if denominador1 > 0:
        for i in range(denominador1, 0, -1):
            if numerador1 % i == 0 and denominador1 % i == 0:
                print(f"Fração {numerador1} / {denominador1} simplificada: "
                      f"{int(numerador1 / i)} / {int(denominador1 / i)}")
                break

    elif denominador1 < 0:
        for i in range(denominador1, 0, 1):
            if numerador1 % i == 0 and denominador1 % i == 0:
                print(f"Fração {numerador1} / {denominador1} simplificada: "
                      f"{int(numerador1 / i)} / {int(denominador1 / i)}")
                break


def calculo_fracoes(numerador1, denominador1, numerador2, denominador2):
    """
    Função que recebe duas frações e imprimi na tela o resultado da soma,
    subtração, produto e quociente das duas frações, e imprimi o resultado
    de cada operação simplificada, através da função simplifica_fracao()
    :param numerador1: Recebe o numerador da primeira fração
    :param denominador1: Recebe o denominador da primeira fração
    :param numerador2: Recebe o numerador da segunda fração
    :param denominador2: Recebe o denominador da segunda fração
    """

    if denominador1 == denominador2:
        novo_numerador = numerador1 + numerador2
        novo_denominador = denominador1

        print(f"\nA soma das duas frações: {novo_numerador} / {novo_denominador}")
        simplifica_fracao(novo_numerador, novo_denominador)

        novo_numerador = numerador1 - numerador2
        novo_denominador = denominador1
        print(f"\nA subtração das duas frações: {novo_numerador} / {novo_denominador}")
        simplifica_fracao(novo_numerador, novo_denominador)

    elif denominador1 != denominador2:

        mmc = 1
        dividindo1 = int(denominador1)
        dividindo2 = int(denominador2)

        for i in range(denominador1):

            for j in range(2, (denominador1+denominador2)):
                if dividindo1 % j == 0 and dividindo2 % j == 0:
                    dividindo1 = int(dividindo1 / j)
                    dividindo2 = int(dividindo2 / j)

                    mmc *= j
                    break

                elif dividindo1 % j == 0 and not(dividindo2 % j == 0):
                    dividindo1 = int(dividindo1 / j)

                    mmc *= j
                    break

                elif dividindo2 % j == 0 and not(dividindo1 % j == 0):
                    dividindo2 = int(dividindo2 / j)

                    mmc *= j
                    break

            if dividindo1 == 1 and dividindo2 == 1:
                break

        nume1 = int(mmc / denominador1 * numerador1)
        nume2 = int(mmc / denominador2 * numerador2)

        novo_numerador = nume1 + nume2

        print(f"\nA soma das duas frações: {novo_numerador} / {mmc}")
        simplifica_fracao(novo_numerador, mmc)

        novo_numerador = nume1 - nume2
        print(f"\nA subtração das duas frações: {novo_numerador} / {mmc}")
        simplifica_fracao(novo_numerador, mmc)

    novo_numerador = numerador1 * numerador2
    novo_denominador = denominador1 * denominador2
    print(f"\nO produto das duas frações: {novo_numerador} / {novo_denominador}")
    simplifica_fracao(novo_numerador, novo_denominador)

    novo_numerador = numerador1 * denominador2
    novo_denominador = denominador1 * numerador2
    print(f"\nO quociente das duas frações: {novo_numerador} / {novo_denominador}")
    simplifica_fracao(novo_numerador, novo_denominador)


num1, den1, num2, den2 = cria_fracao()
simplifica_fracao(num1, den1)
simplifica_fracao(num2, den2)
calculo_fracoes(num1, den1, num2, den2)
