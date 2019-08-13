"""
15) Faça um programa que leia um número inteiro positivo impar N e imprima
todos os números impares de 1 até N em ordem crescente.
"""

num = int(input("Digite um número positivo e impar: "))

print()
if (num > 0) and (num % 2 == 1):
    print(f"Todos os números impares de 1 até {num} em ordem crescente:")
    for i in range(1, num):
        if i % 2 == 1:
            print(i)

else:
    print("Digite um número positivo e impar!!")
