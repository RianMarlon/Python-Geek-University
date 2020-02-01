"""
Introdução ao móduo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais do código fonte

Unidades individuais podem ser: funções, métodos, classes, módulos e etc.

# OBS: Testes unitários não são específics da linguagem Python.

Para criar nossos testes, criamos classes que herdam do unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para a sua unidade

# Conhecendo as assertions

https://docs.python.org/3/library/unittest.html

Método                        Checa se
assertEqual(a, b)             a == b
assertNotEqual(a, b)          a != b
assertTrue(x)                 x é verdadeiro
assertFalse(x)                x é falso
assertIs(a, b)                a é b
assertIsNot(a, b)             a não é b
assertIsNone(x)               x é None
assertIsNotNone(x)            x não é None
assertIn(a, b)                a está em b
assertNotIn(a, b)             a não está em b
assertIsInstance(a, b)        a é instância de b
assertNotIsInstance(a, b)     a não é instância de b


Por convenção, todos os teste em um test case, devem ter seu nome iniciado
com test_

# Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unnitest no modo verboso

python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings em nossos testes.
"""

# Prática - Utilizando a abordagem TDD





