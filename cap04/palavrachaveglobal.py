

# Exemplo de uso da palavra-chave global
variavel_global = 30

def modificar_global():
    global variavel_global
    variavel_global += 5

modificar_global()
print(variavel_global)  # Saída: 35


