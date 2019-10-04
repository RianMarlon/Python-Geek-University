"""
53) Faça uma função que verifica se uma matriz quadrada de ordem
N é a matriz identidade.
"""


def matriz_identidade(args):
    """
    Função que recebe uma matriz quadrada de ordem N e verifica se é uma matriz identidade
    :param args: Recebe uma matriz quadrada de ordem N
    :return: Retorna um valor True, caso seja uma matriz identidade.
    Caso não seja uma matriz quadrada ou uma matriz identidade, retorna False
    """

    quadrada = True

    for i in range(len(args)):
        for j in range(len(args[i])):

            if not(len(args) == len(args[i])):
                quadrada = False

    if quadrada:
        diagonal1 = True
        resto0 = True

        for i in range(len(args)):
            for j in range(len(args[i])):

                if i == j and not(args[i][j] == 1):
                    diagonal1 = False

                if not(i == j) and not(args[i][j] == 0):
                    resto0 = False

        if diagonal1 and resto0:
            return True

        return False

    return False


matriz_quadrada = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(f"É uma matriz identidade? {matriz_identidade(matriz_quadrada)}")
