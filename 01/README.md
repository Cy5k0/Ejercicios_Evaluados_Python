## Ejercios Evaluados de Introducción a Python

### Velocidad de Escape

La velocidad de escape de un planeta se define como la mínima velocidad necesaria para salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula: 

Ve = sqrt(2 x G x R)

(La velocidad de escape es igual a la raíz cuadrada de la Gravedad multiplacada por el Radio del planeta multiplicado por 2)

Ve: corresponde a la Velocidad de Escape en [m/s].
G: corresponde a la constante gravitacional en [m/s2].
R: Corresponde al radio del planeta en [m].

Se crea un script `escape.py` que permite calcular la velocidad de escape ingresando como datos de entradas el radio r y la constante g. Los datos de entrada son ingresados de manera interactiva utilizando la función input().

-----------------------------------------------

### Rentabilidad

Se crea script para calcular las utilidades de un proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:

>𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

**Se contempla realizar el cálculo en 3 versiones:**

-----------------------------------------------------------------
Se desarrolla el programa `emprendedor1.py` que utiliza la fórmula descrita anteriormente para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.

-----------------------------------------------------------------

Se considera 2 tipos de usuarios diferenciados, los usuarios normales y los usuarios premium a los cuales se les cobrará una suscripción un 50% mayor. Se crea una segunda versión llamada `emprendedor2.py` que
permite considerar el caso recién expuesto. Para ello se modifica la fórmula de utilidades en la cual se solicite mediante input() los parámetros de entrada precios de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.

-----------------------------------------------------------------

Y por último en la tercera versión llamada `emprendedor3.py`. Se usa la fórmula original de utilidades:

>𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

Se crea una nueva función en la que se pide (por medio de input()) los
siguientes datos:
● precio de suscripción P
● número de usuarios normales U
● gastos GT
● utilidades del año anterior Uanterior

El programa debe calcular las utilidades actuales Uactuales y mostrar la razón entre las utilidades actuales y las del año anterior:

>𝑅𝑎𝑧ó𝑛 = 𝑈𝑎𝑐𝑡𝑢𝑎𝑙𝑒𝑠 / 𝑈𝑎𝑛𝑡𝑒𝑟𝑖𝑜𝑟

El resultado está redondeado a dos decimales.
