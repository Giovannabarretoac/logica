#64
import random

valores_aleatorios = [random.randint(1, 100) for _ in range(10)]

print("Lista completa:", valores_aleatorios)

multiplos_tres = [valor for valor in valores_aleatorios if valor % 3 == 0]

print("Valores múltiplos de 3:", multiplos_tres)