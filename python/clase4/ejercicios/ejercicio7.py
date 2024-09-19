#Ejercicio 7: Insertar elementos y ordenarlos
# Pedir numeros y meterlos en una lista. cuando el usuario introduzca un numero 0
#nuestro programa dejaría de insertar
# Por ultimo mostrar los numeros de menor a mayor

num = int(input("Ingrese un numero para colocar dentro de la lista y asi ordenarlos: "))
listita = []
while num != 0:
    listita.append(num)
    num = int(input("Ingrese un numero para colocar dentro de la lista y asi ordenarlos: "))
listita.sort()
print(f"La lista ordenada de menor a mayor es: {listita}")
print("\nPrograma finalizado, se ingresó 0")
