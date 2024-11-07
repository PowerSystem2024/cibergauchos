/*
 ejercicio 5: leer 10 enteros en una tabla. Guardar en otra tabla 
los elementos pares de la primera, y a continuacion los elementos impares.
 */
package ejercicios;

import java.util.Scanner;

public class ejercicio5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int arreglo[] = new int[10];
        int conteo_pares = 0;
        int conteo_impares = 0;
        
        System.out.println("Llenamos el arreglo: ");
        for (int i = 0; i < 10; i++) {
            System.out.println("Ingrese el elemento: "+(i+1));
            arreglo[i] = scanner.nextInt();
            if(arreglo[i]%2 == 0){
                conteo_pares += 1;
            }
            else{
                conteo_impares += 1;
            }
        }
        
        //creamos los arreglos pares e impares
        int pares[] = new int[conteo_pares];
        int impares[] = new int[conteo_impares];
        
        conteo_pares = 0;
        conteo_impares = 0;
        
        for (int i = 0; i < 10; i++) {
            if(arreglo[i]%2 == 0){
                pares[conteo_pares] = arreglo[i];
                conteo_pares++;
            }
            else{
                impares[conteo_impares] = arreglo[i];
                conteo_impares++;
            }
        }
        
        System.out.println("Arreglo ingresado: ");
        for (int i = 0; i < 10; i++) {
            System.out.println(arreglo[i]+ "-");
        }
        
        System.out.println("Arreglo de pares: ");
        for (int i = 0; i < conteo_pares; i++) {
            System.out.println(pares[i] +"-");
        }
        
        System.out.println("Arreglo de impares: ");
        for (int i = 0; i < conteo_impares; i++) {
            System.out.println(impares[i] +"-");
        }
    }
}
