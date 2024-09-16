#Ejercicio 5: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar la lista con el bucle for,
# los elementos deben mostrarse de la siguiente forma:
# 1-2-3-4-5...-50

#listaNumeros = []
#i = 0;
#while i <= 50:
#    listaNumeros.append(i)
#    i = i + 1

listaNumeros = list(range(1, 51))
for i in listaNumeros:
    print(i, end="-")
