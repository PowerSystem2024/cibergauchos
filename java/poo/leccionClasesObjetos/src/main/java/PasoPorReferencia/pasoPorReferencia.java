
package PasoPorReferencia;

import Clases.Persona;

public class pasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Rigoberto"; // Tener en cuenta que en el archivo al que estamos llamando debe estar público tanto el archivo como la variable.
        System.out.println("persona1 nombre: "+ persona1.nombre);
        cambiarValor(persona1); // Llamamos al método.
        System.out.println("El nuevo nombre es: "+ persona1);
        System.out.println("El nuevo nombre es: "+ persona1.nombre);
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = null;
        //persona2 = cambiarElValor(persona2);
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("persona2 = " + persona2.nombre);
    }
    public static void cambiarValor(Persona persona){ // Asi se pasa un parámetro por referencia.
        persona.nombre = "Rigoberta";

    }
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("El valor de persona es invalido: Null");
            return null;
        }
        else{
            persona.nombre = "Danilo";
            return persona;
        }
    }
}
