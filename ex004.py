a = input('\033[4;35mDigite algo:\033[m').strip()
print('O tipo primitivo desse valor é', '\033[36m', a.__class__, '\033[m')
print('Só tem espaços?', '\033[36m', a.isspace(), '\033[m')
print('É um número?','\033[36m', a.isnumeric(), '\033[m')
print('É alfabético?', '\033[36m', a.isalpha(), '\033[m')
print('Está em maiúsculas?','\033[36m', a.isupper(), '\033[m')
print('Está em minúsculas?','\033[36m', a.islower(), '\033[m')
print('Está capitalizada?', '\033[36m', a.istitle(), '\033[m')