"""
13) Faça um programa que leia um número inteiro positivo par N e imprima
todos os números pares de 0 até N em ordem crescente.
"""

n = int(input("Digite um número positivo e par: "))

print()
if n % 2 == 0:
    print(f"Todos os números pares de 0 até {n}:")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)

else:
    print("O número digitado não é par ou é negativo/neutro!")