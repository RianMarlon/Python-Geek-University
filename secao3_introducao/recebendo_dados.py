"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entrw:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas Simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples tripla -> '''Angelina Jolie
"""
# - Aspas duplas triplas -> """Angelina Jolie"""

# Entrada de dados
nome = input("Qual o seu nome?")

# Exemplo de print 'antigo' 2x
# print("Seja bem-vindo %s" %(nome))

# Exemplo de print 'moderno' 3x
# print("Seja bem-vindo {0}".format(nome))

# Exemplo de print 'mais atual' 3.7
print(f"Seja bem-vindo {nome}")

idade = int (input("Qual sua idade?"))

# Processamento

# Saida
# Exemplo de print 'antigo' 2x
# print("O %s tem %d anos" %(nome, idade))

# Exemplo de print 'moderno' 3x
# print("O {0} tem {1} anos".format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f"O {nome} tem {idade} anos")

print(f"O {nome} nasceu {2019 - idade}")
