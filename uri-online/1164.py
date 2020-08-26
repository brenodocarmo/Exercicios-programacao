def numero_perfeito(n):
	lista = []
	for i in range(1, n+1):
		if n % i == 0:
			lista.append(i)
	return sum(lista[:-1])

valor = int(input())

for i in range(valor):
	np = int(input())
	if numero_perfeito(np) == np:
		print(f"{np} eh perfeito")
	else:
		print(f"{np} nao eh perfeito")
