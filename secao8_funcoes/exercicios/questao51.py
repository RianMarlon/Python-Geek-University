"""
51) Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule
e retorne a soma dos elementos que estão na diagonal secundária.
"""


def diagonal_secundaria(args):
    """
    Função que recebe uma matriz 3 x 3 de elementos numéricos e retorna a soma
    dos elementos que estão na diagonal secundária
    :param args: Recebe uma matriz de 3 x 3 de elementos numéricos
    :return: Retorna a soma dos elementos que se encontram na diagonal principal.
    Caso não seja uma matriz 3 x 3 ou não possua apenas valores numéricos, retorna um valor do tipo None
    """

    soma = 0
    tamanho = True

    if len(args) == 3:

        for i in range(len(args)):

            if len(args[i]) == 3:
                for j in range(len(args[i])):

                    if not(type(args[i][j]) == int) or (type(args[i][j]) == float):
                        tamanho = False

                    else:
                        # 2, porque as posições vão de 0 à 2
                        if j == 2 - i:
                            soma += args[i][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[907, 44, 404], [769, 770, 6767], [394, 584, 8798]]
print(f"Soma dos elementos que estão na diagonal secundária: {diagonal_secundaria(matriz)}")
