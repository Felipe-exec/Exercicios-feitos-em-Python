print('Calcularei uma distância escrita por você em metros e transformarei para km, cm e mm.')
n = float(input('Digite a distância:'))
km = n*0.001
cm = n*100
mm = n*1000
print('O valor em km, cm e mm é, respectivamente, {}km, {}cm e {}mm.'.format(km,cm,mm))
