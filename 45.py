#45
lista_valores = []

for contador in range(1, 6):
    valor_entrada = int(input(f"Insira o {contador}º valor: "))
    lista_valores.append(valor_entrada)

maior_valor = max(lista_valores)

print(f"O maior valor inserido foi: {maior_valor}")