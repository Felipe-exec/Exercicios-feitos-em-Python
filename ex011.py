print('calcularei a quantidade a área de sua parede e a quantidade de tinta necessária para pintá-la, sendo que cada litro de tinta pinta 2m^2 de área')
l = float(input('Qual a largura de sua parede?'))
a = float(input('Qual a altura de sua parede?'))
área = l*a
tinta = área//2
print('A área de sua parede é de {} metros e a quantidade de tintas necessárias será de aproximadamente {} latas'.format(área,tinta))
