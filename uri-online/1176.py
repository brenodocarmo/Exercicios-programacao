def fib(n):
	a, b = 0, 1
	cont = 0
	fib_list = []
	while cont <= n:
		fib_list.append(a)
		a, b = b, a+b
		cont += 1
	return fib_list[-1]

valor = int(input())

for caso in range(valor):
	f = int(input())
	print(f"Fib({f}) = {fib(f)}")
