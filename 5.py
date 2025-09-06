#5
valor_a = int(input("Insira o primeiro valor: "))
valor_b = int(input("Insira o segundo valor: "))

if valor_a % 2 == 0 and valor_b % 2 == 0:
    print("Ambos os valores são pares.")
else:
    print("Pelo menos um dos valores não é par.")