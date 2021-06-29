nome = input('Qual o seu Nome?:')
peso = float(input('Qual o seu Peso?:'))


if peso <= 65:
    categoria = 'Pena'
elif peso > 65 and peso < 72:
    categoria = 'Leve'
elif peso > 72 and peso < 79:
    categoria = 'Ligeiro'
elif peso > 79 and peso < 86:
    categoria = 'Meio medio'
elif peso > 86 and peso < 93:
    categoria = 'Medio'
elif peso > 93 and peso < 100:
    categoria = 'Meio pesado'
elif peso > 100:
    categoria = 'Pesado'

print('O lutador {} pesa {} kg se enquadra na categoria {}'.format(nome, peso,categoria))


