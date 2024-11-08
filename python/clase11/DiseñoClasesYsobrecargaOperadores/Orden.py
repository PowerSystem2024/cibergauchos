from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto) #Para agregar un nuevo producto

    def calcular_total(self):
        total = 0 # Variable temporal para almacenar el total de la orden
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + " | "
        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'

if __name__ == "__main__":
    producto1 = Producto("Camiseta", 1000)
    producto2 = Producto("Pantalon", 150)
    productos1 = [producto1, producto2] # Lista de productos
    orden1 = Orden(productos1) # Creamos una orden con los productos(lista pasada)
    print(orden1)

    producto3 = Producto("Medias", 50)
    producto4 = Producto("Zapatos", 700)
    productos2 = [producto3, producto4] # Lista de productos
    orden2 = Orden(productos2) # Creamos una orden con los productos(lista pasada)
    print(orden2)