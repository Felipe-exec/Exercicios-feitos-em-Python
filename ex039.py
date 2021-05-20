print('\033[32mALISTAMENTO MILITAR 1.0')
idade = int(input('Quantos anos de vida você tem até a data atual?'))
conta = idade - 18
if idade == 18:
    print('Você está apto ao alistamento militar! Verifique a Junta Militar mais próxima.')
elif idade < 18:
    print('Você não está apto para o serviço militar este ano, aliste-se já na Junta Militar mais próxima.')
elif idade > 18:
    print('O seu alistamento está atrasado em {} anos ou já passou, por favor, verifique na Junta Militar mais próxima sobre seu estado atual.'.format(conta))