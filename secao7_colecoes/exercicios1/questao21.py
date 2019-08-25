"""
21) Faça um programa que receba do usuário dois vetores, A e B,
com 10 números inteiros cada. Crie um novo vetor denominado C
calculando C = A - B. Mostre na tela os dados do vetor C
"""

a = []
b = []

for i in range(10):
    a.append(int(input("Digite um valor A: ")))
    b.append(int(input("Digite um valor B: ")))

c = []
for i in range(10):
    c.append(a[i] - b[i])

print(f"\nDados do vetor C:")
print(*c, sep=', ')
