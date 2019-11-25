"""
9) Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo
com o conteúdo dos dois primeiros (o conteúdo do primeiro seguido do conteúdo do
segundo).
"""


nome_arquivo1 = str(input("Digite o caminho do arquivo ou o seu nome "
                          "(caso o arquivo esteja no mesmo local do programa): "))

try:
    with open(nome_arquivo1, "r", encoding="utf-8") as arquivo1:

        nome_arquivo2 = str(input("Digite o caminho do arquivo ou o seu nome "
                                  "(caso o arquivo esteja no mesmo local do programa): "))

        with open(nome_arquivo2, "r", encoding="utf-8") as arquivo2:
            with open("arquivos/juncao_arquivos.txt", "w", encoding="utf-8") as arquivo_novo:
                arquivo_novo.write(arquivo1.read()+"\n")
                arquivo_novo.write(arquivo2.read())

    print("\nInformações inseridas no arquivo com sucesso!")

except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
