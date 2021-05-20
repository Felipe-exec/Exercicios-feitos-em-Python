from time import sleep
print('Os forgos vão estourar na contagem regressiva de 10 segundos!')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('AEEEEEEEE!!! \033[31mROJÃO!')