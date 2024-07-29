# funcion de validacion de respuesta para preguntas que solo sea 's' o 'n'
def validar_respuesta(pregunta):
    while True:
        respuesta = input(pregunta).upper()
        if respuesta in ['S', 'N']:
            return respuesta
        else:
            print("Por favor, ingrese solo 'S' o 'N'.")


nombre = input("Nombre Paciente: ")
respuesta_estimulos = validar_respuesta("Responde a estímulo (S/N): ")

if respuesta_estimulos == "S":
    print(f"Lleva al paciente {nombre} al hospital más cercano")
else:
    print('Abra la vía aérea')
    respuesta_respira = validar_respuesta("¿Respira? S/N: ")
    if respuesta_respira == 'S':
        print(f'Permitir posición de suficiente ventilación')
    else:
        print('Administrar 5 ventilaciones y llamar a ambulancia')
        ambulancia = 'N'
        while ambulancia == 'N':
            signos_vida = validar_respuesta(f'{nombre} presenta signos de vida? (S/N): ')
            if signos_vida == 'N':
                print('Administrar Compresiones Torácicas hasta que llegue la ambulancia')
            else:
                print('Revaluar la espera de la ambulancia')
            ambulancia = validar_respuesta('¿Llegó la ambulancia? (S/N): ')
        print(f'Despachar a {nombre} en la ambulancia al hospital')


