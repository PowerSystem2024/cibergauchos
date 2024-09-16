/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo, 
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/
package Clase03;

import javax.swing.JOptionPane;

public class EjercicioCiclos04JoptionPane {
    public static void main(String[] args) {
        int numero,conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0) {
            JOptionPane.showMessageDialog(null, "El número "+numero+" es positivo");            
            conteo++;            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));            
        }
        JOptionPane.showMessageDialog(null, "Ha ingresado "+conteo+" números que no son negativos");
    }    
}
