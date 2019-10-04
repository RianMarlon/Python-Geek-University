"""
68) Faça uma função que receba duas string e retorne a intercalação letra a letra
da primeira com a segunda string. A string intercalada deve ser retornada na primeira string
"""


def intercalar(str1, str2):
    """
    Função que recebe duas string e retorna a intercalação letra a letra
    da primeira com a segunda string
    :param str1: Recebe uma string
    :param str2: Recebe uma string
    :return: Retorna a intercalação letra a letra da primeira com a segunda string.
    Caso não seja uma string, retorna um valor o tipo None
    """

    if type(str1) == str and type(str2) == str:
        inter = ''

        if len(str1) <= len(str2):
            for i in range(len(str1)):
                inter += str1[i] + str2[i]

        else:
            for i in range(len(str2)):
                inter += str1[i] + str2[i]

        return inter


texto1 = "University"
texto2 = "Geek"
print(f"{intercalar(texto1, texto2)}")
