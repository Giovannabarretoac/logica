#52
while True:
    senha_usuario = input("Insira a senha: ")
    if senha_usuario == "1234":
        print("Senha correta. Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")