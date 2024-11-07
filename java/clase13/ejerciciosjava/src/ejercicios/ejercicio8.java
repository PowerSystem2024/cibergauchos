/*
 Ejercicio 8: Utilizando dos matrices de tamaño 5x9 y 9x5, cargar la primera
y transponerla en la segunda.
 */
package ejercicios;

import java.util.Scanner;

public class ejercicio8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Definimos las matrices
        int[][] matrizA = new int[5][9]; // Matriz 5x9
        int[][] matrizB = new int[9][5]; // Matriz 9x5
        
        // Cargando la primera matriz (5x9)
        System.out.println("Ingrese los elementos de la matriz 5x9:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print("Elemento [" + i + "][" + j + "]: ");
                matrizA[i][j] = scanner.nextInt();
            }
        }
        
        // Transponiendo matrizA en matrizB
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                matrizB[j][i] = matrizA[i][j];
            }
        }
        
        // Mostramos la matriz transpuesta (9x5)
        System.out.println("Matriz transpuesta (9x5):");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matrizB[i][j] + "\t");
            }
            System.out.println();
        }
        
    }
}

