

def factorial(n_fact):
    if n_fact < 0:
        return "El factorial no está definido para números negativos"
    resultado = 1
    for i in range(1, n_fact + 1): # se le agrega +1 a n_fact, ya que el metodo range no considera el 2do argumento
        resultado *= i
    return resultado

nro_factorial = int(input('Ingresa un número para obtener su factorial: '))

print(factorial(nro_factorial))

    