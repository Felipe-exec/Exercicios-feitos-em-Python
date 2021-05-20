print('Formulário 2021')
s = 0
for c in range(1, 8):
    ano = int(input('Em que ano a pessoa {} nasceu?'.format(c)))
    if ano < 2000:
        print('Esta pessoa é maior de idade.')
        s += 1
    else:
        print('Esta pessoa é menor de idade.')
print('O número de pessoas maiores de idade é: {}'.format(s))