while true:
    try:
        valor = float(input("Digite o valor do saque: r$ "))

        if valor <=0:
            print("O valor deve ser maior que zero.")
        elif valor > 1000:
             print("Saque não permitido. O limite é R$ 1000.")
        else:
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
           break

    except ValueError:
       print("Entrada inválida. Digite apenas números.")

