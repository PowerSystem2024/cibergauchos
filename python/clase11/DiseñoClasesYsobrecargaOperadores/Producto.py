class Producto:
    contador_productos = 0 # Variable de clase para contar la cantidad de productos creados

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 # Incrementamos el contador de productos
        self._id_producto = Producto.contador_productos # asignamos el id del producto
        self._nombre = nombre
        self._precio = precio
    
    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        this._nombre = nombre
    
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        this._precio = precio

    # Método para mostrar los datos del producto str
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: ${self._precio}'

if __name__ == "__main__": #Solo se verá visible si la prueba se ejecuta desde aquí
    producto1 = Producto("Camiseta", 1000)
    producto2 = Producto("Pantalon", 150)