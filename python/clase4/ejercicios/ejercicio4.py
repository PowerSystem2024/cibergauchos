#Ejercicio 4: Sacar la raiz cuadrada de un numero positivo
import math
numero = int(input("Digite un numero positivo: "))
while numero < 0:
    print("Error -> numero menor a 0")
    numero = int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero):.2f}")

