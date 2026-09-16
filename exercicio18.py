# Leitura dos dois números reais
valor1 = float(input("Primeiro valor: "))
valor2 = float(input("Segundo valor: "))

# Estrutura condicional para verificar qual é o maior ou se são iguais
if valor1 > valor2:
    print(f"Maior valor: {valor1}")
elif valor2 > valor1:
    print(f"Maior valor: {valor2}")
else:
    print("Não existe maior (VALORES IGUAIS)")

