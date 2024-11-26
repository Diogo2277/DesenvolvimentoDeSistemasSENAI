letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'p' in letras:
        print('PARABÉNS VOÇÊ ACHOU UMA DAS LETRAS')
        break

print('TENTE NOVAMENTE')
print(f'Palavras tentadas: {letras}')