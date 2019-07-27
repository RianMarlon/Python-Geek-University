"""
21) Escreva o menu de opções abaixo. Leia a opção do usuário e
execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.

    Escolha a opção:
    1 - Soma de 2 números.
    2 - Diferença entre 2 número (maior pelo menor).
    3 - Produto entre 2 números.
    4 - Divisão entre 2 números (o denominador não pode ser zero).
    Opção
"""

print("1 - Soma de 2 números.\n"
      "2 - Diferença entre 2 número (maior pelo menor).\n"
      "3 - Produto entre 2 números.\n"
      "4 - Divisão entre 2 números (o denominador não pode ser zero).\n")

opcao = int(input("Escolha a opção: "))

print()
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print()
if opcao == 1:
    print(f"A soma dos dois número: {num1 + num2}")

elif opcao == 2:
    if num1 >= num2:
        print(f"A diferença entre os dois números: {num1 - num2}")
    elif num1 >= num1:
        print(f"A diferença entre os dois números: {num2 - num1}")

elif opcao == 3:
    print(f"O produto dos dois números: {num1 * num2}")

elif opcao == 4:
    if num2 != 0:
        print(f"A divisão dos dois números: {num1 / num2}")
    else:
        print("O denominador não pode ser zero!")

else:
    print("Opção inválida!")