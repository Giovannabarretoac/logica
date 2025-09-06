#50
limite_inicial = int(input("Insira um valor inteiro positivo: "))

if limite_inicial > 0:
    print(f"Valores de {limite_inicial} até 1 (decrescente):")
    for contador in range(limite_inicial, 0, -1):
        print(contador)
else:
    print("Valor inválido. Por favor, insira um valor inteiro positivo.")