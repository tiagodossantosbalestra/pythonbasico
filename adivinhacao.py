import random

# O computador escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
acertou = False

print("🎯 Bem-vindo ao Jogo da Adivinhação!")
print("Estou pensando em um número entre 1 e 100...")

while not acertou:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("🔼 Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("🔽 Muito alto! Tente novamente.")
    else:
        acertou = True
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")

print("Fim de jogo!")