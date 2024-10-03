
class Persona:  # Creamos una clase
    # init (metodo init dunder) es el llamado al constructor de la clase y self se refiere el objeto propio de la clase
    def __init__(self,nombre,apellido,edad):  
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: nombre={self.nombre}; apellido={self.apellido}; edad={self.edad}')


persona1 = Persona('Agustin','Lorca',27) # El constructor de la clase Persona() apunta directamente al método init
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Pedro','Perez',40)
print(f'Objeto 2 de la clase persona {persona2.nombre} {persona2.apellido} {persona2.edad}')


# Modificar los atributos de un objeto
persona1.nombre = 'Manu'
persona1.apellido = 'Lanzini'
persona1.edad = 33

print(f'Objeto 1 modificado de la clase persona {persona1.nombre} {persona1.apellido} {persona1.edad}')


# Los atributos son las carecterísticas de un objeto
# Los métodos son el comportamiento que van a tener los objetos (acciones)
# Los métodos son funciones asociadas a una clase. Las funciones por sí solas tienen comportamiento propio

persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Si llamamos a un método de la clase directamente hay que pasarle la referencia del objeto
# Persona.mostrar_detalle(persona1)


# Una ventaja de python es que se pueden agregar atributos a un objeto, sin que esos atributos existan
# en el método __init__()
# ACLARACIÓN: este atributo es solo correspondiente al objeto en que se asigna y listo, no se agrega a la clase

print("-------- Agregando un atributo superficial a un objeto ---------")
persona1.residencia = "Mendoza"
print(f'Lugar de residencia de la persona 1: {persona1.residencia}')

# print(f'Lugar de residencia de la persona 2: {persona2.residencia}') # Da ERROR