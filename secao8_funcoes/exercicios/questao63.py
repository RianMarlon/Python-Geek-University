"""
63) Crie uma função que compara duas string e que retorna se elas
são iguais ou diferentes
"""


def comparacao(texto1, texto2):
    """
    Função que recebe duas string e retorna uma mensagem se elas são iguais
    ou diferentes
    :param texto1: Recebe uma string
    :param texto2: Recebe uma string
    :return: Retorna uma mensagem informando se os textos são iguais ou não. Caso
    alguma das variaveis não seja uma string, retorna um valor do tio None
    """

    if type(texto1) == str and type(texto2) == str:

        if texto1 == texto2:
            return "Iguais"

        return "Diferentes"


frase1 = "É igual sim"
frase2 = "É igual sim"

print(f"Os dois textos são iguais ou diferentes? {comparacao(frase1, frase2)}")
