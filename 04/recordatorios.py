recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Instrucciones
recordatorios.insert(1, ['2021-01-02', '06:00', 'Empezar el año']) # instrucción_1
recordatorios[3][0] = '2021-07-16' # instrucción_2
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"]) # instrucción_3
recordatorios.insert(4, ['2021-12-24', '22:00', 'Cena de Navidad']) # instrucción_4
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo']) # instrucción_4

# Output
print('')
print('Recordatorios:')
print('--------------')
for recordatorio in recordatorios:
    print(recordatorio)
print('')
