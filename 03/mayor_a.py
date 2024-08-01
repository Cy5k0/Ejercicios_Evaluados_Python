# aplicación que busca números mayores que el ingresado en la variable 'valor_objetivo', esta busqueda la realiza en el diccionario 'ventas'
# La respuesta de esta busqueda es un diccionario con los datos filtrados

# ventas = {
#     "Enero": 15000,
#     "Febrero": 22000,
#     "Marzo": 12000,
#     "Abril": 17000,
#     "Mayo": 81000,
#     "Junio": 13000,
#     "Julio": 21000,
#     "Agosto": 41200,
#     "Septiembre": 25000,
#     "Octubre": 21500,
#     "Noviembre": 91000,
#     "Diciembre": 21000,
# }


# # Función para buscar los valores mayores al ingresado
# def ventas_mayores(valor):
#     return {mes: venta for mes, venta in ventas.items() if venta > valor}


# # Función para la validación del valor objetivo para que sea un enterto (int)
# def obtener_valor_objetivo():
#     while True:
#         try:
#             return int(input("Ingrese el valor objetivo: "))
#         except ValueError:
#             print("Por favor, ingrese un número entero válido.")

# def filtrado_valores():
#     while True:
#         valor_objetivo = obtener_valor_objetivo()
#         filtrado = ventas_mayores(valor_objetivo)
#         print(f"Ventas mayores a {valor_objetivo}:")
#         print(filtrado) # imprime el diccionario filtrado
        

#         while True:
#             continuar = input("¿Desea repetir el proceso? (s/n): ").lower()  # convierte a minúsculas
#             if continuar in ["s", "n"]:  # COn el in verifica si el valor es el solicitado
#                 break
#             else:
#                 print('Por favor, ingresa "s" para SI o "n" para NO.')

#         if continuar == ('n'):
#             print('Se cierra el programa.')
#             break
 

# filtrado_valores()

import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Función para buscar los valores mayores al ingresado
def ventas_mayores(valor):
    return {mes: venta for mes, venta in ventas.items() if venta > valor}

# Función para la validación del valor objetivo para que sea un entero (int)
def obtener_valor_objetivo():
    while True:
        try:
            return int(input("Ingrese el valor objetivo: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def filtrado_valores(valor_inicial=None):
    while True:
        if valor_inicial is not None:
            valor_objetivo = valor_inicial
            valor_inicial = None  # Reset para futuras iteraciones
        else:
            valor_objetivo = obtener_valor_objetivo()
        
        filtrado = ventas_mayores(valor_objetivo)
        print(f"Ventas mayores a {valor_objetivo}:")
        print(filtrado)  # imprime el diccionario filtrado

        if len(sys.argv) > 1:
            break  # Si se proporcionó un argumento, salimos después de una ejecución

        while True:
            continuar = input("¿Desea repetir el proceso? (s/n): ").lower()
            if continuar in ["s", "n"]:
                break
            else:
                print('Por favor, ingresa "s" para SI o "n" para NO.')

        if continuar == 'n':
            print('Se cierra el programa.')
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            valor_inicial = int(sys.argv[1])
            filtrado_valores(valor_inicial)
        except ValueError:
            print("Error: El argumento debe ser un número entero.")
            sys.exit(1)
    else:
        filtrado_valores()