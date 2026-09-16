# Entrada de dados
valor_imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Prazo (anos): "))

# Cálculos base
# Converte o prazo de anos para meses para calcular a prestação
meses = anos * 12
prestacao = valor_imovel / meses

# Calcula o limite máximo permitido (30% do salário)
limite_salario = salario * 0.30

# Verificação condicional para aprovação
if prestacao <= limite_salario:
    resultado = "APROVADO"
else:
    resultado = "NEGADO"

# Exibição dos resultados formatados
print("-" * 30)
print(f"Prestação: R$ {prestacao:.2f}")
print(f"Limite (30% salário): R$ {limite_salario:.2f}")
print(f"Resultado: {resultado}")
print("-" * 30)

