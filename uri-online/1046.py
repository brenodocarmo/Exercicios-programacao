horas = input().split()

hora_inicial = int(horas[0])
hora_final = int(horas[1])

qtd_horas = hora_final - hora_inicial

if qtd_horas < 0:
    qtd_horas += 24

elif qtd_horas == 0:
    qtd_horas+= 24

print('O JOGO DUROU {} HORA(S)'.format(qtd_horas))