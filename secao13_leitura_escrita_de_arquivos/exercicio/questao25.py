"""
25) Faça um programa gerenciar uma agenda de contatos. Para cada contato
armazene o nome, o telefone e o aniversário (dia e mes). O programa deve
permitir

    (a) Inserir contato
    (b) remover contato
    (c) pesquisar um contato pelo nome
    (d) listar todos os contatos
    (e) listar os contatos cujo nome inicia com uma dada letra
    (f) imprimir os aniversariantes do mês

Sempre que o programa for encerrado, os contatos devem ser armazenados em um
arquivo binário. Quando o programa iniciar, os contatos devem ser inicializados
com os dados contidos neste arquivo binário.
"""

from datetime import date

from verificacao import verificar_nome, verificar_telefone


def inserir(arquivo):

    """Função que recebe o caminho/nome do arquivo e insere no mesmo os dados
    dos contatos informados pelo usuário. Caso o arquivo não exista o mesmo
    será criado"""

    try:
        with open(arquivo, "ab") as insercao:

            print(f"\n\n{'-' * 54}INSERÇÃO{'-' * 55}")

            cod = abs(int(input("Digite o identificador(código) do contato: ")))

            print("-" * 117)

            codigo_existe = False

            with open(arquivo, "rb") as leitura:

                informacoes = leitura.read().decode("utf8").strip().splitlines()
                informacoes = [infor.split(";") for infor in informacoes]

                for linha in informacoes:

                    if int(linha[0]) == cod:
                        codigo_existe = True

            if codigo_existe:

                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O IDENTIFICADOR(CÓDIGO) JÁ EXISTE!")

                print("-" * 117)

            else:
                nome = str(input("Digite o nome do contato: ")).strip().title()
                print("-" * 117)

                if verificar_nome(nome):

                    telefone = str(input(f"Digite o número do telefone de {nome}: "))
                    print("-" * 117)

                    if verificar_telefone(telefone):

                        mm = abs(int(input(f"Digite o mês do aniversário de {nome}: ")))
                        print("-" * 117)

                        dd = abs(int(input(f"Digite o dia do aniversário de {nome}: ")))
                        print("-" * 117)

                        if ((mm > 0) and (mm < 13)) and ((dd > 0) and (dd < 32)):

                            mes = str(mm)
                            dia = str(dd)

                            if len(mes) == 1:

                                mes = "0"+mes

                            if len(dia) == 1:

                                dia = "0"+dia

                            insercao.write(f"{cod};{nome};{telefone};{dia}/{mes}\n".encode("utf8"))

                            print(f"\n\n{'-' * 53}INFORMAÇÃO{'-' * 54}")

                            print("CONTATO INSERIDO COM SUCESSO!")

                            print("-" * 117)

                        else:
                            print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                            print("DATA INVÁLIDA(VALORES FORA DO INTERVALO PERMITIDO)!")

                            print("-" * 117)

                    else:
                        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                        print("TELEFONE INVÁLIDO!")

                        print("-" * 117)

                else:

                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                    print("NOME INVÁLIDO!")

                    print("-" * 117)

    except ValueError:

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


def deletar(arquivo):

    """Função que recebe o caminho/nome do arquivo e deleta o contato do mesmo,
    de acordo com o identificador(código) do contato informado pelo usuário. Caso
    o arquivo não exista o mesmo será criado"""

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as conteudo:

            informacoes = conteudo.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:

                informacoes = [infor.split(";") for infor in informacoes]

                print(f"\n\n{'-' * 55}DELEÇÃ0{'-' * 55}")

                cod = abs(int(input("Digite o identificador(código) do contato que você deseja deletar: ")))

                print("-" * 117)

                with open(arquivo, "wb") as delecao:

                    codigo_existe = False

                    for linha in informacoes:

                        if int(linha[0]) == cod:
                            informacoes.remove(linha)
                            codigo_existe = True

                    for linha in informacoes:

                        delecao.write(f"{linha[0]};{linha[1]};{linha[2]};{linha[3]}\n".encode("utf8"))

                    if codigo_existe:

                        print(f"\n\n{'-' * 53}INFORMAÇÃO{'-' * 54}")

                        print("CONTATO DELETADO COM SUCESSO!")

                        print("-" * 117)

                    else:
                        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                        print("IDENTIFICADOR(CÓDIGO) NÃO EXISTENTE!")

                        print("-" * 117)

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O ARQUIVO ESTÁ VAZIO!")

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


def pesquisar_por_nome(arquivo):

    """Função que recebe o caminho/nome do arquivo e de acordo
    com os dados fornecidos pelo usuário imprimi o contato. Caso o
    arquivo não exista o mesmo será criado"""

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:

            texto = leitura.read().decode("utf8").strip().splitlines()

            if len(texto) > 0:

                texto = [informacoes.split(";") for informacoes in texto]

                print(f"\n\n{'-' * 49}PESQUISAR POR NOME{'-' * 50}")
                nome = str(input("Digite o nome do contato: ")).strip().title()
                print("-" * 117)

                if verificar_nome(nome):

                    existe = False

                    print(f"\n\n{'-' * 54}CONTATOS{'-' * 55}")

                    for informacoes in texto:

                        if informacoes[1].strip().title() == nome:
                            print(f"{informacoes[0]} - {informacoes[1]} - {informacoes[2]} - {informacoes[3]}"
                                  f"\n{'-' * 117}")

                            existe = True

                    if not existe:
                        print(f"\n{'-' * 117}")

                else:
                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                    print("OS NOMES DOS CONTATOS NÃO CONTÉM CARACTERES ESPECIAIS OU NÚMEROS!")

                    print("-" * 117)

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 117)

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

    except IndexError:
        print(f"\n{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def listar_contatos(arquivo):
    """Função que recebe o caminho/nome do arquivo e imprimi na tela
    o texto que contém no mesmo, informando os contatos. Caso o arquivo não
    exista o mesmo será criado"""

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            print(f"\n\n{'-' * 50}LISTA DE CONTATOS{'-' * 50}")
            texto = leitura.read().decode("utf8").strip().splitlines()

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


def pesquisar_por_letra(arquivo):

    """Função que recebe o caminho/nome do arquivo e de acordo com os dados
    fornecidos pelo usuário, imprimi na tela o nome dos contatos que iniciar
    com a letra informada. Caso o arquivo não exista o mesmo será criado"""

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:

            texto = leitura.read().decode("utf8").strip().splitlines()

            if len(texto) > 0:
                texto = [informacoes.split(";") for informacoes in texto]

                print(f"\n\n{'-' * 49}PESQUISAR POR LETRA{'-' * 49}")

                letra = str(input("Digite uma letra: ")).strip().title()[0]

                print("-" * 117)

                print(f"\n\n{'-' * 54}CONTATOS{'-' * 55}")

                existe = False

                for informacoes in texto:

                    if informacoes[1].strip().title()[0] == letra:
                        print(f"{informacoes[0]} - {informacoes[1]} - {informacoes[2]} - {informacoes[3]}"
                              f"\n{'-' * 117}")

                        existe = True

                if not existe:
                    print(f"\n{'-' * 117}")

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 117)

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

    except IndexError:
        print(f"\n{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def aniversariante_do_mes(arquivo):

    """Função que recebe o caminho/nome do arquivo e imprimi na tela
    o(s) aniversariante(s) do mês de acordo com o mês e o dia do aniversário
    do contato contido no arquivo. Caso o arquivo não exista o mesmo será criado"""

    mes_atual = date.today().month

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:

            texto = leitura.read().decode("utf8").strip().splitlines()

            if len(texto) > 0:

                texto = [informacoes.split(";") for informacoes in texto]

                print(f"\n\n{'-' * 47}ANIVERSARIANTES DO MÊS{'-' * 48}")

                existe = False

                for informacoes in texto:

                    if int(informacoes[-1].strip()[-2::]) == int(mes_atual):
                        print(f"{informacoes[1]}\n{'-' * 117}")

                        existe = True

                if not existe:
                    print(f"\n{'-' * 117}")

            else:

                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 117)

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

    except IndexError:
        print(f"\n{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


if __name__ == "__main__":

    nome_arquivo = "arquivos/contatos.bin"

    try:

        while True:

            print(f"\n\n{'-' * 56}MENU{'-' * 57}")
            print("1 - Inserir um contato")

            print(f"{'-' * 117}")
            print("2 - Deletar um contato")

            print(f"{'-' * 117}")
            print("3 - Pesquisar um contato pelo nome")

            print(f"{'-' * 117}")
            print("4 - Listar todos os contatos")

            print(f"{'-' * 117}")
            print("5 - Listar os contatos cujo nome inicia com uma dada letra")

            print(f"{'-' * 117}")

            print("6 - Imprimir os aniversariantes do mês")

            print(f"{'-' * 117}")
            opcao = abs(int(input("\nDigite o número da opção que você deseja: ")))

            print(f"{'-' * 117}")

            if opcao == 1:
                inserir(nome_arquivo)

            elif opcao == 2:
                deletar(nome_arquivo)

            elif opcao == 3:
                pesquisar_por_nome(nome_arquivo)

            elif opcao == 4:
                listar_contatos(nome_arquivo)

            elif opcao == 5:
                pesquisar_por_letra(nome_arquivo)

            elif opcao == 6:
                aniversariante_do_mes(nome_arquivo)

            else:
                print(f"\n\n{'-' * 51}FIM DO PROGRAMA{'-' * 51}")
                break

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("OPÇÃO INVÁLIDA!")
        print("-" * 117)

