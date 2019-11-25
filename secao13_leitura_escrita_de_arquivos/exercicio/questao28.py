"""
28) Faça um programa que recebe como entrada o nome de um arquivo
de entrada e o nome de um arquivo de saída. Cada linha do arquivo
de entrada possui colunas de tamanho de 30 caracteres. No arquivo de saída
deverá ser escrito o arquivo de entrada de forma inversa. Veja um exemplo:

Arquivo de entrada:
Hoje é dia de prova de AP
A prova está muito fácil
vou tirar uma boa nota

Arquivo de saída
Aton aob amu ratir uov
Licáf otium átse avorp A
PA ed avortp ed aid é ejoH
"""


arquivo_entrada = str(input("Digite o caminho do arquivo de entrada ou o seu nome "
                            "(caso o arquivo esteja no mesmo do programa): ")).strip()

arquivo_entrada = arquivo_entrada if ".txt" in arquivo_entrada else arquivo_entrada+".txt"

try:

    with open(arquivo_entrada, "w", encoding="utf-8") as escreve:
        texto = str(input("\nInsira o texto do arquivo de entrada: ")).strip()

        conteudo = ""

        for palavra in range(len(texto)):

            conteudo += f"{texto[palavra]}\n" if (palavra+1) % 30 == 0 else f"{texto[palavra]}"

        escreve.write(conteudo)

    with open(arquivo_entrada, "r", encoding="utf-8") as leitura:

        arquivo_saida = str(input("\nDigite o caminho do arquivo de saída ou o seu nome "
                                  "(caso o arquivo esteja no mesmo do programa): ")).strip()

        arquivo_saida = arquivo_saida if ".txt" in arquivo_saida else arquivo_saida + ".txt"

        with open(arquivo_saida, "w", encoding="utf-8") as saida:
            saida.write(leitura.read()[::-1])

except ValueError:
    print("\nValor inválido")

except FileNotFoundError:
    print("\nO programa não possui permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivos!")
