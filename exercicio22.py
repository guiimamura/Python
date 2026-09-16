# Leitura das duas notas do aluno
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

# Cálculo da média aritmética
media = (nota1 + nota2) / 2

# Exibição da média formatada com uma casa decimal
print(f"\nMédia: {media:.1f}")

# Verificação da situação do aluno com base nas faixas
if media < 5.0:
    print("Situação: REPROVADO")
elif media < 7.0:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: APROVADO")

