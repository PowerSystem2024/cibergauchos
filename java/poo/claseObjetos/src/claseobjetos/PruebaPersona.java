
package claseobjetos;


public class PruebaPersona {
    public static void main(String[] args) {
        
        Persona persona1 = new Persona(); // Instanciamos un objeto de la clase Persona a través del constructor
        
        persona1.nombre = "Jose"; // El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Lopez";
        
        persona1.obtenerInformacion();
        
        // Creamos un nuevo objeto del tipo Persona
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        
        persona2.nombre = "Jorge"; 
        persona2.apellido = "Perez";
        
        persona2.obtenerInformacion();
    }
}
