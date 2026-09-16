# Entrada de dados: lê a idade da pessoa como um número inteiro
idade = int(input("Digite a idade da pessoa: "))

# Estrutura condicional para determinar a categoria de votação
if idade < 16:
    print("NÃO PODE VOTAR")
elif 16 <= idade <= 17:
    print("VOTO OPCIONAL")
elif 18 <= idade <= 69:
    print("VOTO OBRIGATÓRIO")
else:  # Para 70 anos ou mais
    print("VOTO OPCIONAL")

