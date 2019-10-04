"""
26) Faça um algoritmo que receba um número inteiro positivo n e calcule o
somatório de 1 até n.
"""


def somatorio(numero):
    """
    Função que recebe um inteiro positivo e retorna o valor do somatório de 1 até n
    :param numero: Recebe um inteiro positivo
    :return: Retorna o resultado do somatório. Caso o número
    seja float ou não seja positivo, retorna um valor do tipo None
    """
    if (numero > 0) and (numero // 1 == numero):

        soma = 0
        for i in range(1, numero+1):
            soma += i

        return soma


num = int(input("Digite um número: "))
print(f"\nSomatório de 1 até {num}: {somatorio(num)}")
