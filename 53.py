#53
numero = int(input("Digite um número para a contagem regressiva: "))

if numero > 0:
    print(f"Contagem regressiva de {numero} até 1:")
    for i in range(numero, 0, -1):
        print(i)
else:
    print("Digite um número inteiro positivo.")