import random
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str(input('Digite o aluno 2:'))
a3 = str(input('Aluno 3:'))
a4 = str(input('Aluno 4:'))
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))