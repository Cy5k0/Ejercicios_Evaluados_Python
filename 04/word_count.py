# importa librerias necesarias
import sys

archtxt = sys.argv[1]

with open(archtxt, "r") as file:
    texto = file.read()


letras_distintas = len(set(texto))
nro_palabras = len(set(texto.split(" ")))
print('')
print("************************************************************")
print(f' Número de palabras en el texto {nro_palabras} ')
print(f' Número de letras distintas en el texto {letras_distintas} ')
print("************************************************************")