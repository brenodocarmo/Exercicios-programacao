
valor = int(input())

for v in range(valor):
    n = input().split()

    x = int(n[0])
    y = int(n[1])

    if y == 0:
        print('divisao impossivel')
    else:
        print('{}'.format(x/y))
