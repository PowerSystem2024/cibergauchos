/*
Ejercicio 11: Diseñar un programa que muestre el producto de los primeros
10 números impares
*/
package ciclos11;

import javax.swing.JOptionPane;

public class EjercicioCiclos11JOP {
    public static void main(String[] args) {
        
        long producto = 1;
        for(int i = 1; i <= 20; i += 2){ // El iterador comienza en 1, mientras sea menor o igual a 20 y va aumentando en 2 para 
            producto *= i;  // Ir realizando la cuenta cuando los números sean impares
        }  
        JOptionPane.showMessageDialog(null, "El producto de los primeros 10 números impares es: " + producto);
    }
}
