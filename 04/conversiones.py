# ingresa tasas de conversion mediante argumentos, donde el 4° argumento corresponde al valor a convertir.

# importa la libreria sys para hacer uso del argv, e ingresar via argumento las variables
import sys

# verificacion de que se ingrese efectivamente los 4 valores solicitados via argumento
if len(sys.argv) < 5:
    print('')
    print('!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!!!')
    print('Por favor, ingresa exactamente 4 valores \nEJ: conversiones.py (tc sol peruano) (tc peso argentino) (tc USD) (valor a convertir en peso chileno).')
    sys.exit(1)# valor 0 para programa ejecutado correctamente , cualquier otro número para salir por error.

# función para validar que el ingreso sea un valor numérico
def validar_ingreso(valor):
    try:
        return float(valor)
    except ValueError:
        print('')
        print(f"Error!!!: '{valor}' no es un valor numérico.")
        sys.exit(1) # valor 0 para programa ejecutado correctamente , cualquier otro número para salir por error.

# declaración de variables, asignandose cada variable segun su índice en el argumento
tc_solPeruano = validar_ingreso(sys.argv[1])
tc_pesoArgentino = validar_ingreso(sys.argv[2])
tc_USD = validar_ingreso(sys.argv[3])
valorAconvertir = validar_ingreso(sys.argv[4])

print('')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(f'Los {valorAconvertir} pesos equivalen a: ')
print(f'{tc_solPeruano * valorAconvertir} Soles.')
print(f'{tc_pesoArgentino * valorAconvertir} Pesos Argentinos.')
print(f'{tc_USD * valorAconvertir} Dólares')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('')