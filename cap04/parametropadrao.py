

# Exemplo de parâmetro padrão
def saudacao_personalizada(nome, saudacao="Olá"):
    """Esta função imprime uma saudação personalizada."""
    print(f"{saudacao}, {nome}!")


# Chamada de função com parâmetro padrão
saudacao_personalizada("Maria")  # Saída: "Olá, Maria!"
saudacao_personalizada("João", saudacao="Bom dia")  # Saída: "Bom dia, João!"


