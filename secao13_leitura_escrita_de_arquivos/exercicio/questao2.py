"""
2) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas linhas esse arquivo possui
"""

nome_arquivo = str(input("Digite o caminho do arquivo ou o nome do mesmo "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

try:
    with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
        texto = arquivo.read()
        quebra_de_linha = len(texto.splitlines())
        print(f"\nO arquivo possui {quebra_de_linha + 1} linhas!")

except FileNotFoundError:
    print("\nArquivo informado não encontrado!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
