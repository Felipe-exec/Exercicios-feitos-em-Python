soma = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
    else:
        print('Este é um número ímpar!')
print('A soma dos números pares é:{} '.format(soma))