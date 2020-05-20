leds = {
    '1' : 2,
    '2' : 5,
    '3' : 5,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 3,
    '8' : 7,
    '9' : 6,
    '0' : 6,
}
numero_test  = int(input())
i = 0

while i < numero_test:
    valor = list(input())
    soma = 0

    for l in range(len(valor)):
        for c,v in leds.items():
            if valor[l] == c:
                soma+= v
                
    print('{} leds'.format(soma))
    i +=1
