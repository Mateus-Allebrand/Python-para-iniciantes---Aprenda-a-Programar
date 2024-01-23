
class Calculadora:
    def calcular(self, a, b=None, c=None):
        if c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

# Exemplo de polimorfismo de sobrecarga
calc = Calculadora()
print(calc.calcular(1))          # Saída: 1
print(calc.calcular(1, 2))       # Saída: 3
print(calc.calcular(1, 2, 3))    # Saída: 6


