preco = float(input('digite o preço do produto:'))
p = float(input('digite o percentual de desconto(0-100):'))

desconto = preco*(p/100)
final = preco - desconto

print('o preço do produto é {}. Desconto de {}%.'.format(preco , p))
print('valor calculado do desconto: {}. valor final do produto: {}'.format(desconto , final))