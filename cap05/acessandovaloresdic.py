



# Exemplo de criação de dicionário
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

cores_rgb = {
    "vermelho": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255)
}



# Exemplo de acesso a valores em dicionário
print(pessoa["nome"])  # Saída: "Ana"
print(cores_rgb["verde"])  # Saída: (0, 255, 0)



# Exemplo de uso do método get
idade = pessoa.get("idade", 0)  # Se "idade" não existir, retorna 0
print(idade)  # Saída: 25



