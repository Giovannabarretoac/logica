#57
import random

numero_secreto = random.randint(1, 10)

palpite = None

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número secreto (entre 1 e 10): "))
    if palpite != numero_secreto:
        print("Errado! Tente novamente.")

print("Parabéns! Você adivinhou o número corretamente!")