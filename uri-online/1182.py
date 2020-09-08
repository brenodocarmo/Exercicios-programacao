
coluna_matriz = int(input())
operacao = input().upper()

TAM = 3
soma = 0.0
media = 0.0

matriz = []
for l in range(TAM):
	linha = []
	for c in range(TAM):
		elemento = float(input())
		linha.append(elemento)
	matriz.append(linha)


if operacao == "S":
	for ele in matriz:
		#print(ele[coluna_matriz])
		soma += ele[coluna_matriz]
	print(f"{soma:.1f}")

elif operacao == "M":
	for ele in matriz:
		#print(ele[coluna_matriz])
		soma += ele[coluna_matriz]
	media = soma / TAM
	print(f"{media:.1f}")


