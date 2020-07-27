nome_A = input()
nome_B = input()
nome_C = input()

# vertebrado
# mamifero
# onivoro

if nome_A == 'vertebrado' and nome_B == 'ave' and nome_C == 'carnivoro':
    print('aguia')
elif nome_A == 'vertebrado' and nome_B == 'ave' and nome_C == 'onivoro':
    print('pomba')

elif nome_A == 'vertebrado' and nome_B == 'mamifero' and nome_C == 'onivoro':
    print('homem')
elif nome_A == 'vertebrado' and nome_B == 'mamifero' and nome_C == 'herbivoro':
    print('vaca')

elif nome_A == 'invertebrado' and nome_B == 'inseto' and nome_C == 'hematofago':
    print('pulga')
elif nome_A == 'invertebrado' and nome_B == 'inseto' and nome_C == 'herbivoro':
    print('lagarta')

elif nome_A == 'invertebrado' and nome_B == 'anelideo' and nome_C == 'hematofago':
    print('sanguessuga')
elif nome_A == 'invertebrado' and nome_B == 'anelideo' and nome_C == 'onivoro':
    print('minhoca')
