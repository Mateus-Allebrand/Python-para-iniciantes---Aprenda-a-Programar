
class MinhaExcecaoPersonalizada(Exception):
    def __init__(self, mensagem="Ocorreu um erro personalizado."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# Exemplo de uso da exceção personalizada
try:
    raise MinhaExcecaoPersonalizada("Este é um erro personalizado.")
except MinhaExcecaoPersonalizada as e:
    print(f"Capturada exceção personalizada: {e}")


