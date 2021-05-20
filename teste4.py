tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo'if tempo<=3 else'carro cagado')
nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Felipe':
    print('Que nome maneiro!')
else:
    print('Seu nome é normalzinho, nojento!')
print('Bom dia {}!'.format(nome))