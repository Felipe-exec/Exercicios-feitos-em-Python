print('Exercício 035 refeito com mais detalhes!')
print('Digite os 3 segmentos de retas para ver o tipo de triângulo que se forma!')
s1 = float(input('Digite o tamanho do segmento 1:'))
s2 = float(input('Digite o segmento 2:'))
s3 = float(input('Digite o segmento 3:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s3:
    print('Você pode formar um triângulo!')
    if s1 == s2 == s3:
        print('Você formou um triângulo de natureza EQUILÁTERO.')
    elif s1 != s2 != s3:
        print('Você formou um triângulo de natureza ESCALENO.')
    else:
        print('Você formou um triângulo de natureza ISÓSCELES.')
else:
    print('Você não pode formar um triângulo!')