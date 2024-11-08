package test;


public class TestArreglos {
    
    public static void main(String[] args) { //Lado derecho instanciamos un objeto de tipo OBJECT 
        int edades[] = new int [3];//El lado izquierdo declaramos la variable
        System.out.println("edades = " + edades);
        
        edades[0] = 15;
        System.out.println("edades 0 = " + edades[0]);
        
        edades[1] = 20;
        System.out.println("edades 1 = " + edades[1]);
        
        edades[2] = 13;
        System.out.println("edades 2 = " + edades[2]);
        
        //edades[3] = 7;//Fuera de rango,error en tiempo de ejecuciòn
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }       
    }   
}