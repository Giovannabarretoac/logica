#3
codigo_dia = input("Insira um código de 1 a 7 (onde 1 = Domingo, 2 = Segunda, ..., 7 = Sábado): ")

mapeamento_dias = {
    "1": "Domingo",
    "2": "Segunda-feira",
    "3": "Terça-feira",
    "4": "Quarta-feira",
    "5": "Quinta-feira",
    "6": "Sexta-feira",
    "7": "Sábado"
}

if codigo_dia in mapeamento_dias:
    print(f"O dia correspondente é: {mapeamento_dias[codigo_dia]}")
else:
    print("Código inválido. Por favor, insira um código de 1 a 7.")