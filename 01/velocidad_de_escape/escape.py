# La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
# salir de un planeta venciendo la gravedad.

import math

# Función para validar que sea número el input
def verifica_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


        
#función principal
def velocEscap ():

    planeta = input('Cual es el nombre del planeta: ')


    while True:
        g_input = input('Ingresa la constante gravitacional de gravedad del planeta (m/s²): ')
        if verifica_float(g_input): #llama a la funcion para verificar
            g = float(g_input)
            break
        else:
            print('Por favor, ingrese un valor numérico válido.')

    while True:
        r_input = input('Ingresa el radio del planeta en metros, kilometros o millas: ')
        if verifica_float(r_input): #llama a la función para verificar
            radio = float(r_input)
            break
        else:
            print('Por favor, ingrese un valor numérico válido.')




    #validacion de que sea el valor correcto ingresado
    while True: 
        medida = input('En que medida esta el radio del planeta, para kilometros ingresa: km, para metros: m, para millas: mi: ').lower()
        if medida in ['km', 'm', 'mi']: #con 'in' verifica lo que hay en medida
            break
        else:
            print('Por favor, ingrese solo km, m o mi.')

    # calculo de medidas
    if medida == 'km':
        r = float(radio * 1000)
    elif medida == 'm':
        r = radio
    elif medida == 'mi':
        r = float(radio * 1609.34)
    # cálculo de velocida de escape
    velocidadEscape = math.sqrt(2 * g * r)
    Ve = round(velocidadEscape, 2)

    print("")
    print('--------------------------------------------------------------------------------------------------------')
    print(f'La velocidad de escape del planeta {planeta} con radio {r} metros y una gravedad de {g} [m/s^2] es de: \n{Ve} [m/s]')
    print('')
    print('--------------------------------------------------------------------------------------------------------')
    print('')
#mientras sea verdadero repetirá la función principal o cerrar el programa
while True:
    velocEscap()
    
    while True:
        repetir = input('¿Desea repetir la función? (S/N): ').lower() #pasa de mayúscula a minúscula
        if repetir in ['s', 'n']: #'in' verifica lo que hay en repetir
            break
        else:
            print('Por favor, ingrese S para sí o N para no.')
    
    if repetir == 'n':
        print('El programa se cierra, Gracias Totales!')
        break