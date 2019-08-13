"""
11) faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem crescente.
"""

num = int(input("Digite um valor: "))

print()
if num > 0:
    for i in range(0, num+1):
        print(i)

else:
    print("Digite um número positivo!")