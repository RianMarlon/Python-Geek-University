"""
13) Fazer um programa ler 5 valores e, em seguida, mostrar a posição onde
se encotram o maior e o menor valor.
"""

lista = []

for i in range(5):
    lista.append(float(input("Digite um valor: ")))

print(f"\nA posição onde se encontra o maior valor: {lista.index(max(lista))}")
print(f"A posição onde se encontra o menor valor: {lista.index(min(lista))}")
