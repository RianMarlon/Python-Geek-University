"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, como os atributos, dividimos os métodos em 3 grupos: Métodos de instância, Métodos de Classe
e Métodos Estáticos.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor
e sua função é construir o objeto a partir da classe.

OBS: Todo elemento em ýthon que inicia e finaliza ocm duplo underline é chamado de dunder
(Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.


ATENÇÃO! Por mais que possamos criar nossas próprias funções dunder (underline no início
e no fim) não é aconselhado. Python possui vários métodos com esta forma de nomenclatura
e pode ser que mudemos o comportamento dessas funções mágicas internas da linguagem. Então
evite ao máximo. De preferência, nunca o faça.

p1 = Produto("Playstation 4", "Video Game", 1800)

print(p1.desconto(50))

print(Produto.desconto(p1, 10))

user1 = Usuario("Angelina", "Jolie", "angelina@gmail.com", "123456")
user2 = Usuario("Felicity", "Jones", "felicity@gmail.com", "654321")

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

print(f"Senha: {user1._Usuario__senha}")  # Acesso de forma errada de um atributo de classe
print(f"Senha: {user2._Usuario__senha}")  # Acesso de forma errada de um atributo de classe

nome1 = input("Informe o nome: ")
sobrenome1 = input("Informe o sobrenome: ")
email1 = input("Informe o e-mail: ")
senha1 = input("Informe a senha: ")
confirma1 = input("Confirme a senha: ")

while senha1 != confirma1:
    print("\nAs senhas digitadas não são as mesmas, tente novamente!")
    senha1 = input("\nInforme a senha: ")
    confirma1 = input("Confirme a senha: ")

print("\nUsuário criado com sucesso!")

user1 = Usuario(nome1, sobrenome1, email1, senha1)

senha1 = input("\nInforme a senha para acesso: ")

if user1.checa_senha(senha1):
    print("\nAcesso permitido!")
    print(f"Senha do User 1 Criptografada: {user1._Usuario__senha}")  # Acesso errado

else:
    print("\nAcesso negado!")

# Métodos de Classe em Python são conhecidos como métodos estáticos em outras linguagens

user = Usuario("felicity", "jones", "felicity@gmail.com", "123456")

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta


# Métodos de Classe

user = Usuario("felicity", "jones", "felicity@gmail.com", "123456")

print(user._Usuario__gera_usuario())  # Acesso, de forma ruim...


# Métodos Estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario("felicity", "jones", "felicity@gmail.com", "123456")

print(user.contador)

print(user.definicao())


"""


from passlib.hash import pbkdf2_sha512 as cryp


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo

        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto passado por parâmetro"""
        return self.__valor - ((porcentagem / 100) * self.__valor)


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f"Classe: {cls}")
        print(f"Temos {cls.contador} usuário(s) no sistema")

    @classmethod
    def ver(cls):
        print("Teste")

    @staticmethod
    def definicao():
        return "UXR344"

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome.strip().title()
        self.__sobrenome = sobrenome.strip().title()
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=2000000, salt_size=28)
        Usuario.contador = self.__id

        print(f"Usuário criado: {self.__gera_usuario()}")

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True

        return False

    def __gera_usuario(self):
        return self.__email.split("@")[0]



