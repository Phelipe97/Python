km = int(input('Quatos km foram percorridos ?'))
dias = int(input('Por quatos dias ele foi alugado ?'))

preco= 60 * dias + 0.15 * km
print('km = {}. Dias:{}'.format(km,dias))
print('Valor a ser pago:{}'.format(preco))
