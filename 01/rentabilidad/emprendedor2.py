# Mide las utilidades con las variables de precio, utilidad y gastos totales



# Función para validar que sea número el input
def verifica_int(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


        
#función principal
def utilidadesV2 ():

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
            Q_normalUser = input('Ingresa la cantidad de USUARIOS con suscpricpión NORMAL(debe ser un número entero): ')
            if verifica_int(Q_normalUser): #llama a la funcion para verificar
                Q_normalUser = int(Q_normalUser)
                break
            else:
                print('Por favor, ingrese un valor numérico válido.')

        while True:
            Q_premiumUser = input('Ingresa la cantidad de USUARIOS con suscripción PREMIUM(debe ser un número entero): ')
            if verifica_int(Q_premiumUser): #llama a la funcion para verificar
                Q_premiumUser = int(Q_premiumUser)
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

    
        utilidades = ((precioSuscripcion * Q_normalUser) + (precioSuscripcion * 1.5 * Q_premiumUser)) - gastoTotal
        print('')
        print('---------------------------------------------------------------------------------------------------')
        print(f'Las utilidades por concepto de {Q_normalUser} usuarios normales y de {Q_premiumUser} usuarios premium fue de: \n ${utilidades}.-')
        print('---------------------------------------------------------------------------------------------------')
        print('')

        while True:
            repetir = input('¿Desea repetir la función? (S/N): ').lower() #pasa de mayúscula a minúscula
            if repetir in ['s', 'n']: #"in" verifica lo que hay en repetir
                break
            else:
                print('Por favor, ingrese S para sí o N para no.')
        
        if repetir == 'n':
            print('El programa se cierra, Gracias Totales!')
            break #punto de salida del programs

utilidadesV2()
