
package Operaciones;

public class claseAritmetica {
    public static void main(String[] args) {
        
        var a = 10; // Varibles Locales
        int b = 7; // Memoria stack 
        miMetodo(); // Acá se llama al nuevo método.
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        
        aritmetica1.sumarNumeros();
        
        // Para almacenar un objeto o los atributos del mismo de usa la memoria heap.
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        int resultado1= aritmetica1.sumarConArgumentos(3, 15);
        System.out.println("resultado = " + resultado1);
        
        int resultado2 = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado2);
        
        System.out.println("aritmetica 1 a: "+ aritmetica1.a);
        System.out.println("aritmetica 1 b: "+ aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        Persona persona = new Persona("Ulises", "Sánchez");
        System.out.println("persona nombre = " + persona.nombre );
        System.out.println("persona apellido = " + persona.apellido );
    } 
    
    // Modularidad, esta es la creación de un nuevo método
    public static void miMetodo(){
        int a = 10;
        System.out.println("Aqui hay otro método.");
    }
           
}

// Para crear nuevas clases solo 1 puede ser de tipo pública, por lo tanto se pone el modificador de acceso de tipo default o package
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ // Contructor.
        //super(); // Llamamos al contructor de la clase Padre que debemos tener en cuenta que debe estar en la primera línea
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this.nombre + this.apellido);
    }
}

class Imprimir{
    public Imprimir(){
        super(); // llamamos al constructor de la clase padre, para reservar memoria y no repetir el mismo proceso
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+ persona);
        System.out.println("Imprimimos el objeto actual ,el this: " + this);
    }
}
