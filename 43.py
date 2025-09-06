#43
quantidade_repeticoes = int(input("Quantas vezes você quer que a mensagem seja exibida? "))

texto_mensagem = input("Insira a mensagem que deseja exibir: ")

for iteracao in range(quantidade_repeticoes):
    print(f"{iteracao+1}: {texto_mensagem}")