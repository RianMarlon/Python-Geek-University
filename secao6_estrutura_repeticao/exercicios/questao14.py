"""
14) Faça um programa que leia um número inteiro positivo par N e imprima
todos os números pares de 0 até N em ordem decrescente.
"""

num = int(input("Digite um número positivo e par: "))

print()
if (num > 0) and (num % 2 == 0):
    print(f"Todos os números impares de 1 até {num} em ordem decrescente:")
    for i in range(num+1, -1, -1):
        if i % 2 == 0:
            print(i)

else:
    print("Digite um número positivo e par")
