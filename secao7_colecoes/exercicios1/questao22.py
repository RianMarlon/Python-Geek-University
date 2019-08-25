"""
22) Faça um programa que leia dois vetores de 10 posições e calcule
outro vetor contendo, nas posições pares os valores do primeiro
e nas posições impares os valores do segundo.
"""

lista1 = []
lista2 = []

for i in range(10):
    lista1.append(int(input("Digite um valor para o primeiro vetor: ")))

print()
for i in range(10):
    lista2.append(int(input("Digite um valor para o segundo vetor: ")))

lista3 = []
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f"Terceiro vetor: {lista3}")
