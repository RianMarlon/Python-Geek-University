"""
60) Escreva uma função que retorne a primeira posição de uma sub-string
dentro de uma string. Caso a sub-string não seja encontrada, a função
deve retornar -1.
"""


def posicao_substring(string, substring):
    """
    Função que recebe uma substring e retorna a primeira posição
    onde foi encontrada a substring
    :param string: Recebe a string
    :param substring: Recebe a substring que deve ser encontrada na string
    :return: Retorna a primeira posição da substring encontrada na string.
    Caso não seja encontrada a substring ou algum valor informado não seja do tipo 'str'
    retorna o valor -1
    """

    tipo = True
    if not(type(string) == str and type(substring) == str):
        tipo = False

    if tipo:

        # A preguiça de percorrer toda a string, fez eu usar um try/except
        try:
            posicao = string.index(substring)
            return posicao

        except ValueError:
            return -1

    return -1


texto = "O tempo é muito lento para os que esperam" \
        "Muito rápido para os que têm medo" \
        "Muito longo para os que lamentam" \
        "Muito curto para os que festejam" \
        "Mas, para os que amam, o tempo é eterno."

sub = "lamentam"

print(f"Posição onde foi encontra a substring: {posicao_substring(texto, sub)}")
