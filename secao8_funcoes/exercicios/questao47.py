"""
47) Faça uma função que receba ua matriz de 4 x 4 e retorne quantos valores
maiores do que 10 ela possui
"""


def maior_que_10(args):
    """
    Função que recebe uma matriz 4 x 4 e retorna a quantidade de valores maiores que 10 ela possui
    :param args: Recebe um vetor de números
    :return: Retorna a quantidade de valores maiores que 10 que existe na matriz.
    Caso a matriz não seja 4 x 4, retorna uma valor do tipo None
    """

    tamanho = True
    quantidade = 0

    # A matriz deve ter 4 vetores
    if len(args) == 4:

        for i in range(len(args)):

            # Tamanho de cada vetor dentro da matriz deve ser 4
            if len(args[i]) == 4:

                for j in range(len(args[i])):

                    if args[i][j] > 10:
                        quantidade += 1

            else:
                tamanho = False

        # Caso o tamanho seja inválido, retorna um valor do tipo None
        if tamanho:
            return quantidade


matriz = [[-112, 7, 89, 9], [3, 354, -23, -78], [232, 133, 789, -568], [678, 357, 990, 567]]
print(f"Quantidade de valores maiores que 10: {maior_que_10(matriz)}")
