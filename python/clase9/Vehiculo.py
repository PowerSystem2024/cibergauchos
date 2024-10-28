class Vehiculo:
    '''
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y metodos:

    Vehiculo (clase padre)
    -Atibutos(color, ruedas)
    -Metodo(__init__() y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(Velocidad (KM/HR))
    -Metodos(__init__() y __str__())

    Bicicletas(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Metodo(__init__() y __str__()

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', velocidad(km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo


# 1er Objeto clase padre vehiculo
vehiculo = Vehiculo('Negro', 4)
print(vehiculo)

# 2do Objeto, de la clase auto
auto = Auto('Rojo', 4, 180)
print(auto)

# Tercer objeto, último de la clase Bicicleta
bici = Bicicleta('Verde', 2, 'Deportiva')
print(bici)
