## Ejercios Evaluados - Sentencias condicionales e iterativas (II)

### [Mayor a: ](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/mayor_a.py)

Una empresa provee de los balances del año anterior en un diccionario como se muestra a
continuación:
`ventas = {
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
}`



Se usan 3 funciones, una función ***ventas_mayores(valor)*** donde en la cual se realiza el flitrado de los valores según la variable ingresada mediante la función ***obtener_valor_objetivo()***, y por útlimo una función ***filtrado_valores()*** la cual trae la lista filtrada para imprimir el resultado.

##### Variables: 

- valor_objetivo : Almacena el valor, de forma de un *int*, para efectuar la comparacion y buscar en el diccionario los mayores a dicho valor. 
- filtrado : Variable tipo diccionario, el cual presenta el diccionario original ya filtrado.
- venta : Contiene el valor del diccionario representado como un *int*.
- mes : Contiene el mes del diccionario representado como una *string*.
- continuar : Contiene la respuesta como string para repetir el script.

##### Prerequisitos

* Sistema Operativos: Windows 10, 11, Linux, iOS.
* Python 3.12

##### Ejecución

###### Windows
`python mayor_a.py`

###### Linux y iOS
`python3 mayor_a.py`

#### Autor
[Francisco Colomer B](https://github.com/Cy5k0)

-----------------------------------------------

### [Primeros Auxilios](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/primeros_auxilios.py)

Se construye una aplicación que permita indicar los pasos a seguir ante una emergencia. Se provee de un diagrama que explica las distintas instancias a la que se está sometido durante una emergencia.

![diagrama primeros auxilios](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/assets/img/diagrama_primeros_aux.jpg?raw=true)

##### Variables: 

- nombre: contiene el nombre del paciente y es un *string*.
- respuesta_estimulos = contiene una respuesta (S/N).
- respuesta_respira = contiene una respuesta (S/N).
- ambulancia = contiene la respuesta (S/N) si es que llegó o no la ambulancia.
- signos_vida = contiene la respuesta (S/N) si es que el paciente presenta signos de vida.

Las variables *respuesta_estimulos*, *respuesta_respira*, *ambulancia* y *signos_vida* son chequeadas mediante la función **validar_respuesta(pregunta)**.

##### Prerequisitos

* Sistema Operativos: Windows 10, 11, Linux, iOS.
* Python 3.12

##### Ejecución

###### Windows
`python primeros_auxilios.py`

###### Linux y iOS
`python3 primeros_auxilios.py`

#### Autor
[Francisco Colomer B](https://github.com/Cy5k0)