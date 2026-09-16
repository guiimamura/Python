# Leitura dos dados de entrada
preco = float(input("Preço: R$ "))
opcao = int(input("Opção: "))

# Estrutura condicional para aplicar o desconto ou acréscimo
if opcao == 1:
    # Dinheiro ou Pix: 10% de desconto
    valor_final = preco * 0.90
elif opcao == 2:
    # Débito: 5% de desconto
    valor_final = preco * 0.95
elif opcao == 3:
    # Crédito à vista: Sem alteração
    valor_final = preco
elif opcao == 4:
    # Crédito parcelado: 8% de acréscimo
    valor_final = preco * 1.08
else:
    print("Opção inválida!")
    valor_final = None

# Exibição do resultado se a opção for válida
if valor_final is not None:
    print(f"Valor Final: R$ {valor_final:.2f}")

