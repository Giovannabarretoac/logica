#13
numero_mes = int(input("Insira o número do mês (1 a 12): "))

if numero_mes in [12, 1, 2]:
    periodo_ano = "Verão"
elif numero_mes in [3, 4, 5]:
    periodo_ano = "Outono"
elif numero_mes in [6, 7, 8]:
    periodo_ano = "Inverno"
elif numero_mes in [9, 10, 11]:
    periodo_ano = "Primavera"
else:
    periodo_ano = "Mês inválido"

print(f"A estação do ano é: {periodo_ano}")