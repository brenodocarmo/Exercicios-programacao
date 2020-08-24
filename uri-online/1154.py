valor_positivo = []

while True:
    valor = int(input())

    if valor < 1:
        break
    valor_positivo.append(valor)

print(f"{sum(valor_positivo) / len(valor_positivo):0.2f}")
