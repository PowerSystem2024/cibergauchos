/*
ejercicio 4: leer por teclado una tabla de 10 elementos numericos enteros
y una posicion (entre 0 y 9). Eliminar el elemento situado en la posición dada
sin dejar huecos.
 */
package ejercicios;


import java.util.Scanner;

public class ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[10];

        // Leemos los 10 elementos numéricos del usuario
        System.out.println("Ingrese 10 números enteros:");
        for (int i = 0; i < array.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            array[i] = scanner.nextInt();
        }

        // Leemos la posición a eliminar
        int posicion;
        do {
            System.out.print("Ingrese la posición a eliminar (entre 0 y 9): ");
            posicion = scanner.nextInt();
        } while (posicion < 0 || posicion > 9);

        // Eliminamos el elemento y desplazamos los elementos a la izquierda
        for (int i = posicion; i < array.length - 1; i++) {
            array[i] = array[i + 1];
        }

        // Imprimimos el array sin el último elemento porque se eliminó uno
        System.out.println("Array resultante:");
        for (int i = 0; i < array.length - 1; i++) {
            System.out.print(array[i] + " ");
        }
    }
}

