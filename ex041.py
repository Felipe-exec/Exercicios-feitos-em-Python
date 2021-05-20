from time import sleep
print('-=-'*20)
print('\033[34mConfederação Nacional de Natação.\033[m')
print('-=-'*20)
sleep(2)
print('\033[34mBem-Vindo! Responda a pergunta abaixo\033[m')
sleep(1)
ano = int(input('\033[34mDigite seu ano de nascimento:\033[m'))
idade = 2021 - ano
if idade <= 9:
    print('\033[34mVocê é o time MIRIM de atletas!\033[m')
elif 9 < idade < 14:
    print('\033[34mVocê é do time INFANTIL de atletas!\033[m')
elif 14 < idade < 19:
    print('\033[34mVocê é do time JUNIOR de atletas!\033[m')
elif 19 < idade < 20:
    print('\033[34mVocê pertence ao time SÊNIOR de atletas!\033[m')
elif idade >= 20:
    print('\033[34mVocê é do time Master da Confederação.\033[m')
print('Compareça na confederação entre as datas 26/02 e 04/03 para pegar seu certificado e começar os treinos em 16/03.\033[m]')