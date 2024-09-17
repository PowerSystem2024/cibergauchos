# Ejercicio 8: Menú Interactivo - Cajero Automatico
# Hacer un programa que simule un cajero automatico con un saldo inicial de 
# 1000$ y tendrá el siguiente menu de opciones:
# 1. Ingresar dinero a la cuenta.
# 2. Retirar dinero de la cuenta.
# 3. Mostrar dinero disponible.
# 4. Salir.
saldo = float(1000) 
while True:
    print(f'\t.:MENÚ:.')
    print('1. Ingresar dinero a la cuenta.')
    print('2. Retirar dinero de la cuenta.')
    print('3. Mostrar dinero disponible.')
    print('4. Salir.')
    opcion = int(input('Ingrese una opcion de menú:'))
    print("")
    if opcion == 1:
        dineroIngresar = float(input('Ingrese la cantidad de dinero que desea ingresar: '))
        saldo += dineroIngresar
        print(f'Dinero de la cuenta actualizado a: ${saldo}')
    elif opcion == 2:
        dineroRetirar = float(input('Ingrese la cantidad de dinero que desea retirar: '))
        if dineroRetirar > saldo:
            print('¡Transaccion Incorrecta! La cuenta no posee tal cantidad de dinero.')
            print()
        else: 
            saldo -= dineroRetirar
            print(f'Dinero de la cuenta actualizado a: ${saldo}')
            print()
    elif opcion == 3:
        print(f'El saldo actual de la cuenta es: {saldo}')
        print()
    elif opcion == 4:
        print('Gracias por utilizar el cajero automatico, vuelva pronto.')
        break
    else:
        print('¡ERROR!, Ingrese una opcion de menu activa.')
        print()