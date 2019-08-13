"""
12) Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente
"""

n = int(input("Digite um número positivo: "))

print()
if n > 0:
    print("Todos os números naturais de 0 até N em ordem decrescente: ")
    for i in range (n, -1 , -1):
        print(i)

else:
    print("O número deve ser positivo!")

