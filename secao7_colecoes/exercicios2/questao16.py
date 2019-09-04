"""
16) Faça um programa para corrigir uma prova com 10 quetões de múltipla
escolha (a, b, c, d ou e), em uma turma com 3 alunos. Cada questão vale
1 ponto. Leia o gabarito, e para cada aluno leia sua matricula (número inteiro)
e suas respostas. Calcule e escreva: Para cada aluno, escreva sua matrícula, suas
respostas, e sua nota. O percentual de aprovação, assumindo média 7.0.
"""

gabarito = []

cont = 0
while len(gabarito) < 10:

    alternativa = str(input(f"Digite a alternativa correta da questão {cont+1}: "))

    if (alternativa.lower() == 'a') or (alternativa.lower() == 'b') or (alternativa.lower() == 'c') or \
       (alternativa.lower() == 'd') or (alternativa.lower() == 'e'):

        gabarito.append(alternativa)

    else:
        print("Alternativa inválida")
        cont -= 1

    cont += 1

matriculas = []

alunos = []

cont = 0
while len(alunos) < 3:

    matricula = int(input(f"\nDigite o número da matrícula do aluno {cont+1}: "))

    # Verificando se a matricula já foi digitada
    if matricula not in matriculas:
        matriculas.append(matricula)

        respostas = []
        for j in range(10):
            resposta = str(input(f"Digite a resposta da questão {j+1} do aluno {cont+1}: "))

            if (resposta.lower() == 'a') or (resposta.lower() == 'b') or (resposta.lower() == 'c') or \
               (resposta.lower() == 'd') or (resposta.lower() == 'e'):

                respostas.append(resposta)

            else:

                # Caso o aluno digite uma alternativa inválida ou deixe em branco, a questão estará errada
                respostas.append('z')

        alunos.append([matricula, respostas])

    else:
        print("Essa matrícula já foi digitada")
        cont -= 1

    cont += 1


for i in range(3):

    corretos = 0
    for j in range(10):

        # Acessando a lista de respostas, indice 1
        if alunos[i][1][j] == gabarito[j]:
            corretos += 1

    # Acessando o número da matrícula, indice 0
    print(f"\nA matrícula do aluno {i+1}: {alunos[i][0]}")
    print(f"\nAs respostas do aluno {i+1}:")

    for j in range(10):
        print(f"Questão {j+1}: alternativa {alunos[i][1][j]}")

    print(f"\nNota do aluno {i+1}: {corretos}")

    # Fazendo uma regra de 3
    percentual_aprovacao = int((corretos * 100) / 7)

    print(f"Percentual de aprovação do aluno {i+1}: {percentual_aprovacao}%")
