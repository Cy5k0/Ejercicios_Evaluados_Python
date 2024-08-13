# ingresar por línea de comando ej: python3 ong.py fact_1=5 prod_1=[2,3,4,5,6,7] fact_2=7 

import sys

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def productoria(lista):
    if not lista:
        return "La lista está vacía"
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def calcular(**kwargs): 
    for key, valor in kwargs.items(): 
        if key.startswith('fact'):    
            resultado = factorial(valor)
            print(f"El factorial de {valor} es {resultado}")
        elif key.startswith('prod'):
            resultado = productoria(valor)
            print(f"La productoria de {valor} es {resultado}")
        else:
            print(f"No se reconoce: {key}")

args = {} #diccionario 
for arg in sys.argv[1:]:
    if '=' in arg:  # Verifica que el argumento contiene '='
        key, valor = arg.split('=')
        key = key.strip()
        valor = valor.strip()
        
        if key.startswith('fact'):
            args[key] = int(valor)  # Convierte el valor a entero
        elif key.startswith('prod'):
            # Convierte la cadena a una lista de enteros
            valor = valor.strip('[]')  # Elimina corchetes
            lista_numeros = [int(x) for x in valor.split(',')]  # Convierte cada elemento a entero
            args[key] = lista_numeros
    else:
        print(f"El argumento '{arg}' no tiene un '=' y se ignorará.")

calcular(**args)



# calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)