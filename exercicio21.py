# Leitura das duas notas do aluno
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

# Cálculo da média aritmética
media = (nota1 + nota2) / 2

# Exibição da média formatada com uma casa decimal
print(f"\nMédia: {media:.1f}")

# Estrutura condicional para verificar a situação do aluno
if media >= 7.0:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")

