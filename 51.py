#51
total_acumulado = 0

while True:
    valor_entrada = float(input("Insira um valor (ou 0 para encerrar): "))
    if valor_entrada == 0:
        break
    total_acumulado += valor_entrada

print(f"A soma dos valores inseridos é: {total_acumulado}")