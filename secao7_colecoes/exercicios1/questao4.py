"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""

lista = []

for i in range(8):
    lista.append(int(input("Digite um valor: ")))

x = int(input("\nDigite um valor referente a posição do vetor: "))
y = int(input("Digite outro valor referente a posição do vetor: "))

print(f"\nSoma dos valores encontrados nas respectivas posições: {lista[x] + lista[y]}")
