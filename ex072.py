cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente.')
print('Você digitou o número {}'.format(cont[núm]))
pergunta = str(input('Você quer tentar novamente?[Sim/Não]')).strip().upper()[0]
if pergunta == 'S':
    while True:
        pergunta2 = int(input('Qual número você quer em extenso?[99 para parar.] '))
        if 0 <= pergunta2 <= 20:
            print('Você digitou o número {}'.format(cont[pergunta2]))
        elif pergunta2 == 99:
            print('Volte sempre!')
            break
        else:
            print('Tente novamente.')