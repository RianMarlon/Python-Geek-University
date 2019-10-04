"""
34) Faça uma função não-recursiva que receba um número inteiro positivo impar N e
retorne o fatorial duplo desse número. O fatorial duplo é definido como
o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
Assim, o fatorial duplo de 5 é: 5!! = 1 * 3 * 5 = 15
"""


def fatorial_duplo(numero):
    """
    Função que recebe um número inteiro positivo impar e retorna o fatorial duplo do mesmo
    :param numero: Recebe um número inteiro, positivo e impar
    :return: Retorna o resultado do fatorial duplo do número ímpar. Caso o número
    seja float ou não seja positivo ou par, retorna um valor do tipo None
    """

    if (numero > 0) and (numero // 1 == numero) and (numero % 2 == 1):

        fatorial = 1
        for i in range(1, numero+1):
            if i % 2 == 1:
                fatorial *= i

        return fatorial


num = int(input("Digite um número: "))
print(f"\nFatorial duplo de {num}: {fatorial_duplo(num)}")
