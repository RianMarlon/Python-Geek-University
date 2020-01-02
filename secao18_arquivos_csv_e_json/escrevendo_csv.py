"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha


from csv import writer

# writer() -> Gera um objeto para que possamos escrever em um arquivo csv
# writerow() -> Escrever mais uma linha no arquivo. Este método recebe uma lista

with open("filmes.csv", "w", encoding="utf-8") as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(["Título", "Gênero", "Duração"])

    while filme != "sair":
        filme = input("\nInforme o nome do filme: ").strip().title()

        if filme.lower() != "sair":

            genero = input("Informe o gênero: ").strip().title()
            duracao = input("Informe a duração (em minutos): ").strip()

            escritor_csv.writerow([filme, genero, duracao])

        else:
            filme = filme.lower()


"""

# DictWriter

# OBS: As chaves do dicionário devem ser as mesmas utilizados no cabeçalho


from csv import DictWriter


with open("filmes3.csv", "w", encoding="utf-8") as arquivo:
    cabecalho = ["Título", "Gênero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None

    while filme != "sair":

        filme = input("\nInforme o nome do filme: ").strip().title()

        if filme.lower() != "sair":

            genero = input("Informe o gênero do filme: ").strip().title()
            duracao = input("Informe a duração do filme (em minutos): ").strip().title()
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})

        else:

            filme = filme.lower()

