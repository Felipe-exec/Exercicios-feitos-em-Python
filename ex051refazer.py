from time import sleep
a1 = int(input('Digite o primeiro termo de sua P.A.: '))
r = int(input('Digite a razão de sua P.A.: '))
a10 = a1 + 9*r
print('Mostrarei os 10 primeiros termos dessa progressão!')
sleep(1)
print('Carregando..')
sleep(2)
for pa in range(a1, a10 + r, r):
    print(pa, end='--> ')
print('Fim :)')