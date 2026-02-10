while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            break
        else:
            print("a nota deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")