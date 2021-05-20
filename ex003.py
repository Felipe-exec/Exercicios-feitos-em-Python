n1 = int(input('\033[0;32mDigite um número:\033[m'))
n2 = int(input('\033[0;33mDigite outro número:\033[m'))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} é {}{}{}!!'.format('\033[0;32m', n1,'\033[m','\033[0;33m', n2, '\033[m','\033[36m', s, '\033[m'))
