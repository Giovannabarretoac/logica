#63
valores_lista = []

for contador in range(1, 6):
    valor_entrada = int(input(f"Insira o {contador}º valor: "))
    valores_lista.append(valor_entrada)

soma_total = sum(valores_lista)

print(f"A soma dos valores é: {soma_total}")