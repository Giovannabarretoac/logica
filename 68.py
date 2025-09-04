import re
from datetime import datetime

class Aluno:
    def __init__(self, nome, email, data_nascimento):
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.matricula = Aluno._gerar_matricula()

    @staticmethod
    def _gerar_matricula():
        Aluno._contador_matricula += 1
        return Aluno._contador_matricula

    def __str__(self):
        return (
            f"Matrícula: {self.matricula}\n"
            f"Nome: {self.nome}\n"
            f"E-mail: {self.email}\n"
            f"Data de Nascimento: {self.data_nascimento}\n"
        )

def validar_nome(nome):
    if len(nome.strip()) == 0:
        raise ValueError("Nome não pode ser vazio.")
    return nome.strip()

def validar_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(regex, email):
        raise ValueError("E-mail inválido.")
    return email.strip()

def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida. Use o formato DD/MM/AAAA.")

def buscar_aluno_por_matricula(lista_alunos, matricula):
    for aluno in lista_alunos:
        if aluno.matricula == matricula:
            return aluno
    return None

def cadastrar_aluno(lista_alunos):
    try:
        nome = validar_nome(input("Digite o nome: "))
        email = validar_email(input("Digite o e-mail: "))
        data_nascimento = validar_data(input("Digite a data de nascimento (DD/MM/AAAA): "))
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    aluno = Aluno(nome, email, data_nascimento)
    lista_alunos.append(aluno)
    print(f"Aluno cadastrado com sucesso! Matrícula: {aluno.matricula}")

def atualizar_aluno(lista_alunos):
    try:
        matricula = int(input("Digite a matrícula do aluno que deseja atualizar: "))
    except ValueError:
        print("Matrícula inválida!")
        return
    
    aluno = buscar_aluno_por_matricula(lista_alunos, matricula)
    if aluno is None:
        print("Aluno não encontrado.")
        return
    
    print("O que deseja atualizar?")
    print("1 - Nome")
    print("2 - E-mail")
    print("3 - Data de nascimento")
    opcao = input("Escolha a opção: ")

    try:
        if opcao == "1":
            novo_nome = validar_nome(input("Digite o novo nome: "))
            aluno.nome = novo_nome
        elif opcao == "2":
            novo_email = validar_email(input("Digite o novo e-mail: "))
            aluno.email = novo_email
        elif opcao == "3":
            nova_data = validar_data(input("Digite a nova data de nascimento (DD/MM/AAAA): "))
            aluno.data_nascimento = nova_data
        else:
            print("Opção inválida.")
            return
        print("Dados atualizados com sucesso.")
    except ValueError as e:
        print(f"Erro: {e}")

def excluir_aluno(lista_alunos):
    try:
        matricula = int(input("Digite a matrícula do aluno que deseja excluir: "))
    except ValueError:
        print("Matrícula inválida!")
        return
    
    aluno = buscar_aluno_por_matricula(lista_alunos, matricula)
    if aluno is None:
        print("Aluno não encontrado.")
        return
    
    lista_alunos.remove(aluno)
    print(f"Aluno com matrícula {matricula} excluído com sucesso.")

def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de alunos:")
    for aluno in lista_alunos:
        print("-" * 30)
        print(aluno)
    print("-" * 30)

def mostrar_aluno(lista_alunos):
    try:
        matricula = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida!")
        return
    
    aluno = buscar_aluno_por_matricula(lista_alunos, matricula)
    if aluno is None:
        print("Aluno não encontrado.")
    else:
        print("\nDados do aluno:")
        print(aluno)

def main():
    lista_alunos = []
    while True:
        print("\nMenu:")
        print("1 - Cadastrar aluno")
        print("2 - Atualizar dados do aluno")
        print("3 - Excluir aluno")
        print("4 - Listar todos os alunos")
        print("5 - Mostrar dados de um aluno")
        print("Qualquer outra tecla para sair.")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno(lista_alunos)
        elif opcao == "2":
            atualizar_aluno(lista_alunos)
        elif opcao == "3":
            excluir_aluno(lista_alunos)
        elif opcao == "4":
            listar_alunos(lista_alunos)
        elif opcao == "5":
            mostrar_aluno(lista_alunos)
        else:
            print("Encerrando o sistema.")
            break

if __name__ == "__main__":
    main()
