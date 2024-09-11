# SET
# - No tiene un orden y no permite almacenar elementos duplicados
# - No se puede modificar, pero si permite agregar o eliminar
# - No mantiene ningún índice, quiere decir que el orden es aleatorio (por ej: al imprimir)


planetas = {'Tierra','Marte','Jupiter'}

print("planetas: ",planetas)
print("")

# Calcular la longitud
print("Longitud del set")
print(len(planetas))
print("")

# Revisar si un elemento existe dentro del set
print("Revisar elemento está dentro del set o no")
print('Marte' in planetas) # Devuelve True o False, el elemento tiene que ser exactamente igual
print('Márte' in planetas)
print('Tierra' not in planetas)
print("")

# Agregar un elemento
print("Agregar un elemento")
planetas.add('Venus')
print(planetas)
print("")

# Eliminar elementos 
print("Eliminar un elemento mediante remove")
planetas.remove('Marte') # Lanza una excepción del tipo KeyError si el elemento no se encuentra en el set
print(planetas)
print("")

print("Eliminar un elemento mediante discard")
planetas.discard('Tierraa') # No lanza una excepción si el elemento no se encuentra en el set
print(planetas)
print("")

# Borrar todos los elementos de un set

#planetas.clear()
#print(planetas)

# Eliminar el set

#del planetas
#print(planetas)