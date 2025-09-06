#67
def exibir_tabuleiro(matriz_jogo):
    print("\n")
    for linha in range(3):
        print(" | ".join(matriz_jogo[linha]))
        if linha < 2:
            print("-" * 9)
    print("\n")

def checar_vitoria(matriz_jogo, simbolo_jogador):
    # Linha
    for linha in matriz_jogo:
        if all(posicao == simbolo_jogador for posicao in linha):
            return True
    # Coluna
    for coluna in range(3):
        if all(matriz_jogo[linha][coluna] == simbolo_jogador for linha in range(3)):
            return True
    # Diagonal
    if all(matriz_jogo[i][i] == simbolo_jogador for i in range(3)):
        return True
    if all(matriz_jogo[i][2 - i] == simbolo_jogador for i in range(3)):
        return True
    return False

def matriz_completa(matriz_jogo):
    return all(all(posicao != " " for posicao in linha) for linha in matriz_jogo)

def iniciar_jogo():
    matriz_jogo = [[" " for _ in range(3)] for _ in range(3)]
    jogador_vez = "X"

    while True:
        exibir_tabuleiro(matriz_jogo)
        try:
            linha_escolhida = int(input(f"Jogador {jogador_vez}, insira a linha (1-3): ")) - 1
            coluna_escolhida = int(input(f"Jogador {jogador_vez}, insira a coluna (1-3): ")) - 1
        except ValueError:
            print("Por favor, insira números válidos entre 1 e 3.")
            continue
        
        if linha_escolhida not in range(3) or coluna_escolhida not in range(3):
            print("Posição inválida! Escolha valores entre 1 e 3.")
            continue
        
        if matriz_jogo[linha_escolhida][coluna_escolhida] != " ":
            print("Essa posição já está ocupada! Tente outra.")
            continue

        matriz_jogo[linha_escolhida][coluna_escolhida] = jogador_vez

        if checar_vitoria(matriz_jogo, jogador_vez):
            exibir_tabuleiro(matriz_jogo)
            print(f"Parabéns! Jogador {jogador_vez} venceu!")
            break

        if matriz_completa(matriz_jogo):
            exibir_tabuleiro(matriz_jogo)
            print("Empate! O tabuleiro está cheio.")
            break

        jogador_vez = "O" if jogador_vez == "X" else "X"

if __name__ == "__main__":
    iniciar_jogo()