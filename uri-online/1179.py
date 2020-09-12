
valores_par = []
valores_impar = [] 
cont_par = 0
cont_impar = 0

for caso in range(15):
	
	caso = int(input())
	
	if caso % 2 == 0:
		
		valores_par.append(caso)
		#print(valores_par)
		cont_par +=1
		
		if cont_par == 5:
			for posicao, elemento in enumerate(valores_par):
				print(f"par[{posicao}] = {elemento}")
			cont_par = 0
			valores_par.clear()

	else:
		
		valores_impar.append(caso)		
		cont_impar +=1
		
		if cont_impar == 5:
			for posicao, elemento in enumerate(valores_impar):
				print(f"impar[{posicao}] = {elemento}")
			cont_impar = 0
			valores_impar.clear()
	
for posicao, elemento in enumerate(valores_impar):
	print(f"impar[{posicao}] = {elemento}")	

for posicao, elemento in enumerate(valores_par):
	print(f"par[{posicao}] = {elemento}")

