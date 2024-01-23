
class Forma:
    def calcular_area(self):
        pass  # Método a ser sobrescrito pelas subclasses

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

# Exemplo de polimorfismo de classes
formas = [Retangulo(base=5, altura=3), Circulo(raio=2)]

for forma in formas:
    print(forma.calcular_area())
# Saída:
# 15 (área do retângulo)
# 12.56 (área do círculo)


