"""
Treinando Data e Hora

import datetime
# from pytz import timezone

try:
    data_nascimento = input("Digite sua data de nascimento(dd/mm/yyyy): ").strip()

    # fuso_horario = timezone("America/Fortaleza")

    data = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")

    # data = data.astimezone(fuso_horario)

    idade = datetime.datetime.now() - data

    idade = idade.days // 365

    print(f"\nVocê tem {idade} {'ano' if idade <= 1 else 'anos'}")

except ValueError:
    print("\nO valor informado deve ser uma data no formato dd/mm/yyyy")


from textblob import TextBlob

data = datetime.datetime.now()

# Usa a internet
print(f"{data.day} de {str(TextBlob(data.strftime('%B')).translate(to='pt-br')).title()} de {data.year}")


def formato_data(data):

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
             "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    try:
        return f"{data.day} de {meses[data.month - 1]} de {data.year}"

    except ValueError:
        return "\nO valor passado por parâmetro deve ser do tipo datetime"


data = datetime.datetime(year=2012, month=10, day=20)
print(formato_data(data))


backup = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time(hour=3))

print(f"\nO backup irá acontecer em {backup}")

print(f"\nO backup irá acontecer às {formato_data(backup)} às {backup.strftime('%H:%M:%S %p')}")


janta = datetime.time(hour=18, minute=30)

print(janta)

almoco = datetime.timedelta(hours=janta.hour, minutes=janta.minute) + datetime.timedelta(hours=16, seconds=48)

print(almoco)
print(almoco.seconds)

hora = almoco.seconds // 3600
minutos = (almoco.seconds % 3600) // 60
segundos = (almoco.seconds % 60)

print(f"\n{hora}:{minutos}:{segundos}")


def dia_da_semana(data):

    try:

        dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
                "Sexta-feira", "Sábado", "Domingo"]

        return dias[data.weekday()]

    except ValueError:
        return "O valor passado por parâmetro deve ser uma data do tipo datetime"


hoje = datetime.datetime.today()

antigo = datetime.datetime(year=1992, month=6, day=22)

print(dia_da_semana(hoje))
print(dia_da_semana(antigo))


aniversario = datetime.datetime(year=2020, month=1, day=28)

print(aniversario.strftime('%d/%m/%Y'))


"""

import datetime

manuntencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=4)), datetime.time(hour=1))

print(manuntencao.strftime("%d/%m/%Y %H:%M:%S"))

agora = datetime.datetime.now()

agora = agora.replace(year=2021, month=8, day=6)

print(agora)


