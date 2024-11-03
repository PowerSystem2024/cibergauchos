
package domain;

public class Persona {
  //lo private no se hereda a las clases hijas.
    //el modificador de acceso protected esta pensado para la herencia.
    //Atributos de herencia
    protected  String nombre;//por defecto NULL
    protected char genero;//por defecto '' vacio
    protected int edad;// por defecto 0
    protected String direccion; //por defecto NULL
    
    //Constructor vacio: este es para crear objetos sin necesidad de inicializar  los atributos de la clase.
    public Persona (){//Constructor - 1 vacio
        
    }
 
    public Persona (String nombre){//Constructor- 2--solo nombre
        this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String direccion) {//Constructor - 3 todos los datos
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    public String getDireccion() {
        return this.direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{");
        sb.append("nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion=").append(direccion);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }

    
    
    
}
