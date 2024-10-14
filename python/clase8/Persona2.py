class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Metodo Getter
        print('Estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre
    @property
    def apellido(self):
         return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


persona1 = Persona2('Maria', 'Gonzalez', 32)
print(persona1.nombre)  # Llamamos al metodo getter
persona1.nombre = 'Lucas Rodriguez'  # Llamamos al metodo setter
print(persona1.nombre)  # Otro vez con el metodo getter
print(persona1.mostrar_detalles())  # Llamamos el metodo mostrar detalles
# Atributo read-only (solo lectura) seria la edad porque no tiene el metodo set
print(persona1.edad)

# Tarea: crear tres objetos mas, utilizando los metodos getter and setter
# para modificar y mostrar los cambios con el metodo mostrar detalles

# Objeto numero uno de la tarea
persona2 = Persona2('Fabri', 'Marto', 27)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
persona2.nombre = 'Fabricio'
persona2.apellido = 'Martinez'
persona2.edad = 24
print(persona2.mostrar_detalles())

# Objeto numero dos de la tarea
persona3 = Persona2('Bris', 'Roma', 39)
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
persona3.nombre = 'Brisa'
persona3.apellido = 'Romero'
persona3.edad = 47
print(persona3.mostrar_detalles())

# Objeto numero tres de la tarea
persona4 = Persona2('Robert', 'Fernand', 21)
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
persona4.nombre = 'Roberto'
persona4.apellido = 'Fernandez'
persona4.edad = 29
print(persona4.mostrar_detalles())
