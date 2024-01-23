
class Animal:
    def fazer_som(self):
        pass  # Método a ser sobrescrito pelas subclasses

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Exemplo de polimorfismo de métodos
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.fazer_som())
# Saída:
# "Au Au!"
# "Miau!"


