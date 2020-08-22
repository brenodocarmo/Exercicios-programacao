while True:
    conjunto = input().split()

    m, n = int(conjunto[0]), int(conjunto[1])

    maior = max(m, n)
    menor = min(m, n)

    if m <= 0 or n <= 0:
        break
    else:
        cont = 0
        for numero in range(menor, maior + 1):
            cont += numero
            print(f"{numero} ", end="")

        print(f"Sum={cont}")
