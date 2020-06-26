qtd = int(input())

soma_cobaia = 0


c = 0
r = 0
s = 0
# if qtd >= 1 and qtd <= 15:

cobaia = [tuple(input().split()) for i in range(qtd)]

for num, let in cobaia:
    num = int(num)

    soma_cobaia += num

    if let == 'C':
        c += num
    
    if let == 'R':
        r  += num
    
    if let == 'S':
        s += num

print('Total: {} cobaias'.format(soma_cobaia))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format((c * 100) / soma_cobaia))
print('Percentual de ratos: {:.2f} %'.format((r * 100) / soma_cobaia))
print('Percentual de sapos: {:.2f} %'.format((s * 100) / soma_cobaia))