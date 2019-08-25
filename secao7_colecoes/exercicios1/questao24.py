"""
24) Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura
em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do
aluno mais baixo e do mais alto, juntamente com suas alturas.
"""

dicionario = {}

for i in range(10):

    numero = int(input(f"Digite o número do {i+1}° aluno: "))

    # Verifica se o número digitado é o número de um aluno já existente
    if numero in dicionario.keys():
        print("Número já existente\n")
        continue

    # Se o número digitado não existe, vai pedr para adicioonar a altura
    else:
        altura = float(input(f"Digite a altura do {i + 1}° aluno: "))
        dicionario[numero] = altura

        print()

for numero, altura in dicionario.items():

    if dicionario[numero] == min(dicionario.values()):
        print(f"Aluno mais alto - Número: {numero}; altura: {altura}")

    elif dicionario[numero] == max(dicionario.values()):
        print(f"Aluno mais alto - Número: {numero}; altura: {altura}")
