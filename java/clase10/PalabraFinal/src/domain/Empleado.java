
package domain;

public class Empleado extends Persona{
    @Override   
    public void imprimir(){
        System.out.println("M�todo imprimir desde la clase hija");
    }
}
