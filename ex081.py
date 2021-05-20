numeros = list()
quantidade = quantidade2 = 0
while True:
    n = int(input('Digite um número: '))
    quantidade += 1
    if n not in numeros:
        numeros.append(n)
        quantidade2 += 1
    else:
        print('Este número já foi adicionado!')
    pergunta = str(input('Você quer continuar?[S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('O total de números digitado por você(mesmo que repetido) foi {}'.format(quantidade))
print('O total de números digitado por você(sem repetir) foi {}'.format(quantidade2))
numeros.sort(reverse=True)
print('Seus números em ordem decrescente são: {}'.format(numeros))
if 5 in numeros:
    print('O número 5 está presente! Ele se encontra na posição {}'.format(numeros.index(5)))
else:
    print('O número 5 não foi digitado! :(')