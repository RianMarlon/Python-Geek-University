"""
47) Faça um programa que apresente um menu de opções para o cálculo
das seguintes operações entre dois números:

    - adição (opção 1)
    - subtração (opção 2)
    - multiplicação (opção 3)
    - divisão (opção 4)
    - saídaa (opção 5)

O programa deve possibilitar ao usuário a escolha da operação desejaada,
a exibição do resultado e a volta ao menu de opções. O programa só termina
quando for escolhida a opção de saída (opção 5).
"""

while True:
    print("* adição (opção 1)\n"
          "* subtração (opção 2)\n"
          "* multiplicação (opção 3)\n"
          "* divisão (opção 4)\n"
          "* saída (opção 5)")
    opcao = int(input("Digite o número referente à opção desejada: "))

    print()
    if (opcao >= 1) and (opcao <= 4):

        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))

        if opcao == 1:
            print(f"{num1} + {num2} = {num1 + num2}\n")

        elif opcao == 2:
            print(f"{num1} - {num2} = {num1 - num2}\n")

        elif opcao == 3:
            print(f"{num1} * {num2} = {num1 * num2}\n")

        elif opcao == 4:
            print(f"{num1} / {num2} = {num1 / num2}\n")

    elif opcao == 5:
        print("FIM!")
        break

    else:
        print("ERRO!")
