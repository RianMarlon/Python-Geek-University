"""
11) Faça um programa no qual o usuário informa o nome do arquivo e uma palavra,
e retorne o número de vezes que aquela palavra aparece no arquivo.
"""

nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavra = str(input("Digite uma palavra: ")).strip().split()

        texto = arquivo.read().lower()
        print(f"\nA palavra '{palavra[0]}' se repete {texto.count(palavra[0].lower())} vez(es) no texto!")

except FileNotFoundError:
    print("\nArquivo não encontrado!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
