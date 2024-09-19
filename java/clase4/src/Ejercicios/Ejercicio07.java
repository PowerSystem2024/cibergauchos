package Ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio07 {

    /* Pedir números hasta que se introduzca uno negativo. Calcular la media 
    de los numeros ingresados*/

    public static void main(String[] args) {
        //ejercicioConClaseScanner();
        ejercicioConJOptionPane();
    }

    public static void ejercicioConClaseScanner() {
        Scanner input = new Scanner(System.in);

        int num, suma = 0, contador = 0;
        float promedio = 0;
        
        System.out.println("Ingrese un número: ");
        num = input.nextInt();
        while(num >= 0){
            suma += num;
            contador++;
            System.out.println("Ingrese otro número: ");
            num = input.nextInt();
        }
        
        if(contador == 0){
            System.out.println("Error. La división entre 0 no existe");
        }else{
            promedio = (float) suma / contador;
            System.out.println("El promedio de todos los números ingresados es: " + promedio);
        }
       
    }

    public static void ejercicioConJOptionPane() {

        int num, suma = 0, contador = 0;
        float promedio = 0;
        
        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while(num >= 0){
            suma += num;
            contador++;
             num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));
        }
        
         if(contador == 0){
            JOptionPane.showMessageDialog(null, "Error. La división entre 0 no existe");
        }else{
            promedio = (float) suma / contador;
            JOptionPane.showMessageDialog(null, "El promedio de todos los números ingresados es: " + promedio);
        }
    }
}
