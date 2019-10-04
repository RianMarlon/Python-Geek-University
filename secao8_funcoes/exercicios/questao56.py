"""
56) Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e uma linha N
e retorne a soma dos elementos dessa linha.
"""


def soma_linha(linha, args):
    """
    Função que recebe uma linha n da matriz e recebe uma matriz 7 x 6.
    Retorna a soma dos elementos dessa linha
    :param linha: recebe a linha da matriz (0 à 6), se digitar 7, vai para a linha 6
    :param args: recebe uma matriz 7 x 6 de elementos numéricos
    :return: Retorna a soma dos elementos que se encontram na linha informada. Caso não seja
    uma matriz 3 x 3 ou não possua apenas valores numéricos, retorna um valor do tipo None.
    Caso a linha informada não exista, retorna 0
    """

    soma = 0
    tamanho = True

    if len(args) == 7:

        for i in range(len(args)):

            if len(args[i]) == 6:
                for j in range(len(args[i])):

                    if not (type(args[i][j]) == int) or (type(args[i][j]) == float):
                        tamanho = False

                    if i == linha:
                        soma += args[i][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[343, 43, 122, 5443, 3443, 344], [769, 770, 289, 4354, 3443, 44], [394, 584, 235, 443, 344, 34],
          [343, 43, 122, 122, 573, 3443], [769, 770, 289, 122, 543, 33], [394, 584, 235, 122, 5443, 93],
          [394, 584, 235, 122, 5443, 93]]
linha = 6
print(f"Soma dos elementos da linha {linha}: {soma_linha(linha, matriz)}")
