## 05 - Estructuras de datos y funciones (II)

### [1.- Conversor de divisas](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/04/conversiones.py)
Se crea un archivo `conversiones.py` y una estructura de datos apropiada que permite ingresar tasas de conversión. Las distintas tasas de conversión se ingresan mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.

Para ello se consideran las siguientes tasas de conversión de Peso Chileno:
● a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.00013
Se debe ingresar un 4to argumento que sea el valor en peso chileno a convertir. El programa debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.



Se usa 1 función ***validar_ingreso()***, la cual valida que el ingreso sea un valor numérico usando try except.



##### Variables: 

- tc_solPeruano : variable que adquiere el valor de la tasa de conversión del sol peruano ingresada por línea de comando. (arg1)
- tc_pesoArgentino : variable que adquiere el valor de la tasa de conversión del peso argentino ingresada por línea de comando.(arg2)
- tc_USD : variable que adquiere el valor de la tasa de conversión del dólar ingresada por línea de comando.(arg3)
- valorAconvertir : variable que adquiere el valor de del peso chileno a convertir, ingresada por línea de comando.(arg4)

##### Prerequisitos

* Sistema Operativos: Windows 10, 11, Linux, iOS.
* Python 3.12

##### Ejecución

###### Windows
`python conversiones.py <arg1> <arg2> <arg3> <arg4>`


###### Linux y iOS
`python3 conversiones.py <arg1> <arg2> <arg3> <arg4>`

#### Autor
[Francisco Colomer B](https://github.com/Cy5k0)

-----------------------------------------------

### [2. Word Count](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/04/word_count.py)

El texto lorem ipsum es un texto de prueba que se utiliza para demostrar distintas tipografías además de usarse para rellenar espacios que requieran largos textos.
¿Cuántas palabras componen este texto?

Se crea un archivo llamado `word_count.py` que importa un texto a Python y realiza las siguientes tareas:

● Se utiliza una estructura de datos que cuenta la cantidad de caracteres distintos que componen un texto.
● Cuenta el número de palabras distintas que componen el texto ingresado.

Para separar un texto por espacios se utiliza el método .split("").)

##### Variables: 

- archtxt : variable que almacena el archivo txt ingresado por linea de comando. (arg1)
- texto : variable que almancena el texto leido del archivo.
- letras_distintas : variable que almacena la cantidad de caracteres distintos del documento.
- nro_palabras: variable que almacena la cantidad de palabras del texto

##### Prerequisitos

* Sistema Operativos: Windows 10, 11, Linux, iOS.
* Python 3.12

##### Ejecución

###### Windows
`python word_count.py <arg1.txt>`

###### Linux y iOS
`python3 word_count.py <arg1.txt>`

#### Autor
[Francisco Colomer B](https://github.com/Cy5k0)


-----------------------------------------------

### [3. Recordatorio](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/04/recordatorios.py)

Se crea el archivo `recordatorios.py` que incluye una serie de eventos que quieren ser recordados. El formato de estos recordatorios son una fecha (año-mes-día), una hora y una descripción del evento.

Se aplican métodos apropiados para la estructura de datos entregada, se edita la lista de recordatorios de la siguiente manera:

NOTA: Los eventos son editados de tal manera que mantengan su orden en el tiempo. Y el código debe ejecutarse en el orden entregado en las instrucciones dadas a continuación:

1. Se Agrega un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
2. Al revisar los eventos, se nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
3. Le tocará trabajar el día del trabajo. Se elimina el evento del día del trabajo.
4. Se agrega una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.




##### Variables: 

- recordatorios : variable que almacena la lista a modificar

##### Prerequisitos

* Sistema Operativos: Windows 10, 11, Linux, iOS.
* Python 3.12

##### Ejecución

###### Windows
`python recordatorios.py`

###### Linux y iOS
`python3 recordatorios.py`

#### Autor
[Francisco Colomer B](https://github.com/Cy5k0)