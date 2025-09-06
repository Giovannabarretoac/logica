#1
numero = input("Digite um número de 1 a 3: ")

numeros_extenso = {
    "1": "um",
    "2": "dois",
    "3": "três"
}

if numero in numeros_extenso:
    print(f"O número digitado foi: {numeros_extenso[numero]}")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 3.")