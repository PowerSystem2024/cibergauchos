#Ejerciio 11: Agenda telefonica.
# Hacer un programa que simule una agenda de contactos. Crear un 
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguiente menu de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos Existentes
#       4. Salir

agenda= {}
opciones=(
    f'Bienvenidos a la Agenda\n'
    f'Ingrese una Opcion\n'
    f'#       1. Nuevo contacto\n' 
    f'#       2. Borrar contacton\n'
    f'#       3. Ver contactos Existentes\n'
    f'#       4. Salir\n'
)


while True:
    opcionElegida= input(opciones)
       
    if opcionElegida=="1":
        nombre=input("Ingrese Nombre\n")
        telefono=input("Ingrese Telefono\n")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("contacto agregado correctamente.\n")
        else:
            print("Este nombre de contacto ya existe.")
            
    elif opcionElegida=="2":
        NombreABorrar=input("Ingrese Nombre a borrar\n")
        if NombreABorrar  in agenda:
            del(agenda[NombreABorrar])
            print("Se elimino el contacto correctamente.")
        else:
            print("No existe el contacto a eliminar.")
    elif opcionElegida=="3":
        for nombre,telefono in agenda.items():
            print(f'Nombre:{nombre}, TElefono: {telefono}\n')
    
    elif opcionElegida=="4":
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("Se equivoco de opcion de menu.")
                
#print (agenda)
                
