#17
primeiro_numero = float(input("Insira o primeiro número: "))
segundo_numero = float(input("Insira o segundo número: "))

resultado_soma = primeiro_numero + segundo_numero
resultado_subtracao = primeiro_numero - segundo_numero
resultado_multiplicacao = primeiro_numero * segundo_numero

if segundo_numero != 0:
    resultado_divisao = primeiro_numero / segundo_numero
    print(f"Soma: {resultado_soma}")
    print(f"Subtração: {resultado_subtracao}")
    print(f"Multiplicação: {resultado_multiplicacao}")
    print(f"Divisão: {resultado_divisao}")
else:
    print(f"Soma: {resultado_soma}")
    print(f"Subtração: {resultado_subtracao}")
    print(f"Multiplicação: {resultado_multiplicacao}")
    print("Divisão: Erro - divisão por zero não é permitida.")