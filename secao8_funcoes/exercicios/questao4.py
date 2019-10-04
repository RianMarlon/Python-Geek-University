"""
4) Faça uma função para verificar se um número é um quadrado perfeito.
Um quadrado perfeito é um número inteiro não negativo que pode ser
expresso como o quadrado de outro número inteiro. Ex: 1, 4, 9...
"""


def quadrado_perfeito(numero):
    """
    Função que recebe um número e imprimir na tela se é um quadrado perfeito ou não
    :param numero: recebe um número
    """

    if numero > 0:

        # Verificando se o quadrado do número digitado é um inteiro
        if (numero ** 0.5) // 1 == numero ** 0.5:
            print("\nQuadrado perfeito")

        else:
            print("\nNão é um quadrado perfeito")

    else:
        print("\nO número deve ser positivo")


numero_argumento = int(input("Digite um número: "))

quadrado_perfeito(numero_argumento)
