

# Exemplo de escrita em um arquivo de texto
novo_caminho_arquivo = 'novo_arquivo.txt'

with open(novo_caminho_arquivo, 'w') as novo_arquivo:
    novo_arquivo.write("Este é um novo arquivo.\n")
    novo_arquivo.write("Com algumas linhas escritas por Python.\n")


