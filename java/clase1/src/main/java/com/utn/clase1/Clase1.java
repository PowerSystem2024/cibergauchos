package com.utn.clase1;

public class Clase1 {
    public static void main(String[] args) {
        whileCycle();
        doWhileCycle();
        forCycle();
        forCycleWithBreak();
        forCycleWithContinue();
        labels();
    }
    public static void whileCycle(){
        System.out.println("--------- while - cycle -------------");
        var counter = 0;

        while (counter < 5){
            System.out.println("counter = " + counter);
            counter++;
        }
    }

    public static void doWhileCycle(){
        System.out.println("--------- do while - cycle -------------");
        var counter = 0;
        do{
            System.out.println("counter = " + counter);
            counter++;
        }while(counter < 5);
    }
    
    public static void forCycle(){
        System.out.println("--------- for - cycle -------------");
        for (var i = 0; i <=3; i++){
            System.out.println("i = " + i);
        }
    }
    public static void forCycleWithBreak(){
        System.out.println("--------- for-cycle with the reserved word break -------------");
        for (var i = 0; i < 7; i++){
            if(i % 2 == 0){
                System.out.println("first even number = " + i);
                break; //breaks the iteration and ends the cycle
            }

        }
    }
    public static void forCycleWithContinue(){
        System.out.println("--------- for-cycle with the reserved word continue -------------");
        for (var i = 0; i < 7; i++){
            if(i % 2 != 0){

                continue; //continue to the next iteration
            }
            System.out.println("even numbers = " + i);

        }
    }

    public static void labels(){

        System.out.println("--------- labels -------------");
        inicio:
        for (var i = 0; i < 7; i++){
            if(i % 2 == 0){
                System.out.println("i = " + i);
                break inicio;
            }

        }
    }

}
