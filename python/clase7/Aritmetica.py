
class Aritmetica:
    """
        Clase donde se van a realizar operaciones de suma, resta, multiplicación y más
    """
    def __init__(self,operadorA, operadorB):
        self.operadorA = operadorA
        self.operadorB = operadorB

    # Método sumar
    def sumar(self):
        return self.operadorA + self.operadorB
    
    # Método restar
    def restar(self):
        return self.operadorA - self.operadorB
    
    # Método multiplicar
    def multiplicar(self):
        return self.operadorA * self.operadorB
    
     # Método dividir
    def dividir(self):
        return self.operadorA / self.operadorB
    

aritmetica1 = Aritmetica(10,5) # Le pasamos los argumentos al objeto del tipo Aritmética
print(f'La suma de los números es:  {aritmetica1.sumar()}')
print(f'La resta de los números es:  {aritmetica1.restar()}')
print(f'La multiplicación de los números es:  {aritmetica1.multiplicar()}')
print(f'La división de los números es:  {aritmetica1.dividir():.2f}')