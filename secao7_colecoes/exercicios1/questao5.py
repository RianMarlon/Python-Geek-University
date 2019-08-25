"""
5) Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""

lista = []
cont = 0

for _ in range(10):
    lista.append(int(input("Digite um número: ")))

for i in lista:
    if i % 2 == 0:
        cont += 1

print(f"\nPossui {cont} valores pares")
