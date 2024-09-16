#Ejercicio 2: adivina el numero
#Realizar un juego para adivinar un numero. Para ello se debe 
#generar un numero aleatorio entre 1 - 100, y luego ir pidiendo 
#numeros indicando es mayor, o es menor, segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
#  y alli debe mostrar el numero de intentos. 


import random
print("BIENVENIDOS AL JUEGO DE ADIVINAR")
numero_aleatorio = random.randint(0, 100)
numero_a_ingresar = int(input("Ingrese un numero para saber si acertó: "))
intentos = 1


while numero_a_ingresar != numero_aleatorio:
    intentos += 1
    if numero_aleatorio < numero_a_ingresar:
        print("El numero ingresado es mayor al generado")
    if numero_aleatorio > numero_a_ingresar:
        print("El numero ingresado es menor al generado")
    numero_a_ingresar = int(input("Vuelva a intentarlo: "))
    
print(f"Has acertado el numero con: {intentos} intentos.")
print("YOU WIN")
print("End Game")
