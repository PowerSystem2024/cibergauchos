#Ejercicio 8: Sumar numeros pares dentro de un rango
#Hacer un programa para sumar numeros pares dentro de un rango por ejemplo 
# Suma de numeros pares del 2 al 30
# Suma = 240

n = int(input("Ingrese un numero de rangos a sumar: "))
suma_pares = 0
for i in range(2, n + 1):
    if i % 2 == 0:
        suma_pares = suma_pares + i
print(f"La suma de los numeros pares dentro del rango establecido es de: {suma_pares}")