<<<<<<< HEAD
# ingresar por línea de comando ej: python3 ong.py fact_1=5 prod_1=[2,3,4,5,6,7] fact_2=7 

import sys

def factorial(n):
    if n < 0:
=======
# Apoyo Matemático

import sys

# función para calcular factorial y comprobar que no sea números negativos, 
# usando el metodo range el cual define el el indice en el que comienza,
# y el útlimo indice , este no se toma en cuenta por eso se suma 1.

def factorial(n_fact):
    if n_fact < 0:
>>>>>>> 0874275071d3a4a76fae34f1345e0f21e7f273b4
        return "El factorial no está definido para números negativos"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# función para calcular la productoria y valida que esta lista no esté vacía
def productoria(lista):
    if not lista:
        return "La lista está vacía"
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

<<<<<<< HEAD
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
=======
# Verifica si se ingresaron los argumentos correctos
if len(sys.argv) < 3:
    print("Uso: python script.py <lista_numeros> <numero_factorial>")
    print("Ejemplo: python script.py 1,2,3,4 5")
    sys.exit(1)

# Obtiene la lista de números y el número para el factorial desde la linea de comando
lista_str = sys.argv[1]
lista_num = [int(num.strip()) for num in lista_str.split(',') if num.strip()]

# verifica que el número ingresado sea correcto
try:
    nro_factorial = int(sys.argv[2])
except ValueError:
    print("El número para el factorial debe ser un entero válido.")
    sys.exit(1)


print(f"El factorial de {nro_factorial} es: {factorial(nro_factorial)}")
print(f"La productoria de la lista {lista_num} es: {productoria(lista_num)}")
>>>>>>> 0874275071d3a4a76fae34f1345e0f21e7f273b4
