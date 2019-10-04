"""
59) Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos
inteiros e que calcule e retorne, taambém por parâmetro, o vetor união
dos dois primeiros.
"""


def vetor_uniao(args1, args2):
    """
    Função que recebe dois vetores de 10 elementos inteiros e retorna um vetor união dos
    dois vetores recebidos como parâmetro
    :param args1: Recebe um vetor de 10 elementos inteiros
    :param args2: Recebe um vetor de 10 elementos inteiros
    :return: Retorna um vetor união dos dois vetores. Caso algum dos vetores não possua apenas
    valores inteiros e possua 10 elementos, retorna um valor do tipo None
    """

    tipo = True

    if len(args1) == 10 and len(args2) == 10:
        for i in range(10):

            if not ((type(args1[i]) == int) and (type(args2[i]) == int)):
                tipo = False

        if tipo:
            lista = []

            for i in range(10):
                lista.append(args1[i])

            for i in range(10):
                lista.append(args2[i])

            return lista


vetor1 = [23, 32, 432, 434, 43, 32, 565, 4432, 232, 243]
vetor2 = [2343, '3432', 4342, 434, 473, 352, 5654, 32, 2, 43]

print(f"Vetor união dos dois vetores: {vetor_uniao(vetor1, vetor2)}")

