# Leitura dos três lados
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# Verificação da condição de existência do triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    # Classificação do triângulo
    if a == b == c:
        print("EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("NÃO FORMA TRIÂNGULO")

