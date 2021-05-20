soma = 0
for c in range(3, 498, 2):
    if c % 3 == 0:
        soma += c
        print(c, end=' ')
print(soma)