from random import randint
computador = randint(0, 10)
print('Sou seu PC mermão! Pensei em um número entre 0 e 10!')
print('Você consegue adivinhar?')
acertou = False
s = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    s += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS!! CABEÇA DE BAGRE...')
        elif jogador > computador:
            print('MENOS BURRÃO...')
print('Acertouuu! Teve {} palpites!'.format(s))