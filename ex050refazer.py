s = 0
for c in range(1, 7):
    n = int(input('Digite o {} número inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
        print('A soma dos valores pares até agora: {}'.format(s))
    else:
        print('Este é um número ímpar!')
print('O total de números pares somados é {}'.format(s))