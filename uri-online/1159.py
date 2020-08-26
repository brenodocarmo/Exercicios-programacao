
def numero_par(n):
	lista = []

	for i in range(n, 1000000):
		if i % 2 == 0:
			lista.append(i)
			if len(lista) == 5:
				break
	return sum(lista)

while True:
	p = int(input())

	if p == 0:
		break
	else:
		print(numero_par(p))
