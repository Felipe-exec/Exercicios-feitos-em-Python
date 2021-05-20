palavras = ('chinelo', 'celular', 'caneca', 'chocalho', 'vara de pescar',
         'machucado', 'morango')
for palavra in palavras:
    print('\nNa palavra \033[32m{}\033[m temos '.format(palavra), end='')
    for letras in palavra:
        if letras in 'aeiou':
            print('\033[36m{}\033[m'.format(letras), end=' ')