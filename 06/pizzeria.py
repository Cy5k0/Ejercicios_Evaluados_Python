from ingredientes import tipo_masa, tipo_salsa, agregar_ingrediente

# Función para eliminar un ingrediente
def eliminar_ingrediente(ingredientes_actuales):
    ingrediente = input(f"Elige un ingrediente para eliminar ({', '.join(ingredientes_actuales)}): ")
    if ingrediente in ingredientes_actuales:
        ingredientes_actuales.remove(ingrediente)
        print(f"Ingrediente {ingrediente} eliminado.")
    else:
        print(f"El ingrediente {ingrediente} no está en la pizza.")
    return ingredientes_actuales

# Función para ver la configuracion pizza 
def mostrar_pizza(masa, salsa, ingredientes):
    print("\n--- Tu Pizza ---")
    print(f"Masa: {masa}")
    print(f"Salsa: {salsa}")
    print(f"Ingredientes: {', '.join(ingredientes) if ingredientes else 'Ninguno'}\n")

# Función para mostrar el menú
def menu():
    print("\n--- Menú Pizza JAT ---")
    print("1. Cambiar tipo de masa")
    print("2. Cambiar tipo de salsa")
    print("3. Agregar ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Mostrar Pizza actual")
    print("6. Salir")

#Función principal para ejecutar el programa
def arma_pizza():
    masa = "Tradicional" #declaracion de variables locales
    salsa = "Tomate"
    ingredientes = []

    while True:
        menu()
        opcion = input("Selecciona una opción: ")



        if opcion == "1":
            nueva_masa = tipo_masa()
            if nueva_masa:
                masa = nueva_masa

        elif opcion == "2":
            nueva_salsa = tipo_salsa()
            if nueva_salsa:
                salsa = nueva_salsa

        elif opcion == "3":
            ingredientes = agregar_ingrediente(ingredientes)

        elif opcion == "4":
            if ingredientes:
                ingredientes = eliminar_ingrediente(ingredientes)
            else:
                print("No hay ingredientes para eliminar.")

        elif opcion == "5":
            mostrar_pizza(masa, salsa, ingredientes)

        elif opcion == "6":
            tiempo = 20 + (len(ingredientes) * 2)
            print(f"\nEn {tiempo} minutos estará lista tu pizza JAT")
            print("Que disfrutes tu pizza!!!!!")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    arma_pizza()
