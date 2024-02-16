import random
import os

continuar= 0
tentativas= 0
num_sorteio= random.randint(1,100)


print('Bem-vindo ao jogo de Advinhar o número.')
print('Escolha um número entro 1 e 10 e tenta acertar o número sorteado.')
num_jogador=int(input('Escolha seu número: '))
while num_sorteio != num_jogador:
    os.system('cls') 
    if num_jogador > num_sorteio:
        print('Errou!!! O número é menor.')
    elif num_jogador < num_sorteio:
        print('Errou!!! O número é maior.')
    tentativas+=1
    num_jogador=int(input('Escolha seu número: '))
print(f'Acertou Parabéns, o número sorteado foi {num_sorteio}, você acertou em {tentativas+1} tentativas.') 
    