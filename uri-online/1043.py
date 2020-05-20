a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if (a + b > c) and (b + c > a) and (a + c > b):
    perimetro_triangulo = a+b+c
    print('Perimetro = {:.1f}'.format(perimetro_triangulo))
else:
    area_trapezio = ((a+b)*c) / 2
    print('Area = {:.1f}'.format(area_trapezio))
