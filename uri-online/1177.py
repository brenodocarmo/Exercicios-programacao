p = 0
t = int(input())
dic = {}

if 2 <= t <= 50:
	valor = [int(x) for x in range(1000)]
	valor_2 = [int(x) for x in range(t)]
	while p < len(valor):
		for v in valor_2:
			dic[p] = v
			p+=1	
	for posicao, valor in dic.items():
		if posicao < 1000:
			print(f"N[{posicao}] = {valor}")

