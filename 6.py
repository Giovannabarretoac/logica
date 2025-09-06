#6
tipo_operacao = input("Selecione a operação (+, -, *, /): ").strip()

primeiro_valor = float(input("Insira o primeiro valor: "))
segundo_valor = float(input("Insira o segundo valor: "))

if tipo_operacao == "+":
    resultado_final = primeiro_valor + segundo_valor
elif tipo_operacao == "-":
    resultado_final = primeiro_valor - segundo_valor
elif tipo_operacao == "*":
    resultado_final = primeiro_valor * segundo_valor
elif tipo_operacao == "/":
    if segundo_valor != 0:
        resultado_final = primeiro_valor / segundo_valor
    else:
        resultado_final = "Erro: Divisão por zero não é permitida."
else:
    resultado_final = "Operação inválida."

print(f"Resultado: {resultado_final}")