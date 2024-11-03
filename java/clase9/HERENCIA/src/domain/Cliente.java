
package domain;
//Se improta para ser usado por las fechas.
import java.util.Date;


public class Cliente extends Persona {
    //Atributos
    private int idCleinte;
    private Date fechaREgistro;// Importar la clase Date.
    private boolean vip; //Very important person
    private static int contadorCliente;//Tipo estatico
    
    //Constructor
    public Cliente(Date fechaRegistro, boolean vip, String nombre,
            char genero, int edad, String direccion){
        super(nombre,genero,edad,direccion);
        this.idCleinte = ++Cliente.contadorCliente;
        this.fechaREgistro = fechaRegistro;
        this.vip = vip;       
        
    }

    public int getIdCleinte() {
        return this.idCleinte;
    }

    public Date getFechaREgistro() {
        return this.fechaREgistro;
    }

    public void setFechaREgistro(Date fechaREgistro) {
        this.fechaREgistro = fechaREgistro;
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("idCleinte=").append(idCleinte);
        sb.append(", fechaREgistro=").append(fechaREgistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
}
