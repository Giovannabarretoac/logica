# atividade 7
#7
pontuacao = float(input("Insira uma pontuação de 0 a 10: "))

if 0 <= pontuacao < 4:
    nivel = "Baixo"
elif 4 <= pontuacao < 7:
    nivel = "Médio"
elif 7 <= pontuacao <= 10:
    nivel = "Alto"
else:
    nivel = "Pontuação inválida"

print(f"A classificação da pontuação é: {nivel}")