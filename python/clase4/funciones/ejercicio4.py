# Ejercicio 4: Sumar números pares dentro de un rango.
# suma de numeros pares del 2 al 30.

a = int(input('Digite donde va a comenzar la suma: '))
b = int(input('Digite hasta donde llegar a sumar: '))
suma = 0
for i in range(a, b+1): # Itera siempre que i este entre esos rangos
    if i % 2 == 0: # Solo se suma si el numero por el que va el iterador es par.
        suma += i

print(f'La suma de los numeros pares en el rango de {a} y {b} es: {suma}')