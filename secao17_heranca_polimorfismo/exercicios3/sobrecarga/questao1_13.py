"""
1) Crie um novo pacote chamado sobrecarga.

2) Crie uma classe Pessoa.

3) Na classe Pessoa crie 3 variáveis de instância: código, nome, idade

4) Crie um método exibe(), que exiba o conteúdo de todas as variáveis
declaradas na classe em questão

5) Crie uma sobrecarga no método exibe() que receba como parâmetro um
número inteiro e decida por meio do valor desse parâmetro se a idade será
exibida ou não. Para isso use o seguinte critério: se o valor do parâmetro
for igual a 1, imprima idade, se não, não imprima a idade, mas apenas as
outras variáves de instância.

6) Crie um construtor padrão explícito para a classe Pessoa, esse construtor
deverá exibir uma mensagem: "Construtor padrão"

7) Crie uma classe chamada TestaPessoa que instancie um objeto da classe
Pessoa usando o construtor padrão

8) Ainda na classe TestaPessoa, inicialize as variáveis de instância:
código, nome e idade com valores à sua escolha e acione o método exibe(),
sem nenhum parâmetro

9) Repita a operação da questão anterior, acionando o método exibe(),
passando ele um argumento inteiro de valor 1

10) Repita o que foi feito na questão anterior, só que desta vez, passando
um argumento diferente de 1

11) Crie um construtor sobrecarregado que permita instanciar objetos com
os 3 valores sendo inicializados por valores passados como parâmetros

12) Na classe TestaPessoa instancie um objeto usando o segundo construtor (com
os 3 parâmetros).

13) Exiba os dados do objeto que foi instanciado na questão anteiror por
meio do método exibe() sem argumentos
"""

from verificacao import verificar_nome


class Pessoa:

    def __init__(self):
        print("\nConstrutor padrão")

        self.__codigo = 0
        self.__nome = "Sem nome"
        self.__idade = 0

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @codigo.setter
    def codigo(self, novo_valor):

        try:

            if type(novo_valor) != bool:

                if int(novo_valor) >= 1:
                    self.__codigo = int(novo_valor)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nCódigo inválido")

    @nome.setter
    def nome(self, novo_valor):

        try:

            if type(novo_valor) == str:

                if verificar_nome(novo_valor) and novo_valor.strip() != "":
                    self.__nome = novo_valor

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nNome inválido")

    @idade.setter
    def idade(self, novo_valor):

        try:

            if type(novo_valor) != bool:

                if int(novo_valor) >= 0:
                    self.__idade = int(novo_valor)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nIdade inválido")

    def exibe(self, valor=1):
        print(f"\nCódigo: {self.__codigo}")
        print(f"Nome: {self.__nome}")
        if valor == 1:
            print(f"Idade: {self.__idade}")


class TestaPessoa:

    def __init__(self):

        pessoa1 = Pessoa()
        pessoa1.codigo = 1
        pessoa1.nome = "Marcos"
        pessoa1.idade = 17

        pessoa1.exibe()
        pessoa1.exibe(1)
        pessoa1.exibe(2)


if __name__ == "__main__":
    pessoa1 = Pessoa()

    pessoa1.codigo = 5
    pessoa1.nome = "João"
    pessoa1.idade = 20

    pessoa1.exibe()

    teste1 = TestaPessoa()


