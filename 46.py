#46
soma_total = 0

for contador in range(1, 11):
    valor_entrada = float(input(f"Insira o {contador}º valor: "))
    soma_total += valor_entrada

media_calculada = soma_total / 10

print(f"A média dos valores inseridos é: {media_calculada:.2f}")