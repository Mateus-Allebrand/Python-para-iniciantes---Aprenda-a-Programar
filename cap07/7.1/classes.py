
# Exemplo de definição de classe
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def dirigir(self):
        print(f"O carro {self.modelo} está em movimento.")


# Exemplo de criação de objetos
carro1 = Carro(modelo="Fusca", cor="azul")
carro2 = Carro(modelo="Civic", cor="preto")

carro1.dirigir()  # Saída: "O carro Fusca está em movimento."
carro2.dirigir()  # Saída: "O carro Civic está em movimento."



# Exemplo de uso do método __init__
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando objeto Pessoa
pessoa1 = Pessoa(nome="Alice", idade=30)


# Exemplo de atributos de instância e de classe
class ContaBancaria:
    taxa_juros = 0.05  # Atributo de classe

    def __init__(self, saldo):
        self.saldo = saldo  # Atributo de instância

    def calcular_juros(self):
        return self.saldo * ContaBancaria.taxa_juros

# Criando objetos ContaBancaria
conta1 = ContaBancaria(saldo=1000)
conta2 = ContaBancaria(saldo=2000)

print(conta1.calcular_juros())  # Saída: 50.0
print(conta2.calcular_juros())  # Saída: 100.0

