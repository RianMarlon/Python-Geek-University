"""
29) Faça uma prova de matemática para crianças que estão aprendendo
a somar números inteiros menores do que 100. Escolha números aleatórios
entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b,
onde a e b são os números aleatórios. Peça a resposta. Faça cinco
perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou
"""

from random import randint

num1 = randint(1, 100)
num2 = randint(1, 100)

print(f"Qual é a soma de {num1} + {num2}?")
resultado1 = int(input(""))


num3 = randint(1, 100)
num4 = randint(1, 100)

print(f"Qual é a soma de {num3} + {num4}?")
resultado2 = int(input(""))


num5 = randint(1, 100)
num6 = randint(1, 100)

print(f"Qual é a soma de {num5} + {num6}?")
resultado3 = int(input(""))


num7 = randint(1, 100)
num8 = randint(1, 100)

print(f"Qual é a soma de {num7} + {num8}?")
resultado4 = int(input(""))


num9 = randint(1, 100)
num10 = randint(1, 100)

print(f"Qual é a soma de {num9} + {num10}?")
resultado5 = int(input(""))

cont_acertos = 0
print()
if resultado1 == (num1 + num2):
    cont_acertos += 1

if resultado2 == (num3 + num4):
    cont_acertos += 1

if resultado3 == (num5 + num6):
    cont_acertos += 1

if resultado4 == (num7 + num8):
    cont_acertos += 1

if resultado5 == (num9 + num10):
    cont_acertos += 1

print("Respostas:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num3} + {num4} = {num3 + num4}")
print(f"{num5} + {num6} = {num5 + num6}")
print(f"{num7} + {num8} = {num7 + num8}")
print(f"{num9} + {num10} = {num9 + num10}")
print()

print(f"Quantidade de acertos: {cont_acertos}")
