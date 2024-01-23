

# Exemplo de herança múltipla
class Animal:
    def mover(self):
        print("Movendo-se")

class Maquina:
    def ligar(self):
        print("Ligando")

class Robo(Animal, Maquina):
    pass

# Criando objeto
robo = Robo()
robo.mover()  # Saída: "Movendo-se"
robo.ligar()  # Saída: "Ligando"


