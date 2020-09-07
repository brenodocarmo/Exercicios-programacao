acumulador = 1
soma = 0
for i in range(1, 40, 2):
	soma =float(soma + i /acumulador)
	acumulador = acumulador * 2

print(f"{soma:.2f}")
