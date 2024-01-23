
# Exemplo de escrita em um arquivo binário
novo_caminho_arquivo_binario = 'novo_arquivo.bin'

dados_binarios = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  # Dados binários de exemplo

with open(novo_caminho_arquivo_binario, 'wb') as novo_arquivo_binario:
    novo_arquivo_binario.write(dados_binarios)


