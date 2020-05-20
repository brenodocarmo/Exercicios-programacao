

valor = int(input())
md = 0

for v in range(valor):
    nota = input().split()
    n1 = float(nota[0])
    n2 = float(nota[1])
    n3 = float(nota[2])

    md = ((n1*2) + (n2*3) + (n3*5)) / 10

    print('{:.1f}'.format(md))
