from time import sleep
cores = {'vermelho':'\033[31m'}
sleep(2)
print('{}Tem um carro passando perto do radar amaldiçoado 1.0! Será que ele ultrapassou o limite de velocidade?'.format(cores['vermelho']))
sleep(2)
número = int(input('Qual foi a velocidade dele?'))
if número > 30:
    print('Ele está em alta velocidade!!! VAI SER MULTADO RAPÁ!')
    sleep(2)
    print('A multa será de 80km/h x R$7,00 ou seja...')
    print('Processando...')
    sleep(2)
    print('{} REAIS!!'.format(número*7))
    sleep(1)
    print('Eu sou o radar amaldiçoado! mais um pra conta hehe..')
else:
    print('processando....')
    sleep(2)
    print('A velocidade dele está normal e MUITO BAIXA PARA SER PEGO PELO MEU RADAR AMALDIÇOADO 1.0... que chatice --_')