distância = int(input('Você entrou em um uber e o profissional pergunta a distância em km do ponto de partida ao ponto final, qual é a distância?'))
curta = (0.5)*distância
longa = (0.45)*distância
if distância > 201:
    print('A conta a ser paga é de R${}'.format(longa))
else:
    print('A conta a ser paga é de R${}'.format(curta))