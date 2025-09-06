#55
while True:
    numero = float(input("Digite um número maior que 100: "))
    if numero > 100:
        print("Número válido inserido. Encerrando o programa.")
        break
    else:
        print("Número inválido. Tente novamente.")