/*
 ejercicio 1: leer 10 numeros enteros, guardarlos en un arreglo, debemos mostrarlos en el siguiente orden
el primero, el último, el segundo el penultimo, el tercero, etc.
 */
package ejercicios;

import java.util.Scanner;


public class ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int numeros[] = new int[10];
        System.out.println("Ingrese los números para completar la matriz: ");
        for (int i = 0; i < 9; i++) {
            
            numeros[i] = scanner.nextInt();
        }
        System.out.println();
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]);
            System.out.println(9-i);
        }
    }
}
