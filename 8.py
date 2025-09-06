#8
situacao_civil = input("Informe sua situação civil (solteiro, casado, divorciado, viúvo): ").strip().lower()

if situacao_civil == "solteiro":
    print("Você está solteiro(a).")
elif situacao_civil == "casado":
    print("Você é casado(a)!")
elif situacao_civil == "divorciado":
    print("Você está divorciado(a). Aproveite")
elif situacao_civil == "viúvo":
    print("Foi jogar no vasco.")
else:
    print("Situação civil inválida. Por favor, informe uma das opções indicadas.")