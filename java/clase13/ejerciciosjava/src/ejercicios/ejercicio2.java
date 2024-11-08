/*
 ejercicio 2: leer por teclado dos tablas de 10 numeros
 enteros y mezclarlas en una tercera de la forma: el 1ro de A 
el 1ro de B, el 2do de A, el 2do de B, etc.
 */
package ejercicios;

import java.util.Scanner;


public class ejercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int[] A = new int[10];
        int[] B = new int[10];
        int[] C = new int[20]; //este arreglo va a contener la mezcla de a y b
        
        //rellenamos con los elementos para el arreglo A
        System.out.println("Ingrese los elementos del arreglo A: ");
        for (int i = 0; i < 10; i++) {
            A[i] = scanner.nextInt();
        }
        
        //ahora leemos los elementos del arreglo B
        System.out.println("Ingrese los elementos del arreglo B: ");
        for (int i = 0; i < 10; i++) {
            B[i] = scanner.nextInt();
        }
        
        //ahora mezclamos los elementos de A y de B en el arreglo C(auxiliar)
        int j = 0;
        for (int i = 0; i < 10; i++) {
            C[j] = A[i]; // va a colocar el elemento de A en C
            j++;
            C[j] = B[i]; // va a colocar el elemento de B en C
            j++;
        }
        
        //imprimimos el arreglo C
        System.out.println("Así quedó el arreglo C: ");
        for (int i = 0; i < 20; i++) {
            System.out.println(C[i]+"");
        }
        
    }
}
