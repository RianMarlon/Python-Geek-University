"""
10) Faça um porgrama que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as sequintes fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 58
"""

altura = float(input("Digite sua altura: "))
sexo = (input("Digite seu sexo: "))

sexo = sexo.lower()

print()
if (sexo == 'feminino') or (sexo == 'f'):
    peso_ideal = (62.1 * altura) - 58
    print("Seu peso ideal: %.2f" % peso_ideal)

elif(sexo == 'masculino') or (sexo == 'm'):
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal: %.2f" % peso_ideal)

else:
    print("Erro ao digitar o sexo")
