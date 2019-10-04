"""
19) Faça uma função que retorne o maior fator primo de um número.
"""


def fator_primo(numero):
    """
    Função que recebe um número e retorna o maior fator primo do mesmo
    :param numero: Recebe um inteiro
    :return: Retorna o maior fator primo do número recebido.
    Caso o número seja float ou não seja positivo, retorna um valor do tipo None
    """

    if numero // 1 == numero:

        divisores = int(numero)

        maior_fator = 0
        for i in range(1, divisores+1):

            cont = 0
            for j in range(1, i+1):

                if i % j == 0:
                    cont += 1

            # Aqui o fator sempre será maior que 1
            if cont == 2:

                if divisores % i == 0:

                    if i > maior_fator:
                        maior_fator = i

                    divisores = divisores / i

            # Aqui o fator sempre será 1
            elif cont == 1:

                if i > maior_fator:
                    maior_fator = i

        return maior_fator


num = float(input("Digite um número: "))
print(f"\nMaior fator primo de {num}: {fator_primo(num)}")
