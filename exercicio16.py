# Leitura do número real introduzido pelo utilizador
numero = float(input("Digite um número: "))

# Estrutura condicional para verificar a classificação do número
if numero > 0:
    print("Resultado: POSITIVO")
elif numero < 0:
    print("Resultado: NEGATIVO")
else:
    print("Resultado: ZERO")

