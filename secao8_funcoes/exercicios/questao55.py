"""
55) Faça uma função que recebe, por parâmetro, uma matriz A[3][3] e
retorna a soma dos elementos da sua diagonal principal e da sua diagonal secundária
"""


def soma_diagonais(args):
    """
    Função que recebe uma matriz 3 x 3 de elementos numéricos e retorna a soma
    dos elementos que estão na diagonal principal e da secundária
    :param args: Recebe uma matriz de 3 x 3 de elementos numéricos
    :return: Retorna a soma dos elementos que se encontram na diagonal principal e secundária.
    Caso não seja uma matriz 3 x 3 ou não possua apenas valores numéricos, retorna um valor do tipo None
    """

    soma = 0
    tamanho = True

    if len(args) == 3:

        for i in range(len(args)):

            if len(args[i]) == 3:
                for j in range(len(args[i])):

                    if not (type(args[i][j]) == int) or (type(args[i][j]) == float):
                        tamanho = False

                    else:
                        # 2, porque as posições vão de 0 à 2
                        if j == 2 - i:
                            soma += args[i][j]

                        elif i == j:
                            soma += args[i][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[343, 43, 122], [769, 770, 289], [394, 584, 235]]
print(f"Soma dos elementos que estão na diagonal principal e secundária: {soma_diagonais(matriz)}")
