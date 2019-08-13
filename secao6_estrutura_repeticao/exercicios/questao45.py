"""
45) Faça um algoritmo que converta uma velocidade expressa em km/h
para m/s e vice versa. Você deve criar um menu com as duas opções de
conversão e com uma opção para finalizar o programa. O usuário poderá
fazer quantas conversões desejar, sendo que o programa só será finalizado quando
a opção de finalizar for escolhida.
"""

while True:
    print("[1] -> Converter velocidade expressa em km/h para m/s\n"
          "[2] -> Converter velocidade expressa em m/s para km/h \n"
          "[3] -> Finalizar o programa")
    opcao = str(input("Digite o número referente à opção que você deseja: "))

    print()
    if (opcao == '1') or (opcao == '[1]'):
        km_h = float(input("Digite a velocidade expressa em km/h: "))

        print()
        print("Velocidade em m/s: %.2f\n" % (km_h / 3.6))

    elif (opcao == '2') or (opcao == '[2]'):
        m_s = float(input("Digite a velocidade expressa em m/s: "))

        print()
        print("Velocidade em km/h: %.2f\n" % (m_s * 3.6))

    elif (opcao == '3') or (opcao == '[3]'):
        print('FIM')
        break

    else:
        print("ERRO!\n")
