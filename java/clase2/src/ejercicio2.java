
import javax.swing.JOptionPane;


public class ejercicio2 {
    //Leer un numero e indicar si es positivo o negativo.
    //El proceso se repetirá hasta que se introduzca un cero
    public static void main(String[] args) {
        int num = 0;
        do{
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
            if(num > 0){
                JOptionPane.showMessageDialog(null,"El número "+ num + " es positivo.");
            }else if (num < 0){
                JOptionPane.showMessageDialog(null,"El número "+ num + " es negativo.");
            }
        } while(num != 0);
        JOptionPane.showMessageDialog(null,"Saliste del programa.");
        
    }
}
