"""
39) A importância de R$ 780.000,00 será dividida entre três
ganhadores de um concurso. Sendo que da quantia total:
 - O primeiro ganhador receberá 46%;
 - O segundo receberá 32%;
 - O terceiro receberá o restante;

Calcule e imprima a quantia ganha por cada um dos ganhadores
"""

valor = 780000.00

primeiro_ganhador = 780000.00 * 0.46
segundo_ganahdor = 780000.00 * 0.32
terceiro_ganhador = 780000.00 * 0.22

print("\nO primeiro ganhador receberá: R$%.2f\n"
      "O segundo ganahdor receberá: R$%.2f\n"
      "O terceiro ganhador receberá: R$%.2f"
      % (primeiro_ganhador, segundo_ganahdor, terceiro_ganhador))
