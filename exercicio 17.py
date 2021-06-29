kwh = float(input('Quantos kwh?'))
tipo= input('qual o tipo de inslatação (R, C ou I)')

if(tipo == 'R'):
    if kwh<=500:
        preço=0.4
    else:
        preço=0.65

elif (tipo == 'C'):
    if kwh<=1000:
        preço=0.55
    else:
        preço=0.6

elif (tipo == 'I'):
    if kwh <= 5000:
        preço = 0.55
    else:
        preço = 0.6

else:
    print('inslação invalida!')

print('Total a pagar:{}'.format(kwh*preço))