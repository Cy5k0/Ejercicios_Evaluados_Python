# Función para escoger el tipo de masa
def tipo_masa():
    """
    Permite al usuario seleccionar el tipo de masa para la pizza.

    El usuario ingresa una opción entre las masas disponibles. 
    Si la selección es válida, se devuelve la masa seleccionada; de lo contrario, se devuelve None.

    Returns:
        str: El tipo de masa seleccionado si es válido.
        None: Si la masa seleccionada no está disponible.
    """
    masas_disponibles = ["Tradicional", "Delgada", "Bordes de Queso"]
    nueva_masa = input(f"Elige el tipo de masa ({', '.join(masas_disponibles)}): ").capitalize()
    if nueva_masa in masas_disponibles:
        return nueva_masa
    else:
        print("Masa no disponible.")
        return None

# Función para seleccionar el tipo de salsa
def tipo_salsa():
    """
    Permite al usuario seleccionar el tipo de salsa para la pizza.

    El usuario ingresa una opción entre las salsas disponibles.
    Si la selección es válida, se devuelve la salsa seleccionada; de lo contrario, se devuelve None.

    Returns:
        str: El tipo de salsa seleccionada si es válida.
        None: Si la salsa seleccionada no está disponible.
    """
    salsas_disponibles = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
    nueva_salsa = input(f"Elige el tipo de salsa ({', '.join(salsas_disponibles)}): ").capitalize()
    if nueva_salsa in salsas_disponibles:
        return nueva_salsa
    else:
        print("Salsa no disponible.")
        return None

# Función para agregar un ingrediente
def agregar_ingrediente(ingredientes_actuales):
    """
    Permite al usuario agregar uno o varios ingredientes a la pizza.

    El usuario ingresa ingredientes separados por comas. Se valida cada ingrediente y 
    se agrega a la lista de ingredientes actuales si está disponible y no ha sido agregado previamente.

    Args:
        ingredientes_actuales (list): Lista de ingredientes actuales en la pizza.

    Returns:
        list: La lista actualizada de ingredientes después de agregar los nuevos ingredientes.
    """
    ingredientes_disponibles = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    
    ingrediente_input = input(f"Elige uno o varios ingredientes para tu pizza (separados por comas) ({', '.join(ingredientes_disponibles)}): ")
    
    # Convierte los ingresos en una lista, elimina espacios y coloca mayúscula en cada ingrediente
    ingredientes_a_agregar = [ingrediente.strip().capitalize() for ingrediente in ingrediente_input.split(",")]
    
    # Procesa los ingredientes de la lista
    for ingrediente in ingredientes_a_agregar:
        if ingrediente in ingredientes_disponibles:
            if ingrediente not in ingredientes_actuales:
                ingredientes_actuales.append(ingrediente)
                print(f"Ingrediente {ingrediente} agregado.")
            else:
                print(f"El ingrediente {ingrediente} ya está en la pizza.")
        else:
            print(f"Ingrediente {ingrediente} no disponible.")
    
    return ingredientes_actuales
