
while True:

    v = int(input())

    if v == 0:
        break

    valor = [n for n in range(1, v+1)]

    f = ""
    for i in valor:
        f += str(i) + " "
    print(f[:-1])
