



seq = [x for x in range(60 , -5 , -5)] 
seq1 = [y for y in range(1 , 60+1, 3)]

menor_lista = min(len(seq), len(seq1)) # retorna o tamanho da menor lista

x = 0

while x < menor_lista:
    print('I={} J={}'.format(seq1[x], seq[x]))
    x+=1