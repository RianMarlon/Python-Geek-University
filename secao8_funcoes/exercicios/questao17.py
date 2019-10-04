"""
17) Faça ua função que receba dois números inteiros positivos
por parâmetro e retorne a soma dos N números inteiros existentes
entre eles.
"""


def entre_numeros(numero1, numero2):
    """
    Função que recebe dois números e retorna a soma dos N números
    que estão entre os números digitados.
    :param numero1:  Recebe um inteiro
    :param numero2: Recebe um inteiro
    :return: Retorna o resultado da soma dos N números entre os números recebidos.
    Caso algum número seja float ou não seja positivo, retorna um valor do tipo None
    """

    soma = 0

    if numero1 // 1 == numero1 and numero2 // 1 == numero2:

        if numero1 >= numero2:
            for i in range(numero2+1, numero1, 1):
                soma += i

        elif numero2 >= numero1:
            for i in range(numero1+1, numero2, 1):
                soma += i

        return soma


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\nA soma dos N entre os números recebidos: {entre_numeros(num1, num2)}")
