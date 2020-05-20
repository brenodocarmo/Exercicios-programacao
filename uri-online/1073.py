
valor = int(input())
pot = 2
for v in range(1, valor+1):
    if v % 2 == 0:
        print('{}^{} = {}'.format(v, pot, v**pot))
