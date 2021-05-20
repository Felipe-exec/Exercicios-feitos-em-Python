temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 30)
print('Ao todo, você cadastrou {} pessoas.'.format(len(princ)))
print('O maior peso foi de {}Kg'.format(mai))
for p in princ:
    if p[1] == mai:
        print('O mais pesado é: {}'.format(p[0]))
print('O menor peso foi de {}Kg'.format(men))
for p in princ:
    if p[1] == men:
        print('O menos pesado é: {}'.format(p[0]))