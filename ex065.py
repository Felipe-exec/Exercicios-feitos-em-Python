s = q = m = maior = menor = 0
resposta = 'S'
while resposta in 'S':
    n = int(input('Digite um número inteiro: '))
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
m = s / n
print('Você digitou {} números e a média foi {}.'.format(q, m))
print('O maior número foi {} e o menor número foi {}.'.format(maior, menor))