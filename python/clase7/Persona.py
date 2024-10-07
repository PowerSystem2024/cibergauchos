class Persona:  # Creamos una clase
    # init (metodo init dunder) es el llamado al constructor de la clase y self se refiere el objeto propio de la clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: nombre= {self.nombre} apellido= {self.apellido} dni= {self._dni} edad= {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Agustin','Lorca', 41432543, 27) # El constructor de la clase Persona() apunta directamente al método init
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Pedro','Perez', 30453213, 40)
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

#clase 7
persona1.telefono = '263424565'
print(f'Este es el número de teléfono de: {persona1.nombre} {persona1.telefono}') #hemos creado un atributo de un objeto

# Una ventaja de python es que se pueden agregar atributos a un objeto, sin que esos atributos existan
# en el método __init__()
# ACLARACIÓN: este atributo es solo correspondiente al objeto en que se asigna y listo, no se agrega a la clase

print("-------- Agregando un atributo superficial a un objeto ---------")
persona1.residencia = "Mendoza"
print(f'Lugar de residencia de la persona 1: {persona1.residencia}')

# print(f'Lugar de residencia de la persona 2: {persona2.residencia}') # Da ERROR
persona3 = Persona('Rogelio', 'Romero',23546462, 22, 'Telefono', '434556564', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo= 2021)
persona3.mostrar_detalle()
# print(persona3._dni)  esto no se debe utilizar (esta encapsulad)esto dice que lo desconocemos en python
# persona3.__nombre esta totalmente encapsulado