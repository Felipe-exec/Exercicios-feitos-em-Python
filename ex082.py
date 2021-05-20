a = list()
b = list()
c = list()
print('Verificarei se seu número é par ou ímpar.')
while True:
    a.append(int(input('Digite um número: ')))
    pergunta = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
for i, v in enumerate(a):
    if v % 2 == 0:
        b.append(v)
    else:
        c.append(v)
sorted(a)
sorted(b)
sorted(c)
print('Todos os números digitados: \033[34m{}\033[m'.format(a))
print('Somente os pares: \033[34m{}\033[m'.format(b))
print('Somente os ímpares: \033[34m{}\033[m'.format(c))