n = c = mul = 0
while True:
    if n < 0:
        break
    n = int(input('Digite o número que você deseja ver a tabuada: '))
    for c in range(1, 11):
        mul = n*c
        print(f'{n} x {c} = {mul}')
print('Acabo')