
soma = 0
cont = 0

while True:
    nota = float(input())

    if nota >= 0.0 and nota <= 10.0:

        soma += nota
        cont+= 1

        if cont == 2:
            print('media = {:.2f}'.format(soma / cont))
            break

    else:
        print('nota invalida')
