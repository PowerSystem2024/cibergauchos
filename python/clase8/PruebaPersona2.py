from Persona2 import Persona2
# Al importar nos trae todo el archivo, incluso las ejecuciones

print('Creación de objetos'.center(50,'-'))

if __name__ == '__main__': # Comprobación del método principal en ejecución
    persona5 = Persona2('Joey','Tribbiani',30)
    persona5.mostrar_detalles()
    print(__name__)


print('Eliminación de objetos'.center(50,'-'))

del persona5
# Estamos llamando al método destructor de la clase Persona 2