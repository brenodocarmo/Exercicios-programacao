
v1, v2 = input().split()

x = int(v1)
y = int(v2) + 1
p = y


# valor = [str(x) for x in range(1, y)]
cont = 1

for v in range(1, int(y/x) + 1):
    text = ''

    for i in range(x):
        text += str(cont) + ''
        cont += 1
    print(text)
