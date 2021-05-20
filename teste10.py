num = [2, 5, 9, 1]
num[2] = 4                       #substituir um número.
num.append(7)                      #adicionar valor no final.
num.sort(reverse=True)               #colocar em ordem ou ordem reversa.
num.insert(2, 2)                  #adicionar um valor no meio.
num.pop()                #eliminar valor.
if 5 in num:
    num.remove(5)                 #eliminar o primeiro valor que você escolheu, em ordem.
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
valores = list()
valores.append(1)
valores.append(2)
valores.append(3)
valores.append('Vaaai!')

for c, v in enumerate(valores):
    print('Na posição {} encontrei o valor {}'.format(c, v))
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:]           #Cópia de a