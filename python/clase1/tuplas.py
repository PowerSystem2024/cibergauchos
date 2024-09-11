# Definimos una tupla

lenguajes = ("python","java","javascript")

print(lenguajes)
# print(len(lenguajes)) #Longitud de una tupla

#--------------- Acceder a un elemento ---------------

# print(lenguajes[0])

#-------------------- Acceder de manera inversa (atrás hacia delante) ---------------------

# print(lenguajes[-1])

#---------------- Acceder a un rango -------------------------

#print(lenguajes[0:2])


#---------------------- Diferencia entre tupla y string ----------------------------

#animales = ("gato") #string
#animales = ("gato", ) #tupla

# Recorrer una tupla
for elemento in lenguajes:
    print(elemento, end = " ") # end se usa para eliminar los saltos de linea

# ------------------- Agregar elementos a una tupla (mala práctica) -------------------------
# Dado que las tuplas son inmutables, para agregar un elemento tenemos que hacer la conversión a lista

lenguajesLista = list(lenguajes) # convertimos la tupla a lista
lenguajesLista.append("PHP") # agregamos el elemento deseado

lenguajes = tuple(lenguajesLista) # convertimos la lista a tupla y la asignamos a la tupla anterior

print("\n",lenguajes)

# Eliminar una tupla

#del lenguajes
#print(lenguajes)

# Una tupla puede tener varios tipos de datos al igual que las listas
print("")
print("Tupla con varios tipos de datos: ")
tupla = (4,True,10.5,'Tuplas',[1,2,3])
print(tupla)
print("")

# Verificar si un elemento está en la tupla
print("Verificar si un elemento está en la tupla: ")
print("4 in tupla: ", 4 in tupla)

# Al igual que las listas tambien podemos usar index, count, len
