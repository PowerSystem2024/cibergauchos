/*
Ejercicio 12: Pedir un número y calcular su factorial.
*/
package Ciclos12;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ejercicio12ClaseScanner {
    public static void main(String[] args) {
        //Scanner consolaEntrada = new Scanner(System.in);
        long factorial = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: ")); // Pide por el panel un número
        for(int i = 1; i <= numero; i++){ // Empieza el iterador en 1 mientras sea menor o igual al número ingresado el iterador va aumetando
            factorial *= i; // Y realizando la cuenta para sacar el factorial
        }
        //System.out.println("El factorial del numero es: "+ factorial); // Esto sería para mostrar el resultado en consola.
        JOptionPane.showMessageDialog(null, "El factorial del número es: "+ factorial); // Y esto por medio del JOptionPane.
    }
}
