
import json

# Exemplo de serialização para JSON
dados_python = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "Wonderland"
}

dados_json = json.dumps(dados_python)
print(dados_json)


