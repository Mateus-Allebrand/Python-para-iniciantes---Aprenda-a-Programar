

# Exemplo de criação de strings
nome = 'Ana'
mensagem = "Bem-vindo ao mundo Python!"



# Exemplo de concatenação de strings
saudacao = "Olá"
nome = "Maria"
mensagem = saudacao + ", " + nome + "!"
print(mensagem)  # Saída: "Olá, Maria!"


# Exemplo de concatenação com formatação de strings (Python 3.6 e posterior)
saudacao = "Olá"
nome = "Maria"
mensagem = f"{saudacao}, {nome}!"
print(mensagem)  # Saída: "Olá, Maria!"



# Exemplo de repetição de strings
linha = "-" * 30
print(linha)  # Saída: "------------------------------"



# Exemplo de indexação em string
fruta = "banana"
primeira_letra = fruta[0]  # Obtendo a primeira letra ("b")



# Exemplo de fatiamento de string
fruta = "banana"
substring = fruta[1:4]  # Obtendo os caracteres do índice 1 ao 3 ("ana")



# Exemplo de obtenção do comprimento de uma string
mensagem = "Python é incrível!"
comprimento = len(mensagem)
print(comprimento)  # Saída: 18



# Exemplo de alguns métodos de string
texto = "Python é divertido!"
maiusculas = texto.upper()  # Converte para maiúsculas
minusculas = texto.lower()  # Converte para minúsculas
substituido = texto.replace("divertido", "poderoso")  # Substitui parte da string
palavras = texto.split()  # Divide a string em uma lista de palavras


