"""
57) Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e
uma coluna N e retorne a soma dos elementos dessa coluna.
"""


def soma_coluna(coluna, args):
    """
    Função que recebe uma coluna n da matriz e recebe uma matriz 7 x 6.
    Retorna a soma dos elementos dessa coluna
    :param coluna: recebe a coluna da matriz (0 à 5)
    :param args: recebe uma matriz 7 x 6 de elementos numéricos
    :return: Retorna a soma dos elementos que se encontram na coluna informada. Caso não seja
    uma matriz 3 x 3 ou não possua apenas valores numéricos, retorna um valor do tipo None.
    Caso a coluna informada não exista, retorna 0
    """

    soma = 0
    tamanho = True

    if len(args) == 7:

        for i in range(len(args)):

            if len(args[i]) == 6:
                for j in range(len(args[i])):

                    if not (type(args[i][j]) == int) or (type(args[i][j]) == float):
                        tamanho = False

                    if j == coluna:
                        soma += args[i][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[343, 43, 122, 5443, 3443, 344], [769, 770, 289, 4354, 3443, 44], [394, 584, 235, 443, 344, 34],
          [343, 43, 122, 122, 573, 3443], [769, 770, 289, 122, 543, 33], [394, 584, 235, 122, 5443, 93],
          [394, 584, 235, 122, 5443, 93]]
coluna = 0
print(f"Soma dos elementos da coluna {coluna}: {soma_coluna(coluna, matriz)}")

