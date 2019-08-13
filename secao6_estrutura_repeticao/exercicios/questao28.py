"""
28) Faça um porgrama que leia um valor N inteiro e positivo,
calcule e mostre o valor E, conforme a fórmula a seguir
    E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""
n = int(input("Digite um valor inteiro e positivo: "))

e = 1

print()
if n > 0:
    for i in range(1, n+1):
        fatores = i

        for j in range(1, fatores):
            fatores *= j

        e += 1/fatores

    print(f"O valor de E = {e}")

else:
    print("O valor deve ser positivo!")
