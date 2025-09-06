#44
valores_pares = []

for contador in range(1, 11):
    valor_entrada = int(input(f"Insira o {contador}º valor: "))
    if valor_entrada % 2 == 0:
        valores_pares.append(valor_entrada)

print("Valores pares inseridos:")
for valor_par in valores_pares:
    print(valor_par)