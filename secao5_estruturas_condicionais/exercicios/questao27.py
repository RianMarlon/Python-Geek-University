"""
27) Excreva um programa que, dada a idade de um nadador, classique-o em
uma das seguintes categorias:

     Categoria   | Idade
     Infantil A  | 5 a 7
     Infantil B  | 8 a 10
     Juvenil A   | 11 a 13
     Juvenil B   | 14 a 17
     Sênior      | maiores de 18 anos
"""

idade = int(input("Digite a idade do nadador: "))

print()
if (idade >= 5) and (idade <= 7):
    print("Infantil A")

elif (idade >= 8) and (idade <= 10):
    print("Infantil B")

elif (idade >= 11) and (idade <= 13):
    print("Juvenil A")

elif (idade >= 14) and (idade <= 17):
    print("Juvenil B")

elif idade > 18:
    print("Sênior")

else:
    print("Não possui classificação para idade menor que 5 anos")
