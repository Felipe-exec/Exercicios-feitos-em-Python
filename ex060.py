from math import factorial
import sys
escolheu = False
while not escolheu:
    escolha = int(input('Escolha um número inteiro para o cálculo de sua fatorial: '))
    fatorial = factorial(escolha)
    print('O fatorial de {} é {}!'.format(escolha, fatorial))
    desejo = str(input('Quer escolher outro número para calcular o fatorial? [Yes/No]')).strip().upper()[0]
    if desejo == 'N':
        sys.exit()