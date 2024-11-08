from Empleado import Empleado
from Gerente import Gerente
def imprimir_detalles(objeto):
    #print(objeto) # De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if(isinstance(objeto, Gerente)):
        print(objeto.departamento)


empleado1 = Empleado('Ulises', 500000.00)
imprimir_detalles(empleado1)

gerente1 = Gerente('Agustin', 7000000000.00, 'Programación')
imprimir_detalles(gerente1)