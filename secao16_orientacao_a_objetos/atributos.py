"""
POO - Atributos

Atributos - Representam as caracteristicas do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, divimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){

    private Integer voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(Integer voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public Integer getVoltagem(){
        return this.voltagem;
    }

    public String getCor(){
        return this.cor;
    }

    public String getLigada(){
        return this.ligada;
    }
}


Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe
é público. Ou seja, pode ser acessado em todo o projeto. Caso queiramos demonstrar
que determinado atributo deve ser tratado como privado, ou seja, deve ser acessado/
utilizado somente dentro da própria classe onde está declarado, utiliza-se __ duplo
underscore no início de seu nome.

Isso é conhecido também como Name Mangling.

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem
# Python não vai impedir que façamos acesso aos atributos sinalizados
# como privados fora da classe

# Exemplo

user = Acesso("user@gmail.com", "123456")
print(user.email)

print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso. Mas não deveriamos fazer este acesso
print(user.get_senha())
print(user.get_email())

# O que signfica atributos de instância?

# Significa, que ao criarmos instância/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso("user1@gmail.com", "1123456")
user2 = Acesso("user2@gmail.com", "654321")

print(user1.get_email())
print(user2.get_email())

# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe,
# ou seja, fora do construtor. Geralmente já inicializamos um valor, e este é compartilhada entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter
# seus próprios valores como é o caso dos atributos de instância, com os atributos de classe
# todas as instâncias terão o mesmo valor para este atributo


p1 = Produto("Playstation 4", "video game", "1800.00")
p2 = Produto("Xbox One S", "video game", "2300.00")

# Acesso possível, mas incorreto de um atributo de uma classe
print(p1.valor)

# Acesso possível, mas incorreto de um atributo de uma classe
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a atributos
# de classe

# Acesso correto de um atributo de classe
print(Produto.imposto)

print(p1.id)
print(p2.id)

# OBS: Em linguagem como o Java, os atributos conhecidos como atributos de classes
# aqui em Python são chamadas de atributos estáticos

"""

# class Lampada:
#
#     def __init__(self, voltagem, cor):
#         self.__voltagem = voltagem
#         self.__cor = cor
#         self.__ligada = False
#
#     @property
#     def get_voltagem(self):
#         return self.__voltagem
#
#     @property
#     def get_cor(self):
#         return self.__cor
#
#     @property
#     def get_ligada(self):
#         return self.__ligada


# Classe com Atributos de Instância Público
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Publicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def get_email(self):
        return self.email


# Refatorar a classe Produto
class Produto:

    # Atributo de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos Dinâmicos -> Um atributos de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)


