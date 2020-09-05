qtd = int(input())

for caso in range(qtd):
	text = [s for s in input().split()]
	x, y = text[0], text[1]
	texto = ''
		
	maior_string = max(len(x), len(y))
	
	for letra in range(maior_string):
		if letra < len(x):
			texto += x[letra]
		if letra < len(y):
			texto += y[letra]
	print(texto)
