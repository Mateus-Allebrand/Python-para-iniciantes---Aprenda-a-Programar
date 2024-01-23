
try:
    # Código que pode gerar uma exceção
    resultado = operacao_arriscada()
except TipoDeExcecao as nome_da_excecao:
    # Código a ser executado se ocorrer uma exceção do TipoDeExcecao
    lidar_com_excecao(nome_da_excecao)
else:
    # Código a ser executado se NENHUMA exceção ocorrer
    processamento_bem_sucedido(resultado)
finally:
    # Código a ser executado sempre, independentemente de exceções
    finalizar()
