"""
25) Calcule as raízes da equeção de 2° grau;.
    Lembrando que:
    x = – b ± √∆
          2∙a

        Onde:
    ∆ = b² - 4ac
    E ax² + bx + c = 0 representa uma equeção de 2° grau.

A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem
"Não é equação de segundo grau."
    - Se ∆ < 0, não existe real. Imprima a mensagem Não existe raiz
    - Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
    - Se ∆ > 0,imprima as duas raízes reais.
"""

a = float(input("Digite o valor do ax²: "))
b = float(input("Digite o valor de bx: "))
c = float(input("Digite o valor de c: "))

print()
if a != 0:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Não existe raiz!")

    elif delta == 0:
        x = -b / (2 * a)
        print(f"A raiz única: {x}")

    else:
        x1 = (-b + delta ** 0.5) / 2 * a
        x2 = (-b - delta ** 0.5) / 2 * a
        print(f"As raízes são {x1} e {x2}")

else:
    print("Não é equação de segundo grau.")