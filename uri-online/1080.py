
valor = [int(input()) for p, v in enumerate(range(100))]

maio_valor = max(valor)
valor_posicao = valor.index(maio_valor) + 1

print(maio_valor)
print(valor_posicao)