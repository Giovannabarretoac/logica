#47
base_tabuada = int(input("Insira um valor para ver a tabuada: "))

print(f"Tabuada do {base_tabuada}:")
for multiplicador in range(1, 11):
    resultado_calculo = base_tabuada * multiplicador
    print(f"{base_tabuada} x {multiplicador} = {resultado_calculo}")