"""
20) Crie um programa que receba como entrada o número de alunos de
uma disciplina. Aloque dinamicamente dois vetores para armazenar
as informações a respeito desses alunos. O primeiro vetor contém
o nome dos alunos e o segundo contém suas notas finais. Crie
um arquivo que armazene, a cada linha, o nome do aluno e sua nota
final. Use nomes com no máximo 40 caracteres. Se o nome não contém 40 caracteres,
complete com espaço em branco.
"""

from verificacao import verificar_nome

try:
    qtd_alunos = int(input("Digite a quantidade de alunos: "))

    nome_alunos = []
    nota_alunos = []
    for aluno in range(qtd_alunos):

        while True:

            nome = str(input(f"\nDigite o nome do aluno {aluno+1}: ")).strip().title()

            if verificar_nome(nome):

                # Caso nome fornecido tenha 40 caracteres ou mais, irá pegar apenas os primeiros
                # 40 caracteres do nome, caso o nome não contenha 40 caracteres ele irá preencher até
                # 40 caracteres usando espaços em branco
                novo_nome = nome[0:40:1] if len(nome) >= 40 else nome + " " * (40 - len(nome))

                # usei o abs() para não aceitar notas negativas
                nota = abs(float(input(f"Digite a nota final do {nome}: ")))

                nome_alunos.append(novo_nome)
                nota_alunos.append(nota)

                break

            else:
                print("\nNome inválido!")

    with open("arquivos/alunos_notas.txt", "a", encoding="utf-8") as arquivo:

        for i in range(qtd_alunos):

            arquivo.write(f"{nome_alunos[i]} {nota_alunos[i]}\n")

    print("\nInformações inseridas no arquivo com sucesso!")


except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO valor fornecido é inválido!")
