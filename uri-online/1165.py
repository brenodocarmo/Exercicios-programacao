n = int(input())

for i in range(n):
    primo = True
    i = 2
    valor = int(input())
    while i < valor and primo:
        if valor % i == 0:
            primo = False
        i += 1

    if primo:
        print(f"{valor} eh primo")
    else:
        print(f"{valor} nao eh primo")
