#56
quantidade = int(input("Quantas vezes deseja exibir a mensagem? "))
mensagem = input("Digite a mensagem: ")

contador = 0

while contador < quantidade:
    print(f"{contador + 1}: {mensagem}")
    contador += 1