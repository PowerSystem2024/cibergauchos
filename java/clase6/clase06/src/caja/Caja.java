//Ejercicio caja
package Caja;
public class Caja {
    //Atributos(caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodo y constructores
    public Caja(){ //Constructor 1 = vacio
    }
    //Constructor con parametros
    public Caja(int ancho, int alto, int profundo){//Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    public int calcularVolumen(){//Para calcular
        return ancho * alto * profundo;   
    }
}
