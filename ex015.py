print('Mostrarei o preço a ser pago por um carro que custa R$60,00 por dia e R%0,15 por Km rodado.')
Vc = float(input('Por quantos dias alugou o carro?'))
Vk = float(input('Por quantos Km você rodou?'))
R = Vc*60 + Vk*0.15
print('O total a se pagar é de R${}'.format(R))