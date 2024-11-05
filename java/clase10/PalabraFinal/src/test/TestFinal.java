/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique:
        variables: Evitar cambiar el valor que almacena la variable
        métodos: Evita que se modifique la definición o el comportamiento 
                de un método des una subclase (hija)
        clases: Evita que se creen clases hijas
Ptra caracteristica es que normalmente, cuando trabjamos con variables
se combina con el modificador de acceso estático para convetir una
variable en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase math en la cuál todos sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce
como una constante
*/
package test;

import domain.Persona;


public class TestFinal {
    public  static void main(String[] args){
        final int miDni = 34025935;
        System.out.println("miDni = " + miDni);
        //miDni = 34025936; No se puede modificar
        //Persona.CONSTANTE_AQUI = 9;//No se modifica
        System.out.println("Mi atributo constante es: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Luciano Marquez");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre = " + persona1.getNombre());
    }
}
