
import java.util.Scanner;


public class ciclos {
    public static void main(String[] args) {
        ejercicio1();
    }
    public static Scanner input = new Scanner(System.in);

    public static void ejercicio1(){
        // Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un
        // número negativo
        int num, cuadrado;
        System.out.print("Ingrese un número: ");
        num = input.nextInt();
        while (num > 0){
            cuadrado = num * num;
            System.out.println(num + "^2 = " + cuadrado);
            System.out.print("Ingrese un número: ");
            num = input.nextInt();
        }
        System.out.println("Saliste del programa.");
    }
}
