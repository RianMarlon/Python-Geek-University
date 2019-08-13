"""
50) Chico tem 1.50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1.10
metros e cresce 3 centímetros por ano. Escreva um programa que calcule e imprima
quantos anos serão necessários para que Zé seja maior que Chico.
"""

chico = 1.50
ze = 1.20

for i in range(1, 50):
    chico += 0.02
    ze += 0.03

    if ze > chico:
        print(f"Zé possui %.2f metros" % ze)
        print("Chico possui %.2f metros" % chico)
        print(f"Serão necessários {i} anos para que Zé seja maior que Chico")
        break
