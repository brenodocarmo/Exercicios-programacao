valores = input().split()
numeros = [float(x) for x in valores]
ordem_inversa = sorted(numeros, reverse=True)

lado_A = ordem_inversa[0]
lado_B = ordem_inversa[1]
lado_C = ordem_inversa[2]

while True:

    if (lado_A >= lado_B + lado_C):
        print('NAO FORMA TRIANGULO')
        break

    if (lado_A**2 == lado_B**2 + lado_C**2):
        print('TRIANGULO RETANGULO')

    if (lado_A**2 > lado_B**2 + lado_C**2):
        print('TRIANGULO OBTUSANGULO')

    if (lado_A**2 < lado_B**2 + lado_C**2):
        print('TRIANGULO ACUTANGULO')

    if (lado_A == lado_B == lado_C):
        print('TRIANGULO EQUILATERO')

    if (lado_A == lado_B != lado_C) or (lado_A == lado_C != lado_B) or (lado_B == lado_C != lado_A):
        print('TRIANGULO ISOSCELES')
    
    break