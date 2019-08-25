"""
32) Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma
que o usuário não informa elementos repetidos). Calcule e mostre os
vetores resultantes em cada caso abaixo:

    . Soma entre x e y: soma de cada elemento x com o elemento da mesma
    posição em y.
    . Produto entre x e y: multiplicação de cada elemento de x com o
    elemento da mesma posição em y.
    . Diferença entre x e y: todos os elementos de x que não existam em y.
    . Interseção entre x e y: apenas os elementos que aparecem nos dois vetores
    . União entre x e y: todos os elemntos de x, e todos os elementos de y
    que não estão em x.
"""

x = []
y = []

for i in range(5):
    x.append(int(input("Digite um elemento do vetor x: ")))

print()
for i in range(5):
    y.append(int(input("Digite um elemnto do vetor y: ")))

conjunto_x = set(x)
conjunto_y = set(y)

soma = sum(conjunto_x) + sum(conjunto_y)

produto = 1
for i in range(5):
    produto *= (x[i] * y[i])

diferenca = conjunto_x.difference(conjunto_y)
intersecao = conjunto_x.intersection(conjunto_y)
uniao = conjunto_x.union(conjunto_y)

print(f"\nSoma entre x e y: {soma}")
print(f"Produto entre x e y: {produto}")
print(f"Diferença entre x e y: {diferenca}")
print(f"Interseção entre x e y: {intersecao}")
print(f"União entre x e y: {uniao}")
