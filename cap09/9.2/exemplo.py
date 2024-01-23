

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError as ve:
    print("Por favor, digite um número inteiro válido.", ve)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print("Operação bem-sucedida.")
finally:
    print("Fim do programa.")


