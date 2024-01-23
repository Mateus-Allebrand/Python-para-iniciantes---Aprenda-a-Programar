
import struct

# Exemplo de uso do módulo struct para ler dados binários em uma estrutura
with open('dados_binarios.dat', 'rb') as arquivo_binario:
    dados = arquivo_binario.read(8)  # Lê 8 bytes
    valores = struct.unpack('ii', dados)  # Desempacota dois inteiros (4 bytes cada)
    print(valores)

