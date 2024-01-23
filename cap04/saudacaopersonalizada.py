

# Exemplo de argumento padrão
def saudacao_personalizada(nome, saudacao="Olá"):
    """Esta função imprime uma saudação personalizada."""
    print(f"{saudacao}, {nome}!")



# Chamada de função com argumento padrão
saudacao_personalizada("Carlos")  # Saída: "Olá, Carlos!"
saudacao_personalizada("Maria", saudacao="Bom dia")  # Saída: "Bom dia, Maria!"


