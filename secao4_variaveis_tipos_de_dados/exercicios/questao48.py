"""
48) Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
"""

# 4000 segundos
valor = int(input("Digite um valor em segundos: "))

# 4000 / 60 / 60 = 1, porque fiz um casting para inteiro então não pega as casas decimais
horas = int(valor / 60 / 60)
# 4000 - (1 * 60 * 60) = 400
minutos = valor - (horas * 60 * 60)
# 400 / 60 = 6, porque fiz um casting para inteiro então não pegará as casas decimais
minutos = int(minutos / 60)
# 4000 - (1 * 60 * 60) - (6 * 60 * 60) = 40
segundos = int(valor - (horas * 60 * 60) - (minutos * 60))

print(f"\n{horas} horas\n{minutos} minutos\n{segundos} segundos")
