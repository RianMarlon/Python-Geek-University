"""
54) Faça uma função que recebe, por parâmetro, uma matriz A[4][4] e retorna
a soma dos seus elementos
"""


def soma_elementos(args):
    """
    Função que recebe uma matriz 4 x 4 e retorna a soma dos seus elementos
    :param args: Recebe uma matriz 4 x 4 de apenas números
    :return: Retorna a soma dos elementos da matriz. Caso não seja uma matriz 4 x 4
    ou não possua apenas valores numéricos, retorna um valor do tipo None
    """

    tamanho = True
    soma = 0

    if len(args) == 4:

        for i in range(len(args)):

            if len(args[i]) == 4:

                for j in range(len(args[i])):

                    # Se não for um valor numérico, retorna um valor do tipo None
                    if not (type(args[i][j]) == int or type(args[i][j]) == float):
                        tamanho = False

                    else:
                        soma += args[i][j]

            else:
                tamanho = False

        if tamanho:
            return soma


matriz = [[345, 434, 342, 424], [43, 65, 34, 32], [21, 66, 44, 34], [44, 657, 45, 434]]
print(f"Soma dos elementos da matriz: {soma_elementos(matriz)}")
