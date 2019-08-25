"""
11) Faça um programa que preencha um vetor com 10 números reais,
calcule e mostre a quantidade de números negativos e a soma dos números
positivos desse vetor.
"""

lista = []
contador = []
somador = []

for i in range(10):
    lista.append(float(input(f"Digite um número decimal: ")))

    if lista[i] < 0:
        contador.append(lista[i])

    else:
        somador.append(lista[i])

print(f"\nA quantidade de números negativos: {len(contador)}")
print(f"A soma dos números positivos: {sum(somador)}")
