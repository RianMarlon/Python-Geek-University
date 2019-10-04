"""
52) Escreva uma função que recebe uma matriz quadrada de ordem
N e calcule a sua transposta (se B é a matriz transposta de A então aij = bji).
"""


def matriz_transposta(args):
    """
    Função que recebe uma matriz quadrada de ordem N e retorna a sua transposta
    :param args: Recebe uma matriz quadrada de ordem N
    :return: Retorna a matriz transposta da matriz recebida por parâmetro.
    Caso não seja uma matriz quadrada, retorna um valor do tipo None
    """

    transposta = []

    quadrada = True
    for i in range(len(args)):

        for j in range(len(args[i])):

            if not(len(args) == len(args[i])):
                quadrada = False

    if quadrada:
        for i in range(len(args)):
            matriz = []

            for j in range(len(args[i])):
                matriz.append(args[j][i])

            transposta.append(matriz)

        return transposta


matriz_quadrada = [[2, 0, 3], [5, 4, 3], [2, -1, 0]]
print(f"Matriz transposta de {matriz_quadrada}: {matriz_transposta(matriz_quadrada)}")
