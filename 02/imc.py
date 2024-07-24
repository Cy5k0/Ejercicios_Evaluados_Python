# Aplicación que calcula el índice de masa corporal (IMC) y posteriormente clasifica el resultado
# según tabla OMS de IMC adjunta en readme.md
# Se controla que el valor ingresado en las variables sea numérico y positivo, además el IMC se redondea con 2 decimales
# variables:
# peso = variable del peso en Kg
# peso_input = variable para comprobar el valor de peso
# altura = variable de altura en Cm, posteriormente en la ecuación se convierte a Metros, multiplicando el valor por 100
# altura_input = variable para comprobar el valor de altura
# imc = indice de masa corporal


print("")
print("")
print("")

print('******************************************************************')
print('********  Calculadora del Indice de Masa Corporal  ***************')
print('******************************************************************')


# Función para verificar que los datos ingresados sean de tipo float donde "valor" es
# el valor que retorna desde la función principal
def verificador_float(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Función principal
def calculadora_imc():
    print('')

# Ingresa variable peso, verificando su valor
    while True:
        peso_input = input('Ingresa el peso en Kg: ')
        if verificador_float(peso_input) and float(peso_input) >= 0 : #verifica que sea un valor numérico Y que sea positivo
            peso = float(peso_input)
            break
        else:
            print('Por favor, solo ingrese valores válidos para el peso en Kg, ejemplo 82.4')

    print('')

# Ingresa variable altura, verificando su valor
    while True:
        altura_input = input('Ingresa el altura en Cm: ')
        if verificador_float(altura_input) and float(altura_input) >= 0: #verifica que sea un valor numérico Y que sea positivo
            altura = float(altura_input)
            break
        else:
            print('Por favor, solo ingrese valores válidos para la altura en Cm, ejemplo 179')
    
    print('')
    print('')

# Cálculo de IMC (Indice de Masa Corporal) con las variables ingresadas

    imc =  peso / ((altura / 100) ** 2)   
    imc = round(imc, 2)
    
    print('----------------------R E S U L T A D O---------------------------')
    print('')

# Análisis del IMC

    if imc < 18.5:
        print(f'Con un Indice de Masa Corporal de {imc} esta persona se encuentra BAJO PESO.')
    elif 18.5 < imc <= 25:
        print(f'Con un Indice de Masa Corporal de {imc} esta persona se encuentra en un nivel ADECUADO.')
    elif 25 < imc <= 30:
        print(f'Con un Indice de Masa Corporal de {imc} esta persona se encuentra con SOBREPESO.')
    elif 30 < imc <= 35:
        print(f'Con un Indice de Masa Corporal de {imc} esta persona se encuentra con OBESIDAD GRADO I.')
    elif 35 < imc <= 40:
        print(f'Con un Indice de Masa Corporal de {imc} esta persona se encuentra con OBESIDAD GRADO II.')
    else:
        print(f'Con un Indice de Masa Corporal de {imc} esta persona se encuentra con OBESIDAD GRADO III.')

    print('')
    print('-----------------------------------------------------------------')
    print('')
    print('')
    print('')



#mientras sea verdadero repetirá la función principal o cerrar el programa

while True:
    calculadora_imc()
    
    while True:
        repetir = input('¿Desea repetir la función? (S/N): ').lower() #pasa de mayúscula a minúscula
        if repetir in ['s', 'n']: #'in' verifica lo que hay en repetir
            break
        else:
            print('Por favor, ingrese S para sí o N para no.')
    
    if repetir == 'n':
        print('El programa se cierra, Gracias Totales!')
        print('')
        break