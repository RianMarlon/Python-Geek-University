"""
67) Faça uma rotina que receba como parâmetro um vetor de caracteres e
seu tamanho. A função deverá de ler uma string do teclado, caractere por caractere
usando a função getchat() até que o usuário digite enter ou o tamanho máximo do
vetor seja alcançado.
"""


def getchar():
    """
    Função que retorna o caractere informado pelo usuário durante a execução da função
    :return: Retorna o caractere informado pelo usuário durante a execução da função.
    Caso o usuário digite mais de um caractere, será retornado um valor do tipo None
    """
    caractere = input("Informe um caractere: ")

    if len(caractere) <= 1:
        return caractere


def rotina(args, tamanho):
    """
    Função que recebe um vetor e realiza uma rotina preenchendo o vetor
    através de um looping até chegar ao tamanho desejado pelo usuário
    :param args: Recebe um vetor
    :param tamanho: Recebe a quantidade de vezes que deve ser preenchida pelo usuário
    :return: Retorna o vetor preenchido pelo usuário
    """

    for _ in range(tamanho):

        valor = getchar()

        if valor != "":
            args.append(valor)

        else:
            break

    return args


vetor = []
tam = 8

print(f"{rotina(vetor, tam)}")
