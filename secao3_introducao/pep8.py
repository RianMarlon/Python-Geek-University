"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classe;
EX.
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utile nomes em minúsculo, separados por underlines para funções e váriaveis
Ex.
def soma():
    pass

def soma_dois():
    pass

numero = 4
numero_impar = 5


[3] - utileze 4 espaços para indentação(NÃO use TAB)

if ("a" in "banana"):
    print("tem")


[4] - linhas em branco
- Separar funções e definições de classe com duas linhas em braco;
- Metódos dentro de uma classe devem ser separadas com uma única linha em branco;


[5] - imports
- imports sempre devem ser feitos em linhas separadas

#Import Errado

import sys, os

#Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from typer import (
    StringType,
    ListType,
    SetType
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstring e
# antes de constantes ou variáveis globais.


[6] - Espaço em expressõe e instruções

#Não faça:
funcao ( algo [ 1 ], { outro: 2 } )

#Faça:

funcao(algo[1], {outro: 2})

# Não faça:
dict ['chave'] = list [indice]

# Faça:

dict['chave'] = lista[indice]


[7] - Termine sempre uma instrução com uma nova linha

"""