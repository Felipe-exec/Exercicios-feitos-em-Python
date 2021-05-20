import random
a1 = str(input('Digite o nome de um aluno:'))
a2 = str(input('Digite o aluno 2:'))
a3 = str(input('Aluno 3:'))
a4 = str(input('Aluno 4:'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O escolhido para limpar um quadro foi: {}'.format(escolhido))
