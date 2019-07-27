"""
24) Leia um valor de área em metros quadrados e m² e apresente-o
convertido em acres. A fórmula de conversão é: A = M * 0,000247, sendo M
a área em metros quadrados e A área em acres.
"""

metros_quadrados = float(input("Digite o valor da área em metros quadrados: "))

acres = metros_quadrados * 0.000247

print(f"\nO valor da área em acres é {acres}")
