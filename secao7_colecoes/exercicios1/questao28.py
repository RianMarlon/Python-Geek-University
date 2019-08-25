"""
28) Leia 10 números inteiros e armazene em um vetor v. Crie
dois novos vetores v1 e v2. Copie os valores ímpares de v para v1,
e os valores pares de v para v2. Note que cada um dos valores v1 e v2
têm no máximo 10 elementos, mas nem todos os elementos são utilizados.
No final escreva os elementos UTILIZADOS de v1 e v2.
"""

v = []

for i in range(10):
    v.append(int(input("Digite um número: ")))

v1 = []
v2 = []

for i in v:
    if i % 2 == 0:
        v2.append(i)

    else:
        v1.append(i)

utilizado1 = set(v1)
utilizado2 = set(v2)

print(f"\nOs valores ímpares utilizados: {utilizado1}")
print(f"Os valores pares utilizados: {utilizado2}")
