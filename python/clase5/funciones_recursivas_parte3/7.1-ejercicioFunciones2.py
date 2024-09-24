# Ejercicio 2: Función con * args para multiplicar 
# Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parametro de la función y regresar
# como resultado la multiplicación de todos los valores pasados como argumentos.

def multiplicar_valores(*args):
    multiplicador = 1
    for arg in args:
        multiplicador *= arg
    return multiplicador

resultado = multiplicar_valores(2, 4, 6, 10) 
print(f"El resultado de la multiplicación es: {resultado}")
resultado2 = multiplicar_valores(3, 4, 5, 6, 7)
print(f"El resultado de la multiplicación es: {resultado2}") 
resultado3 = multiplicar_valores(10, 5, 2, 6)
print(f"El resultado de la multiplicación es: {resultado3}")