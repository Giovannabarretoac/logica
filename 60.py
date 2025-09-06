#60
numero = int(input("Digite um número inteiro positivo: "))

if numero > 0:
    print(f"Divisores de {numero}:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
else:
    print("Por favor, digite um número inteiro positivo.")