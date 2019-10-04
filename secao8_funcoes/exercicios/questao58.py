"""
58) Faça uma função que receba, por parâmetro, duas matrizes quadradas
de ordem N, A e B, e retorna uma matriz C
"""


def nova_matriz(args_a, args_b):
    """
    Função que recebe duas matrizes quadradas de ordem N e retorna uma matriz C,
    com a junção das duas matrizes recebidas por parâmetro
    :param args_a: Recebe a primeira matriz quadrada
    :param args_b: Recebe a segunda matriz quadrada
    :return: Retorna uma nova matriz com a junção dos elementos das matrizes recebidas. Caso alguma das
    matrizes não seja uma matriz quadrada, retorna um valor do tipo None.
    """

    quadrada_a = True
    quadrada_b = True

    for i in range(len(args_a)):
        for j in range(len(args_a[i])):

            if not (len(args_a) == len(args_a[i])):
                quadrada_a = False

    for i in range(len(args_b)):
        for j in range(len(args_b[i])):

            if not (len(args_b) == len(args_b[i])):
                quadrada_b = False

    if quadrada_a and quadrada_b:
        matriz_c = []

        if len(args_a) >= len(args_b):

            for i in range(len(args_a)):
                matriz = []
                for j in range(len(args_a[i])):

                    matriz.append(args_a[i][j])

                matriz_c.append(matriz)

            for i in range(len(args_b)):

                for j in range(len(args_b[i])):

                    matriz_c[i].append(args_b[i][j])

        else:
            for i in range(len(args_b)):
                matriz = []
                for j in range(len(args_b[i])):

                    matriz.append(args_b[i][j])

                matriz_c.append(matriz)

            for i in range(len(args_a)):

                for j in range(len(args_a[i])):

                    matriz_c[i].append(args_a[i][j])

        return matriz_c


matriz_quadrada1 = [[1, 6, 56, 3], ['Rian', 'Marlon', 95, 3], [True, 23, False, 4], [43, 435, 'Teste', 'Uau']]
matriz_quadrada2 = [[9, 45, 34], ['Guidon', 'Alexia', '<3'], [True, 1, True]]
print(f"Nova matriz: {nova_matriz(matriz_quadrada1, matriz_quadrada2)}")
