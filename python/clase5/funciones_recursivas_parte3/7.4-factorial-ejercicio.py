# Funciones recursivas
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero - 1) # Caso recursivo
#resultado = factorial(5)
num_ingresado = int(input("Ingrese un número: "))
resultado = factorial(num_ingresado)
print(f"El factorial de {num_ingresado} es: {resultado}")
