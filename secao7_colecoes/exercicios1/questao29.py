"""
29) Faça um programa que receba 6 números inteiros e mostre:

    . Os números pares digitados;
    . A soma dos números pares digitados;
    . Os números ímpares digitados;
    . A quantidade de número ímpares digitados;
"""

lista = []

for i in range(6):
    lista.append(int(input("Digite um número: ")))

pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)

    else:
        impares.append(i)

print(f"\nOs números pares digitados: {pares}")
print(f"A soma dos números pares digitados: {sum(pares)}")
print(f"Os números ímpares digitados: {impares}")
print(f"A quantidade de número ímpares digitados: {len(impares)}")
