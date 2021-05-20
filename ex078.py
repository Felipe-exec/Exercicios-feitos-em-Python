números = list()
n = 0
for c in range(1, 6):
    n = int(input('Digite o {} valor: '.format(c)))
    if n not in números:
        números.append(n)
    else:
        print('Você já digitou esse número!')
print('O maior valor digitado foi: {}'.format(max(números)))
print('O menor valor digitado foi: {}'.format(min(números)))