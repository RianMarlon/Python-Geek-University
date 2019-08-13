"""
16) Faça um programa que leia um número inteiro positivo impar N
imprima todos os núemros impares de 1 até N em ordem decrescente.
"""

num = int(input("Digite um número positivo e impar: "))

print()
if num % 2 == 1:
    print(f"Todos os números impares de 1 até {num} em ordem crescente:")
    for i in range(num+1, 0, -1):
        if i % 2 == 1:
            print(i)

else:
    print("Digite um número impar e positivo!")
