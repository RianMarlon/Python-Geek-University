"""
Unittest - Antes e após hooks

Hooks - São os testes em si. Ou seja, a execução dos testes.

setUp() -> Antes de cada método de teste, é útil para criarmos
instância de objets e outros dados;

tearDown() -> é executado ao final de cada método de teste. é útil
para excluir dados ou fechar conexões com banco de dados
"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeito(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodas após o teste
        pass

    def test_segundo(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodas após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass





