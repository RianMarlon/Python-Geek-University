"""
50) Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule
e retorne a soma dos elementos que estão na diagonal principal.
"""


def diagonal_principal(args):
    """
    Função que recebe uma matriz de 3 x 3 elementos e retorna a soma
    dos elementos que estão na diagonal principal
    :param args: Recebe uma matriz de 3 x 3 elementos numericos
    :return: Retorna a soma dos elementos que se encontram na diagonal principal.
    Caso não seja uma matriz 3 x 3 ou não possua apenas valores numéricos, retorna um valor do tipo None
    """

    tamanho = True
    soma = 0

    if len(args) == 3:

        for i in range(len(args)):

            if len(args[i]) == 3:

                for j in range(len(args[i])):

                    # Se não for um valor numérico, retorna um valor do tipo None
                    if not (type(args[i][j]) == int or type(args[i][j]) == float):
                        tamanho = False

                    else:
                        if i == j:
                            soma += args[i][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[997, 8044, 434], [760, 870, 6767], [384, 584, 8798]]
print(f"Soma dos elementos que estão na diagonal principal: {diagonal_principal(matriz)}")
