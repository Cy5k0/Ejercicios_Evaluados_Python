
nombre = input("Nombre Paciente: ")
respuesta_estimulos = input("Responde a estímulo (S/N): ")

if respuesta_estimulos == ("S"):
    print(f"Lleva al paciente {nombre} al hospital más cercano")
else:
    print('Abra la vía aérea')
    respuesta_respira = input("¿Respira? S/N: ")