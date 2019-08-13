"""
40) Elabore um programa que faça leitura de vários números inteiros, até que se
digite um número negativo. O programa tem que retornar o maior e o menor
número lido.
"""

numero = int(input("Digite um número: "))

if numero > 0:
    maior = numero
    menor = numero

    while numero >= 0:
        numero = int(input("Digite um número: "))

        if numero < 0:
            break

        elif numero > maior:
            maior = numero

        elif numero < menor:
            menor = numero

    print()
    print(f"O menor número digitado é {menor}")
    print(f"O maior número digitado é {maior}")

else:
    print("O número deve ser maior ou igual a zero")
