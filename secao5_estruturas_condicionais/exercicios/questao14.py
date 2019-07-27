"""
14) A nota final de um estudante é calculada a partir de três notas atribuídas entre
o intervalo de 0 até 10, respectivamente, a trabalho do laboratório, a uma avaliação
semestral e a um exame final. A média das três notas mencionadaa anteriormente obdece aos
pesos: Trabalho de Laboratório: 2; Avaliaçõ Semestral: 3; Exame final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9),
de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

trabalho_laboratorio = float(input("Digite a nota do trabalho do laboratório do aluno: "))
avaliacao_semestral = float(input("Digite a nota da avaliação semestral do aluno: "))
exame_final = float(input("Digite a nota do exame final do aluno: "))


print()
if ((trabalho_laboratorio >= 0) and (trabalho_laboratorio <= 20)) and ((avaliacao_semestral >= 0) and (avaliacao_semestral <= 30)) and ((exame_final >= 0) and (exame_final <= 50)):

    media = (trabalho_laboratorio + avaliacao_semestral + exame_final) / (2 + 3 + 5)
    print("A média do aluno é %.1f" % media)

    if (media >= 0) and (media <= 2.9):
        print("O aluno está reprovado.")

    elif (media >= 3) and (media <= 4.9):
        print("O aluno está de recupeção")

    else:
        print("O aluno está aprovado")

else:
    print("Nota(s) digitada incorretamente!")