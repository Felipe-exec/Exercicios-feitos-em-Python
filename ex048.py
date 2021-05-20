soma = 0
for c in range(1, 498, 2):
    if c % 3 == 0:
        soma += c
print('A soma entre todos os valores solicitados é {}'.format(soma))
print(sum(range(3, 500, 6)))