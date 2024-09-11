
# LISTAS

names = ['Juan', "Pedro", "Diego", "Jorge"]

# ----------- Imprimimos la lista completa ----------
print(names)
print("")

# ---------- Acceder a un elemento específico dentro de la lista --------

print("Acceder a un elemento especifico")
print("names[0]: ", names[0])  # Arranca desde el principio
print("names[-1]: ", names[-1])  # Arranca desde el último
print("")

# ----------- Acceder a rangos ---------------
print("Acceder mediante rangos")
print("names[1:3]: ", names[1:3])  # Desde 1 incluido a 3 sin incluir
# Desde el inicio de la lista al 3 sin incluir
print("names[ :3]: ", names[:3])
print("names[1 ]: ", names[1:])  # Desde el 1 incluido al final
print("")

# ------------- Modificar un valor dentro de la lista ----------------
print("Modificar un valor dentro de la lista")
names[2] = 'Maria'
print(names)

# -------------------- Iterar una lista ------------------------

print("Iterar la lista")
for name in names:
    print(name)
print("")

# ------------------- Tamaño de la lista ----------------------

print("Longitud de la lista: ")
print(len(names))
print("")

# ------------------ Agregar un elemento a una lista ---------------
print("Agregar un elemento a la lista (no hay restricciones de tipo)")
names.append('Norma') # Se agrega al final (efecto cola)
names.append([1,2,3]) # Se puede agregar una lista dentro de otra lista 
names.append(True) # Valores booleanos
names.append(20.3) # Tipo flotante
print(names)
print("")
# ------------------ Ingresar elemento en un indice específico ---------------
print("Agregar un elemento en un índice específico")
names.insert(1,'Lucas') #Este nombre pasaría a ocupar la posición 1, desplazando todos hacia la derecha
names.insert(-1,'Lucas')
print(names)

# ---------------------- Eliminar un elemento de la lista --------------------------
print("Eliminar un elemento")
names.remove('Juan')
print(names)
print("")

# ---------------------- Eliminar un elemento y devolverlo --------------------------
print("Eliminar un elemento y almacenarlo en una variable:")
delete1 = names.pop() #Borra el ítem -1 por default, es decir, el último y además podemos almacenarlo en una variable
print(names)
print("names.pop(), elimina el item -1 por default: ", delete1)
delete2 = names.pop(1) #Borra el elemento 1 y nos devuelve el elemento eliminado
print("names.pop(1), elimina el item 1 especificado: ", delete1)
print(names)
print("")
# ---------------------- Eliminar un índice específico sin devolver --------------------------
print("Eliminar un elemento en un índice dado sin necesidad de devolverlo con la funcion del: ")
del names[2] #A diferencia de pop, sólo lo elimina, no devuelve nada
print(names)

# --------------------- Eliminar, borrar o limpiar todos los elementos ----------------------
print("Limpiar una lista: ")
names.clear()
print(names)
print("")

# ---------------------- Otras funciones útiles para listas ------------------------
# Concatenar una lista con +
print("Concatenar listas con +")
lista1 = [1,2,3]
print('lista1 = ',lista1)
lista2 = [4,5,6]
print('lista2 = ',lista2)
lista3 = lista1 + lista2
print('lista3 = lista1 + lista2 = ',lista3)
print("")

# Agregar varios elementos con extend
print("Agregar varios elementos a una lista con extend:")
lista3.extend([7,8,9])
print("lista3.extend([7,8,9]) = ", lista3)
print("")

# Uso de la función index() para saber en qué indica está un elemento dentro de la lista
print("Saber en qué indice está un elemento con index():")
print("N° 5 está en el índice: ", lista3.index(5))
print("")

# Saber cuantos elementos repetidos hay en una lista con count()
print("Saber cuantos elementos repetidos hay en una lista con count():")
print("Cuanto está repetido el n° 7: ",lista3.count(7))
print("Agrego un 7 con append()")
lista3.append(7)
print("Verifico nuevamente cuantas veces está repetido el n° 7: ",lista3.count(7))
print("")

# Poner una lista al reves con reverse
print("Poner la lista al reves con reverse")
lista3.reverse()
print(lista3)
print("")

# Para que una lista se multiplique repitiendo sus elementos
lista = ["a","b","c"]
print('lista = ',lista)
listaRepetida =  lista * 2
print('lista*2 (repetir la lista dos veces) = ', listaRepetida)
print("")

# Métodos de ordenamiento
# Ordenar con sort (no devuelve la lista, retorna None), por default es ascendente
# Ordenar de forma ascendente con sort()
lista4 = [5,3,6,2,1,4]
print('lista4 = ',lista4)
print("Ordenamos con sort(): ")
lista4.sort()
print(lista4)
print("")
# Ordenar en forma descendente con sort(), indicando reverse = True
print("Ordenamos con sort(reverse = true): ")
lista4.sort(reverse = True)
print(lista4)
print("")