#Ejercicio 4: Mostrar una frase sin espacios y contar su longitud 
# Hacer un programa donde el usuario ingrese una frase, se le devolverá 
# la misma frase pero sin espacios en blanco, y ademas un contador de cuantos 
# caracteres tiene la frase (sin contar los espacios en blanco)
# Ejemplo: frase = vivir por siempre en paz
# frase final = vivirporsiempreenpaz
# n° de caracteres = 21

frase = input("Ingrese una frase: ")
frase2 = ""
for i in frase:
    if i != " ":
        frase2 += i
frase = frase2
print(f"\nFrase final: {frase}")
print(f"Cantidad de caracteres: {len(frase)}")
