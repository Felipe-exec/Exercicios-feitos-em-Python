print('\033[34m=\033[m'*30)
print('    10 TERMOS DE UMA P.A.')
print('\033[34m=\033[m'*30)
a1 = int(input('Digite o primeiro termo de sua PA: '))
r = int(input('Digite a razão de sua PA: '))
a10 = a1 + 9*r
for c in range(a1, a10 + r, r):
    print('{}'.format(c), end=' --> ')
print('FIM :)')