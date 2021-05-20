produtosepreços = ('leite', 5,
                   'doritos', 4,
                   'pastel', 5.50,
                   'hamburguer', 10,
                   'suco', 7,
                   'esfiha', 3.70,
                   'coxinha', 3.50)
print('-'*20)
print('LISTAGEM DE PREÇOS')
print('-'*20)
for pos in range(0, len(produtosepreços)):
    if pos % 2 == 0:
        print(f'{produtosepreços[pos]:.<30}', end='')
    else:
        print(f'R${produtosepreços[pos]:4.2f}')