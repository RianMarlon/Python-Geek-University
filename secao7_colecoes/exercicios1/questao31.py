"""
31) Faça um programa que leia dois vetores de 10 elementos. Crie
um vetor que seja a união entre os 2 vetores anteriores, ou seja,
que contém os números dos dois vetores. Não deve conter números
repetidos.
"""

vetor1 = []
vetor2 = []

for i in range(10):
    vetor1.append(int(input("Digite um elemento do primeiro vetor: ")))

print()
for i in range(10):
    vetor2.append(int(input("Digite um elemento do segundo vetor: ")))

conjunto1 = set(vetor1)
conjunto2 = set(vetor2)

uniao = conjunto1.union(conjunto2)

print(f"\nOs números dos dois vetores: {uniao}")
