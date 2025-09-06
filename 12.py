#12
meio_transporte = input("Selecione um meio de transporte (carro, bicicleta, a pé): ").strip()

if meio_transporte == "carro":
    print("Velocidade média: 100 km/h")
elif meio_transporte == "bicicleta":
    print("Velocidade média: 20 km/h")
elif meio_transporte == "a pé":
    print("Velocidade média: 5 km/h")
else:
    print("Meio de transporte inválido.")