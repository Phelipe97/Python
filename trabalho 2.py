def ler_numero(minimo, maximo):
    while True:
        try:
            n = int(input(f'Digite um número entre {minimo} e {maximo}: '))
            if minimo <= n <= maximo:
                return n
            else:
                print(f'O número deve estar entre entre {minimo} e {maximo}')
        except ValueError:
            print('Você não digitou um número')


n = ler_numero(10000, 30000)

x = n
total = 0
for peso in range(6, 1, -1):
    x, digito = divmod(x, 10)
    total += digito * peso

print('resultado:')
dv = total % 7
print(f'{n}-{dv}')