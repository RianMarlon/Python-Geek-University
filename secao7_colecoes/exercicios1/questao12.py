"""
12) Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores
lidos juntamente com o maior, o menor e a média dos valores.
"""

lista = []

for i in range(5):
    lista.append(float(input("Digite um número decimal: ")))

print(f"\nOs valores lidos: ", end='')
print(*lista, sep=', ')

print(f"O maior número dos valores lidos: {max(lista)}")
print(f"O menor número dos valores lidos: {min(lista)}")
print(f"A média dos valores lidos: {sum(lista) / len(lista)}")
