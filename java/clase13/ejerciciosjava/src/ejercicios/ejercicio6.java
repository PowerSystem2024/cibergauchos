/*
 ejercicio 6: leer dos series de 10 enteros, que estaran ordenados crecientemente
fusionar las dos tablas en una tercera, de forma que sigan ordenados.
 */
package ejercicios;

import java.util.Scanner;

public class ejercicio6{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] serie1 = new int[10];
        int[] serie2 = new int[10];
        int[] fusion = new int[20];
        
        // Leemos los elementos de la primera serie
        System.out.println("Ingrese 10 números enteros en orden creciente para la primera serie:");
        for (int i = 0; i < serie1.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            serie1[i] = scanner.nextInt();
        }
        
        // Leemos los elementos de la segunda serie
        System.out.println("Ingrese 10 números enteros en orden creciente para la segunda serie:");
        for (int i = 0; i < serie2.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            serie2[i] = scanner.nextInt();
        }
        
        // Fusionamos ambas series en orden
        int i = 0, j = 0, k = 0;
        while (i < serie1.length && j < serie2.length) {
            if (serie1[i] < serie2[j]) {
                fusion[k++] = serie1[i++];
            } else {
                fusion[k++] = serie2[j++];
            }
        }
        
        // Copiamos los elementos restantes de serie1 si los hay
        while (i < serie1.length) {
            fusion[k++] = serie1[i++];
        }
        
        // Copiamos los elementos restantes de serie2 si los hay
        while (j < serie2.length) {
            fusion[k++] = serie2[j++];
        }
        
        // Imprimimos la serie fusionada
        System.out.println("Serie fusionada en orden:");
        for (int num : fusion) {
            System.out.print(num + " ");
        }
    }
}
