while True:
    print("1- cadastrar")
    print("2- consultar")
    print("3- sair")

    opcao = input("escolha uma opção: ")

    if opcao in ["1","2","3"]:
        break
    else:
        print("opção inválida! - escolha novamente")

print("você escolheu: ",opcao)
    
