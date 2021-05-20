from random import randint
computador = randint(1, 10)
jogador = str(input('''Digite um número entre 1 e 10 para tentar adivinhar qual o número o computador pensou! 
Pressione ENTER para jogar: '''))
s = 0
while not jogador == computador:
    jogador = int(input('Qual número estou pensando? '))
    s += 1
if jogador == computador:
    print('Parabéns! Acertou o número que o pc pensou! Número de erros: {} erros'.format(s))