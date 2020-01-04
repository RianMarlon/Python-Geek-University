"""
Manipulando Data e Hora

Python tem um módulo built-in(integrado) para se trabalhar com data e hora,
chamado de datetime

2020-01-02 20:49:38.492479

2020-01-02 21:00:00

import datetime

print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2020-01-02 20:49:38.492479    BR 02/01/2020

# datetime.datetime(year, month, day, hour, minite, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() -> para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minutos, 0 secundos, 0 microsecundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# Recebendo dados do usuário e convertendo para data

print(type(evento))
print(type("02/01/2020"))

print(evento)

nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")

nascimento = nascimento.split("/")

print(nascimento)

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""

import datetime

evento = datetime.datetime(2021, 1, 1, 0)

# Acesso indiidual dos elementos da data e hora

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo

print(dir(evento))






