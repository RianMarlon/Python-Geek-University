"""
27) Faça um programa para gerenciar as notas dos alunos de uma turma
salva em um arquivo. O programa deverá ter um menu contendo as seguinte opções:

    (a) Definir informações da turma;
    (b) Inserir aluno e notas;
    (c) Exibir alunos e médias;
    (d) Exibir alunos aprovados;
    (e) Exibir alunos reprovados;
    (f) Salvar dados em Disco;
    (g) Sair do programa (fim)

Faça a rotina que gerencia o menu dentro do main, e para cada uma das
opções deste menu, crie uma função específica

# OBS: Não irá ser necessário criar a função/opção para salvar os dados
em disco, pois será salvo automaticamente
"""

from verificacao import verificar_texto


def informacoes_turma(arquivo):
    """Função que recebe o caminho/nome do arquivo e imprimi na tela
    as informações da turma. Caso o arquivo não exista o mesmo será criado"""

    try:

        with open(arquivo, "a") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:
            print(f"\n\n{'-' * 48}INFORMAÇÕES DA TURMA{'-' * 49}")
            texto = leitura.read().strip().splitlines()

            if len(texto) > 0:
                [print(f"{informacao.replace(';', ' - ')}\n{'-' * 117}") for informacao in texto]

            else:
                print(f"\n{'-' * 117}")

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)


def inserir_notas_alunos(arquivo):
    """Função que recebe o caminho/arquivo e insere no mesmo os dados
    dos alunos e as notas informadas pelo usuário. Caso o arquivo não exista o mesmo
    será criado"""

    try:

        with open(arquivo, "a", encoding="utf-8") as insercao:
            print(f"\n\n{'-' * 54}INSERÇÃO{'-' * 55}")

            cod = abs(int(input("Insira o identificador(código) do aluno: ")))

            print("-" * 117)

            codigo_existe = False

            with open(arquivo, "r", encoding="utf-8") as leitura:

                texto = leitura.read().strip().splitlines()

                texto = [informacao.split(";") for informacao in texto]

                for linha in texto:

                    if cod == int(linha[0]):
                        codigo_existe = True

            if not codigo_existe:
                nome = str(input("Insira o nome do aluno: ")).strip().title()
                print("-" * 117)

                if verificar_texto(nome):

                    nota1 = float(input("Insira a primeira nota do aluno: "))
                    print("-" * 117)

                    nota2 = float(input("Insira a segunda nota do aluno: "))
                    print("-" * 117)

                    nota3 = float(input("Insira a terceira nota do aluno: "))
                    print("-" * 117)

                    insercao.write(f"{cod};{nome};{nota1} - {nota2} - {nota3}\n")

                else:
                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                    print("NOME INVÁLIDO!")

                    print("-" * 117)

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("IDENTIFICADOR(CÓDIGO) JÁ EXISTENTE!")

                print("-" * 117)

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO OU AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def media_aluno(linha):
    """Função que recebe a linha referente ao arquivo
    que armazena as informações dos alunos e retorna sua média"""

    notas = [float(nota) for nota in linha[-1].split(" - ")]

    media = float("{:.1f}".format(float(sum(notas) / len(notas))))

    return media


def alunos_medias(arquivo):
    """Função que recebe o caminho/arquivo e imprimi na tela
    o nome e a média de cada aluno. Caso o arquivo não exista o mesmo
    será criado"""

    try:

        with open(arquivo, "a", encoding="utf-8") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:

            texto = leitura.read().strip().splitlines()

            texto = [informacoes.split(";") for informacoes in texto]

            print(f"\n\n{'-' * 51}ALUNOS E MÉDIAS{'-' * 51}")

            [print(f"{linha[1]} - {media_aluno(linha)}\n{'-' * 117}") for linha in texto]

    except ValueError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def alunos_aprovados(arquivo):
    """Função que recebe o caminho/arquivo e imprimi na tela
    o nome dos alunos que estão aprovados. Caso o arquivo não
    exista o mesmo será criado"""

    try:

        with open(arquivo, "a", encoding="utf-8") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:

            texto = leitura.read().strip().splitlines()

            texto = [informacoes.split(";") for informacoes in texto]

            print(f"\n\n{'-' * 54}APROVADOS{'-' * 54}")

            [print(f"{linha[1]}\n{'-' * 117}") for linha in texto if media_aluno(linha) >= 6.0]

    except ValueError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def alunos_reprovados(arquivo):
    """Função que recebe o caminho/arquivo e imprimi na tela
    o nome dos alunos que estão reprovados. Caso o arquivo
    não exista o mesmo será criado"""

    try:

        with open(arquivo, "a", encoding="utf-8") as _:
            pass

        with open(arquivo, "r", encoding="utf-8") as leitura:

            texto = leitura.read().strip().splitlines()

            texto = [informacoes.split(";") for informacoes in texto]

            print(f"\n\n{'-' * 54}REPROVADOS{'-' * 54}")

            [print(f"{linha[1]}\n{'-' * 117}") for linha in texto if media_aluno(linha) < 6.0]

    except ValueError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


if __name__ == "__main__":

    nome_arquivo = "arquivos/turma.txt"

    try:

        while True:

            # Como as funções já irão salvar os dados em disco
            # automaticamente, então não criarei a opção para salvar dados em disco

            print(f"\n\n{'-' * 56}MENU{'-' * 57}")
            print("1 - Definir informações da turma")

            print(f"{'-' * 117}")
            print("2 - Inserir aluno e notas")

            print(f"{'-' * 117}")
            print("3 - Exibir alunos e médias")

            print(f"{'-' * 117}")
            print("4 - Exibir alunos aprovados")

            print(f"{'-' * 117}")
            print("5 - Exibir alunos reprovados")

            print(f"{'-' * 117}")
            print("6 - Sair do programa (fim)")

            print(f"{'-' * 117}")
            opcao = abs(int(input("\nInsira o número da opção que você deseja: ")))

            print(f"{'-' * 117}")

            if opcao == 1:
                informacoes_turma(nome_arquivo)

            elif opcao == 2:
                inserir_notas_alunos(nome_arquivo)

            elif opcao == 3:
                alunos_medias(nome_arquivo)

            elif opcao == 4:
                alunos_aprovados(nome_arquivo)

            elif opcao == 5:
                alunos_reprovados(nome_arquivo)

            elif opcao == 6:
                print(f"\n\n{'-' * 51}FIM DO PROGRAMA{'-' * 51}")
                break

            else:

                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                print("OPÇÃO INVÁLIDA!")
                print("-" * 117)

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("OPÇÃO DEVE SER UM NÚMERO INTEIRO!")
        print("-" * 117)

