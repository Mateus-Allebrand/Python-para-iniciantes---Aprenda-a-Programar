

# Exemplo de leitura de JSON de arquivo
with open(caminho_arquivo_json, 'r') as arquivo_json:
    dados_python = json.load(arquivo_json)
    print(dados_python)
