"""
26) Faça um programa que calcule o desvio padrão de um vetor
v contendo n = 10 números, onde m é a média do vetor.

    Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)

"""

lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))

n = len(lista)
m = sum(lista) / n

quadrado_distancia = 0
for i in lista:
    quadrado_distancia += (i - m) ** 2

desvio_padrao = (quadrado_distancia / n) ** 0.5

print(f"\nO desvio padrão é {desvio_padrao}")
