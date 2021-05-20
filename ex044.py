print('Bem-vindo à lojinha maluca 1.0')
produto = float(input('Qual o preço do seu produto?'))
pagamento = float(input('''Qual a sua forma de pagamento?
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] em 3x ou mais no cartão
Sua resposta: '''))
if pagamento == 1:
    valor1 = produto*0.9
    print('O valor a ser pago é {} reais'.format(valor1))
elif pagamento == 2:
    valor2 = produto*0.95
    print('O valor a ser pago é {} reais'.format(valor2))
elif pagamento == 3:
    valor3 = produto/2
    print('Nos próximos dois mêses você terá que pagar os 50 reais, sendo 25 reais para cada mês.')
elif pagamento == 4:
    valor4 = (produto*120/100)
    totparc = int(input('Vai parcelar em quantas vezes?'))
    parcela = valor4*totparc
    print('O valor a ser pago é de {} reais'.format(parcela))
else:
    print('Digite um número válido.')