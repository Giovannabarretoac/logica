def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for i, linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < 2:
            print("-" * 5)

def jogada_valida(tabuleiro, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == " "

def fazer_jogada(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = jogador

def verificar_vitoria(tabuleiro, jogador):
    linhas = any(all(c == jogador for c in linha) for linha in tabuleiro)
    colunas = any(all(tabuleiro[r][c] == jogador for r in range(3)) for c in range(3))
    diagonal1 = all(tabuleiro[i][i] == jogador for i in range(3))
    diagonal2 = all(tabuleiro[i][2 - i] == jogador for i in range(3))
    return linhas or colunas or diagonal1 or diagonal2

def tabuleiro_cheio(tabuleiro):
    return all(c != " " for linha in tabuleiro for c in linha)

def pedir_jogada(jogador):
    while True:
        try:
            pos = input(f"Jogador {jogador}, digite sua jogada (linha e coluna de 1 a 3, separadas por espaço): ")
            linha, coluna = map(int, pos.strip().split())
            return linha - 1, coluna - 1
        except (ValueError, IndexError):
            print("Entrada inválida! Digite dois números entre 1 e 3 separados por espaço.")

def jogo_da_velha():
    while True:
        tabuleiro = criar_tabuleiro()
        jogador_atual = "X"
        while True:
            mostrar_tabuleiro(tabuleiro)
            linha, coluna = pedir_jogada(jogador_atual)

            if not jogada_valida(tabuleiro, linha, coluna):
                print("Jogada inválida! Essa posição já está ocupada ou fora do tabuleiro.")
                continue

            fazer_jogada(tabuleiro, linha, coluna, jogador_atual)

            if verificar_vitoria(tabuleiro, jogador_atual):
                mostrar_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break

            if tabuleiro_cheio(tabuleiro):
                mostrar_tabuleiro(tabuleiro)
                print("Empate!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != "s":
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    jogo_da_velha()
