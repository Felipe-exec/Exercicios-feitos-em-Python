from time import sleep
print('Bem vindo ao aumentador de salários!')
sleep(1)
print('carregando..')
sleep(2)
cash = float(input('Digite quanto recebe um funcionário:'))
if cash >= 1250:
    c1 = cash*(115/100)
    print('O novo salário com 15% é {}'.format(c1))
else:
    c2 = cash*(110/100)
    print('O novo salário com 10% é {}'.format(c2))