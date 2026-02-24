import random

print('************')
print('**** Jogo de Adivinhação *****')
print('*************')

# Escolha do nível de dificuldade
print("Escolha um nível de dificuldade:")
print("1. Fácil")
print("2. Médio")
print("3. Difícil")

nivel = input("Digite o número do nível (1, 2 ou 3): ")

if nivel == "1":
    total_tentativas = 5
    numero_secreto = random.randrange(1, 21)  # Faixa de 1 a 20
elif nivel == "2":
    total_tentativas = 3
    numero_secreto = random.randrange(1, 31)  # Faixa de 1 a 30
elif nivel == "3":
    total_tentativas = 1
    numero_secreto = random.randrange(1, 51)  # Faixa de 1 a 50
else:
    print("Opção inválida. O nível será definido como 'Médio'.")
    total_tentativas = 3
    numero_secreto = random.randrange(1, 31)

print(f"Nível escolhido: {nivel}")
print(f"O número secreto foi definido. Você tem {total_tentativas} tentativas.")

# Iniciar o loop de tentativas
for rodada in range(1, total_tentativas + 1):
    print(f"Tentativa {rodada} de {total_tentativas}")

    # Obter o chute do jogador com verificação de entrada
    while True:
        try:
            chute_str = input(f"Digite um número entre 1 e {numero_secreto}: ")
            chute = int(chute_str)
            if 1 <= chute <= numero_secreto:
                break
            else:
                print(f"Você deve digitar um número entre 1 e {numero_secreto}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

    print(f"Seu número é: {chute}")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!!")
        break  # Sai do loop, jogo terminado
    else:
        if maior:
            print("O seu chute foi maior que o número secreto.")
        elif menor:
            print("O seu chute foi menor que o número secreto.")

# Fim do jogo
if not acertou:
    print(f"Você não acertou! O número secreto era {numero_secreto}.")
print("Fim de jogo!")