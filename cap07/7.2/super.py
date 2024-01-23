
# Exemplo de uso do método super
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def fazer_som(self):
        som_animal = super().fazer_som()
        return f"{som_animal} -> Au Au!"

# Criando objeto
cachorro = Cachorro(nome="Rex")
print(cachorro.fazer_som())  # Saída: "Som genérico -> Au Au!"


