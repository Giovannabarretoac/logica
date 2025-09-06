#41
limite_superior = int(input("Insira um valor inteiro positivo: "))

if limite_superior > 0:
    print("Valores de 1 até", limite_superior)
    for contador in range(1, limite_superior + 1):
        print(contador)
else:
    print("Valor inválido. Por favor, insira um valor inteiro positivo.")