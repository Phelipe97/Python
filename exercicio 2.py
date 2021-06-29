d=int(input('quantos dias?'))
h=int(input('quantas horas?'))
m=int(input('quantos minutos?'))
s=int(input('quantos segundos'))

total=s+(m*60)+(h*60*60)+(d*24*60*60)

resp='o total de segundos calculados é de {}.'.format(total)
print(resp)