"""
10) Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
calcule e imprima a média geral.
"""

lista = []

for i in range(15):
    lista.append(float(input(f"Digite a nota do {i + 1}° aluno: ")))

print("\nA média geral dos alunos: %.1f" % (sum(lista) / len(lista)))
