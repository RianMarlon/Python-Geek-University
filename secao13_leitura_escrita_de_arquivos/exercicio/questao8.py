"""
8) Faça um programa que leia o conteúdo de um arquivo e crie um arquivo
com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas.
Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. A função
que converte maiúscula para minúscula é o toupper(). Ela é aplicada em cada caractere da string.
"""


nome_arquivo = str(input("Digite o caminho do arquivo ou seu nome "
                         "(caso o arquivo esteja no mesmo local que o programa): "))

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        with open("arquivos/arq3.txt", "w", encoding="utf-8") as arquivo_novo:

            arquivo_novo.write(arquivo.read().upper())

    print("\nInformações inseridas no arquivo com sucesso!")

except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
