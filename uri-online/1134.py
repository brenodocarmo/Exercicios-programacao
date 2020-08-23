alcool = 0
gasolina = 0
diesil = 0

while True:
    opcao = int(input())
    
    if opcao < 1:
        break

    if opcao == 1:
        alcool += 1

    if opcao == 2:
        gasolina += 1

    if opcao == 3:
        diesil += 1

    if opcao == 4:
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesil}")
