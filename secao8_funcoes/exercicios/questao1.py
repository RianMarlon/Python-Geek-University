"""
1) Crie uma função que recebe como parâmetro um número inteiro e devolve
o seu dobro.
"""


def dobro(numero):
    """
    Função simples que retornar o dobro do número inteiro informado pelo usuário
    :param numero: recebe um número inteiro
    :return: Retorna o dobro da variavel 'numero'. Caso 'numero' seja float, retorna um valor do tipo None
    """

    if numero // 1 == numero:

        return numero * 2


num = float(input("Digite um número: "))

print(f"\nDobro de {num}: {dobro(num)}")
