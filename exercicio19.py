# Leitura dos três números reais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Inicializa o maior e o menor com o primeiro número
maior = num1
menor = num1

# Verificação do maior número
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Verificação do menor número
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Exibição dos resultados
print(f"Maior: {maior}")
print(f"Menor: {menor}")

