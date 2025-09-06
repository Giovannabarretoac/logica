#33
preco_produto = float(input("Insira o preço do produto: R$ "))

desconto_aplicado = preco_produto * 0.10
preco_final = preco_produto - desconto_aplicado

print(f"Preço com 10% de desconto: R$ {preco_final:.2f}")