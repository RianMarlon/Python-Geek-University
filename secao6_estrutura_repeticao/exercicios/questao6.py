"""
6) Faça um programa que leia 10 inteiros e imprima sua média.
"""

media = 0
for i in range(1, 11):
    num = int(input(f"Digite o {i}° valor: "))
    media += num
    if i >= 10:
        media = media/i

print()
print(f"Média: {media}")
