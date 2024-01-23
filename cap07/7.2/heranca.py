
# Exemplo de herança
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass  # Método a ser sobrescrito pelas subclasses

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Criando objetos
cachorro = Cachorro(nome="Rex")
gato = Gato(nome="Whiskers")

print(cachorro.nome)  # Saída: "Rex"
print(cachorro.fazer_som())  # Saída: "Au Au!"

print(gato.nome)  # Saída: "Whiskers"
print(gato.fazer_som())  # Saída: "Miau!"


