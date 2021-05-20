n = int(input('Digite um número inteiro e mostrarei a tabuada dele de 1 a 10:'))
for c in range(1, 11):
    t = n*c
    print('{} x {} = {}'.format(n, c, t))