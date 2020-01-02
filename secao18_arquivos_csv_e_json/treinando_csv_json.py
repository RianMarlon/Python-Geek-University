"""
Treinando arquivos CSV e JSON

from csv import writer
from os.path import exists

if exists("pessoas.csv"):

    with open("pessoas.csv", "a", encoding="utf-8") as arquivo:

        conteudo = writer(arquivo)
        nome = None

        while nome != "Sair":

            nome = str(input("\nInforme o seu nome: ")).strip().title()

            if nome != "Sair":

                sobrenome = str(input("Informe o seu sobrenome: ")).strip().title()
                data_nascimento = str(input("Informe a data de nascimento: ")).strip()
                cpf = str(input("Informe o seu cpf: ")).strip()

                conteudo.writerow([nome, sobrenome, data_nascimento, cpf])

else:

    with open("pessoas.csv", "a", encoding="utf-8") as arquivo:

        conteudo = writer(arquivo)
        conteudo.writerow(["Nome", "Sobrenome", "Data Nascimento", "CPF"])

        nome = None

        while nome != "Sair":

            nome = str(input("\nInforme o seu nome: ")).strip().title()

            if nome != "Sair":

                sobrenome = str(input("Informe o seu sobrenome: ")).strip().title()
                data_nascimento = str(input("Informe a data de nascimento: ")).strip()
                cpf = str(input("Informe o seu cpf: ")).strip()

                conteudo.writerow([nome, sobrenome, data_nascimento, cpf])


from csv import DictWriter
from os.path import exists

if exists("pessoas.csv"):

    with open("pessoas.csv", "a", encoding="utf-8") as arquivo:

        cabecalho = ["Nome", "Sobrenome", "Data Nascimento", "CPF"]
        conteudo = DictWriter(arquivo, fieldnames=cabecalho)

        nome = None

        while nome != "Sair":

            nome = input("\nInforme o seu nome: ").strip().title()

            if nome != "Sair":

                sobrenome = input("Informe o seu sobrenome: ").strip().title()
                data_nascimento = input("Informe a data de nascimento: ").strip()
                cpf = input("Informe o seu CPF: ").strip()

                conteudo.writerow({"Nome": nome, "Sobrenome": sobrenome, "Data Nascimento": data_nascimento,
                                   "CPF": cpf})

else:

    with open("pessoas.csv", "a", encoding="utf-8") as arquivo:

        cabecalho = ["Nome", "Sobrenome", "Data Nascimento", "CPF"]
        conteudo = DictWriter(arquivo, fieldnames=cabecalho)
        conteudo.writeheader()

        nome = None

        while nome != "Sair":

            nome = input("\nInforme o seu nome: ").strip().title()

            if nome != "Sair":

                sobrenome = input("Informe o seu sobrenome: ").strip().title()
                data_nascimento = input("Informe a data de nascimento: ").strip()
                cpf = input("Informe o seu CPF: ").strip()

                conteudo.writerow({"Nome": nome, "Sobrenome": sobrenome, "Data Nascimento": data_nascimento,
                                   "CPF": cpf})


# Lendo arquivos CSV

from csv import reader

with open("pessoas.csv", "r", encoding="utf-8") as arquivo:

    conteudo = reader(arquivo)

    for linha in conteudo:

        print(f"Nome: {linha[0]}; Sobrenome: {linha[1]}; Data Nascimento: {linha[2]}; CPF: {linha[3]}")


from secao17_heranca_polimorfismo.exercicios1.questao16 import Moto8
import pickle

with open("motos.pickle", "wb") as arquivo:

    moto1, moto2 = Moto8(), Moto8()

    moto1.marca = "yamaha"
    moto1.modelo = "xj6"
    moto1.cor = "branco"
    moto1.maior_marcha = 6
    moto1.menor_marcha = 1
    moto1.ligar()
    moto1.marcha_acima()
    moto1.marcha_acima()

    moto2.marca = "yamaha"
    moto2.modelo = "xj6"
    moto2.cor = "vermelho"
    moto2.maior_marcha = 8
    moto2.menor_marcha = 1
    moto2.ligar()
    moto2.marcha_acima()
    moto2.marcha_acima()

    pickle.dump((moto1, moto2), arquivo)

with open("motos.pickle", "rb") as arquivo:
    motot1, moto2 = pickle.load(arquivo)
    print("INFORMAÇÕES DA PRIMEIRA MOTO:")
    print(f"Marca: {moto1.marca}\nModelo: {moto1.modelo}\nCor: {moto1.cor}")

    print("\nINFORMAÇÕES DA SEGUNDA MOTO:")
    print(f"Marca: {moto2.marca}\nModelo: {moto2.modelo}\nCor: {moto2.cor}")



from secao17_heranca_polimorfismo.exercicios1.questao16 import Moto8
import json

moto1 = Moto8()

moto1.marca = "yamaha"
moto1.modelo = "xj6"
moto1.cor = "branco"
moto1.maior_marcha = 6
moto1.menor_marcha = 1
moto1.ligar()
moto1.marcha_acima()
moto1.marcha_acima()

conteudo = json.dumps(moto1.__dict__)
print(conteudo)


"""


from secao17_heranca_polimorfismo.exercicios1.questao16 import Moto8
import jsonpickle

moto1 = Moto8()

moto1.marca = "yamaha"
moto1.modelo = "xj6"
moto1.cor = "branco"
moto1.maior_marcha = 6
moto1.menor_marcha = 1
moto1.ligar()
moto1.marcha_acima()
moto1.marcha_acima()

conteudo = jsonpickle.encode(moto1)
print(conteudo)


with open("moto_yamaha.json", "w", encoding="utf-8") as arquivo:

    conteudo = jsonpickle.encode(moto1)
    arquivo.write(conteudo)


with open("moto_yamaha.json", "r", encoding="utf-8") as arquivo:

    conteudo = arquivo.read()
    moto1 = jsonpickle.decode(conteudo)

    print(moto1.marca)
    print(moto1.modelo)
