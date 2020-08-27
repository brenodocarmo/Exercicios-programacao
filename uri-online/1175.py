
def troca_valor(lista):
	inicio = 0
	final = len(lista) - 1

	while inicio < final:
		lista[inicio], lista[final] = lista[final], lista[inicio]

		
		i += 1
		j -= 1
	
	return lista

valor = []

for i in range(20):
	valor.append(int(input())

troca = troca_valor(valor)

for i, a enumerate(troca):
	print(f"N[{i}] = {a}")
