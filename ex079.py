números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        pergunta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if pergunta == 'N':
            break
    else:
        print('Este número já foi adicionado!')
print('Os valores digitados, em ordem crescente, são: {}'.format(sorted(números)))