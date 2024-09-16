#Ejercicio 1: tabla de multiplicar
# hacer un programa que pida un numero por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10 
# Por ej: se digita el 5 en la lista tendra: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

numero = int(input("Ingrese un numero para mostrarle su tabla de multiplicar: "))
tabla = []
while numero <= 0:
    print("Error, se ingresó un numero negativo")
    numero = int(input("Ingrese un numero para mostrarle su tabla de multiplicar: "))
for i in range(1, 11):
    tabla.append(i*numero)
print(f"La tabla del {numero} es: {tabla}")

for indice, i in enumerate(tabla):
    print(f"{numero} x {i} = {tabla[indice]}")

