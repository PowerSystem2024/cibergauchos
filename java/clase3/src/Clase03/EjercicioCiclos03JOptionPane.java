/*
Ejercicio 3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
*/
package Clase03;

import javax.swing.JOptionPane;

public class EjercicioCiclos03JOptionPane {
    public static void main(String[] args){
        int numero;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" es Par");                
            }
            else{
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" es Impar") ;
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
            
        }
        JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" finaliza el programa");
        
    }
    
}
