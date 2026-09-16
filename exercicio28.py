# Leitura dos três lados
lado_a = float(input("Digite o primeiro lado: "))
lado_b = float(input("Digite o segundo lado: "))
lado_c = float(input("Digite o terceiro lado: "))

# Verificação das três desigualdades triangulares
if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):
    print("Resultado: FORMAM UM TRIÂNGULO")
else:
    print("Resultado: NÃO FORMAM")

