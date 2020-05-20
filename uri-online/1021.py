valor = float(input(': '))

apagar = valor
valor_atual = 100
cedula = 0

print('Notas:')
while True:
	if valor_atual <= apagar:
		apagar = apagar - valor_atual
		cedula = cedula + 1

	else:
		print(f'{cedula} de {valor_atual:.2f}')	

		if apagar == 0:
			break

		if valor_atual == 100:
			valor_atual = 50


		elif valor_atual == 50:
			valor_atual = 20

		elif valor_atual == 20:
			valor_atual = 10

		elif valor_atual == 10:
			valor_atual = 5
				

		elif valor_atual == 5:
			valor_atual = 2		


		elif valor_atual == 2:
			valor_atual = 1

		
		elif valor_atual == 1:
			valor_atual = 0.50

		elif valor_atual == 0.5:
			valor_atual = 0.25

		elif valor_atual == 0.25:
			valor_atual = 0.10

		elif valor_atual == 0.10:
			valor_atual = 0.05	

		elif valor_atual == 0.05:
			valor_atual = 0.01	
			break	
			

		cedula = 0	
print('Alô')

