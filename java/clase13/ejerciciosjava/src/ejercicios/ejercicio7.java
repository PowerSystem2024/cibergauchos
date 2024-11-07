/*
 ejercicio 7: leer 10 enteros ordenados crecientemete. leer N y buscarlo en la tabla
se debe mostrar la posición en la que se encuentra, si no está indicarlo con un
mensaje
 */
package ejercicios;

import java.util.Scanner;

public class ejercicio7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[10];

        // Leemos los 10 elementos en orden creciente
        System.out.println("Ingrese 10 números enteros en orden creciente:");
        for (int i = 0; i < array.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            array[i] = scanner.nextInt();
        }

        // Leemos el número a buscar
        System.out.print("Ingrese el número que desea buscar: ");
        int n = scanner.nextInt();

        // Buscamos el número en el arreglo
        int posicion = -1;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == n) {
                posicion = i;
                break;
            }
        }

        // Mostramos el resultado
        if (posicion != -1) {
            System.out.println("El número " + n + " se encuentra en la posición " + posicion + " del arreglo.");
        } else {
            System.out.println("El número " + n + " no se encuentra en el arreglo.");
        }
    }
}
