

# Exemplo de retorno de múltiplos valores
def divisao_e_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

resultado = divisao_e_resto(10, 3)
print(resultado)  # Saída: (3, 1)


