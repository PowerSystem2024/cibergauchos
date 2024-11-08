from Orden import Orden
from Producto import Producto

producto1 = Producto("Camiseta", 1000)
producto2 = Producto("Pantalon", 150)
producto3 = Producto("Medias", 50)
producto4 = Producto("Zapatos", 700)
producto5 = Producto("Gorra", 200)
producto6 = Producto("Bufanda", 300)
producto7 = Producto("Guantes", 250)

productos1 = [producto1, producto2] # Lista de productos
orden1 = Orden(productos1) # Creamos una orden con los productos(lista pasada)
orden1.agregar_producto(producto5) # Agregamos un producto
orden1.agregar_producto(producto6) # Agregamos un producto
print(orden1)
print(f"Total de la orden 1: {orden1.calcular_total()}") # Imprimimos el total de la orden

productos2 = [producto3, producto4] # Lista de productos
orden2 = Orden(productos2) # Creamos una orden con los productos(lista pasada)
orden2.agregar_producto(producto7) # Agregamos un producto
orden2.agregar_producto(producto5) # Agregamos un producto
print(orden2)
print(f"Total de la orden 2: {orden2.calcular_total()}")