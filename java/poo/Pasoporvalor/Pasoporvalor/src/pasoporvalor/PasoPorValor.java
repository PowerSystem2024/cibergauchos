
package pasoporvalor;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 15;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX);//Una copia enviada
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg1){//Parametros por valor
        System.out.println("arg1 = " + arg1);
    }
}
