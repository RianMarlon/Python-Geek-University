"""
15) Faça um programa que receba como entrada o ano corrente e o nome de dois
arquivos: um de entrada e outro de saída. Cada linha do arquivo de entrada
contém o nome de uma pessoa (ocupando 40 caracteres) e o seu ano de nascimento.
O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece
o nome da pessoa seguida por uma string que representa a sua idade.

    . Se a idade for menor do que 18 anos, escreva "menor de idade"
    . Se a idade for maior do que 18 anos, escreva "maior de idade
    . Se a idade for igual a 18 anos, escreva "entrando na maior idade"
"""

ano_corrente = int(input("Digite o ano corrente: "))

nome_arquivo = str(input("\nDigite o caminho do arquivo ou o seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

try:

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        nome_arquivo2 = str(input("Digite o caminho ou o nome do arquivo que você deseja criar "
                                  "(caso o arquivo esteja no mesmo local do programa): "))

        nome_arquivo2 = nome_arquivo2 if ".txt" in nome_arquivo2 else nome_arquivo2 + ".txt"

        informacoes = arquivo.read().splitlines()

        nomes = [dado[0:40:1] for dado in informacoes]
        ano_nascimento = [dado[41::] for dado in informacoes]

        with open(nome_arquivo2, "w", encoding="utf-8") as novo_arquivo:

            for linha in range(len(nomes)):

                nome = nomes[linha].strip()
                idade = ano_corrente - int(ano_nascimento[linha])

                if idade < 18:
                    novo_arquivo.write(f"{nome}: menor de idade\n")

                elif idade > 18:
                    novo_arquivo.write(f"{nome}: maior de idade\n")

                else:
                    novo_arquivo.write(f"{nome}: entrando na maior idade\n")

        print("\nInformações inseridas no arquivo com sucesso!")

except FileNotFoundError:
    print("\nArquivo informado não encontrado ou o programa não tem permissão para criar o diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
