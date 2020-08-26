def numeros_impares(x, y):
	lista = []
	if x == 1 and y == 1:
		return 1
	
	for i in range(x, 100000000):
		if i % 2 == 1:
			lista.append(i)
			if len(lista) == y:
				break
	return sum(lista)

n = int(input())

for i in range(n):
	valor = [int(a) for a in input().split()]
	print(numeros_impares(valor[0], vaor[1]))
