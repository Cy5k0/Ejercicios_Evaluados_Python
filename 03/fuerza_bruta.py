# Se importa ascii_lowercase para tener el alfabeto a comparar y getpass para ocultar la contraseña
from string import ascii_lowercase
import getpass

# Función para validar la contraseña
def validacion_passwd(contrasena):
    return all(letra.lower() in ascii_lowercase for letra in contrasena)

# Se ingresa la contraseña sin mostrarla
while True:
    user_pass = getpass.getpass("Ingrese la contraseña y presione ENTER: ")
    if user_pass == "":
        print("No se ingresó ninguna contraseña.")
    elif not validacion_passwd(user_pass):
        print("La contraseña debe contener solo letras del alfabeto.")
    else:
        break

# Se guarda la longitud de la contraseña
long_pass = len(user_pass)

intentos = 0
passwrd_encontrada = ""
# Se recorre cada letra de la contraseña
for posicion in range(long_pass):
    # Se recorre cada letra del alfabeto
    for letra in ascii_lowercase:
        intentos += 1
        if letra.lower() == user_pass[posicion].lower():
            passwrd_encontrada += letra
            break

print(f"La contraseña es: {passwrd_encontrada}")
print(f"Se realizaron {intentos} intentos")








