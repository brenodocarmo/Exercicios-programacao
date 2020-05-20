# Empacota os valores inseridos
valor = input().split()

# Desempacotando os valores
cod_x = float(valor[0])
cod_y = float(valor[1])


if cod_x == 0.0 and cod_y == 0.0:
    print('Origem')

elif cod_x > 0.0 and cod_y > 0.0: # Q1
    print('Q1')

elif cod_x < 0.0 and cod_y > 0.0: # Q2
    print('Q2')

elif cod_x < 0.0 and cod_y < 0.0: # Q3
    print('Q3')

elif cod_x > 0.0 and cod_y < 0.0: # Q4
    print('Q4')

elif cod_x == 0.0 and cod_y != 0.0:
    print('Eixo Y')

elif cod_x != 0.0 and cod_y == 0.0:
    print('Eixo X')
