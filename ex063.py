n = int(input('Quantos termos de fibonacci você quer? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 0
while cont <= n:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    cont += 1
    print(' -> {}'.format(t3), end='')
print(' ->FIM')