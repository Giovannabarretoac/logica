#49
quantidade_maiores = 0

for iteracao in range(1, 8):
    valor_entrada = float(input(f"Insira o {iteracao}º valor: "))
    if valor_entrada > 10:
        quantidade_maiores += 1

print(f"Quantidade de valores maiores que 10: {quantidade_maiores}")