#42
total_soma = 0

for contador in range(1, 6):
    valor_entrada = int(input(f"Insira o {contador}º valor inteiro: "))
    total_soma += valor_entrada

print(f"A soma dos 5 valores é: {total_soma}")