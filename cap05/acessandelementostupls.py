
# Exemplo de criação de tupla
coordenadas = (3, 5)
cores = ("vermelho", "verde", "azul")
mistura = (1, "texto", True)

# Exemplo de acesso a elementos de tupla
print(coordenadas[0])  # Saída: 3
print(cores[2])  # Saída: "azul"


# Exemplo de índices negativos em tupla
print(mistura[-1])  # Saída: True (último elemento)


# Tentativa de modificar uma tupla (gerará um erro)
coordenadas[0] = 4  # Isso resultará em um TypeError


