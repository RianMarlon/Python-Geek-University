"""
Estrututras lógicas: and(e). or(ou), not(não), is(é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:

Para o 'and', ambos os avlores precisam ser true
Para 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vire False, se for False vira True
"""

ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo usuário")

else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
