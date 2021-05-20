print('Adivinhe o número que eu to pensando! Escolha entre 1 e 3')
from random import randint
from time import sleep
computador = randint(0, 3)
print('-=-'*20)
sleep(3)
print('Será que ele irá me vencer? humano ridiculo...')
sleep(3)
print('Não... ele é muito fraco para conseguir...')
sleep(2)
print('-=-'*20)
resposta = int(input('Escolha seu destino:'))
print('Processando...')
sleep(3)
if resposta == computador:
    print('Você me pegou! Maldito!!!!!!')
else:
    print('HAHAHA PODRE! ERROU RIDICULAMENTE...')

