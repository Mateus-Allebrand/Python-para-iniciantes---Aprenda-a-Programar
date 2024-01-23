



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



# Exemplo de modificação de dicionário
pessoa["idade"] = 26  # Modificando o valor associado à chave "idade"
pessoa["profissao"] = "Engenheira"  # Adicionando um novo par chave-valor
del pessoa["cidade"]  # Removendo a chave "cidade" e seu valor associado


# Exemplo de iteração sobre dicionário
for chave in pessoa:
    print(chave, pessoa[chave])

# Saída:
# nome Ana
# idade 26
# profissao Engenheira


# Exemplo de uso dos métodos keys, values e items
chaves = pessoa.keys()  # Retorna uma visualização das chaves
valores = pessoa.values()  # Retorna uma visualização dos valores
itens = pessoa.items()  # Retorna uma visualização dos itens (pares chave-valor)

print(chaves)  # Saída: dict_keys(['nome', 'idade', 'profissao'])
print(valores)  # Saída: dict_values(['Ana', 26, 'Engenheira'])
print(itens)  # Saída: dict_items([('nome', 'Ana'), ('idade', 26), ('profissao', 'Engenheira')])



