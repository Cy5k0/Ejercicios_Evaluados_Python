# Desafíos Evaluados del Curso: "Fundamentos de Programación en Python"



## [01 - Introducción a Python](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/tree/main/01)
Ejercicios introductorios a Python. Detalles de ambos ejercicios en el archivo **[Readme.md](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/01/README.md)** de la carpeta principal **[01](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/tree/main/01)**.

##### [1. Velocidad de Escape](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/01/velocidad_de_escape/escape.py)
Aplicación en Python que hace el cálculo de la velocidad de escape de algún planeta.

##### [2. Rentabilidad](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/tree/main/01/rentabilidad)
Aplicación que realiza el cálculo de utilidades de un negocio, son 3 casos distintos.


-----------------------------------------------------------
-----------------------------------------------------------

## [02 - Sentencias condicionales e iterativas (I)](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/tree/main/02)
##### [1. IMC](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/02/imc.py)

Aplicación en Python 3.12 que calcula el Indice de Masa Corporal (IMC) y compara el resultado con tabla de categorías según la OMS. Para mas detalles ver [Readme.md](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/02/Readme.md) del proyecto.



##### [2. Cachipun](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/02/cachipun.py)

Aplicación desarrollada en Python 3.12 sobre el juego conocido como ***Cachipun*** en Chile, ***Scissors, Paper, Stone*** en paises anglos. El juego fue desarrollado en español e inglés.Para mas detalles ver [Readme.md](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/02/Readme.md) del proyecto.


----------------------------------------------------------
----------------------------------------------------------

## [03 - Sentencias condicionales e iterativas (II)](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/tree/main/03)

##### [1. Filtrado Compacto](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/mayor_a.py)

Se solicita devolver un informe resumido que exponga los meses que superan un cierto umbral. El programa `mayor_a.py` debe retornar un diccionario con el mes y el valor asociado siempre y cuando superen el umbral especificado.
Para más información ver el [Readme.md]((https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/ReadMe.md)) del proyecto
*Ejemplo*:
`python mayor_a.py 40000`
`{'Mayo': 81000, 'Agosto': 41200, 'Noviembre': 91000}`

##### [2. Primeros Auxilios](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/primeros_auxilios.py)

Se requiere la construcción de una aplicación interactiva `primeros_auxilios.py` que entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega en tiempo real.
Para más información ver el [Readme.md]((https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/ReadMe.md)) del proyecto



##### [3. Fuerza Bruta](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/fuerza_bruta.py)

Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.
Para más información ver el [Readme.md]((https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/03/ReadMe.md)) del proyecto

------------------------------------------------------------
------------------------------------------------------------

## [04 - Estructuras de datos y funciones (I)](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/tree/main/04)

##### [1.- Conversor de divisas](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/04/conversiones.py)

Se crea un archivo `conversiones.py` y una estructura de datos apropiada que permite ingresar tasas de conversión. Las distintas tasas de conversión se ingresan mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.

Para ello se consideran las siguientes tasas de conversión de Peso Chileno:
● a Sol peruano: 0.0046
● a Peso Argentino: 0.093
● a Dólar Americano: 0.00013
Se debe ingresar un 4to argumento que sea el valor en peso chileno a convertir. El programa debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.

##### [2. Word Count](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/04/word_count.py)

El texto lorem ipsum es un texto de prueba que se utiliza para demostrar distintas tipografías además de usarse para rellenar espacios que requieran largos textos.
¿Cuántas palabras componen este texto?

Se crea un archivo llamado `word_count.py` que importa un texto a Python y realiza las siguientes tareas:

● Se utiliza una estructura de datos que cuenta la cantidad de caracteres distintos que componen un texto.
● Cuenta el número de palabras distintas que componen el texto ingresado.

Para separar un texto por espacios se utiliza el método .split("").

##### [3. Recordatorio](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/04/recordatorios.py)

Se crea el archivo `recordatorios.py` que incluye una serie de eventos que quieren ser recordados. El formato de estos recordatorios son una fecha (año-mes-día), una hora y una descripción del evento.

Se aplican métodos apropiados para la estructura de datos entregada se edita la lista de recordatorios de la siguiente manera:

NOTA: Los eventos son editados de tal manera que mantengan su orden en el tiempo. Y el código debe ejecutarse en el orden entregado en las instrucciones dadas a continuación:

1. Se Agrega un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
2. Al revisar los eventos, se nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
3. Le tocará trabajar el día del trabajo. Se elimina el evento del día del trabajo.
4. Se agrega una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.


------------------------------------------------------------
------------------------------------------------------------

## [05 - Estructuras de datos y funciones (II)](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/tree/main/05)

##### [1.- Filtrado Relevante](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/05/filtro.py)

Se requiere implementar un filtrado por precio. Para ello se desarrolla el archivo `filtro.py` con la solución al problema. Dada una muestra de los productos que actualmente se encuentran disponibles en la tienda (un diccionario), se implementa una función que permite entregar lo siguiente:

● Un diccionario con los productos que cumplen una cierta condición dado un umbral
● La función permite mostrar los valores mayor que o menor que un umbral
(siempre estrictos).
● Por defecto la función debe siempre mostrar los valores mayor que el umbral a
menos que se indique lo contrario.
Para desarrollar la funcionalidad se le entrega a usted un diccionario de prueba para verificar sus resultados.

~~~
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}
~~~

##### [2. Alertas Temáticas](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/05/velocidad.py)

Suponiendo el siguiente escenario: Una empresa de flotas que debe medir mediante telemetría las velocidades de cada una de sus correas transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que, para poder entregar energía a las correas más lentas, es necesario ralentizar las más rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se requiere levantar una alerta de la posición de las correas transportadoras que están por sobre el promedio.
● Para ello se determinar una funcionalidad que calcula el promedio de una lista
de velocidades. Supongamos que el servidor donde se pretende instalar esta funcionalidad no cuenta con mucha capacidad por lo que se pide no depender de librerías externas.
● Se listan las posiciones de todas las correas transportadoras que están sobre el
promedio.
● Se implementa la solución mediante una función en un archivo llamado `velocidad.py`.
Se usa la siguiente lista con una muestra de velocidades para probar las funcionalidades.

~~~
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
~~~


##### [3. Apoyo Matemático](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/05/ong.py)

Suponiendo el siquiente escenario, en un programa de ayuda escolar que tiene la esta ONG se está enseñando a programar algunas operaciones avanzadas a niños con alto potencial pero de escasos recursos. Se quiere enseñar dos operaciones conocidas como el factorial y la productoria y se requiere que usted prepare una script que implemente esto.



------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------


##### Autor

[Francisco Colomer Bonometti.](https://github.com/Cy5k0)
  
![pythn](https://github.com/Cy5k0/Ejercicios_Evaluados_Python/blob/main/assets/img/pyth_1.jpeg?raw=true)