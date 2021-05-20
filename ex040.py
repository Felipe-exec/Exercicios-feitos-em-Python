print('Média de duas notas para alunos do colegial com média mínima de 5.0 1.0')
n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
m = (n1 + n2) /2
if m < 5.0:
    print('\033[31mSua nota é de {}, ou seja, menor que 5.0, reprovado.\033[m'.format(m))
elif 5.0 < m < 6.9:
    print('\033[33mSua nota é de {}, ou seja, você está de recuperação\033[m'.format(m))
elif m >= 7.0:
    print('\033[32mVocê passou! Sua nota é de {}, parabéns!\033[m'.format(m))