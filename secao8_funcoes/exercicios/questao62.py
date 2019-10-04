"""
62) Crie uma função que calcule o comprimento de uma string.
"""


def comprimento_string(texto):
    """
    Função que recebe uma string e retorna seu tamanho
    :param texto: Recebe uma string
    :return: Retorna o tamanho da string. Caso o valor não seja uma string
    retorna um valor do tipo None
    """

    if type(texto) == str:
        cont = 0

        for _ in texto:
            cont += 1

        return cont


frase = "Não olhe, perigo!"
print(f"O comprimento de '{frase}': {comprimento_string(frase)}")
