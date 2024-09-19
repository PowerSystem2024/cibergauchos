
package Ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ejercicio06 {
    /*Pedir números hasta que se teclee un 0, mostrar 
    la suma de todos los números introducidos*/
    
    public static void main(String[] args) {
        //ejercicioConClaseScanner();
        ejercicioConJOptionPane();
    }
    
    public static void ejercicioConClaseScanner(){
        Scanner input = new Scanner(System.in);
        
        int num, suma = 0;
        do{
             System.out.println("Ingrese un número entero: ");
             num = input.nextInt();
             suma += num;
        } while(num != 0);
        
        System.out.println("La suma de todos los números ingresados es: " + suma);
    }
    
    public static void ejercicioConJOptionPane(){
        
        int num, suma = 0;
        do{
             num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
             suma += num;
        } while(num != 0);
        
        JOptionPane.showMessageDialog(null, "La suma de todos los números ingresados es: " + suma);
    }
    
}
