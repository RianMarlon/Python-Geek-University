"""
22) Escreva um programa completo que permita a qualquer aluno
introduzir, pelo teclado, uma sequência arbitrária de notas(válidas no intervalo de
10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética.
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido
ao programa, o qual terminará quando for introduzido um valor que não seja válido
como nota de aprovação.
"""

nota = 0.0

soma = 0.0
cont = 0
while True:
    nota = float(input("Digite uma nota entre 10 e 20: "))

    if (nota >= 10) and (nota <= 20):
        soma += nota
        cont += 1

    else:
        if cont == 0:
            cont += 1
        print(f"Nota {nota} inválida!")
        break

print()
print("Média aritmética: %.1f (excluindo a última nota digitada)" % (soma / cont))
