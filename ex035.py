print('-=-'*15)
print('Formador de triângulos 1.0')
print('-=-'*15)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Você pode formar triângulos!')
else:
    print('Você não pode formar triângulos!')