import sys
print('Bem-vindo a calculadora maluca 3.0!')
print('''Você terá diversas opções para utilizar!
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] QUAL É O MAIOR VALOR DENTRE OS 2 NÚMEROS DIGITADOS?
[ 4 ] ARREPENDIDO DE SEUS NÚMEROS? DIGITE DE NOVO!
[ 5 ] SAIR DO PROGRAMA''')
escolheu = False
while not escolheu:
    n1 = float(input('Escolha um valor: '))
    n2 = float(input('Escolha outro valor: '))
    escolha = int(input('Qual é a sua escolha de acordo com o menu acima? '))
    if escolha == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}!'.format(n1, n2, s))
    elif escolha == 2:
        m = n1*n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}!'.format(n1, n2))
        else:
            print('{} é maior que {}!'.format(n2, n1))
    elif escolha == 4:
        print('Digite novamente então!')
    if escolha == 5:
        print('TCHAU! ATÉ MAIS!!')
        sys.exit()