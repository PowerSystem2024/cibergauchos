//Paso por referencia
package pasoporreferencia;

import Clases.Persona;


public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Micaela";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio realizado en el nombre es: "+persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = new Persona();
        //Persona persona2 = null;
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo valor del objeto es: "+persona2.nombre);
    }
    public static void cambiarValor(Persona persona){ //Paso por referencia
        persona.nombre = "Leonela";
        
    }
    public static Persona cambiarElValor(Persona persona) {
        if(persona == null){
            System.out.println("Valor de persona es invalido : Null");
            return null;
        }
        else{
            persona.nombre = "Agustina";
        return persona;   
        }   
    }
}
