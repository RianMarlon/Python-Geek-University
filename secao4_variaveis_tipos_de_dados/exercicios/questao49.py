"""
49) Faça um programa para ler o horário (hora, minuto e segundo)
de ínicio e duração em segundos, de uma experiência biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
"""

hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial: "))
segundo_inicial = int(input("Digite o segundo inicial: "))

print()
# 10_000
duracao = int(input("Digite a duração em segundos: "))

# 10000 / 60 / 60 = 2, porque fiz um casting para inteiro então não pega as casas decimais
hora_duracao = int(duracao / 60 / 60)
# 10000 - (2 * 60 * 60) = 2800
minuto_duracao = duracao - (hora_duracao * 60 * 60)
# 2800 / 60 =  46, porque fiz um casting para inteiro então não pega as casas decimais
minuto_duracao = int(minuto_duracao / 60)
# 10000 - (2 * 60 * 60) - (46 * 60) = 40
segundo_duracao = duracao - (hora_duracao * 60 * 60) - (minuto_duracao * 60)

hora_final = hora_inicial + hora_duracao
minuto_final = minuto_inicial + minuto_duracao
segundo_final = segundo_inicial + segundo_duracao

# Se a soma do minuto incial com o minuto da duração for igual ou
# maior que 60, adiciona mais uma hora na hora final
if minuto_final >= 60:
    hora_final += 1
    minuto_final -= 60

# Se a soma do segundo incial com o segundo da duração for igual ou
# maior que 60, adiciona mais um minuto no minuto final
if segundo_final >= 60:
    minuto_final += 1
    segundo_final -= 60

print(f"\nO término da experiência biológica foi em:\n"
      f"{hora_final}h {minuto_final}min {segundo_final}s")
