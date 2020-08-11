def casos_test(n):
    # n = int(n)
    for i in range(n):
        valores = input().split()
        x, y = int(valores[0]), int(valores[1])
        a = maior_menor(x, y)
        numero_primo(a[0], a[1])


def maior_menor(x, y):
    maior = max(x, y)
    menor = min(x, y)
    return maior, menor


def numero_primo(x, y):
    total = 0
    a = maior_menor(x, y)
    if a[0] == a[1]:
        print(0)
    elif a[0] == a[1] + 1:
        print(0)
    else:
        for i in range(a[1] + 1, a[0]):
            if i % 2 != 0:
                total += i
        print(total)


casos_test(int(input()))
