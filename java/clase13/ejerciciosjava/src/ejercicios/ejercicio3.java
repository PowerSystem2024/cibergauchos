/*
Ejercicio 3: leer 5 elementos numericos que se introducirán ordenados de forma
creciente, estos los guardaremos en una tabla de tamaño 10, leer un numero N
e insertarlo en el lugar adecuado para que la tabla continue ordenada.
 */
package ejercicios;

import java.util.Scanner;

public class ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int[] array = new int[10];
        
        // Leer los primeros 5 elementos, asegurándose de que estén ordenados de forma creciente
        System.out.println("Ingrese 5 números en orden creciente:");
        for (int i = 0; i < 5; i++) {
            array[i] = scanner.nextInt();
        }
        
        // Leer el número adicional que se quiere insertar
        System.out.println("Ingrese un número adicional para insertar:");
        int num = scanner.nextInt();
        
        // Encontrar la posición correcta para insertar el número
        int pos = 5; // Inicialmente asumimos que el número será insertado al final de los primeros 5 elementos
        for (int i = 0; i < 5; i++) {
            if (num < array[i]) {
                pos = i;
                break;
            }
        }
        
        // Desplazar los elementos hacia la derecha para hacer espacio en la posición `pos`
        for (int i = 5; i > pos; i--) {
            array[i] = array[i - 1];
        }
        
        // Insertar el número en la posición correcta
        array[pos] = num;
        
        // Imprimir el arreglo resultante
        System.out.println("Arreglo después de insertar el número:");
        for (int i = 0; i < 6; i++) {
            System.out.print(array[i] + " ");
        }
        
    }
}
