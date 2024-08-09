import sys

# diccionario a filtrar
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}
# función de validación de ingreso numérico en el primer argumento de la línea de comando
def validar_ingreso_precio(valor):
    try:
        return float(valor)
    except ValueError:
        print(f"\nError!!!: '{valor}' no es un valor numérico.")
        sys.exit(1)

# función de validación de ingreso en el segundo argumento de la línea de comando
def validar_opcion(opc):
    opc = opc.lower()
    if opc not in ['mayor', 'menor']:
        print("\nError: Solo debe ingresar 'mayor' o 'menor'.")
        sys.exit(1)
    return opc


if len(sys.argv) < 2:
    print('\nERROR  ! ! ! !')
    print('Debe ingresar al menos un argumento')
    print('')
    sys.exit(1)


if len(sys.argv) > 3:
    print('\nERROR!!!')
    print('Uso: python filtro.py <precio> <mayor/menor>')
    sys.exit(1)

precio = validar_ingreso_precio(sys.argv[1])
# opcion = validar_opcion(sys.argv[2])

while len(sys.argv) == 2:
    articulos_filtrados = [item for item, valor in precios.items() if valor > precio]

    if articulos_filtrados:
        print(f'\nArtículos con precio mayor a {precio}:')
        print(', '.join(articulos_filtrados))
        print('')
    else:
        print(f'\nNo se encontraron artículos con precio mayor a {precio}.')
        print('')

    sys.exit(0)

while len(sys.argv) == 3:
    opcion = validar_opcion(sys.argv[2])
    while opcion == 'mayor' or opcion == 'menor':
        if opcion == 'mayor':
            articulos_filtrados = [item for item, valor in precios.items() if valor > precio]
        else:
            articulos_filtrados = [item for item, valor in precios.items() if valor < precio]


        if articulos_filtrados:
            print(f'\nArtículos con precio {opcion} a {precio}:')
            print(', '.join(articulos_filtrados))
            print('')
        else:
            print(f'\nNo se encontraron artículos con precio {opcion} a {precio}.')
            print('')

        sys.exit(0)

