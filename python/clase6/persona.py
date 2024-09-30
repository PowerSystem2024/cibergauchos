class Persona: #Creamos una clase
      
      def __init__(self,nombre,apellido,edad): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad  
    

persona1 = Persona("Ariel","Betancud", 40)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f'el objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}')
persona1 = Persona('Ariel', 'Betancud', 40)
print(f'el objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')
