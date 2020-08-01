x = int(input())
y = int(input())

maior = max(x, y)
menor = min(x, y)


for valor in range(menor+1, maior):
    if valor % 5 in [2, 3]:
        print(valor)