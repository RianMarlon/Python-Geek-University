"""
72) Considerando a estrutura

    struct Vetor{
    float x;
    float y;
    float z;
    };

para representar um vetor de R³, implemente umaa função que calcule a soma
de dois vetores. Essa função deve obedecer ao protótipo:

void soma (struct Vetor* v1, struct Vetor* v2, struct Vetor* res);

onde os parâmetros v1 e v2 são ponteiros para os vetores a seren somados, e o parâmetro
res é um ponteiro para uma estrutura vetor onde o resultado da operação deve ser
armazenado
"""


def soma(args1, args2):
    """
    Função que recebe dois vetores e retorna outro vetor, com a soma dos elementos dos vetores
    recebidos por parâmetro
    :param args1: Recebe um vetor de números
    :param args2: Recebe um vetor de números
    :return: Retorna um terceiro vetor com a soma dos elementos de cada vetor recebido. Caso
    os valores informados não sejam números, retorna um valor do tipo None
    """

    elementos = True

    for i in args1:
        if not(type(i) == int or type(i) == float):
            elementos = False

    for i in args2:
        if not(type(i) == int or type(i) == float):
            elementos = False

    if elementos:
        novo_vetor = []

        if len(args1) >= len(args2):
            for i in range(len(args2)):
                novo_vetor.append(args1[i] + args2[i])

            for i in range(len(novo_vetor), len(args1)):
                novo_vetor.append(args1[i])

        elif len(args2) > len(args1):
            for i in range(len(args1)):
                novo_vetor.append(args1[i] + args2[i])

            for i in range(len(novo_vetor), len(args2)):
                novo_vetor.append(args2[i])

        return novo_vetor


vetor1 = [3, 344, 43, 32, 35, 343, 7, 65, 65]
vetor2 = [32, 54, 32, 3, 3435]

print(f"Soma dos vetores: {soma(vetor1, vetor2)}")
