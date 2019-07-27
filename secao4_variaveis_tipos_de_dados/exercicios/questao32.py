"""
32) Leia um número inteiro e imprima a soma do sucessor
de seu triplo com o antecessor e seu dobro.
"""

numero = int(input("Digite um número: "))

sucessor_triplo = (numero*3) + 1
antecessor_dobro = (numero*2) - 1

print(f"\n{sucessor_triplo} + {antecessor_dobro} = {(sucessor_triplo+antecessor_dobro)} ")
