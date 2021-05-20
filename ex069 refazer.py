tot18 = totm = tot20 = p = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F]')).upper().strip()[0]
        if sexo == 'M':
            totm += 1
    if idade < 20 and sexo == 'F':
        tot20 += 1
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    p += 1
    if pergunta == 'N':
        break
print(f'Você registrou {p} pessoas.')
print(f'{tot18} pessoas são maiores de idade.')
print(f'{totm} são homens cadastrados.')
print(f'{tot20} são mulheres com menos de 20 anos cadastradas.')