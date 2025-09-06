#26
valor_a = int(input("Insira o primeiro valor: "))
valor_b = int(input("Insira o segundo valor: "))

if valor_a % 5 == 0 and valor_b % 5 == 0:
    print("Ambos os valores são múltiplos de 5.")
else:
    print("Nenhum dos valores são múltiplos de 5.")