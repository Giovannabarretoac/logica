#59
while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if num1 > num2:
        print("O primeiro número é maior que o segundo. Encerrando o programa.")
        break
    else:
        print("O primeiro número não é maior que o segundo. Tente novamente.")