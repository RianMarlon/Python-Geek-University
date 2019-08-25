"""
9) Crie um programa que lê 6 valores inteiros pares e,
em seguida, mostre na tela os valores lidos na ordem inversa.
"""

lista = []

for i in range(6):
    par = int(input("Digite um valor par: "))
    if par % 2 == 0:
        lista.append(par)

    else:
        print("Digite apenas números pares.\n")

print("\nOs valores pares lidos na ordem reversa: ", end='')
print(*lista[::-1], sep=', ')
