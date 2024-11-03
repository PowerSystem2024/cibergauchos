from abc import ABC, abstractmethod
# ABC : Abstract base class, convierte una clase en abstracta

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        # Creamos validaciones
        if self._valifar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}.')
        if self._valifar_valores(alto):
            self._alto = alto
        else: 
            self._alto = 0   
            print(f'Valor erroneo alto: {alto}')     

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._valifar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._valifar_valores(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')


    @abstractmethod
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'
    
    def _valifar_valores(self, valor): # Metodo encapsulado.
        return True if 0 < valor < 10 else False
