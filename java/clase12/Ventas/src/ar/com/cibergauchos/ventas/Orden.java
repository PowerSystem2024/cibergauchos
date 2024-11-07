package ar.com.cibergauchos.ventas;

public class Orden {

    private int idOrden;
    private Producto productos[];
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;

    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }

    public void agregarProducto(Producto producto) {
        if (this.contadorProductos < Orden.MAX_PRODUCTOS) {
            this.productos[this.contadorProductos++] = producto;
        } else {
            System.out.println("Se ha superado el máximo de productos: " + Orden.MAX_PRODUCTOS);
        }
    }

    public double calcularTotal() {
        double total = 0;
        for (int i = 0; i < this.contadorProductos; i++) {
            total += this.productos[i].getPrecio();
        }
        return total;
    }

    public void mostrarOrden() {
        System.out.println("------------------------ Orden n° " + this.idOrden + " ------------------------");
        double totalOrden = this.calcularTotal();
        System.out.println("## Total: $" + totalOrden);
        System.out.println("## Productos: ");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println("  *"+this.productos[i]);
        }
    }
}
