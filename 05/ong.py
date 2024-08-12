# Apoyo Matemático

import sys

# función para calcular factorial y comprobar que no sea números negativos, 
# usando el metodo range el cual define el el indice en el que comienza,
# y el útlimo indice , este no se toma en cuenta por eso se suma 1.

def factorial(n_fact):
    if n_fact < 0:
        return "El factorial no está definido para números negativos"
    resultado = 1
    for i in range(1, n_fact + 1):
        resultado *= i
    return resultado

# función para calcular la productoria y valida que esta lista no esté vacía
def productoria(lista):
    if not lista:
        return "La lista está vacía"
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

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