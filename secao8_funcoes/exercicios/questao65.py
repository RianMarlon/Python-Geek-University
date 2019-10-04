"""
64) Implemente a função a qual recebe duas strings, str1 e str2, e um
valor inteiro positivo N. A função concatena não mais que N caractere
da string apontada por str2 à string apontada por str1 e termina str1 com NULL.
"""


def concatenar(str1, str2, n):
    """
    Função que recebe duas strings e um número inteiro positivo e retorna
    os N caractes de str2 concatenados com str1
    :param str1: Recebe uma string
    :param str2: Recebe uma string
    :param n: Recebe um inteiro positivo
    :return: retorna os N caractes de str2 concatenados com str1. Caso alguma variável
    não possua o tipo desejado da função, retorna um valor do tipo None
    """

    if type(str1) == str and type(str2) == str:

        if type(n) == int and n > 0:

            conca = str1 + str2[:n:]
            str1 = None

            return conca


texto1 = "Ana "
texto2 = "Julia"
num = 3

print(f"{concatenar(texto1, texto2, num)}")
