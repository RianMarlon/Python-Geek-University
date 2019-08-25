"""
27) Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os
elementos que são primos e suas respectivas posições no vetor.
"""

lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))

print("\nElementos que são primos e suas respectivas posições no vetor: ")
for i in lista:
    cont = 0

    for j in range(1, i+1):
        if i % j == 0:
            cont += 1

    if cont <= 2:
        print(f"elemento = {i} -> posição = {lista.index(i)}")
