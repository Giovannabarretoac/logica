#66
lista_cadastros = []

def cadastrar_pessoa():
    nome_pessoa = input("Insira o nome para cadastrar: ").strip()
    lista_cadastros.append(nome_pessoa)
    print(f"Nome '{nome_pessoa}' cadastrado com sucesso.")

def atualizar_pessoa():
    if not lista_cadastros:
        print("Nenhum nome cadastrado para atualizar.")
        return
    listar_pessoas()
    nome_antigo = input("Insira o nome que deseja atualizar: ").strip()
    if nome_antigo in lista_cadastros:
        novo_nome = input("Insira o novo nome: ").strip()
        indice = lista_cadastros.index(nome_antigo)
        lista_cadastros[indice] = novo_nome
        print(f"Nome '{nome_antigo}' atualizado para '{novo_nome}'.")
    else:
        print(f"Nome '{nome_antigo}' não encontrado.")

def excluir_pessoa():
    if not lista_cadastros:
        print("Nenhum nome cadastrado para excluir.")
        return
    listar_pessoas()
    nome_remover = input("Insira o nome que deseja excluir: ").strip()
    if nome_remover in lista_cadastros:
        lista_cadastros.remove(nome_remover)
        print(f"Nome '{nome_remover}' excluído com sucesso.")
    else:
        print(f"Nome '{nome_remover}' não encontrado.")

def listar_pessoas():
    if not lista_cadastros:
        print("Nenhum nome cadastrado.")
    else:
        print("Nomes cadastrados:")
        for i, nome in enumerate(lista_cadastros, start=1):
            print(f"{i}. {nome}")

while True:
    print("\nMenu:")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar todos os cadastrados")
    print("Qualquer outra tecla para sair.")
    
    opcao_escolhida = input("Escolha uma opção: ").strip()
    
    if opcao_escolhida == '1':
        cadastrar_pessoa()
    elif opcao_escolhida == '2':
        atualizar_pessoa()
    elif opcao_escolhida == '3':
        excluir_pessoa()
    elif opcao_escolhida == '4':
        listar_pessoas()
    else:
        print("Encerrando o programa.")
        break
    
    continuar_operacao = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if continuar_operacao != 's':
        print("Encerrando o programa.")
        break