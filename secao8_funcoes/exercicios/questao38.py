"""
38) Faça uma função não-recursiva que receba um número inteiro
positivo n e retorne o fatorial exponencial desse número. Um
fatorial exponencial é um inteiro positivo n elevado à potência
de n - 1, que por sua vez é elevado à potência de n - 2 e assim
em diante. Ou seja:

n ** (n-1) ** (n-2) ...
"""


def fatorial_exponencial(numero):
    """
    Função que recebe um número inteiro positivo e retorna o fatorial exponencial do número
    :param numero: Recebe um inteiro positivo
    :return: Retorna o fatorial exponencial da variavel 'numero'.
    Caso 'numero' seja float ou não seja positivo, retorna um valor do tipo None
    """

    if (numero > 0) and (numero // 1 == numero):

        exponencial = numero

        for i in range(1, exponencial, 1):

            if numero - i > 0:
                exponencial **= numero - i

        return exponencial


num = int(input("Digite um número: "))
print(f"\nO fatorial exponencial de {num}: {fatorial_exponencial(num)}")
