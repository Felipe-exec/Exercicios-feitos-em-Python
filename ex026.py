frase = str(input('Digite uma frase:')).strip().lower()
print('Existem {} letras "a"'.format(frase.count('a')))
print('A letra a aparece pela primeira vez na posição {}'.format(frase.find('a')))
print('A letra a aparece pela última vez em {}'.format(frase.rfind('a')))