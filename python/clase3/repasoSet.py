# REPASO DE CONJUNTOS (CLASE 3.1)

conjunto = set()  # Asi se crea un conjunto vacio.

conjunto1 = {'Bye'}  # Recordar que en un conjunto hay valores únicos (No se pueden repetir)
# (Y que puede tener varios tipos de datos)
# Tener en cuenta que para inicializar un conjunto con corchetes hay que poner algun elemento.


conjunto.add(7) # Recordar que para ingresar datos a un conjunto se puede usar la funcion .add
conjunto.add('Hola')

print(conjunto)

#Tener en cuenta que en los conjuntos o sets no se pueden agregar múltiples elementos a la vez.
conjunto1.add('Hola') # Tener en cuenta que para inicializar un conjunto con corchetes hay que poner algun elemento.
print(conjunto1)
print(3 not in conjunto1) # Recordar que devuelve un booleano a la condicion.
# (En este caso pregunto si el numero 3 esta en el conjunto.)

print(conjunto1 == conjunto) # Devuelve booleano (Pregunta si un conjunto es igual a otro)

# Como unir conjuntos
conjunto3 = conjunto1 | conjunto # se usa | para operar la union entre conjuntos.
print(conjunto3)

# Unir elementos repetidos en conjuntos
conjunto3 = conjunto1 & conjunto
#con este operador (&) nos une en un conjunto los elementos que estan en ambos conjuntos
print(conjunto3)

# Como Seleccionar los elementos que estan en un solo conjunto (-)
conjunto3 = conjunto1 - conjunto
#En este caso guardaria los elementos que estan en el conjunto al que se le va a restar
# (Minuendo) y no los que estan en el (Sustraendo)
print(conjunto3)

# Como guardar los elementos que estan en los 2 conjuntos, pero que no estan en ámbos
conjunto3 = conjunto1 ^ conjunto
print(conjunto3)

# Como determinar si un conjunto es subconjunto de otro (Uno esta dentro del otro)
conjunto3 = conjunto1 | conjunto
print(conjunto1.issubset(conjunto3)) # Se usa esta funcion para saber si el conjunto 1 es subconjunto del conjunto 3

# como saber si dos conjuntos no comparten elementos (son disconexos)
print(conjunto1.isdisjoint(conjunto)) #Devuelve un booleano.

# como convertir un conjunto en inmutable
conjunto1 = frozenset # este comando no permite modificar de ninguna manera, ni siquiera eliminarlo.