"""
9) Faça um programa que leia um número inteiro N e depois imprima
os N primeiros números naturais ímpares
"""

n = int(input("Digite um número: "))

soma_impares = 0
cont = 0

print()
for i in range(1, n*n):
    if i % 2 == 1:
        print(i)
        cont += 1

    if cont >= n:
        break
