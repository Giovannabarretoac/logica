#36
numero_mes = int(input("Digite um número de 1 a 12: "))

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

if 1 <= numero_mes <= 12:
    print(f"O mês correspondente é: {meses[numero_mes - 1]}")
else:
    print("Número inválido. Por favor, digite um número de 1 a 12.")