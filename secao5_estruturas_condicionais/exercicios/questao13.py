"""
13) Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

if ((nota1 >= 0.0) and (nota1 <= 100.0)) and ((nota2 >= 0.0) and (nota2 <= 100.0)) and ((nota3 >= 0.0) and (nota3 <= 200)):

    media = (nota1 + nota2 + nota3) / (1 + 1+ 2)

    print("\nA média do aluno é %.1f" % media)

    if media >= 60:
        print("Aluno aprovado.")

    else:
        print("Aluno reprovado.")

else:
    print("Nota(s) digitada incorretamente!")
