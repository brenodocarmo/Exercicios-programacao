
tamanho = 12

lin = int(input())
ops = input()

matriz= []
for l in range(tamanho):
	linha = []
	for c in range(tamanho):
		linha.append(float(input()))
	matriz.append(linha)


soma = 0.0

for valor in matriz[lin]:
	soma += valor

resultado = soma

if ops == "M":
	resultado = soma / tamanho

print(f"{resultado:.1f}")
