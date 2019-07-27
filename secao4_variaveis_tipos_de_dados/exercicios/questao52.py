"""
52) Três amigos jogaram na loteria. Caso eles ganhem,
o prêmio deve ser repartido porporcionalmente ao valor
que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

apostador1 = float(input("Quanto o apostador 1 investiu: "))
apostador2 = float(input("Quanto o apostador 2 investiu: "))
apostador3 = float(input("Quanto o apostador 3 investiu: "))

valor_premio = float(input("\nQual o valor prêmio: "))

premio_apostador1 = (apostador1 + valor_premio / 3)
premio_apostador2 = (apostador2 + valor_premio / 3)
premio_apostador3 = (apostador3 + valor_premio / 3)

print("\nO apostador 1 vai ganhar: %.2f\n"
      "O apostador 2 vai ganhar: %.2f\n"
      "O apostador 3 vai ganhar: %.2f"
      % (premio_apostador1, premio_apostador2, premio_apostador3))
