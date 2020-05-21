
dia_1 = int(input().split()[1])
hora_inicial = input().split(':')

hora_1 = int(hora_inicial[0])
min_1 = int(hora_inicial[1])
seg_1 = int(hora_inicial[2])

dia_2 = int(input().split()[1])
hora_final = input().split(':')

hora_2 = int(hora_final[0])
min_2 = int(hora_final[1])
seg_2 = int(hora_final[2])

total_dias = dia_2 - dia_1

horas_total = hora_2 - hora_1

if horas_total < 0:
    horas_total += 24
    total_dias -= 1

minutos_total = min_2 - min_1

if minutos_total < 0:
    minutos_total += 60
    horas_total -= 1

segundos_total = seg_2 - seg_1

if segundos_total < 0:
    segundos_total += 60
    minutos_total -= 1

print('{} dia (s)'.format(total_dias))
print('{} hora (s)'.format(horas_total))
print('{} minuto (s)'.format(minutos_total))
print('{} segundo (s)'.format(segundos_total))

