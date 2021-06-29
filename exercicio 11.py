A=int(input('digite o 1°lado do triangulo:'))
B=int(input('digite o 2°lado do triangulo:'))
C=int(input('digite o 3°lado do triangulo:'))

if A > 0 and B > 0 and C > 0:
    if (A+B>C) and (A+C>B) and (B+C>A):
    #Se voce chegou ate aqui e porque o tringulo e valodo !
     if A!=B and A!=C and B!=C:
         print('triangulo escaleno!')
     else:
         if A == B and A == C and B == C :
             print('triangulo equilatero!')
         else:
             print('triangulo isoceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triangulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triangulo')