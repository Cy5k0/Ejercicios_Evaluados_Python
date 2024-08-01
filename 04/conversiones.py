# ingresa tasas de conversion mediante argumentos, donde el 4° argumento corresponde al valor a convertir.

# importa la libreria sys para hacer uso del argv, e ingresar via argumento las variables
import sys

# verificacion de que se ingrese efectivamente los 4 valores solicitados via argumento
if len(sys.argv) < 5:
    print('')
    print('!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!!!')
    print('Por favor, ingresa exactamente 4 valores \nEJ: conversiones.py (tc sol peruano) (tc peso argentino) (tc USD) (valor a convertir en peso chileno).')
    sys.exit(1)

# declaración de variables, asignandose cada variable segun su índice en el argumento
tc_solPeruano = float(sys.argv[1])
tc_pesoArgentino = float(sys.argv[2])
tc_USD = float(sys.argv[3])
valorAconvertir = float(sys.argv[4])

print('')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(f'Los {valorAconvertir} pesos equivalen a: ')
print(f'{tc_solPeruano * valorAconvertir} Soles.')
print(f'{tc_pesoArgentino * valorAconvertir} Pesos Argentinos.')
print(f'{tc_USD * valorAconvertir} Dólares')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('')