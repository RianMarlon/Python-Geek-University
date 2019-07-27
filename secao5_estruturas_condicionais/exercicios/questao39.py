"""
39) Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
tabela que consideraa o salário atual e o tempo de serviço de cada funcionário.
Os funcionários com menor salário terão um aumento proporcionalmente maior do que
os funciopnários com um salário maior, e conforme o tempo de serviço na empresa, cada
funcionário irá receber um bônus adicional de salário. Faça um programa que leia:

    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
    empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima
o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha
direito a nenhum aumento.

    |   Salário Atual   |   Reajuste    | Tempo de Serviço |  Bônus     |
    | Até 500,00        |     25%       | Abaixo de 1 ano  | Sem bônus  |
    | Até 1000,00       |     20%       | De 1 a 3 anos    |  100,00    |
    | Até 1500,00       |     15%       | De 4 a 6 anos    |  200,00    |
    | Até 2000,00       |     10%       | De 7 a 10 anos   |  300,00    |
    | Acima de 2000,00  | Sem reajuste  | Mais de 10 anos  |  500,00    |

"""

salario_atual = float(input("Diigite o salário do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário(em anos): "))

salario_final = 0.0

print()
if (salario_atual > 0) and (salario_atual <= 500):
    salario_final = salario_atual + (salario_atual * 0.25)

elif (salario_atual > 500) and (salario_atual <= 1000):
    salario_final = salario_atual + (salario_atual * 0.20)

elif (salario_atual > 1000) and (salario_atual <= 1500):
    salario_final = salario_atual + (salario_atual * 0.15)

elif (salario_atual > 1500) and (salario_atual <= 2000):
    salario_final = salario_atual + (salario_atual * 0.10)

elif salario_atual > 2000:
    salario_final = salario_atual

else:
    print("Salário inválido")


if (tempo_servico >= 0) and (tempo_servico < 1):
    print("Sem bônus")

elif (tempo_servico >= 1) and (tempo_servico <= 3):
    salario_final += 100
    print("Bônus de 100,00")
elif (tempo_servico >= 4) and (tempo_servico <= 6):
    salario_final += 200
    print("Bônus de 200,00")

elif (tempo_servico >= 7) and (tempo_servico <= 10):
    salario_final += 300
    print("Bônus de 300,00")

elif tempo_servico > 10:
    salario_final += 500
    print("Bônus de 500,00")

else:
    print("Tempo de serviço inválido")


print("Salário final: %.2f" % salario_final)
