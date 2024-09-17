# Ejercicio 5: Factorial de un número positivo
num = int(input('Ingrese un número positivo:'))
while num < 0: # Esto hace que funcione mientras el numero sea negativo.
    print('¡ERROR!, el número debe ser positivo')
    num = int(input('Ingrese un número positivo:'))

factorial = 1
for i in range(1, num+1):
    factorial *= i

print(f'\nEl factorial de {num} es: {factorial}')