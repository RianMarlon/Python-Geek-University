"""
3) Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.
"""

lista1 = []
lista2 = []
for i in range(10):
    lista1.append(float(input("Digite um número decimal: ")))
    lista2.append(lista1[i] ** 2)

print()
print(lista1)
print(lista2)
