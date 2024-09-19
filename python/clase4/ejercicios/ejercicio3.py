#Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
#Nombre: Aragon
#Clase: Guerrero
#Raza: Dúnadan del norte

#Nombre: Gandalf
#Clase: Mago
#Raza: Istar

#Nombre: Legolas
#Clase: Arquero
#Raza: Elfo Sindar

lista_personajes = []  #creamos arreglo nuevo
#creamos los conjuntos con los personajes
p1 = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dunadan del norte"}
#agregamos el primer personaje a la lista
lista_personajes.append(p1)
#lo mismo con el segundo personaje
p2 = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
lista_personajes.append(p2)
#tercer personaje
p3 = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
lista_personajes.append(p3)

#creacion de dos personajes mas y añadiendolos a la lista
p4 = {"Nombre": "Gimli", "Clase": "Guerrero", "Raza": "Enano"}
lista_personajes.append(p4)

p5 = {"Nombre": "Frodo", "Clase": "Hobbit", "Raza": "Hobbit"}
lista_personajes.append(p5)

print(lista_personajes)
