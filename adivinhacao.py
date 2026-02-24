import random
print('************')
print('****jogo adivinhação*****')
print('*************')

numero_secreto = random.randrange(1,31)
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("tentativa{} de {}".format(rodada,total_tentativas))

while (rodada <= total_tentativas):

    chute_str = input("digite o seu número: ")
    print("seu número é: ", chute_str)

    chute = int(chute_str)

    if(chute< 1 or chute>30):
        print("você deve digitar um número entre 1 e 30! ")
        continue

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