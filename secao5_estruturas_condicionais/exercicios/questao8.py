"""
8) Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas
e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente,
um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este
fato deve ser informado ao usuário e o programa termina.
"""

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite s segunda nota do aluno: "))

print()
if (nota1 >= 0.00) and (nota1 <= 10) and (nota2 >= 0.0) and (nota2 <= 10):
    media = (nota1 + nota2) / 2
    print("Média: %.2f" % media)

else:
    print("A nota não possue um valor válido")
