


n = int(input())
valor = []

# Primeira forma
for i in range(n):
    x = int(input())
    valor.append(x)
dentro = 0
fora = 0
for v in valor:
    if v >= 10 and v <= 20:
        dentro += 1
    else:
        fora += 1

print(dentro,'in')
print(fora,'out')

# Segunda forma de fazer
"""intervalo = range(10,20, 1)
dentro = 0
fora = 0

for i in range(n):
    x = int(input())

    if x in intervalo:
        dentro += 1
    else:
        fora+=1
print(dentro,'in')
print(fora,'out')"""

