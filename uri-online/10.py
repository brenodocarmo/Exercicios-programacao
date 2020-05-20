valor = float(input())
resultado ='Notas:\n'

mod100 = valor % 100
if (mod100 == valor):
    resultado += '%d nota(s) de R$ 100.00\n' % 0
else:
    resultado += '%d nota(s) de R$ 100.00\n' (valor / 100)

