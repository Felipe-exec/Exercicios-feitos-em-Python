from random import randint
from time import sleep
print('\033[35m-=-'*20)
print('Jokenpô')
print('-=-'*20)
sleep(1)
itens = ('Pedra', 'Tesoura', 'Papel')
computador = randint(0,2)
print('''\033[m\033[36mSuas opções:
[ 0 ] Pedra
[ 1 ] Tesoura
[ 2 ] Papel\033[m''')
jogador = int(input('\033[33mQual é a sua jogada?\033[m'))
print('-=-'*10)
print('\033[31mO computador jogou {}\033[m'.format(itens[computador]))
print('\033[36mO jogador jogou {}\033[m'.format(itens[jogador]))
print('-=-'*10)
print('\033[35mCarregando resposta...\033[m')
sleep(2)
if computador == 0:            #Computador jogar PEDRA
    if jogador == 0:
        print('Empate! \033[31maaaaaaaaaaaaaaffff!\033[m')
    elif jogador == 1:
        print('O jogador perdeu! \033[31mhaha!\033[m]')
    elif jogador == 2:
        print('O jogador venceu! \033[31mque saco.\033[m')
    else:
        print('JOGADA INVÁLIDA.')
elif computador == 1:              #Computador jogar TESOURA
    if jogador == 0:
        print('O jogador venceu! \033[31mporcaria...\033[m')
    elif jogador == 1:
        print('Deu empate! \033[31mque maluquice..\033[m')
    elif jogador == 3:
        print('O jogador perdeu! \033[31mnão fica triste, você é ruim, não é culpa sua :P\033[m')
    else:
        print('JOGADA INVÁLIDA.')
elif computador == 2:                  #Computador jogar PAPEL
    if jogador == 0:
        print('O jogador perdeu! \033[31mé, nada mudou, virou freguês do computador!\033[m')
    elif jogador == 1:
        print('O jogador venceu! \033[31mai ai... que mentira.\033[m')
    elif jogador == 2:
        print('Mas que empate! \033[31mimpossível ter dado empate... eu calculei minha vitória certinha..\033[m')
    else:
        print('JOGADA INVÁLIDA.')