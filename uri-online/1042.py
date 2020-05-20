valores = input().split()

crescente = [int(i) for i in valores]

for x in sorted(crescente):
    print(x)

print()

for x in valores:
    print(x)