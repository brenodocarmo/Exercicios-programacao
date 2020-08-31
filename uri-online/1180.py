valor = int(input())

valores = [int(x) for x in input().split()]

menor_valor = min(valores)

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {valores.index(menor_valor)}")

