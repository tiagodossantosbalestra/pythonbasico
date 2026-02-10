while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade <= 0:
            print("Idade inválida. Digite um número maior que zero.")
        else:
            print(f"Idade válida: {idade}")
            break

    except ValueError:
        print("Entrada inválida. Digite apenas números.")