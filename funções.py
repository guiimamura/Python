# Exercício 1: Validação de Strings e Parâmetros

def valida_string(texto, minimo=1, maximo=100):
  
    comprimento = len(texto)
    
    if minimo <= comprimento <= maximo:
        return True
    else:
        return False

print(valida_string("Python"))                  # True (comprimento 6 está entre 1 e 100)
print(valida_string("Oi", minimo=5))            # False (comprimento 2 é menor que 5)
print(valida_string("Teste", minimo=2, maximo=4)) # False (comprimento 5 é maior que 4)


# Exercício 2: Cálculo de Imposto (Funções com Retorno)

def soma_imposto(taxa_imposto, custo):
    valor_final = custo + (custo * (taxa_imposto / 100))
    return valor_final
custo_usuario = float(input("Digite o custo do item antes do imposto: "))
taxa_usuario = float(input("Digite a taxa de imposto sobre vendas (ex: 10 para 10%): "))

resultado = soma_imposto(taxa_usuario, custo_usuario)
print(f"O valor final do produto com imposto é: {resultado:.2f}")


