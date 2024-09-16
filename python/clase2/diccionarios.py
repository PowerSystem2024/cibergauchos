
# *** Diccionarios
# -- Estructura de datos que almacena pares de clave-valor
# -- Cada clave debe ser única. Si se agrega un nuevo par con una clave que ya existe, el valor anterior asociado 
# a esa clave será sobrescrito por el nuevo valor.
# -- Mantienen el orden de inserción de los pares clave-valor, es decir, si iteramos los elementos aparecerán en el orden en 
# que fueron añadidos. 
# -- Están implementados usando tablas hash, lo que permite el acceso rápido a los valores basándose en las claves. 
# Esto significa que las operaciones de búsqueda, inserción y eliminación de pares clave-valor son muy eficientes.
# -- Son mutables
# -- Claves inmutables. Esto se debe a que las claves deben ser "hashables", es decir, deben tener un valor hash que no cambie.


diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programming',
    'SABD':'Sistema de Administración de Bases de Datos'
}

print(diccionario)

# Longitud de un diccionario
print("Longitud: ")
print(len(diccionario))
print("")

# Acceder a un diccionario con la llave (key)
print("Acceder a un diccionario con la llave (key): ")
print(diccionario['OOP'])
print("")

# Otra forma de recuperar un elemento
print("Acceder a un elemento mediante la funcion get con la key: ")
print(diccionario.get('IDE'))
print("")

# Modificar un elemento
print("Modificar un elemento: ")
diccionario['IDE'] = "Entorno de Desarrollo Integrado"
print(diccionario.get('IDE'))
print("")

# Recorrer un diccionario
print("Recorrer un diccionario solo mostrando las keys: ")
for llave in diccionario:
    print(llave)
print("")

print("Recorrer un diccionario y obtener tanto las keys como los valores con la funcion items(): ")
for llave,valor in diccionario.items():
    print('key: ',llave,';','value: ',valor)
print("")

print("Iterar y acceder a las keys mediante la funcion keys(): ")
for llave in diccionario.keys():
    print('key: ',llave)
print("")

print("Iterar y acceder a los valores mediante la funcion values(): ")
for valor in diccionario.values():
    print('value: ',valor)
print("")

# Comprobar la existencia de algun elemento
print("Comprobar si IDE está en el diccionario: ")
print('IDE' in diccionario)

# Agregar un elemento
print("Agregar un elemento")
diccionario['PK'] = 'Primary Key'
print(diccionario)
print("")

# Eliminar un elemento
print("Eliminar un elemento")
diccionario.pop('SABD')
print(diccionario)
print("")

# Limpiar un diccionario
print("Limpiar un diccionario (borrar los elementos): ")
diccionario.clear()
print(diccionario)

# Eliminar todo el diccionario
del diccionario
#print(diccionario)