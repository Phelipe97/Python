palavras=('goku','gohan','piccolo','vegeta','kurilin')

for palavra in palavras:
    print('\npalavra:{}.vogais:'.format(palavra.upper()),end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='')
