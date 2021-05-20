a1 = int(input('Digite o primeiro número de sua P.A.: '))
r = int(input('Digite a razão de sua P.A.: '))
cont = 1
while cont <= 10:
    print('{} --> '.format(a1), end='')
    a1 += r
    cont += 1
pergunta = int(input('Você quer mais termos? Se sim, até qual termo? '))
while cont <= pergunta:
    print('{} --> '.format(a1), end='  ')
    a1 += r
    cont += 1
print('FIM')
