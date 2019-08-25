"""
1) Faça um programa que possua um vetor denominado A que armazene 6 números
inteiros. O programa deve executar os seguintes passos:

(A) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.

(B) Armazene em uma variável inteira(simples) a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.

(C) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.

(D) Mostre na tela cada valor do vetor A, um em cada linha.
"""

a = [1, 0, 5, -2, -5, 7]

b = a[0] + a[1] + a[5]
print(f"Soma dos valores das posições 0, 1, 5 do vetor: {b}\n")

a[4] = 100

for i in a:
    print(i)
