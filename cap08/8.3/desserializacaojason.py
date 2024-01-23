

# Exemplo de desserialização de JSON
dados_json = '{"nome": "Bob", "idade": 25, "cidade": "Cityville"}'

dados_python = json.loads(dados_json)
print(dados_python)


