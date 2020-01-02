"""
Lendo arquivos CSV

CSV - Comma Separated Values -> Valores separados por vírgulas

# Separador por vírgula

1, 2, 3, 4, 5

"geek", "university", "python", ciência", "dados"

# Separador por ponto e vírgula

1; 2; 3; 4; 5

"geek"; "university"; "python"; ciência"; "dados"

# Separador por espaço

1 2 3 4 5

"geek" "university" "python" ciência" "dados"

http://www.dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open("lutadores.csv", "r", encoding="utf-8") as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(",")
    print(dados)

A linguagem Python, possui duas formas diferentes para ler arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderectedDicts


# reader

from csv import reader

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho

    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f"{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros")


# DictReader

from csv import DictReader

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderectedDict
        print(f"{linha['Nome']} nasceu no(a)(s
"""

# DictReader com outro separador

from csv import DictReader

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=",")
    for linha in leitor_csv:
        # Cada linha é um OrderectedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} em centímetros")