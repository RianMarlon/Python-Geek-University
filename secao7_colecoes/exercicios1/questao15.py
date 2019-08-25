"""
15) Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
eliminando elementos repetidos.
"""

lista = []

for i in range(20):
    lista.append(int(input("Digite um valor: ")))

conjunto = set(lista)

print("\nOs elementos distintos do vetor: ", end='')
print(*conjunto, sep=', ')
