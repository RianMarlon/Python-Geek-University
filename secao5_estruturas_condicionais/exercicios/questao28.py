"""
28) Faça um programa que leia três números inteiros positivos e efetue
o cálculo de uma das seguintes médias de acordo com um valor numérico
digitado pelo usuário:
    (a) Geométrica: ³√x * y * z
    (b) Ponderada: (x + 2 * y + 3 * z) / 6
    (c) Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))
    (d) Aritmética: (x + y + z) / 3
"""

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

print()
print("[1] Geométrica: ³√x * y * z\n"
      "[2] Ponderada: (x + 2 * y + 3 * z) / 6\n"
      "[3] Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))\n"
      "[4] Aritmética: (x + y + z) / 3")

calculo = int(input("Escolha o tipo do cáculo [1][2][3][4]: "))

print()
if calculo == 1:
    resultado = (x * y * z) ** (1 / 3)
    print(f"O resultado: {resultado}")

elif calculo == 2:
    resultado = (x + 2 * y + 3 * z) / 6
    print(f"O resultado: {resultado}")

elif calculo == 3:
    resultado = 1 / (1 / x) + (1 / y) + (1 / z)
    print(f"O resultado: {resultado}")

elif calculo == 4:
    resultado = (x + y + z) / 3
    print(f"O resultado: {resultado}")

else:
    print("Essa opção não existe.")