"""
64) Implemente a função a qual recee duas strings, str1 e str2, e
concatena a string apontada por str2 à string apontada por str1
"""


def concatenar(str1, str2):
    """
    Função que recebe duas strings e retorna a primeira string concatenada
    com a segunda string
    :param str1: Recebe uma string
    :param str2: Recebe uma string
    :return: Retorna a primeira string concatenada com a segunda string.
    Caso alguma das variáveis não seja ums string, retorna um valor do tipo None
    """

    if type(str1) == str and type(str2) == str:
        return str1 + str2


texto1 = "Amo "
texto2 = "Programar"

print(f"{concatenar(texto1, texto2)}")
