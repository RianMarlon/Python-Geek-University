"""
39) Faça uma função 'Troque', que recebe duas variáveis reais A e B
e troca o valor delas (i.e., A recebe o valor de B e B recebe o valor de A).
"""


def troque(a, b):
    """
    Função que recebe duas variáveis reais A e B e troca o valor delas
    :param a: Recebe um número real
    :param b: Recebe um número real
    :return: Retorna os dois valores recebidos, mas trocados de posição
    """

    a, b = b, a

    return a, b


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

num1, num2 = troque(num1, num2)

print(f"\n{num1} e {num2}")
