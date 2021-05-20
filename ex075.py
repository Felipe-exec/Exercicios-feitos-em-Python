núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Último número: ')))
print('Você digitou os valores {}'.format(núm))
print('O valor 9 apareceu {} vez(es)'.format(núm.count(9)))
if 3 in núm:
    print('A posição em que o foi digitado o primeiro valor 3 foi na posição {}'.format(núm.index(3)))
else:
    print('O número 3 não foi presente nos seus números!')
for n in núm:
    if n % 2 == 0:
        print('Os valores pares é/são {}!'.format(n, end=' '))
print('Fim')