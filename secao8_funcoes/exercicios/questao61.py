"""
61) Escreva uma função que compare e retorne verdadeiro, caso uma string
seja anagrama da outra, e falso, caso contrario.
"""


def anagrama(frase1, frase2):
    """
    Função que verifica se uma string é anagrama de outra e retorna verdadeiro quando
    é um anagrama
    :param frase1: Recebe uma string
    :param frase2: Recebe outra string
    :return: Retorna True caso uma string seja anagrama da outra. Caso não seja, retorna
    False
    """

    if type(frase1) == str and type(frase2) == str:

        v = True

        for i in range(len(frase1)):

            if frase1.count(frase1[i]) == frase2.count(frase1[i]):
                pass

            else:
                v = False

        if v:
            return True

        return False

    return False


texto1 = "Meu código"
texto2 = "ogcódi ueM"

print(f"'{texto1}' é anagrama de '{texto2}'? {anagrama(texto1, texto2)}")
