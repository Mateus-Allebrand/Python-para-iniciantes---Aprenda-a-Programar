
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

carro = Carro(modelo="Civic")
print(carro.modelo)  # Acesso público


class Pessoa:
    def __init__(self, _nome):
        self._nome = _nome

pessoa = Pessoa(_nome="Maria")
print(pessoa._nome)  # Acesso protegido


class ContaBancaria:
    def __init__(self, __saldo):
        self.__saldo = __saldo

conta = ContaBancaria(__saldo=1000)
# print(conta.__saldo)  # Isso geraria um erro, pois __saldo é privado


class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, novo_titulo):
        if len(novo_titulo) > 0:
            self.__titulo = novo_titulo

livro = Livro(titulo="Python 101", autor="John Doe")
print(livro.get_titulo())  # Obtendo o título
livro.set_titulo(novo_titulo="Python Avançado")  # Modificando o título
print(livro.get_titulo())  # Saída: "Python Avançado"

