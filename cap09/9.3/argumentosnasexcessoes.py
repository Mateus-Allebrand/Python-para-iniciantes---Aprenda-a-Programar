
class ValorNegativoError(Exception):
    def __init__(self, valor, mensagem="O valor não pode ser negativo."):
        self.valor = valor
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# Exemplo de uso da exceção personalizada com argumentos
try:
    valor = -5
    if valor < 0:
        raise ValorNegativoError(valor)
except ValorNegativoError as e:
    print(f"Erro: {e}")



