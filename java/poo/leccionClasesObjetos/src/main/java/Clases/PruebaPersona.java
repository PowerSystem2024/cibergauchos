
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // Llamamos al constructor
        persona1.nombre = "Ulises";// Atraves del constructor podemos acceder a los atributos de la clase
        // El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Sánchez";
        persona1.obtenerInformacion(); // llamamos el método.
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Agustin";
        persona2.apellido = "Lorca";
        persona2.obtenerInformacion();

    }  
}
