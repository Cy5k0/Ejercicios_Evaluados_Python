# Mide las utilidades con las variables de precio, utilidad y gastos totales.



# Función para validar que sea número el input
def verifica_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


        
#función principal
def utilidadesV3 ():

    while True: #para hacer el cierre o repeticion del programa

#Ingreso de variables con verificacion de que sea un número entero
        while True:
            precioSuscripcion = input('Ingresa el precio de suscripción (debe ser un número entero): $')
            if verifica_int(precioSuscripcion): #llama a la funcion para verificar
                precioSuscripcion = int(precioSuscripcion)
                break
            else:
                print('Por favor, ingrese un valor numérico válido.')

        while True:
            Q_Usuarios = input('Ingresa la cantidad de usuarios (debe ser un número entero): ')
            if verifica_int(Q_Usuarios): #llama a la funcion para verificar
                Q_Usuarios = int(Q_Usuarios)
                break
            else:
                print('Por favor, ingrese un valor numérico válido.')
        
        while True:
            gastoTotal = input('Ingresa el gasto total (debe ser un número entero): $')
            if verifica_int(gastoTotal): #llama a la funcion para verificar
                gastoTotal = int(gastoTotal)
                break
            else:
                print('Por favor, ingrese un valor numérico válido.')

        while True:
            utilidad_anual_anterior = input('Ingresa las Utilidades del año ANTERIOR (debe ser un número entero): $')
            if verifica_int(utilidad_anual_anterior): #llama a la funcion para verificar
                utilidad_anual_anterior = int(utilidad_anual_anterior)
                break
            else:
                print('Por favor, ingrese un valor numérico válido.')

    
        utilidades = (precioSuscripcion * Q_Usuarios) - gastoTotal

        razon = round(float(utilidades / utilidad_anual_anterior), 2)

        print('')
        print('-------------------------------------------------------------------------------------')
        print(f'Las utilidades por concepto de usuarios normales fue de: ${utilidades}.-')
        print('')
        print(f'La utilidad actual vs la utilidad del año anterior están a una razón de: {razon}')
        print('-------------------------------------------------------------------------------------')
        print('')

        while True:
            repetir = input('¿Desea repetir la función? (S/N): ').lower() #pasa de mayúscula a minúscula
            if repetir in ['s', 'n']: #'in' verifica lo que hay en repetir
                break
            else:
                print('Por favor, ingrese S para sí o N para no.')
        
        if repetir == 'n':
            print('El programa se cierra, Gracias Totales!')
            break #punto de salida del programs

utilidadesV3()
