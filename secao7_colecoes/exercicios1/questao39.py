"""
39) Escreva um programa que leia um número inteiro positivo n em seguida
imprima n linhas do chamado Triangulo de Pascal:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""

num = int(input("Digite um número positivo: "))

if num > 0:

    linha = list(range(num+1))

    # Formula -> (n!) / p!(n-p)!)
    for i in linha:

        print(f"Linha {i}: ", end=' ')

        for j in range(0, i+1):

            if j == 0 or j == i:
                print(1, end='  ')

            else:

                # Fatorial da linha
                n_fatorial = 1

                # Fatorial da coluna
                p_fatorial = 1

                for k in range(1, i+1):
                    n_fatorial *= k

                for l in range(1, j+1):
                    p_fatorial *= l

                # Fatoria da linha-coluna
                n_p_fatorial = i - j

                resultado_denominador = 1
                for m in range(1, n_p_fatorial+1):
                    resultado_denominador *= m

                # Resultado do denominador
                denominador = p_fatorial * resultado_denominador

                resultado_final = int(n_fatorial / denominador)
                print(resultado_final, end='  ')

        print()

else:
    print("Número inválida!")
