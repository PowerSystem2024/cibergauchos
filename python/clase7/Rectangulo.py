
class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: base y altura,
    el nombre del método será calcular el área usando la fórmula:
    area = base * altura . Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres
    """

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    # Método calculo área
    def calcular_area(self):
        return self.base * self.altura
    
print("--------- Cálculo de área de un rectángulo ------------")
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
rectangulo1 = Rectangulo(base,altura)

print(f'El área del rectángulo con base {base} y altura {altura} es: {rectangulo1.calcular_area():.2f}')