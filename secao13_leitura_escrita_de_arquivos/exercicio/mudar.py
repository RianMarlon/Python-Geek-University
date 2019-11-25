nome_arquivo = "arquivos/vendedores.txt"


with open(nome_arquivo, "r", encoding="utf-8") as verificacao:

    texto = verificacao.read().strip().replace(", ", ";")

    with open(nome_arquivo, "w", encoding="utf-8") as alterando:
        alterando.write(texto)


