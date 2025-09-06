#65
lista_valores = []

for contador in range(1, 6):
    valor_entrada = int(input(f"Insira o {contador}º valor: "))
    lista_valores.append(valor_entrada)

maior_valor = max(lista_valores)
menor_valor = min(lista_valores)

print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")