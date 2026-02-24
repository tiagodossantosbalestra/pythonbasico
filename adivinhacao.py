import random
print('************')
print('****jogo adivinhação*****')
print('*************')

numero_secreto = random.randrange(1,31)
total_tentativas=3
rodada = 1

while (rodada <= total_tentativas):

    chute_str = input("digite o seu número: ")
    print("seu número é: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("você Acertou!! ")
        break
    else:
        if(maior):
            print("o seuchute foi maior que o numero secreto")
        elif(menor):
            print("o seu chute foi menor que o numero secreto")
    rodada = rodada +1

print("fim de jogo!")