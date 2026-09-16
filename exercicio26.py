# Leitura do salário atual
salario_atual = float(input("Digite o salário atual: "))

# Aplicação das regras da tabela de reajuste
if salario_atual <= 1500.00:
    percentual = 15
elif salario_atual <= 3000.00:
    percentual = 10
else:
    percentual = 5

# Cálculo do valor do aumento e do novo salário
aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + aumento

# Exibição dos resultados solicitados nos requisitos
print(f"Percentual aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

