"""
8) Escreva um programa que leia 10 números e escreva o menor
valor lido e o maior valor lido.
"""

menor = 0
maior = 0

for i in range(1, 11):
    num = int(input(f"Digite o {i}° valor: "))

    if menor == 0 and maior == 0:
        menor = num
        maior = num

    elif menor > num:
        menor = num

    elif maior < num:
        maior = num

print()
print(menor)
print(maior)