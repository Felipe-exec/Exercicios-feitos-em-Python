from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a pessoa {} nasceu? '.format(pessoas)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
        print('Essa pessoa é maior de idade.')
    else:
        totmenor += 1
        print('Essa pessoa é menor de idade.')
print('Ao todo tivemos {} menor de idade e {} maiores de idade.'.format(totmenor, totmaior))