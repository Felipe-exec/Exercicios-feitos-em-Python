from random import randint
total = s = 0
while True:
    pi = str(input('Você quer par ou ímpar?[P/I] ')).strip().upper()[0]
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    if pi == 'P' and total % 2 == 0:
        print('Você ganhou uma rodada!')
        s += 1
    elif pi == 'I' and total % 3 == 0:
        print('Você ganhou uma rodada!')
        s += 1
    else:
        print(f'Você perdeu e seu total de acertos foi {s}.')
        break