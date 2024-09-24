# Ejercicio 3: Función recursiva
# Imprimir números de 5 a 1 de manera descendente usando una función recursiva
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5 debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser 3:
# 3
# 2
# 1
# Si se ingresan numeros negativos, no se imprime nada

def imprimirNumeros(numeros):
    if numeros > 0:
        print(numeros)
        imprimirNumeros(numeros - 1)

num_ingresado = int(input("Ingrese un número: "))
imprimirNumeros(num_ingresado)