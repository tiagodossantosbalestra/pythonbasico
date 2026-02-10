while True:
    usuario = input("Digite o usuário: ").strip()

    if usuario == "":
        print("Usuário não pode ser vazio.")
    else:
        break

while True:
    senha = input("Digite a senha: ")

    if len(senha) < 6:
        print("A senha deve ter no mínimo 6 caracteres.")
    else:
        break

print("Login cadastrado com sucesso!")