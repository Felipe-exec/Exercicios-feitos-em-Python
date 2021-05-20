print('--|Detector de palíndromo|--')
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto), -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('Palíndromo.')
else:
    print('Não é um palíndromo.')