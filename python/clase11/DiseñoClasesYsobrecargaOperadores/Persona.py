class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __add__(self, other): # Other significa otro
        return f"{self.nombre} {other.nombre}"
    
    def __sub__(self, otro):
        return self.edad - otro.edad
    
persona1 = Persona("Danilo", 21)
persona2 = Persona("Pietropaolo" , 5)

# persona1.__add__(persona2) sintaxis interna y automatica

print(persona1 + persona2) # DaniloPietropaolo
print(persona1 - persona2) # 16
