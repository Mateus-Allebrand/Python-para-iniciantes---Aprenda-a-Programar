
# Exemplo de leitura de um arquivo binário
caminho_arquivo_binario = 'imagem.jpg'

with open(caminho_arquivo_binario, 'rb') as arquivo_binario:
    dados = arquivo_binario.read()
    # Processar os dados binários conforme necessário


