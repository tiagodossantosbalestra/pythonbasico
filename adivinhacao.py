import random

# Cores no terminal
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
RESET = '\033[0m'

def escolher_nivel():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (10 tentativas)")
    print("2 - Médio (5 tentativas)")
    print("3 - Difícil (3 tentativas)")

    while True:
        nivel = input("Digite o número do nível escolhido: ")
        if nivel == '1':
            return 10
        elif nivel == '2':
            return 5
        elif nivel == '3':
            return 3
        else:
            print(VERMELHO + "Opção inválida. Por favor, escolha um nível válido." + RESET)

def jogar():
    print(AZUL + "************" + RESET)
    print(AZUL + "**** Jogo de Adivinhação *****" + RESET)
    print(AZUL + "*************" + RESET)

    numero_secreto = random.randrange(1, 31)
    total_tentativas = escolher_nivel()
    pontos = 100  # Pontuação inicial
    historico = []  # Para armazenar os chutes anteriores

    for rodada in range(1, total_tentativas + 1):
        print(AZUL + "Tentativa {} de {}".format(rodada, total_tentativas) + RESET)
        print(f"Seu total de pontos: {pontos}")

        chute_str = input("Digite o seu número: ")
        print("Seu número é: ", chute_str)

        chute = int(chute_str)

        if chute < 1 or chute > 30:
            print(AMARELO + "Você deve digitar um número entre 1 e 30!" + RESET)
            continue

        historico.append(chute)

        if chute == numero_secreto:
            print(VERDE + "Você Acertou!!" + RESET)
            break
        else:
            if chute > numero_secreto:
                print(AMARELO + "O seu chute foi maior que o número secreto." + RESET)
            elif chute < numero_secreto:
                print(AMARELO + "O seu chute foi menor que o número secreto." + RESET)

            # Subtraindo pontos para cada tentativa errada
            pontos -= 10

    # Fim do jogo
    print(f"\nFim de jogo! O número secreto era {numero_secreto}.")
    print(f"Seus chutes foram: {historico}")
    print(f"Você terminou com {pontos} pontos.")

# Chama a função principal para jogar
jogar()