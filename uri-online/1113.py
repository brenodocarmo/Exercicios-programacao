
while True:

    v = input().split()
    
    x = int(v[0])
    y = int(v[1])

    if x == y:
        break
    
    if x > y:
        print('Decrescente')
    
    if x < y:
        print('Crescente')

