package ar.com.cibergauchos.test;

import ar.com.cibergauchos.ventas.Orden;
import ar.com.cibergauchos.ventas.Producto;

public class TestVentas {

    public static void main(String[] args) {
        // Productos de ropa
        Producto producto1 = new Producto("Pantalón", 9500);
        Producto producto2 = new Producto("Campera", 11200);

        // Creamos la orden1 y agregamos productos de ropa
        Orden orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);

        // Creamos 10 productos adicionales
        Producto producto3 = new Producto("Laptop", 75000);
        Producto producto4 = new Producto("Celular", 56000);
        Producto producto5 = new Producto("Tablet", 32000);
        Producto producto6 = new Producto("Auriculares", 8500);
        Producto producto7 = new Producto("Mouse", 2500);
        Producto producto8 = new Producto("Teclado", 4000);
        Producto producto9 = new Producto("Impresora", 18500);
        Producto producto10 = new Producto("Silla de oficina", 15000);
        Producto producto11 = new Producto("Escritorio", 20000);
        Producto producto12 = new Producto("Monitor", 28000);

        // Creamos la orden2 y agregamos algunos de los productos adicionales
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);

        // Creamos la orden3 y agregamos el resto de los productos adicionales
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto12);

        // Mostramos todas las órdenes
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();

    }

}
