"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.
"""

lista = []

for i in range(10):
    lista.append(int(input("Digite um valor: ")))

print(f"\nO maior elemnto do vetor é: {max(lista)}")
print(f"O menor elemento do vetor é: {min(lista)}")
