#Ejercicio 3: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# inicial de $1000 y tendrá el siguiente menú de opciones: 
#         1. Ingresar dinero en la cuenta
#         2. Retirar dinero de la cuenta
#         3. Mostrar dinero disponible
#         4. Salir


sueldo = 1000

print("--------BIENVENIDOS AL CAJERO AUTOMATICO--------")


print("\n1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")


opcion = int(input("Elija una opción: "))

if opcion == 1:
    print("Usted seleccionó la opción 1")
    aumento = int(input("¿Cuanto dinero desea ingresar?:  "))
    print(f"Dinero ingresado correctamente, ahora tiene: ${sueldo + aumento}")
elif opcion == 2:
    print("Usted seleccionó la opción 2")
    print(f"Actualmente tiene: {sueldo}")
    retiro = int(input("¿Cuanto dinero desea retirar?:  "))
    while retiro > 1000:
        print("¡Dinero insuficiente!")
        retiro = int(input("¿Cuanto dinero desea retirar?:  "))
    print(f"Dinero retirado correctamente, ahora tiene {sueldo - retiro}")
elif opcion == 3:
    print(f"DINERO DISPONIBLE: ${sueldo}")
elif opcion == 4:
    print("Ha decidido salir")

print("\nGRACIAS POR HABER UTILIZADO EL CAJERO AUTOMÁTICO")
