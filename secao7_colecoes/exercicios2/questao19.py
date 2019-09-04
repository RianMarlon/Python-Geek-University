"""
19) Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo
as seguintes informações sobre alunos de uma disciplina, sendo todas as informações do
tipo inteiro:

    . Primeira coluna: número de matrícula (use um inteiro)
    . Segunda coluna: média das provas
    . Terceira coluna: média dos trabalhos
    . Quarta coluna: nota final

(a) Leia as três primeiras informações de cada aluno.
(b) Calcule a nota final como sendo a soma da média das provas e da média
dos trabalhos.
(c) Imprima a matrícula do aluno que obteve a maior nota final (assuma que
só existe uma maior nota).
(d) Imprima a média aritmética das notas finais.
"""

alunos = []

# Variavel para não se repetir a mátricula
matriculas = []

# Variavel para informar qual aluno está se referindo
cont1 = 0


# while para o usuário fornecer as informações
while len(alunos) < 5:

    lista2 = []

    # Variavel para informar a coluna
    cont2 = 0

    # Enquanto não preencher as 3 colunas do aluno, o looping continua
    while len(lista2) < 3:
        if cont2 == 0:
            matricula = int(input(f"Digite o número da matrícula do aluno {cont1+1}: "))

            # Verificando se a matrícula não foi digitada em algum momento
            if matricula not in matriculas:
                matriculas.append(matricula)
                lista2.append(matricula)

            # Se tiver sido digitada, será informada que a matrícula já foi digitada
            # e no próximo looping ele terá que informar a matrícula do aluno novamente
            # até informar uma que não foi digitada
            else:
                print("Matrícula já digitada\n")
                cont2 -= 1
                pass

        elif cont2 == 1:
            media_prova = int(input(f"Digite a média das provas do aluno {cont1+1}: "))
            lista2.append(media_prova)

        elif cont2 == 2:
            media_trabalho = int(input(f"Digite a média dos trabalhos do aluno {cont1+1}: "))
            lista2.append(media_trabalho)

        cont2 += 1

    cont1 += 1

    alunos.append(lista2)

    print()

# Adicionando a coluna da nota final em cada linha/aluno
for i in range(5):
    nota_final = alunos[i][1] + alunos[i][2]

    alunos[i].append(nota_final)

# Imprimindo a matriz
for i in range(5):

    for j in range(4):
        print(alunos[i][j], end='  ')

    print()

notas_finais = []

# Armazenando todas as notas finais em um vetor
for i in range(5):

    notas_finais.append(alunos[i][3])

soma_final = sum(notas_finais)
matricula = 0

for i in range(5):

    # Verificando qual é o aluno que possui a maior nota final e adicionando a matricula
    # do mesmo em uma matriz
    if alunos[i][3] == max(notas_finais):
        matricula = alunos[i][0]

media_aritmetica = int(soma_final / len(notas_finais))

print(f"\nMátricula do aluno que obteve a maior nota final: {matricula}")
print(f"A média aritmética das notas finais: {media_aritmetica}")
