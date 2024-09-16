#EJERCICIO 2: Operaciones de conjuntos con listas
#Escriba un programa que tenga 2 listas y que a continuación
#cree las siguientes listas(en las que no deben haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [6, 7, 8, 9, 10, 1, 1, 2, 5]

#eliminacion de elementos repetidos
conjunto1 = set(list1)
conjunto2 = set(list2)

union = list(conjunto1 | conjunto2)
solo1 = list(conjunto1 - conjunto2)#muestra conj 1
solo2 = list(conjunto2 - conjunto1)#muestra conj 2
interseccion = list(conjunto1 & conjunto2) #mostramos los elementos que aparecen en ambas listas

print(f"Lista de elementos que aparecen en las listas: {union}")
print(f"Lista de elementos que aparecen en la primera lista pero no en la segunda: {solo1}")
print(f"Lista de elementos que aparecen en la segunda lista pero no en la primera: {solo2}")
print(f"Las dos listas juntas: {interseccion}")