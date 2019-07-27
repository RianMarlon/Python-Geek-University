"""
44) Receba a altura do degrau de uma escada e a altura que o usuário
deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário
deverá subir para atingir seu objetivo.
"""

altura_degrau = float(input("Digite a altura do degrau (em cm): "))
altura = float(input("Digite a altura que deseja alcançar (em m): "))

quant_degraus = int((altura * 100) / altura_degrau)

print(f"\nA quantidade de degraus que deverá subir:\n{quant_degraus} degraus")
