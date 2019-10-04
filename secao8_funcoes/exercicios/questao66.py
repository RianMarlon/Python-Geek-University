"""
66) Faça uma função que dado um caractere qualquer retorne o mesmo
caractere sempre em maiúsculo.
"""


def maiusculo(caractere):
    """
    Função que recebe um caractere qualquer e retorna o mesmo em maisculo
    :param caractere: Recebe um caractere(string)
    :return: Retorna o caractere recebido em maiusculo. Caso não seja apenas um
    caractere ou não seja do tipo string, retorna um valor do tipo None
    """

    if type(caractere) == str and len(caractere) == 1:
        return caractere.upper()


caracter = "a"
print(f"{maiusculo(caracter)}")
