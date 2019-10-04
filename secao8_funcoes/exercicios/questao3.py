"""
3) Faça uma função para verificar se um número é positivo ou negativo.
Sendo que o valor de retorno será 1 se positivo, -1 se negativo
e 0 se for igual a 0
"""


def positivo_ou_negativo(numero):
    """
    Função que retorna o valor 1 caso o número recebido seja positivo,
    -1 se negativo e se for igual a 0
    :param numero: recebe um numero
    :return: retorna um valor para cada caso(positivo, negativo ou igual a 0)
    """

    if numero > 0:
        return 1

    elif numero < 0:
        return -1

    return 0


numero_argumento = int(input("Digite um número: "))

print(f"\n{positivo_ou_negativo(numero_argumento)}")
