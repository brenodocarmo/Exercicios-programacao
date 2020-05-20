
x = int(input())
y = int(input())

cont = 0

if x == y:
    print(cont)

elif x > y:
    for i in range(x-1, y , -1):
        if i % 2 == 1:
            cont += i
    print(cont)

elif x < y:
    for i in range(x+1, y, 1):
        if i % 2 == 1:
            cont += i
    print(cont)




