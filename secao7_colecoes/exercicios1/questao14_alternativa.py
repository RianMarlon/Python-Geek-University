"""
14) Faça um programa que leia um vetor de 10 posições e verifique se existem
valores iguais e os escreva na tela.
"""

from collections import Counter

lista = []

for i in range(10):
    lista.append(int(input("Digite um valor: ")))

verifica = Counter(lista)

print()
for numero, quantidade in verifica.items():
    print(f"O número {numero} se repete {quantidade} vez(es).")