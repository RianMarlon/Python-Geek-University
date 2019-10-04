"""
49) Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule
e retorne a soma dos elementos que estão abaixo da diagonal
"""


def abaixo_diagonal(args):
    """
    Função que recebe uma matriz 3 x 3 e retorna a soma dos elementos
    que estão abaixo da diagonal
    :param args: Recebe uma matriz 3 x 3 de apenas números
    :return: Retorna a soma dos elementos que estão abaixo da diagonal principal.
    Caso não seja uma matriz 3 x 3 ou não possua apenas valores numéricos, retorna um valor do tipo None
    """

    tamanho = True
    soma = 0

    for i in range(len(args)):

        for j in range(len(args[i])):

            # Se não for um valor numérico, retorna um valor do tipo None
            if not (type(args[i][j]) == int or type(args[i][j]) == float):
                tamanho = False

    if len(args) == 3:

        for i in range(len(args)):

            if len(args[i]) == 3:

                for j in range(len(args[i])):

                    # Só é possível ver o que tem abaixo da diagonal principal, quando for antes da
                    # terceira linha/coluna
                    if tamanho and (i < len(args)) and (i == j):

                        # Aqui irá descer o número de linhas necessário para ver o que tem abaixo
                        # da diagonal
                        for k in range(1, len(args)-i):

                            # Exemplo: na linha 0, deve-se descer 2 linhas, pois 3 - 0 = 3
                            # então no looping ele vai descer 1 linha, depois 2 linhas
                            # abaixo da que se encontra
                            soma += args[i+k][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[367, 844, 434], [790, 990, 697], [3884, 54, 878]]
print(f"Soma dos elementos que estão abaixo da diagonal principal: {abaixo_diagonal(matriz)}")
