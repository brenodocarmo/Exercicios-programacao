codigo, item = input().split()

codigo = int(codigo)
item = int(item)

if codigo == 1:
    print('Total: R$ {:0.2f}'.format(item * 4))
elif codigo == 2:
    print('Total: R$ {:0.2f}'.format(item * 4.5))
elif codigo == 3:
    print('Total: R$ {:0.2f}'.format(item * 5))
elif codigo == 4:
    print('Total: R$ {:0.2f}'.format(item * 2))
elif codigo == 5:
    print('Total: R$ {:0.2f}'.format(item * 1.5))
