"""
20) Escreva um programa que leia números inteiros no intervalo [0,50]
e os armazene em um vetor com 10 posições. Preencha um segundo vetor
apenas com os números ímpares do primeiro vetor. Imprima os dois vetores,
2 elementos por linha.
"""

lista = []
impares = []

for i in range(10):
    num = int(input("Digite um número no intervalo [0,50]: "))

    if (num >= 0) and (num <= 50):
        lista.append(num)

        if num % 2 == 1:
            impares.append(num)

print(f"\nPrimeiro vetor: ")
for i in range(0, len(lista), 2):
    print(f"{lista[i]}   ", end='')

    if len(lista) > i+1:
        print(lista[i+1])

print(f"\nSegundo vetor: ")
for i in range(0, len(impares), 2):
    print(f"{impares[i]}   ", end='')

    if len(impares) > i+1:
        print(impares[i+1])
