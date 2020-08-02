x = int(input())
y = int(input())

maior = max(x, y)
menor = min(x, y)

mult = 0
for valor in range(menor, maior + 1):
    if valor % 13 != 0:
        mult += valor

print(mult)


for i in a:


