


import json

# Exemplo de serialização para JSON
dados_python = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "Wonderland"
}

dados_json = json.dumps(dados_python)
print(dados_json)



#Exemplo de escrita de JSON em arquivo
caminho_arquivo_json = 'dados.json'

with open(caminho_arquivo_json, 'w') as arquivo_json:
    json.dump(dados_python, arquivo_json)


