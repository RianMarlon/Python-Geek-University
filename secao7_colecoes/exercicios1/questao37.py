"""
37) Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 >
A7 > A8 > ... > A11, ou seja, está ordenando em ordem crescente até
o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente.
Dado o vetor da questão anterior, proponha um algoritmo para ordenar os
elementos.
"""

lista = []

for i in range(11):
    lista.append(int(input("Digite um número: ")))

lista2 = []

lista.sort()
lista2 += lista[0:6].copy()

lista.reverse()
lista2 += lista[0:5].copy()

print()
print(lista2)
