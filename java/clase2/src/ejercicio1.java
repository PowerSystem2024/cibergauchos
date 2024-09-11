
import javax.swing.JOptionPane;


public class ejercicio1 {
    //JOptionPane en lugar de Scanner
    public static void main(String[] args) {
        int num, cuadrado;
        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while (num > 0){
            cuadrado = num * num;
            System.out.println(num + "^2 = " + cuadrado);
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));
        }
        System.out.println("Saliste del programa.");
    }
}
