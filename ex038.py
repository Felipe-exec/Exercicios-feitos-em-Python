print('Escreva 2 números inteiros na tela para que eu possa compará-los.')
n1 = int(input('Número 1:'))
n2 = int(input('Número 2:'))
if n1 > n2:
    print('O número {} é maior que o {}!'.format(n1, n2))
if n1 < n2:
    print('O número {} é maior que o {}!'.format(n2, n1))
if n1 == n2:
    print('O número {} é igualzinho ao {}!'.format(n1, n2))