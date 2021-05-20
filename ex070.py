preçototal = preço1000 = cont = menor = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    produto = float(input('Qual é o preço do produto? R$'))
    cont += 1
    if cont == 1:
        menor = produto
        barato = produto
    else:
        if produto < menor:
            menor = produto
            barato = produto
    preçototal += produto
    if produto > 1000:
        preço1000 += 1
    pergunta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if pergunta == 'N':
        break
print('Fim do programa.')
print(f'O total da compra foi R${preçototal:.2f}')
print(f'Os produtos com mais de R$1000,00 são {preço1000}')
print(f'O produto mais barato custa R${menor:.2f} e o nome dele é {barato}')