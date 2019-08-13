"""
19) Escreva um algoritmo que leia um número inteiro entre 100 e 999
e imprima na saída cada um dos algarismos que compõem o número
"""

num = int(input("Digite um número entre 100 e 999: "))

print()
if (num >= 100) and (num <= 999):
    lista = str(num)

    print("Cada algarismo que compõem o número:")
    for x, y in enumerate(lista):
        print(y)

else:
    print("O número deve estar entre 100 e 900")
