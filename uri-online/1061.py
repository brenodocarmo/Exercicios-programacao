# Início - Empacota os dados inseridos.
dia_inicio_1 = input().strip().split()[-1]
data_inicio_1 = input().strip().split(':') 

# Final.
dia_final_1 = input().strip().split()[-1]
data_final_1 = input().strip().split(':')

# Tratar os indíces.
inicio_1 = int(dia_inicio_1)
hh_1 = int(data_inicio_1[0])
mm_1 = int(data_inicio_1[1])
ss_1 = int(data_inicio_1[2])


final_1 = int(dia_final_1)
hh_2 = int(data_final_1[0])
mm_2 = int(data_final_1[1])
ss_2 = int(data_final_1[2])

"""
1 dia == 24 horas
1 hora == 60 min
1 min == 60 seg

dia_5 - dia_9 = qtd_dia_4
qtd_dia_4 = 96 horas

"""





