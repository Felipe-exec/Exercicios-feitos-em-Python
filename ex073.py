brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('''Lista de opções
[ A ] Os 5 primeiros colocados.
[ B ] Os últimos 4 colocados.
[ C ] Todos os times em ordem alfabética.
[ D ] Em que posição está o time do Vasco da Gama.''')
escolha = str(input('Qual é a sua escolha? ')).strip().upper()[0]
if escolha == 'A':
    print(brasileirão[0:5])
elif escolha == 'B':
    print(brasileirão[16:])
elif escolha == 'C':
    print(sorted(brasileirão))
elif escolha == 'D':
    print(brasileirão[14])