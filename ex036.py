print('Aprovarei seu empréstimo bancário se as informações baterem corretamente.')
casa = int(input('Qual o valor da casa?'))
salário = int(input('Qual o salário que você recebe?'))
anos = int(input('Em quantos anos você vai pagar?'))
prestação = casa / (anos * 12)
porcentagem = (salário*(30/100))
print('Para financiar esta casa de {:.2f} reais em {} anos'.format(casa, anos))
print('Será uma prestação de {:.2f} reais'.format(prestação))
if prestação > porcentagem:
    print('Você não pode comprar esta casa amigo.')
else:
    print('Você pode comprar esta casa.')