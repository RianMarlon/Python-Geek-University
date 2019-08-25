"""
7) Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""

lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))

print(f"\nVetor: {lista}")
print(f"Maior elemento: {max(lista)}")
print(f"Posição em que se encotra o maior elemento: {lista.index(max(lista))}")
