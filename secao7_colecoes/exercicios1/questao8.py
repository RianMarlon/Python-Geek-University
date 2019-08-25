"""
8) Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre
na tela os valores lidos na ordem inversa
"""

lista = []

for i in range(6):
    lista.append(int(input("Digite um valor: ")))

print("\nOs valores lidos na ordem reversa: ", end='')
print(*lista[::-1], sep=', ')
