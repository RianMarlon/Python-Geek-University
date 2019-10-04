"""
48) Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule a soma
dos elementos que estão acima da diagonal principal.
"""


def cima_diagonal(args):
    """
    Função que recebe uma matriz de 3 x 3 elementos e retorna a soma dos elementos
    que estão acima da diagonal principal.
    :param args: Recebe uma matriz 3 x 3 de apenas números
    :return: Retorna a soma dos elementos que estão acima da diagonal principal.
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

                    # Só é possível ver o que tem acima da diagonal principal, a partir da segunda linha
                    if tamanho and i > 0 and i == j:

                        for k in range(1, j+1, 1):
                            soma += args[i-k][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[123, 805, 344], [433, 789, 657], [334, 8, 67]]
print(f"Soma dos elementos que estão acima da diagonal principal: {cima_diagonal(matriz)}")
