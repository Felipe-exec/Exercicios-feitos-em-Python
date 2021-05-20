from random import randint
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('''Escolhas
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? 0, 1 ou 2 ?'))
print('O jogador jogou {} e o computador jogou {}'.format(itens[jogador], itens[pc]))
if pc == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Ganhaste!')
    elif jogador == 2:
        print('Perdeste!')
elif pc == 1:
    if jogador == 0:
        print('Perdeste!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Ganhaste!')
elif pc == 2:
    if jogador == 0:
        print('Ganhaste!')
    elif jogador == 1:
        print('Perdeste!')
    elif jogador == 2:
        print('Empate!')
else:
    print('Resposta inválida.')