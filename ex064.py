import sys
s = s2 = n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    s += 1
    s2 += n
    if n == 999:
        print('Você digitou {} valores e a soma deles é {}'.format(s - 1, s2 - 999))
        sys.exit()