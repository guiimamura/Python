# Leitura dos dados de entrada
peso = float(input("Peso: "))
altura = float(input("Altura: "))

# Cálculo do IMC
imc = peso / (altura * altura)

# Classificação baseada nos intervalos fornecidos
if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

# Exibição dos resultados formatados
print(f"\nIMC: {imc:.1f}")
print(f"Classificação: {classificacao}")

