
package Operaciones;


public class Aritmetica {
    // Atributos de la clase
    int a; // Su valor por default es 0;
    int b;
    
    // El constructor es un método especial
    // Que hace un constructor?
    // 1-Contruye un objeto.
    // 2-Reserva un espacio de memoria.
    // 3-Inicializa los atributos de la clase.
    // Para inicializar el constructor se usa el nombre de la clase.
    // Contructor 1
    public Aritmetica(){  //Este constructor vacio es el que se crea por defecto
        System.out.println("Se está ejecutando el constructor número uno.");
    }
    // Constructor 2 (Sobrecarga de contructores)
    // Este constructor inicializa los atributos.
    public Aritmetica(int a, int b){
        this.a = a; // El this diferencia el atributo y la variable o punto de memoria.
        this.b = b;
        System.out.println("Se está ejecutando el contructor número dos.");
    }
   
    
   
    
    // Inicializamos el Método
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    public int sumarConRetorno(){
        //int resultado = a + b;
        //return resultado;
        return a + b;
    }
    public int sumarConArgumentos(int a, int b){ // Tener en cuenta que el tipo var no se puede ingresar junto a los parámetros.
        this.a = a;  //El argumento a se asigna al atributo this.a
        this.b = b;  //El this. Hace que se diferencien los atributos de los argumentos.
        //return a + b;    
        return this.sumarConRetorno();
        // System.gc(); es un método para limpiar residuos, no es recomendado usarlo por su gran peso.
    }
}


