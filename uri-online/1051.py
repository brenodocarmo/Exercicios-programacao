# Isento [ 0 - 2000 ]
# salario = 3002.00 - 2000 = 1002.00
#  salario = 4520.00 - 4500 = 28 % 20.00 + 0.08 * 1000 + 0.18 * 1500


valor = float(input())

if valor <= 2000.00:
    print('Isento')
elif 2000.01 <= valor <= 3000:
    # p1 = valor - 2000.0
    result = (valor - 2000.00) * 0.08
    print(f'R$ {result:0.2f}')
elif 3000.01 <= valor <= 4500:
    # p1 = 1000
    # p2 = valor - 3000.0
    result = (1000 * 0.08) + (valor - 3000) * 0.18
    print(f'R$ {result:0.2f}')

else:
    # p1 = 1000
    # p2 = 1500
    # p3 = valor - 4500.0
    result = (1000 * 0.08) + (1500 * 0.18) + (valor - 4500.0) * 0.28
    print(f'R$ {result:0.2f}')
    