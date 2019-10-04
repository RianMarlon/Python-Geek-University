"""
36) Faça uma função não-recursiva que receba um número inteiro positivo N
e retorne o superfatorial desse número. O superfatorial e um número N
é deifinida pelo produto dos N primeiros fatoriais de N. Assim, o super
fatorial de 4 é sf(4) = 1! * 2! * 3! * 4! = 288
"""

from math import factorial


def superfatorial(numero):
    """
    Função que recebe um número inteiro positivo e retorna o resultado do superfatorial do número
    :param numero: Recebe um número inteiro positivo
    :return: Retorna o resultado do cálculo do superfatorial do 'numero'.
    Caso o 'numero' seja float ou não seja positivo, retorna um valor do tipo None
    """

    if (numero > 0) and (numero // 1 == numero):

        super_fatorial = 1

        for i in range(1, numero+1, 1):

            super_fatorial *= factorial(i)

        return super_fatorial


num = int(input("Digite um número: "))
print(f"\nO superfatorial de {num}: {superfatorial(num)}")
