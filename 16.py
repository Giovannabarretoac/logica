#16
tipo_combustivel = input("Selecione o tipo de combustível (gasolina, etanol, diesel): ").strip()

valores_combustivel = {
    "gasolina": 5.79,
    "etanol": 4.29,
    "diesel": 6.39
}

if tipo_combustivel in valores_combustivel:
    print(f"O preço do {tipo_combustivel} é R$ {valores_combustivel[tipo_combustivel]:.2f} por litro.")
else:
    print("Tipo de combustível inválido. Tente novamente.")