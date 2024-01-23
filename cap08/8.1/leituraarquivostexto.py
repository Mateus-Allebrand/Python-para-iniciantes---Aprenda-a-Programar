
# Exemplo de leitura de um arquivo de texto
caminho_arquivo = 'exemplo.txt'

with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


# Leitura de um arquivo linha por linha
with open(caminho_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha)


