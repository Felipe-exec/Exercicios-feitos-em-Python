galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])          #criar cópia anula o dado.clear()
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print('{} é maior de idade.'.format(p[0]))
        totmai += 1
    else:
        print('{} é menor de idade.'.format(p[0]))
        totmen += 1
print('Temos {} maiores de idade e {} menores de idade.'.format(totmai, totmen))