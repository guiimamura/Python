# Leitura do ano inteiro
ano = int(input("Ano: "))

# Verificação da regra utilizando estruturas condicionais
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("Resultado: ANO BISSEXTO")
else:
    print("Resultado: NÃO BISSEXTO")

