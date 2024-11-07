/*
 Ejercicio 9: Crear una matriz "marco" de tamaño 5x5:
todos sus elementos deben ser 0 salvo los de los bordes
que deben ser 1. Mostrarla.
 */
package ejercicios;

public class ejercicio9 {
    public static void main(String[] args) {
        // Definimos la matriz de tamaño 5x5
        int[][] matriz = new int[5][5];
        
        // Llenamos la matriz con el marco
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                // Condición para los bordes (filas y columnas en los extremos)
                if (i == 0 || i == 4 || j == 0 || j == 4) {
                    matriz[i][j] = 1;
                } else {
                    matriz[i][j] = 0;
                }
            }
        }
        
        // Mostramos la matriz
        System.out.println("Matriz marco de 5x5:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}

