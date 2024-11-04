
package domain;

//hija de Persona.
public class Empleado extends Persona {
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;// Es para incrementar.
    
   //Constructores
    public Empleado(){//Constructor 1
        this.idEmpleado= ++Empleado.contadorEmpleados;
    }
    
    
    public Empleado(String nombre, double sueldo){//Constructor 2
        //super(nombre);
        this();// Estamos llamando desde aquí al constructor vacio(llamar a un constructor interno)
        this.nombre = nombre;
        this.sueldo= sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        //Es mas eficiente que la concatenacion comun. El operador + es mucho mas lento.
        //crea objeto StringBuilder
        StringBuilder sb = new StringBuilder();
        //Metodo append, 
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", Persona=").append(this.getNombre());
        sb.append(", sueldo=").append(sueldo);
        sb.append(", =").append(super.toString());
        sb.append('}');
        // para devolver un string, usamos el metodo toString() del sb ya que sino no son compatibles.
        return sb.toString();
    }
    
    
    
}
