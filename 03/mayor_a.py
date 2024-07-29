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

def ventas_mayores(valor):
    return {mes: venta for mes, venta in ventas.items() if venta > valor}

def obtener_valor_objetivo():
    while True:
        try:
            return int(input("Ingrese el valor objetivo: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def filtrado_valores():
    while True:
        valor_objetivo = obtener_valor_objetivo()
        filtrado = ventas_mayores(valor_objetivo)
        print(f"Ventas mayores a {valor_objetivo}:")
        print(filtrado)
        
        continuar = input("¿Desea repetir el proceso? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break

filtrado_valores()