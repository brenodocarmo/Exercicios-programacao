alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def decrypt(msg, pos):
	rot = pos
	cod = ''	
	
	for letter in msg:
		letter_index = alpha.index(letter)
		cod += alpha[(letter_index - rot) % len(alpha)]
	
	return cod

caso = int(input())
for qtd in range(caso):
	frase = input()
	posicao = int(input())
	
	print(decrypt(frase, posicao))