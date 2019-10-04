"""
37) Faça uma função não-recursiva que receba um número inteiro positivo n
e retorne o hiperfatorial desse número. O hiperfatorial de um número n,
escrito H(n), é definido por:

H(n) = | | n / k=1  k**k = 1**1 . 2**2 . 3**3 ... (n - 1) ** n-1 . n**n
"""


def hiperfatorial(numero):
    """
    Função que recebe um número inteiro positivo e retorna o hiperfatorial do número recebido
    :param numero: Recebe um número inteiro positivo
    :return: Retorna o hiperfatorial de 'numero'. Caso o 'numero'
    seja float ou não seja positivo, retorna um valor do tipo None
    """

    if (numero > 0) and (numero // 1 == numero):

        hiper_fatorial = 1

        for k in range(1, numero+1, 1):

            hiper_fatorial *= k ** k

        return hiper_fatorial


num = float(input("Digite um número: "))
print(f"\nHiperfatorial de {num}: {hiperfatorial(num)}")
