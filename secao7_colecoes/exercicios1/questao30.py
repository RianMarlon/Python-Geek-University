"""
30)Faça um programa que leia dois vetores de 10 elementos. Crie
um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que
contém apenas os números que estão em ambos os vetores. Não deve
conter números repetidos.
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

interseccao = conjunto1.intersection(conjunto2)

print(f"\nOs números que estão em ambos os vetores: {interseccao}")
