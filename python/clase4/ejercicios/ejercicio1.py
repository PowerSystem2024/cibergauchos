#EJERCICIO 1: Eliminar duplicados de una lista
#escribir un programa donde tenga una lista y que
#a continuacion elimine los elementos repetidos, por ultimo mostrar la lista
lista = [1, 2, 3, 4, 5, 1, 2, 6]
conjunto = set(lista)
lista = list(conjunto)
print(lista)
