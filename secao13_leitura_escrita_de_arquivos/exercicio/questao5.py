"""
5) Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre
na tela quantas vezes aquele caractere ocorre dentro do arquivo.
"""

nome_arquivo = str(input("Digite o caminho do arquivo ou seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:

        caractere = str(input("Digite o caractere que você deseja saber a quantidade de vezes que ele"
                              "se repete no arquivo: ")).strip().lower()

        texto = arquivo.read()
        texto = texto.lower()

        print(f"\nO caractere {caractere} se repete {texto.count(caractere)} vez(es) no texto!")

except FileNotFoundError:
    print("\nArquivo informado não encontrado!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
