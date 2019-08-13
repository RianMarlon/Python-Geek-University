"""
5) Faça um programa que peça ao usuário para digitar
10 valores e some-os.
"""

soma = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}° valor: "))
    soma += num

print()
print(soma)